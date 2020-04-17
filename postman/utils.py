from __future__ import unicode_literals
try:
    from importlib import import_module
except ImportError:
    from django.utils.importlib import import_module  # Django 1.6 / py2.6
import re
import sys
from textwrap import TextWrapper

from django import VERSION
from django.conf import settings
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.utils.html import strip_tags
from django.utils.translation import ugettext, ugettext_lazy as _
from django.views.decorators.debug import sensitive_variables

# make use of a favourite notifier app such as django-notification
# but if not installed or not desired, fallback will be to do basic emailing
name = getattr(settings, 'POSTMAN_NOTIFIER_APP', 'notification')
if name and name in settings.INSTALLED_APPS:
    name = name + '.models'
    notification = import_module(name)
else:
    notification = None

# give priority to a favourite mailer app such as django-mailer
# but if not installed or not desired, fallback to django.core.mail
name = getattr(settings, 'POSTMAN_MAILER_APP', 'mailer')
if name and name in settings.INSTALLED_APPS:
    send_mail = import_module(name).send_mail
    if name == 'mailer':  # the app didn't adjust to the signature change in Django 1.7 (last check: v1.2.2)
        mailer_send_mail = send_mail
        mailer_send_html_mail = import_module(name).send_html_mail
        @sensitive_variables('subject', 'html_message', 'message')
        def send_mail(subject, message, from_email, recipient_list, **kwargs):
            html_message = kwargs.pop('html_message', None)
            if html_message:
                return mailer_send_html_mail(subject, message, html_message, from_email, recipient_list, **kwargs)
            else:
                return mailer_send_mail(subject, message, from_email, recipient_list, **kwargs)
else:
    # A substitution of django.core.mail.send_mail() to allow extra parameters,
    # such as: headers, reply_to (as of Django 1.8),
    # while keeping the signature pattern for compatibility with a possible third-party mailer app.
    from django.core.mail import EmailMultiAlternatives
    @sensitive_variables('subject', 'html_message', 'message')
    def send_mail(subject, message, from_email, recipient_list, **kwargs):
        html_message = kwargs.pop('html_message', None)
        send_kwargs = {}
        fail_silently = kwargs.pop('fail_silently', None)
        if fail_silently is not None:
            send_kwargs['fail_silently'] = fail_silently
        msg = EmailMultiAlternatives(subject, message, from_email, recipient_list, **kwargs)
        if html_message:
            msg.attach_alternative(html_message, 'text/html')
        return msg.send(**send_kwargs)

# to disable email notification to users
DISABLE_USER_EMAILING = getattr(settings, 'POSTMAN_DISABLE_USER_EMAILING', False)
# custom default 'from'
FROM_EMAIL = getattr(settings, 'POSTMAN_FROM_EMAIL', settings.DEFAULT_FROM_EMAIL)
# custom parameters for emailing
PARAMS_EMAIL = getattr(settings, 'POSTMAN_PARAMS_EMAIL', None)

# default wrap width; referenced in forms.py
WRAP_WIDTH = 55


@sensitive_variables('body', 'quote')
def format_body(sender, body, indent=_("> "), width=WRAP_WIDTH):
    """
    Wrap the text and prepend lines with a prefix.

    The aim is to get lines with at most `width` chars.
    But does not wrap if the line is already prefixed.

    Prepends each line with a localized prefix, even empty lines.
    Existing line breaks are preserved.
    Used for quoting messages in replies.

    """
    indent = force_text(indent)  # join() doesn't work on lists with lazy translation objects ; nor startswith()
    wrapper = TextWrapper(width=width, initial_indent=indent, subsequent_indent=indent)
    # rem: TextWrapper doesn't add the indent on an empty text
    quote = '\n'.join([line.startswith(indent) and indent+line or wrapper.fill(line) or indent for line in body.splitlines()])
    return ugettext("\n\n{sender} wrote:\n{body}\n").format(sender=sender, body=quote)


@sensitive_variables('subject')
def format_subject(subject):
    """
    Prepend a pattern to the subject, unless already there.

    Matching is case-insensitive.

    """
    str = ugettext("Re: {subject}")
    pattern = '^' + str.replace('{subject}', '.*') + '$'
    return subject if re.match(pattern, subject, re.IGNORECASE) else str.format(subject=subject)


@sensitive_variables('subject', 'html_message', 'message')
def email(subject_template, message_template_name, recipient_list, object, action, site):
    """Compose and send an email."""
    context = {'site': site, 'object': object, 'action': action}
    subject = render_to_string(subject_template, context)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())

    # look for html and/or txt versions
    try:
        html_message = render_to_string(message_template_name + '.html', context)
    except TemplateDoesNotExist:
        html_message = None
    try:
        message = render_to_string(message_template_name + '.txt', context)
        if message == '':
            raise TemplateDoesNotExist("The .txt template can't be empty when the .html template doesn't exist")
    except TemplateDoesNotExist as e:
        if html_message is None:
            raise e  # At least a .html or a .txt template must be usable
        message = strip_tags(html_message)  # fallback

    kwargs = PARAMS_EMAIL(context) if PARAMS_EMAIL else {}

    # during the development phase, consider using the setting: EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    send_mail(subject, message, FROM_EMAIL, recipient_list, fail_silently=True, html_message=html_message, **kwargs)


def email_visitor(object, action, site):
    """Email a visitor."""
    email('postman/email_visitor_subject.txt', 'postman/email_visitor', [object.email], object, action, site)


def notify_user(object, action, site):
    """Notify a user."""
    if action == 'rejection':
        user = object.sender
        label = 'postman_rejection'
    elif action == 'acceptance':
        user = object.recipient
        parent = object.parent
        label = 'postman_reply' if (parent and parent.sender_id == object.recipient_id) else 'postman_message'
    else:
        return
    if notification:
        # the context key 'message' is already used in django-notification/models.py/send_now() (v0.2.0)
        notification.send(users=[user], label=label, extra_context={'pm_message': object, 'pm_action': action, 'pm_site': site})
    else:
        if not DISABLE_USER_EMAILING and user.email and user.is_active:
            email('postman/email_user_subject.txt', 'postman/email_user', [user.email], object, action, site)

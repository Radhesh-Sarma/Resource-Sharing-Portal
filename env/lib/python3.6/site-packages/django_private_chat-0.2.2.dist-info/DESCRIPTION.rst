=============================================
:sunglasses: django-private-chat :sunglasses:
=============================================

.. image:: https://badge.fury.io/py/django-private-chat.svg
    :target: https://badge.fury.io/py/django-private-chat

.. image:: https://travis-ci.org/Bearle/django-private-chat.svg?branch=master
    :target: https://travis-ci.org/Bearle/django-private-chat

.. image:: https://codecov.io/gh/Bearle/django-private-chat/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/Bearle/django-private-chat

Please also check out our another package https://github.com/Bearle/django_mail_admin

Django one-to-one Websocket-based Asyncio-handled chat, developed by Bearle team

.. image:: https://github.com/Bearle/django-private-chat/blob/dev/screenshots/screen_1.jpg?raw=true

Important Notes
-------------

This app uses separate management command, run_chat_server for running Websockets in Django context. It is intended to be used with something like Supervisor or Systemd to run asyncio webserver as a separate one from Django.
We didn't want our app to be limited to be used together with Django Channels - that's why we did it that way.

You can find an example Systemd config to run it as a service at https://github.com/Bearle/django-private-chat/blob/dev/example.service

P.S. Don't forget to change CHAT_WS_SERVER_HOST && CHAT_WS_SERVER_PORT && CHAT_WS_SERVER_PROTOCOL settings!

Documentation
-------------

The full documentation is (finally) at  https://django-private-chat.readthedocs.io . You can also check the docstrings & this readme.

Example project
---------------

You can check out our example project by cloning the repo and heading into example/ directory.
There is a README file for you to check, initial data to check out the chat included.


Customize the templates
-----------------------

How to customize the template?
Just copy::

    venv/lib/pythonX.X/site-packages/django_private_chat/templates/django_private_chat/dialogs.html
    to
    yourapp/templates/django_private_chat/dialogs.html
And feel free to edit it as you like!
We intentionally left the JS code inside for it to be editable easily.


Exsiting project quickstart
---------------------------

Install django-private-chat::

    pip install django-private-chat

Migrate::

    python manage.py migrate django-private-chat

Note: you can use this package with or without uvloop, just run either

.. code-block:: python

    python manage.py run_chat_server

or run

.. code-block:: python

    python manage.py run_chat_server_uvloop



Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_private_chat',
        ...
    )

Add the server & port for your asyncio server to settings:

.. code-block:: python

    CHAT_WS_SERVER_HOST = 'localhost'
    CHAT_WS_SERVER_PORT = 5002
    CHAT_WS_SERVER_PROTOCOL = 'ws'

It is possible to change messages datetime format using

.. code-block:: python

    DATETIME_FORMAT

Add django-private-chat's URL patterns:

.. code-block:: python

    from django_private_chat import urls as django_private_chat_urls


    urlpatterns = [
        ...
        url(r'^', include('django_private_chat.urls')),
        ...
    ]

Add

.. code-block:: python

    {% block extra_js %}{% endblock extra_js %}

to your base template

Now you can start a dialog using ::

    /dialogs/some_existing_username


To create a WSS (TLS) server instead:

.. code-block:: python

    python manage.py run_chat_server "path/to/cert.pem"


(also works with uvloop).
The "cert.pem" file should be a plaintext PEM file containing first a private key, then a certificate (may be a concatenation of a .key and a .crt file).
Please note that wss will use TLSv1 by default for python 3.5 & 3.4 and will use ssl.PROTOCOL_TLS_SERVER for 3.6 and above.
Features
--------

-:white_check_mark: Uses current app model (get_user_model() and settings.AUTH_USER_MODEL)

-:white_check_mark: Translatable (uses ugettext and {% trans %} )

-:white_check_mark: One-to-one user chat

-:white_check_mark: Works using WebSockets

-:white_check_mark: Works (optionally) using WSS (TLS) connections (disclaimer - security not guaranteed)

-:white_check_mark: Displays online/offline status

-:white_check_mark: Display typing/not typing status

-:white_check_mark: Soft deletable message model - be sure to keep messages to comply with message-keeping laws

-:white_check_mark: Flash the dialog button when the user you are not currently talking to wrote you a message

-:point_right: TODO: add a dialog to the list when new one started

-:point_right: TODO: add user-not-found and other alerts

-:point_right: possible Redis backend intergration


Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage





History

0.2.2 (2018-12-12)
++++++++++++++++++

* Fix read_message_handler by idonoso


0.2.1 (2018-12-07)
++++++++++++++++++

* Compatibility with python3.7 by Emeka Icha

0.2.0 (2018-10-22)
++++++++++++++++++

* Added WSS fix for python 3.4 & 3.5

0.1.9 (2018-07-16)
++++++++++++++++++

* Added WSS support by @zsmith3

0.1.8 (2018-03-23)
++++++++++++++++++

* Fixed time in Message model to be timezone-aware

0.1.7 (2018-03-20)
++++++++++++++++++

* Additions for django 2.0

0.1.6 (2017-04-11)
++++++++++++++++++

* Fixed bugs with static files and added comment about extra_js block to readme

0.1.5 (2017-03-11)
++++++++++++++++++

* Added flashing other user button when he sent you a message and you're in another dialog


0.1.4 (2017-02-12)
++++++++++++++++++

* Added support for django 1.8,1.9

0.1.3 (2017-02-11)
++++++++++++++++++

* Removed uvloop from requirements


0.1.2 (2017-02-11)
++++++++++++++++++

* Fixed i18n not loaded in dialogs template bug

0.1.1 (2017-02-10)
++++++++++++++++++

* Added migrations.

0.1.0 (2017-02-10)
++++++++++++++++++

* First release on PyPI.



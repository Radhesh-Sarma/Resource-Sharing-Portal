from __future__ import unicode_literals
from types import MethodType

from django import VERSION
from django.db.models.sql.compiler import SQLCompiler
from django.db.models.sql.query import Query
import six


class Proxy(object):
    """
    Code base for an instance proxy.
    """

    def __init__(self, target):
        self._target = target

    def __getattr__(self, name):
        target = self._target
        f = getattr(target, name)
        if isinstance(f, MethodType):
            if six.PY3:
                return MethodType(f.__func__, self)
            else:
                return MethodType(f.__func__, self, target.__class__)
        else:
            return f

    def __setattr__(self, name, value):
        if name != '_target':
            setattr(self._target, name, value)
        else:
            object.__setattr__(self, name, value)

    # added for Django 1.7, object has to be callable
    # see db/models/sql/compiler.py/quote_name_unless_alias()
    def __call__(self, name):
        return self._target(name)


class CompilerProxy(Proxy, SQLCompiler):
    """
    A proxy to a compiler.
    """

    # @Override
    def as_sql(self, *args, **kwargs):
        sql, params = self._target.as_sql(*args, **kwargs)
        if not sql:  # is the case with a Paginator on an empty folder
            return sql, params
        # mimics compiler.py/SQLCompiler/get_from_clause() and as_sql()
        qn = self.quote_name_unless_alias
        qn2 = self.connection.ops.quote_name
        alias = self.query.tables[0] if VERSION < (2, 0) else self.query.base_table
        if VERSION >= (1, 8):
            from_clause = self.query.alias_map[alias]
            alias = from_clause.table_alias
            clause_sql, _ = self.compile(from_clause)  # clause_sql, clause_params
            clause = ' '.join(['FROM', clause_sql])
            from django.db.models.sql.constants import INNER as inner_join
        else:
            # Django 1.4, 1.5: name, alias, join_type, lhs, lhs_col, col, nullable
            # Django 1.6, 1.7: name, alias, join_type, lhs, join_cols, _, join_field
            name, alias, _, _, _, _, _ = self.query.alias_map[alias]
            alias_str = '' if alias == name else ' {0}'.format(alias)
            clause = 'FROM {0}{1}'.format(qn(name), alias_str)
            inner_join = self.query.INNER
        index = sql.index(clause) + len(clause)
        extra_table, extra_params = self.union(self.query.pm_get_extra())
        opts = self.query.get_meta()
        qn2_pk_col = qn2(opts.pk.column)  # usually 'id' but not in case of model inheritance
        new_sql = [
            sql[:index],
            ' {0} ({1}) {2} ON ({3}.{4} = {2}.{5})'.format(
                inner_join, extra_table, self.query.pm_alias_prefix, qn(alias), qn2_pk_col, qn2_pk_col),
        ]
        if index < len(sql):
            new_sql.append(sql[index:])
        new_sql = ''.join(new_sql)
        heading_param_count = sql[:index].count('%s')
        return new_sql, params[:heading_param_count] + extra_params + params[heading_param_count:]

    def union(self, querysets):
        """
        Join several querysets by a UNION clause. Returns the SQL string and the list of parameters.
        """
        # union() is "New in Django 1.11." (docs site)
        # but buggy in 2.0, with a backport in 1.11.8 ; my ticket 29229, fixed in 1.11.12 & 2.0.4.
        # For simplicity, let's even ignore the usable 1.11.0-7 frame.
        # Ticket 29286 reintroduced a bug in 1.11.13 & 2.0.5, by considering oly the annotate() case and not the extra().
        # Ticket 29694 fixed the missing extra() case, but is only effective as of 2.1.1,
        # because extra() is destined to be deprecated.
        # So the final solution here was to replace all extra() by annotate() in this app.
        if VERSION < (1, 11, 12) or (2, 0) <= VERSION < (2, 0, 4):
            result_sql, result_params = [], []
            for qs in querysets:
                sql, params = qs.query.sql_with_params()
                result_sql.append(sql)
                result_params.extend(params)
            return ' UNION '.join(result_sql), tuple(result_params)
        else:
            qs = querysets[0].union(*querysets[1:])
            return qs.query.sql_with_params()


class PostmanQuery(Query):
    """
    A custom SQL query.
    """
    pm_alias_prefix = 'PM'

    # @Override
    def __init__(self, *args, **kwargs):
        super(PostmanQuery, self).__init__(*args, **kwargs)
        self._pm_table = None

    # @Override
    def clone(self, *args, **kwargs):
        obj = super(PostmanQuery, self).clone(*args, **kwargs)
        obj._pm_table = self._pm_table
        return obj

    # @Override
    def get_compiler(self, *args, **kwargs):
        compiler = super(PostmanQuery, self).get_compiler(*args, **kwargs)
        return CompilerProxy(compiler)

    def pm_set_extra(self, table):
        self._pm_table = table

    def pm_get_extra(self):
        return self._pm_table

from sphinx.ext.autodoc import AttributeDocumenter
from typing import List

import odoo
import datetime

MODEL_REFERENCE = {
    'account.account.type': 'addons/account/data/data_account_type.xml',
    'res.country': 'odoo/addons/base/data/res_country_data.xml',
    'res.currency': 'odoo/addons/base/data/res_currency_data.xml',
}


class FieldDocumenter(AttributeDocumenter):
    objtype = 'field'
    directivetype = 'attribute'
    priority = 10 + AttributeDocumenter.priority

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.docstringable = (
            odoo.addons.account.models.account_account_tag.AccountAccountTag,
            odoo.addons.account.models.account_tax_report.AccountTaxReportLine,
            odoo.addons.account.models.chart_template.AccountAccountTemplate,
            odoo.addons.account.models.chart_template.AccountChartTemplate,
            odoo.addons.account.models.chart_template.AccountFiscalPositionTemplate,
            odoo.addons.account.models.chart_template.AccountGroupTemplate,
            odoo.addons.account.models.chart_template.AccountTaxTemplate,
        )

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return isinstance(member, odoo.fields.Field)

    def update_annotations(self, parent):
        super().update_annotations(parent)
        annotation = parent.__annotations__
        attrname = self.object.name
        annotation[attrname] = dict
        field = self.object
        if field.type == 'many2one':
            annotation[attrname] = int
        elif field.type in ('one2many', 'many2many'):
            annotation[attrname] = List[odoo.fields.Command]
        elif field.type in ('selection', 'reference', 'char', 'text', 'html'):
            annotation[attrname] = str
        elif field.type == 'boolean':
            annotation[attrname] = bool
        elif field.type in ('float', 'monetary'):
            annotation[attrname] = float
        elif field.type == 'integer':
            annotation[attrname] = int
        elif field.type == 'date':
            annotation[attrname] = datetime.date
        elif field.type == 'datetime':
            annotation[attrname] = datetime.datetime

    def add_content(self, more_content):
        source_name = self.get_sourcename()
        field = self.object
        self.add_line(f"| **Name:** {field.string}", source_name)
        if field.required:
            self.add_line(f"| **Required**", source_name)
        if field.readonly:
            self.add_line(f"| **Read-only:** this field is not supposed to/cannot be set manually", source_name)
        if not field.store:
            self.add_line(f"| **Not stored:** this field is there only for technical reasons", source_name)
        if field.default:
            self.add_line(f"| **Default:** {field.default(odoo.models.Model)}", source_name)
        if field.type in ('many2one', 'one2many', 'many2many'):
            comodel_name = field.comodel_name
            comodel_class = next((
                _class
                for _class in self.docstringable
                if _class._name == comodel_name
            ), None)
            string = f"| **Comodel:** `{comodel_name}`"
            if comodel_class:
                string += f"  :class:`{comodel_class.__name__}`"
            self.add_line(string, source_name)
            reference = MODEL_REFERENCE.get(comodel_name)
            if reference:
                self.add_line(f"| Available values: `{reference} <https://github.com/odoo/odoo/blob/15.0/{reference}>`__.", source_name)
        if field.help:
            for line in field.help.split('\n'):
                self.add_line(f"| {line}", source_name)
        self.add_line('', source_name)
        super().add_content(more_content)

    def get_doc(self, encoding=None, ignore=None):
        # only read docstring of field instance, do not fallback on field class
        field = self.object
        field.__doc__ = field.__dict__.get('__doc__', "")
        res = super().get_doc(encoding, ignore)
        return res


def setup(app):
    app.add_autodocumenter(FieldDocumenter)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

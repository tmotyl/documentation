
=======================
Accounting Localization
=======================

.. warning::

    This tutorial requires knowledges about how to build a module in Odoo (see
    :doc:`/developer/howtos/backend`).


How localization works
======================

On installing the `account <https://github.com/odoo/odoo/tree/15.0/addons/account>`__ module, the localization module corresponding to the country code of the company is installed automatically.
In case of no country code set or no localization module found, the `l10n_generic_coa <https://github.com/odoo/odoo/tree/15.0/addons/l10n_generic_coa>`__ (US) localization module is installed by default.
Check `post init hook <https://github.com/odoo/odoo/blob/15.0/addons/account/__init__.py>`__ for details.

For example, `l10n_ch <https://github.com/odoo/odoo/tree/15.0/addons/l10n_ch>`__ will be installed if the company has ``Switzerland`` as country.

Building a localization module
==============================

Structure of a basic ``l10n_XX`` module may be described as following ``__manifest__.py`` file:

.. code-block:: py

    {
        "name": "COUNTRY - Accounting",
        "version": "1.0.0",
        "category": "Accounting/Localizations/Account Charts",
        "license": "LGPL-3",
        "depends": [
            "account",
            # "l10n_multilang",
        ],
        "data": [
            # Chart of Accounts
            "data/account_chart_template_data.xml",
            "data/account_account_tag_data.xml",
            "data/account.account.template.csv",
            "data/account.group.template.csv",

            # Taxes
            "data/account_tax_group_data.xml",
            "data/account_tax_report_data.xml",
            "data/account_tax_template_data.xml",
            "data/account_fiscal_position_template_data.xml",
            "data/account_account_template_post_data.xml",

            "data/account_chart_post_data.xml",
            "data/account_chart_template_try_loading.xml",

            # Views and others
            "views/xxxmodel_views.xml"
        ],
        "demo": [
            "demo/demo_company.xml",
        ]
    }


In the first file `data/account_chart_template_data.xml` we give name for the Chart of Accounts and set some basic fields.

.. seealso::
   :ref:`Chart Template References <reference/account_chart_template>`

.. example::
  `addons/l10n_ch/data/l10n_ch_chart_data.xml <https://github.com/odoo/odoo/blob/15.0/addons/l10n_ch/data/l10n_ch_chart_data.xml>`__.

  .. literalinclude:: {ODOO_RELPATH}/addons/l10n_ch/data/l10n_ch_chart_data.xml
    :language: xml
    :start-at: l10nch_chart_template
    :end-at: </record>


.. note::

  Recommended **xmlid** for the record is `chart_template`.
  If you need many chart of accounts, you can add some suffixes, i.e. `chart_template_XXX`.


Chart of Accounts
=================

Accounts
--------

.. seealso::
   - :ref:`Account References <reference/account_account>`
   - :doc:`/applications/finance/accounting/payables`
   - :doc:`/applications/finance/accounting/receivables`

Obviously, *Chart of Accounts* cannot exist without *Accounts*. You need to specify them in `data/account.account.template.csv`.

.. example::
  `addons/l10n_ch/data/account.account.template.csv <https://github.com/odoo/odoo/blob/15.0/addons/l10n_ch/data/account.account.template.csv>`__.

  .. literalinclude:: {ODOO_RELPATH}/addons/l10n_ch/data/account.account.template.csv
    :language: csv
    :end-at: ch_coa_1171

XML is prefered but you may use xml format instead.

.. example::
  `addons/l10n_at/data/account_account_template.xml <https://github.com/odoo/odoo/blob/15.0/addons/l10n_at/data/account_account_template.xml>`__.

  .. literalinclude:: {ODOO_RELPATH}/addons/l10n_at/data/account_account_template.xml
    :language: xml
    :start-at: chart_at_template_0010
    :end-at: </record>

.. warning::

    Avoid the usage of liquidity ``account.account.type``!
    Indeed, the bank & cash accounts are created directly at the installation of the localization module and then, are linked to an ``account.journal``.

.. warning::

    Only one account of type payable/receivable is enough.

.. warning::

    Don't create too much accounts: 200-300 is enough.

Next settings for the chart of accounts are set in a separate file, because we need to provide `list of accounts <#accounts>`__ first. In `data/account_chart_post_data.xml` we set some default accounts:

.. todo add reference to account_id in CoA

.. example::
  `addons/l10n_ch/data/l10n_ch_chart_post_data.xml <https://github.com/odoo/odoo/blob/15.0/addons/l10n_ch/data/l10n_ch_chart_post_data.xml>`__.

  .. literalinclude:: {ODOO_RELPATH}/addons/l10n_ch/data/l10n_ch_chart_post_data.xml
    :language: xml
    :start-at: l10nch_chart_template
    :end-at: </record>

Account tags
------------

.. seealso::
   :ref:`Account Tag References <reference/account_account_tag>`

Tags is a way to sort accounts.
For example, imagine you want to create a financial report having multiple lines but you have no way to find a rule to dispatch the accounts according their ``code`` or ``name``.
The solution is the usage of tags, one for each report line, to filter accounts like you want.

Put the tags in `data/account_account_tag_data.xml` file:

Then apply tags on some accounts (field `tag_ids`).

.. example::
  `addons/l10n_lt/data/account.account.template.csv <https://github.com/odoo/odoo/blob/15.0/addons/l10n_lt/data/account.account.template.csv>`__.

  .. literalinclude:: {ODOO_RELPATH}/addons/l10n_lt/data/account.account.template.csv
    :language: csv
    :end-at: account_account_template_1201

.. example::
  `addons/l10n_at/data/account_account_template.xml <https://github.com/odoo/odoo/blob/15.0/addons/l10n_at/data/account_account_template.xml>`__.

  .. literalinclude:: {ODOO_RELPATH}/addons/l10n_at/data/account_account_template.xml
    :language: xml
    :start-at: chart_at_template_0010
    :end-at: </record>


Account groups
--------------

.. seealso::
   :ref:`Account Group References <reference/account_group>`

Account groups allows to describe structure of chart of accounts.

.. example::
  `addons/l10n_il/data/account.group.template.csv <https://github.com/odoo/odoo/blob/15.0/addons/l10n_il/data/account.group.template.csv>`__.

  .. csv-table::
     :file: {ODOO_ABSPATH}/addons/l10n_il/data/account.group.template.csv
     :widths: 20,20,20,20,20
     :header-rows: 1

Taxes
-----

.. seealso::
   - :ref:`Tax References <reference/account_tax>`
   - :doc:`/applications/finance/accounting/taxation/taxes/taxes`

To add taxes you first need to specify tax groups. It has just two fields: name and country. Create file `data/account_tax_group_data.xml` and list the groups:

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <odoo>
        <data noupdate="1">
            <record id="tax_group_tva_0" model="account.tax.group">
                <field name="name">TVA 0%</field>
                <field name="country_id" ref="base.ch"/>
            </record>

            ...
        </data>
    </odoo>

.. example::
  `addons/l10n_ch/data/account_tax_group_data.xml <https://github.com/odoo/odoo/blob/15.0/addons/l10n_ch/data/account_tax_group_data.xml>`__.

  .. literalinclude:: {ODOO_RELPATH}/addons/l10n_ch/data/account_tax_group_data.xml
    :language: xml
    :start-after: <data
    :end-before: </data>

.. example::
  `addons/l10n_uk/data/account.tax.group.csv <https://github.com/odoo/odoo/blob/15.0/addons/l10n_uk/data/account.tax.group.csv>`__.

  .. literalinclude:: {ODOO_RELPATH}/addons/l10n_uk/data/account.tax.group.csv
    :language: csv


Now you can add the taxes via `data/account_tax_template_data.xml` file.


.. example::
  `addons/l10n_ae/data/account_tax_template_data.xml <https://github.com/odoo/odoo/blob/15.0/addons/l10n_ae/data/account_tax_template_data.xml>`__.

  .. literalinclude:: {ODOO_RELPATH}/addons/l10n_ae/data/account_tax_template_data.xml
    :language: xml
    :start-at: uae_sale_tax_5_dubai
    :end-at: </record>

If some accounts should use default taxes, you can set them up in `data/account_account_template_post_data.xml`

Tax Report
----------

.. seealso::
   - :ref:`Tax Report Line References <reference/account_tax_report_line>`
   - :doc:`/applications/finance/accounting/reporting/declarations/tax_returns`

In previous section you noticed fields `invoice_repartition_line_ids` / `refund_repartition_line_ids` and probably understand nothing about it. Good news: you are not alone on this incomprehension. Bad news: you have to figure it out a bit. The topic is complicated indeed:

.. graphviz:: images/tax_report.dot


But lucky we have a presentation explaining the tax reports in details:

.. youtube:: PuXE_NyFRTM
    :align: right
    :width: 700
    :height: 394

So, once you have properly configured taxes, you just need to add `data/account_tax_report_data.xml` file with a single record for `account.tax.report` in beginning:

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <odoo>
        <record id="tax_report" model="account.tax.report">
            <field name="name">Tax Report</field>
            <field name="country_id" ref="base.XX"/>
        </record>

        ...
    </odoo>

... following by a list of records for `account.tax.report.line`.

.. example::
  `addons/l10n_au/data/account_tax_report_data.xml <https://github.com/odoo/odoo/blob/15.0/addons/l10n_au/data/account_tax_report_data.xml>`__.

  .. literalinclude:: {ODOO_RELPATH}/addons/l10n_au/data/account_tax_report_data.xml
    :language: xml
    :start-at: tax_report
    :end-before: account_tax_report_gstrpt_g3



Fiscal positions
----------------

.. seealso::
   - :ref:`Fiscal Position References <reference/account_fiscal_position>`
   - :doc:`/applications/finance/accounting/taxation/taxes/fiscal_positions`

Specify fiscal positions in `data/account_fiscal_position_template_data.xml` file as following:

You may have as many fiscal position as you need.

.. example::
  `addons/l10n_es/data/account_fiscal_position_template_data.xml <https://github.com/odoo/odoo/blob/15.0/addons/l10n_es/data/account_fiscal_position_template_data.xml>`__.

  .. literalinclude:: {ODOO_RELPATH}/addons/l10n_es/data/account_fiscal_position_template_data.xml
    :language: xml
    :start-at: fp_nacional
    :end-before: fp_intra

Final Steps
===========

The last step on installing Chart of Accounts is applying it on current company. File `data/account_chart_template_try_loading.xml` is responsible for that.

.. example::
  `addons/l10n_ch/data/account_chart_template_data.xml <https://github.com/odoo/odoo/blob/15.0/addons/l10n_ch/data/account_chart_template_data.xml>`__.

  .. literalinclude:: {ODOO_RELPATH}/addons/l10n_ch/data/account_chart_template_data.xml
    :language: xml
    :start-at: <function
    :end-at: </function>

Finally, you may add a demo company, so the localization can be easily tested in demo mode.

.. example::
  `addons/l10n_ch/demo/demo_company.xml <https://github.com/odoo/odoo/blob/15.0/addons/l10n_ch/demo/demo_company.xml>`__.

  .. literalinclude:: {ODOO_RELPATH}/addons/l10n_ch/demo/demo_company.xml
    :language: xml
    :start-after: <odoo>
    :end-before: </odoo>

Accounting reports
==================

.. raw:: html

   <div><span class="badge" style="background-color:#AD5E99">Enterprise feature</span><div>

.. seealso::
  :doc:`/applications/finance/accounting/reporting/overview`

Accounting reports should be added via a separate module **l10n_XX_reports** that should go to the `enterprise repository <https://github.com/odoo/enterprise>`__.

Basic `__manifest__.py` file for such a module looks as following:


.. code-block:: py

    {
        "name": "COUNTRY - Accounting Reports",
        "category": "Accounting/Localizations/Reporting",
        "version": "1.0.0",
        "license": "OEEL-1",
        "depends": [
            "l10n_XX", "account_reports"
        ],
        "data": [
            "data/account_financial_html_report_data.xml",
        ],
        "auto_install": True,
    }


Functional overview of financial reports is here: :doc:`/applications/finance/accounting/reporting/overview/main_reports`.

Some good examples:

* `l10n_ch_reports/data/account_financial_html_report_data.xml <https://github.com/odoo/enterprise/blob/15.0/l10n_ch_reports/data/account_financial_html_report_data.xml>`__
* `l10n_be_reports/data/account_financial_html_report_data.xml <https://github.com/odoo/enterprise/blob/15.0/l10n_be_reports/data/account_financial_html_report_data.xml>`__

For the fields meaning dive directly to the source:

* `account.financial.html.report (v15) <https://github.com/odoo/enterprise/blob/d4eff9d39469cf3fe18589a1547cb0cdb93f4ae9/account_reports/models/account_financial_report.py#L59-L75>`__
* `account.financial.html.report.line (v15) <https://github.com/odoo/enterprise/blob/d4eff9d39469cf3fe18589a1547cb0cdb93f4ae9/account_reports/models/account_financial_report.py#L931-L964>`__

Menu for the new report is created automatically. By default it's located under *Accounting >> Reporting* menu.
To create a dedicated section in Reporting menu, you need to create new `ir.ui.menu` record (usually in the main `l10n_XX` module) and set it as `parent_id` field in `account.financial.html.report` model. Example for Belgium localization:

* `ir.ui.menu record in l10n_be <https://github.com/odoo/odoo/blob/15.0/addons/l10n_be/data/menuitem_data.xml>`__
* `parent_id field in l10n_be_reports (v15) <https://github.com/odoo/enterprise/blob/d4eff9d39469cf3fe18589a1547cb0cdb93f4ae9/l10n_be_reports/data/account_financial_html_report_data.xml#L11>`__

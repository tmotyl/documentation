.. _reference/account_chart_template:

==============
Chart Template
==============

---------------------
Invoicing (`account`)
---------------------

This is the main module for Invoicing.

.. autoclass:: odoo.addons.account.models.chart_template.AccountChartTemplate

    .. autofield:: name
    .. autofield:: parent_id
    .. autofield:: code_digits
    .. autofield:: visible
    .. autofield:: currency_id
    .. autofield:: country_id
    .. autofield:: use_anglo_saxon
    .. autofield:: bank_account_code_prefix
    .. autofield:: cash_account_code_prefix
    .. autofield:: transfer_account_code_prefix
    .. autofield:: account_ids
    .. autofield:: income_currency_exchange_account_id
    .. autofield:: expense_currency_exchange_account_id
    .. autofield:: account_journal_suspense_account_id
    .. autofield:: account_journal_payment_debit_account_id
    .. autofield:: account_journal_payment_credit_account_id
    .. autofield:: default_cash_difference_income_account_id
    .. autofield:: default_cash_difference_expense_account_id
    .. autofield:: default_pos_receivable_account_id
    .. autofield:: property_account_receivable_id
    .. autofield:: property_account_payable_id
    .. autofield:: property_account_expense_categ_id
    .. autofield:: property_account_income_categ_id
    .. autofield:: property_account_expense_id
    .. autofield:: property_account_income_id
    .. autofield:: property_stock_account_input_categ_id
    .. autofield:: property_stock_account_output_categ_id
    .. autofield:: property_stock_valuation_account_id
    .. autofield:: property_tax_payable_account_id
    .. autofield:: property_tax_receivable_account_id
    .. autofield:: property_advance_tax_payment_account_id
    .. autofield:: property_cash_basis_base_account_id


---------------------------------
Multi Language (`l10n_multilang`)
---------------------------------

* Multi language support for Chart of Accounts, Taxes, Tax Codes, Journals,
  Accounting Templates, Analytic Chart of Accounts and Analytic Journals.
* Setup wizard changes.
    - Copy translations for COA, Tax, Tax Code and Fiscal Position from
      templates to target objects.


.. autoclass:: odoo.addons.l10n_multilang.models.account.AccountChartTemplate

    .. autofield:: spoken_languages

# -*- coding: utf-8 -*-
{
    'name': 'Italia - Piano dei conti (personale)',
    'version': '0.3',
    'category': 'Localization/Account Charts',
    'depends': [
        'base_vat',
        'base_iban',
        'account_accountant',
        'account_cancel',
    ],
    'author': 'Luca Crea',
    'website': 'https://github.com/lcrea/odoo-l10n-it-account-chart-templates',
    'description': """
Piano dei conti italiano
========================

Fornisce un piano dei conti sufficientemente completo, comprensivo delle impostazioni base, per gestire
la propria contabilità individuale.
""",
    'data': [
        'data/account_chart_template_data_1.xml',
        'data/account_account_tag_data.xml',
        'data/account_type_data.xml',
        'data/account.account.template.csv',
        'data/account_tax_template_data.xml',
        'data/account_fiscal_position_template_data.xml',
        'data/account_chart_template_data_2.xml',
        'data/account_chart_template_data.yml',
        ],
}

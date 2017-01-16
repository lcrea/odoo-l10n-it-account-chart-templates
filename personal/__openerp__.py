# -*- encoding: utf-8 -*-
{
    'name': 'Italia - Piano dei conti (personale)',
    'version': '0.2',
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
    'license': 'AGPL-3',
    'category': 'Localization/Account Charts',
    'data': [
        'data/account.account.template.csv',
        'data/account.tax.code.template.csv',
        'data/account_chart_template.xml',
        'data/account.tax.template.csv',
        'data/account_fiscal_position_template.xml',
        ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}

# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010
#    OpenERP Italian Community <http://www.openerp-italia.org>
#    Servabit srl
#    Agile Business Group sagl
#    Domsense srl
#    Albatos srl
#
#    Copyright (C) 2011-2012
#    Associazione OpenERP Italia <http://www.openerp-italia.org>
#    -> now "Associazione Odoo Italia" <http://www.odoo-italia.org>
#
#    Copyright (C) 2016
#    Luca Crea <lucacre@yahoo.it>
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Italia - Piano dei conti (personale)',
    'version': '0.1',
    'depends': [
        'base_vat',
        'base_iban',
        'account_accountant',
    ],
    'author': 'Luca Crea',
    'website': 'https://github.com/lcrea/odoo-l10n-it-account-chart-templates',
    'description': """
Piano dei Conti Italiano (personale)
====================================

Fornisce un piano dei conti completo e le impostazioni base per gestire la propria contabilità personale.
""",
    'license': 'AGPL-3',
    'category': 'Localization/Account Charts',
    'data': [
        'data/account.account.template.csv',
        'data/account.tax.code.template.csv',
        'data/account_chart.xml',
        'data/account.tax.template.csv',
        'data/account.fiscal.position.template.csv',
        'data/l10n_chart_it_personal.xml',
        ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}

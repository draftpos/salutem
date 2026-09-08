# -*- coding: utf-8 -*-
{
    'name': 'Salutem Custom Branding',
    'version': '1.1',
    'category': 'Customization',
    'summary': 'Dynamic renaming of core Odoo terminology and financial ratios for Salutem',
    'description': """
        This module provides configuration settings to dynamically rename standard Odoo terms:
        - Customers -> Members
        - Sales -> Contributions
        - Products -> Subscription Packages
        - Invoices -> Premiums
        Also enhances Financial Ratios with Opex Ratio and Staff Cost Ratio.
    """,
    'author': 'Stark',
    'website': '',
    'depends': ['base', 'sale_management', 'contacts', 'product', 'havano_all_in_one'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

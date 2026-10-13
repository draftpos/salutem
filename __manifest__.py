# -*- coding: utf-8 -*-
{
    'name': 'Salutem Custom Branding',
    'version': '1.0',
    'category': 'Customization',
    'summary': 'Dynamic renaming of core Odoo terminology for the Salutem system',
    'description': """
        This module provides configuration settings to dynamically rename standard Odoo terms:
        - Customers -> Members
        - Sales -> Contributions
        - Products -> Subscription Packages
    """,
    'author': 'DraftPOS / Havano Solutions',
    'website': 'https://draftpos.com',
    'license': 'LGPL-3',
    'images': ['static/description/icon.png'],
    'depends': ['base', 'sale_management', 'contacts', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

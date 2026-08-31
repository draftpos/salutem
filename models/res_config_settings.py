# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    rename_customers_to_members = fields.Boolean(
        string='Rename Customers to Members',
        config_parameter='salutem.rename_customers',
        default=False
    )
    
    rename_sales_to_contributions = fields.Boolean(
        string='Rename Sales to Contributions',
        config_parameter='salutem.rename_sales',
        default=False
    )
    
    rename_products_to_subscription_packages = fields.Boolean(
        string='Rename Products to Subscription Packages',
        config_parameter='salutem.rename_products',
        default=False
    )
    
    rename_invoices_to_premiums = fields.Boolean(
        string='Rename Invoices to Premiums',
        config_parameter='salutem.rename_invoices',
        default=False
    )
    
    rename_product_variants_to_subscription_variants = fields.Boolean(
        string='Rename Product Variants to Subscription Variants',
        config_parameter='salutem.rename_product_variants',
        default=False
    )

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        
        # Call the renaming utility function to process the changes
        self.env['salutem.rename.utils'].apply_renames(
            rename_customers=self.rename_customers_to_members,
            rename_sales=self.rename_sales_to_contributions,
            rename_products=self.rename_products_to_subscription_packages,
            rename_invoices=self.rename_invoices_to_premiums,
            rename_product_variants=self.rename_product_variants_to_subscription_variants
        )

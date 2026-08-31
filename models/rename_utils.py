# -*- coding: utf-8 -*-
from odoo import models, api

class SalutemRenameUtils(models.TransientModel):
    _name = 'salutem.rename.utils'
    _description = 'Salutem Renaming Utilities'

    @api.model
    def apply_renames(self, rename_customers, rename_sales, rename_products, rename_invoices, rename_product_variants):
        # 1. Rename Customers to Members globally
        customer_menus = self.env['ir.ui.menu'].search([('name', 'in', ['Customers', 'Members'])])
        for menu in customer_menus:
            menu.name = 'Members' if rename_customers else 'Customers'

        customer_actions = self.env['ir.actions.act_window'].search([('name', 'in', ['Customers', 'Members'])])
        for action in customer_actions:
            action.name = 'Members' if rename_customers else 'Customers'

        # 2. Rename Sales to Contributions globally
        sales_menus = self.env['ir.ui.menu'].search([('name', 'in', ['Sales', 'Contributions'])])
        for menu in sales_menus:
            menu.name = 'Contributions' if rename_sales else 'Sales'

        sales_actions = self.env['ir.actions.act_window'].search([('name', 'in', ['Sales', 'Contributions'])])
        for action in sales_actions:
            action.name = 'Contributions' if rename_sales else 'Sales'

        # 3. Rename Products to Subscription Packages globally
        products_menus = self.env['ir.ui.menu'].search([('name', 'in', ['Products', 'Subscription Packages'])])
        for menu in products_menus:
            menu.name = 'Subscription Packages' if rename_products else 'Products'

        products_actions = self.env['ir.actions.act_window'].search([('name', 'in', ['Products', 'Subscription Packages'])])
        for action in products_actions:
            action.name = 'Subscription Packages' if rename_products else 'Products'

        # 4. Rename Invoices to Premiums globally
        invoice_menus = self.env['ir.ui.menu'].search([('name', 'in', ['Invoices', 'Premiums'])])
        for menu in invoice_menus:
            menu.name = 'Premiums' if rename_invoices else 'Invoices'

        invoice_actions = self.env['ir.actions.act_window'].search([('name', 'in', ['Invoices', 'Premiums'])])
        for action in invoice_actions:
            action.name = 'Premiums' if rename_invoices else 'Invoices'

        # 5. Rename Product Variants to Subscription Variants globally
        variant_menus = self.env['ir.ui.menu'].search([('name', 'in', ['Product Variants', 'Subscription Variants'])])
        for menu in variant_menus:
            menu.name = 'Subscription Variants' if rename_product_variants else 'Product Variants'

        variant_actions = self.env['ir.actions.act_window'].search([('name', 'in', ['Product Variants', 'Subscription Variants'])])
        for action in variant_actions:
            action.name = 'Subscription Variants' if rename_product_variants else 'Product Variants'

        # 6. Global Field Renaming for generic fields
        product_fields = self.env['ir.model.fields'].search([('field_description', 'in', ['Product', 'Subscription Package'])])
        for field in product_fields:
            field.field_description = 'Subscription Package' if rename_products else 'Product'
            
        customer_fields = self.env['ir.model.fields'].search([('field_description', 'in', ['Customer', 'Member'])])
        for field in customer_fields:
            field.field_description = 'Member' if rename_customers else 'Customer'
            
        invoice_fields = self.env['ir.model.fields'].search([('field_description', 'in', ['Invoice', 'Premium'])])
        for field in invoice_fields:
            field.field_description = 'Premium' if rename_invoices else 'Invoice'
            
        variant_fields = self.env['ir.model.fields'].search([('field_description', 'in', ['Product Variant', 'Subscription Variant'])])
        for field in variant_fields:
            field.field_description = 'Subscription Variant' if rename_product_variants else 'Product Variant'

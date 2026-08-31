# -*- coding: utf-8 -*-
from odoo import models, api

class SalutemRenameUtils(models.TransientModel):
    _name = 'salutem.rename.utils'
    _description = 'Salutem Renaming Utilities'

    @api.model
    def apply_renames(self, rename_customers, rename_sales, rename_products):
        # 1. Rename Customers to Members
        customer_menu = self.env.ref('contacts.menu_contacts', raise_if_not_found=False)
        if customer_menu:
            customer_menu.name = 'Members' if rename_customers else 'Contacts'

        customer_action = self.env.ref('contacts.action_contacts', raise_if_not_found=False)
        if customer_action:
            customer_action.name = 'Members' if rename_customers else 'Contacts'

        # 2. Rename Sales to Contributions
        sale_menu_root = self.env.ref('sale.sale_menu_root', raise_if_not_found=False)
        if sale_menu_root:
            sale_menu_root.name = 'Contributions' if rename_sales else 'Sales'

        sale_action = self.env.ref('sale.action_orders', raise_if_not_found=False)
        if sale_action:
            sale_action.name = 'Contributions' if rename_sales else 'Sales Orders'
            
        sale_menu_orders = self.env.ref('sale.menu_sale_order', raise_if_not_found=False)
        if sale_menu_orders:
            sale_menu_orders.name = 'Contributions' if rename_sales else 'Orders'

        # 3. Rename Products to Subscription Packages
        product_menu_catalog = self.env.ref('sale.product_menu_catalog', raise_if_not_found=False)
        if product_menu_catalog:
            product_menu_catalog.name = 'Subscription Packages' if rename_products else 'Products'

        product_action = self.env.ref('sale.product_template_action', raise_if_not_found=False)
        if product_action:
            product_action.name = 'Subscription Packages' if rename_products else 'Products'
            
        # Optional: Attempt to rename the ir.model.fields for form labels if required globally
        # (This is a simplified approach; in production, you might want to translate specific fields)
        if rename_customers:
            self._update_field_string('res.partner', 'name', 'Member Name')
        else:
            self._update_field_string('res.partner', 'name', 'Name')

    @api.model
    def _update_field_string(self, model_name, field_name, new_string):
        """Helper to update a field string label dynamically"""
        field_record = self.env['ir.model.fields'].search([
            ('model', '=', model_name),
            ('name', '=', field_name)
        ], limit=1)
        if field_record:
            field_record.field_description = new_string

# -*- coding: utf-8 -*-
from odoo import models, api
from lxml import etree

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def get_view(self, view_id=None, view_type='form', **kwargs):
        res = super().get_view(view_id=view_id, view_type=view_type, **kwargs)
        if view_type == 'form':
            rename_products = self.env['ir.config_parameter'].sudo().get_param('salutem.rename_products')
            if rename_products:
                doc = etree.XML(res['arch'])
                # Rename the "Add a product" link
                for node in doc.xpath("//create[@name='add_product_control']"):
                    node.set('string', 'Add a subscription package')
                for node in doc.xpath("//create[@name='add_product_control' or @string='Add a product']"):
                    node.set('string', 'Add a subscription package')
                
                # Rename the "Product" column header if it is hardcoded in the view
                for node in doc.xpath("//field[@name='product_id']"):
                    if node.get('string') == 'Product':
                        node.set('string', 'Subscription Package')
                    elif not node.get('string'):
                        node.set('string', 'Subscription Package')
                        
                res['arch'] = etree.tostring(doc, encoding='unicode')
        return res

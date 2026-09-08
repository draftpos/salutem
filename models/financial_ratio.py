# -*- coding: utf-8 -*-
from odoo import models, api


class HavanoFinancialRatio(models.Model):
    _inherit = 'havano.financial.ratio'

    @api.model
    def action_compute_and_open_ratios(self, category):
        """
        Extend financial ratios computation for Salutem:
        - Opex Ratio (%) = (Operating Expenses / Revenue or Contributions) * 100
        - Staff Cost Ratio (%) = (Staff Costs / Revenue or Contributions) * 100
        Ensures these ratios are calculated and visible under Insurance Ratios ('ins')
        and Profitability Ratios ('prof').
        """
        res = super(HavanoFinancialRatio, self).action_compute_and_open_ratios(category)

        if category in ('ins', 'prof'):
            def get_bal(domain):
                records = self.env['account.move.line'].search_read(
                    [('parent_state', '=', 'posted')] + domain,
                    ['balance']
                )
                return sum(r['balance'] for r in records)

            # Revenue / Contributions base
            revenue = -get_bal([('account_id.internal_group', '=', 'income')])
            contributions = get_bal([('account_id.name', 'ilike', 'contribution')]) or revenue
            base_revenue = contributions if (category == 'ins' and contributions) else (revenue or 1.0)
            if not base_revenue:
                base_revenue = 1.0

            # Operating Expenses
            op_expense = get_bal([('account_id.account_type', 'in', ['expense_depreciation', 'expense'])])
            if not op_expense:
                op_expense = get_bal([('account_id.internal_group', '=', 'expense')])

            # Staff Costs (accounts with staff, salary, wage, or payroll in name)
            staff_costs = get_bal([
                ('account_id.internal_group', '=', 'expense'),
                '|', '|', '|',
                ('account_id.name', 'ilike', 'staff'),
                ('account_id.name', 'ilike', 'salary'),
                ('account_id.name', 'ilike', 'wage'),
                ('account_id.name', 'ilike', 'payroll'),
            ])

            opex_ratio = (op_expense / base_revenue) * 100.0
            staff_cost_ratio = (staff_costs / base_revenue) * 100.0

            # Remove any existing to ensure fresh values
            existing = self.search([
                ('create_uid', '=', self.env.user.id),
                ('category', '=', category),
                ('name', 'in', ['Opex Ratio (%)', 'Staff Cost Ratio (%)'])
            ])
            existing.unlink()

            self.create([
                {
                    'name': 'Opex Ratio (%)',
                    'category': category,
                    'value': round(opex_ratio, 2),
                },
                {
                    'name': 'Staff Cost Ratio (%)',
                    'category': category,
                    'value': round(staff_cost_ratio, 2),
                },
            ])

        return res

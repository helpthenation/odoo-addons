from openerp import models, fields, api, exceptions
import openerp.addons.decimal_precision as dp

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    
    @api.model
    def _prepare_order_line_move (self, order, order_line, picking_id, group_id,):
        repercute_tax = self.env.ref ('sd_cost_repercution_purchase.group_repercute_tax') in self.env['res.users'].browse ([self._uid]).groups_id
        repercute_discount = self.env.ref ('sd_cost_repercution_purchase.group_repercute_discount') in self.env['res.users'].browse ([self._uid]).groups_id
        res = super (PurchaseOrder, self)._prepare_order_line_move (order, order_line, picking_id, group_id,)
        if repercute_discount and order_line.discount:
            res[0]['price_unit'] = res[0]['price_unit'] - (res[0]['price_unit'] * (order_line.discount / 100))
            if (self.env['ir.module.module'].search ([['name', '=', 'purchase_pricelist_rules'], ['state', '=', 'installed']]) 
                and self.env.ref ('product_pricelist_rules.group_second_discount') in self.env['res.users'].browse ([self._uid]).groups_id 
                and order_line.discount2):
                res[0]['price_unit'] = res[0]['price_unit'] - (res[0]['price_unit'] * (order_line.discount2 / 100))
            
        if repercute_tax and order_line.taxes_id:
            taxes = 0
            for tax in order_line.taxes_id:
                taxes += tax.amount 
            res[0]['price_unit'] = res[0]['price_unit'] + (res[0]['price_unit'] * taxes)
        return res
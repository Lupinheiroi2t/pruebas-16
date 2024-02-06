from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    move_type = fields.Selection(related='invoice_ids.move_type')
    
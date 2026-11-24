from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    create_by = fields.Many2one(
        comodel_name="res.users",
        string="Created By",
        default=lambda self: self.env.user,
        readonly=True,
        copy=False,
    )

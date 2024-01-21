# © 2023 Lu Pinheiro (<https://github.com/Lucpinheiro>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models


class Connection(models.Model):
    _name = "connection"
    _description = "Connection"

    name = fields.Char()
    type = fields.Char()
    origin = fields.Many2one("city")
    destination = fields.Char("city")




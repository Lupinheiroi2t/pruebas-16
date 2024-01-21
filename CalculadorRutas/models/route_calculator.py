# © 2023 Lu Pinheiro (<https://github.com/Lucpinheiro>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models


class RouteCalculator(models.Model):
    _name = "route.calculator"
    _description = "Route Calculator"

    name = fields.Char()
    connection_ids = fields.Many2one("connection")
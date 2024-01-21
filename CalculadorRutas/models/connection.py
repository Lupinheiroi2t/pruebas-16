# © 2023 Lu Pinheiro (<https://github.com/Lucpinheiro>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models, _, _lt


class Connection(models.Model):
    _name = "connection"
    _description = "Connection"

    name = fields.Char()

class ConnectionType(models.Model):
    _name = "connection.type"
    _description = "Connection Type"

    name = fields.Char(string="Type")
    citys = fields.Many2many("Citys")
    origin = fields.Char(string="Origin")
    destination = fields.Char(String="Destination")
   
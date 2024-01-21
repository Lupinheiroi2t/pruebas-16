# © 2023 Lu Pinheiro (<https://github.com/Lucpinheiro>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models, api 


class Connection(models.Model):
    _name = "connection"
    _description = "Connection"

    name = fields.Char(string="Conexión", compute="_compute_connections", store=True)
    type = fields.Char()
    origin = fields.Many2one("city")
    destination = fields.Many2one("city")



    @api.depends('origin', 'destination')
    def _compute_connections(self):
        for connection in self:
            name = f"{connection.origin.name} - {connection.destination.name}"
            connection.name = name

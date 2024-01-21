# © 2023 Lu Pinheiro (<https://github.com/Lucpinheiro>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models, api 


class Connection(models.Model):
    _name = "connection"
    _description = "Connection"

    name = fields.Char(compute="_compute_connections", string="Conexión", store=True)
    type = fields.Char()
    origin = fields.Many2one("city")
    destination = fields.Many2one("city")


    @api.depends('origin', 'destination')
    def _compute_connections(self):
        for route in self:
            route.name = f"{route.origin} - {route.destination}"

             


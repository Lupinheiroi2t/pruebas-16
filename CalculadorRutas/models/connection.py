# © 2023 Lu Pinheiro (<https://github.com/Lucpinheiro>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models, api 


class Connection(models.Model):
    _name = "connection"
    _description = "Connection"

    name = fields.Char()
    type = fields.Char()
    origin = fields.Char()
    destination = fields.Char()
    connection = fields.Char(string="Conexión", compute="_compute_connections", store=True)


    @api.depends('origin', 'destination')
    def _compute_connections(self):
        for route in self:
            route.connection = '%s - %s' % (route.origin, route.destination)

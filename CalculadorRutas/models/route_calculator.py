# © 2023 Lu Pinheiro (<https://github.com/Lucpinheiro>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models, api


class RouteCalculator(models.Model):
    _name = "route.calculator"
    _description = "Route Calculator"

    name = fields.Char(related='connection_id.name')
    connection_id = fields.Many2one("connection")
    type_id = fields.Many2one("connection.type")

 
    @api.model
    def create(self, values):
        # Llama al método create de la clase base para realizar la creación del registro
        record = super(RouteCalculator, self).create(values)
        # Muestra un mensaje de "Feliz viaje"
        self.env.user.notify_warning(message="¡Feliz viaje!")

        return record
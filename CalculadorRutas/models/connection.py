# © 2023 Lu Pinheiro (<https://github.com/Lucpinheiro>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models, api 
from odoo.exceptions import ValidationError

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
            try:
                if not connection.origin or not connection.destination:
                    raise ValidationError("Debe especificar tanto la ciudad de origen como la de destino.")
                if connection.origin.name != "Barcelona" and connection.destination.name != "Paris":
                    raise ValidationError("No existe ruta válida para estas ciudades'.")
                
                name = f"{connection.origin.name} - {connection.destination.name}"
                connection.name = name

            except ValidationError as e:
                connection.nombre_concatenado = False


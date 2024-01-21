# © 2023 Lu Pinheiro (<https://github.com/Lucpinheiro>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models, api 
from odoo.exceptions import ValidationError, UserError

class Connection(models.Model):
    _name = "connection"
    _description = "Connection"

    name = fields.Char(string="Conexión", compute="_compute_connections", store=True)
    type = fields.Char()
    origin = fields.Many2one("city")
    destination = fields.Many2one("city")

            
    @api.constrains('origin', 'destination')
    def _compute_connections(self):
        for connection in self:
            name = f"{connection.origin.name} - {connection.destination.name}"
            connection.name = name
            if not connection.origin or not connection.destination:
                raise ValidationError("Debe especificar tanto la ciudad de origen como la de destino.")
            if connection.origin.name == 'Barcelona' and connection.destination.name == 'Paris' == True:
                  return True
            if  connection.origin.name == 'Barcelona' and connection.destination.name == 'Roma' == True:
                  return True
            else:
                raise ValidationError('No existe una válida entre Paris y Barcelona.')

                 
         
    # @api.constrains('origin', 'destination')
    # def _compute_connections(self):
    #     for connection in self:
    #         name = f"{connection.origin.name} - {connection.destination.name}"
    #         connection.name = name
    #         if not connection.origin or not connection.destination:
    #             raise ValidationError("Debe especificar tanto la ciudad de origen como la de destino.")
    #         if (
    #             connection.origin.name == 'Paris' and
    #             connection.destination.name == 'Barcelona'
    #         ):
    #             raise ValidationError('No existe una válida entre Paris y Barcelona.')
                 
                 
                 

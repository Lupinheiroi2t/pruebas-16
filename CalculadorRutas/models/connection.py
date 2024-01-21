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
            valor_buscado = 'Paris'  
            destino_encontrado = self.env['city'].search([('name', '=', valor_buscado)])

        if destino_encontrado:
            # Hacer algo con el resultado, por ejemplo, imprimir el ID
            print("ID del destino encontrado:", destino_encontrado.id)
        else:
            print("No se encontró ningún destino con el valor deseado.")
                 
                 
                 
        

    # @api.constrains('origin', 'destination')
    # def _compute_destination(self):
    #     for connection in self:
    #         if not connection.origin or not connection.destination:
    #             raise ValidationError("Debe especificar tanto la ciudad de origen como la de destino.")
    #         if  connection.origin == "paris" and  connection.destination == "barcelona":
    #             raise ValidationError("No existe ruta válida para estas ciudades'.")


    
    # city_connection_ids = fields.Selection(
    #     selection=[
    #         ("paris", "Paris"),
    #         ("barcelona", "Barcelona"),
    #         ("madrid", "Madrid"),
    #         ("roma", "Roma"),
    #         ("valencia", "Valencia"),
    #         ("malta", "malta"),
    #     ],)
    
    # origin = fields.Selection(related='city_connection_ids.origin')
    # destination = fields.Selection(compute="_compute_destination", related='city_connection_ids.destination')

    # @api.constrains('origin', 'destination')
    # def _compute_destination(self):
    #     for connection in self:
    #         if not connection.origin or not connection.destination:
    #             raise ValidationError("Debe especificar tanto la ciudad de origen como la de destino.")
    #         if  connection.origin == "paris" and  connection.destination == "barcelona":
    #             raise ValidationError("No existe ruta válida para estas ciudades'.")
            
            
    # @api.deprends('origin', 'destination')
    # def _compute_connections(self):
    #     for connection in self:
    #         name = f"{connection.origin.name} - {connection.destination.name}"
    #         connection.name = name


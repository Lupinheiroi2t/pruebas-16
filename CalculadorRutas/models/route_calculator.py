# © 2023 Lu Pinheiro (<https://github.com/Lucpinheiro>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class RouteCalculator(models.Model):
    _name = "route.calculator"
    _description = "Route Calculator"

    name = fields.Char(related='connection_id.name')
    connection_id = fields.Many2one("connection")
    type_id = fields.Many2one("connection.type")

 
    @api.model
    def create(self, values): 
        for record in self:
            if values['connection_id'] == True:
                raise ValidationError('"¡Feliz viaje!"')
            return record
    
        # @api.model
    # def write(self, values):  #esos métodos tienen argumentos posicionales 
    #     if self.pages == 0 or self.pages == 300:
    #         raise ValidationError('No se puede guardar')
    #     return super(libreria, self).write(values)

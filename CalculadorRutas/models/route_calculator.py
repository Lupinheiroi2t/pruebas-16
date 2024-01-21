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


    @api.onchange('name', 'connection_id', 'type_id')
    def _onchange_notify_info(self):
        # Muestra un mensaje informativo al usuario actual
        self.env.user.notify_info(message="¡Registro guardado exitosamente!")


    # @api.model
    # def create(self, values):
    #     # Llama al método create de la clase base para realizar la creación del registro
    #     record = super(RouteCalculator, self).create(values)

    #     # Agrega un mensaje informativo al registro recién creado
    #     message = "¡Registro creado! ¡Feliz viaje!"
    #     self.env['mail.message'].create({
    #             'model': 'route.calculator',
    #             'res_id': record.id,
    #             'body': message,
    #             'subject': 'Información',
    #             'message_type': 'comment',
    #         })

    #     return record
 


    # @api.model
    # def create(self, values):
    #     res = super(libreria ,self).create(values)
    #     if values.get("pages") == 0:
    #         values["pages"] = 300  
    #     return res



        # @api.model
    # def write(self, values):  #esos métodos tienen argumentos posicionales 
    #     if self.pages == 0 or self.pages == 300:
    #         raise ValidationError('No se puede guardar')
    #     return super(libreria, self).write(values)

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
        # Llama al método create de la clase base para realizar la creación del registro
        record = super(RouteCalculator, self).create(values)

        # Añade un mensaje al chatter indicando que el registro se creó manualmente
        record.message_post(
            body="¡Registro creado manualmente!",
            subject="Registro Creado",
            message_type="notification"
        )

        return record

def write(self, values):
        # Llama al método write de la clase base para realizar la actualización del registro
        result = super(RouteCalculator, self).write(values)

        # Añade un mensaje al chatter indicando que el registro se actualizó manualmente
        self.message_post(
            body="¡Registro actualizado manualmente!",
            subject="Registro Actualizado",
            message_type="notification"
        )

        return result

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

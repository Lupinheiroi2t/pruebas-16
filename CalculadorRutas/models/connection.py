# © 2023 Lu Pinheiro (<https://github.com/Lucpinheiro>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models, api 


class Connection(models.Model):
    _name = "connection"
    _description = "Connection"

    name = fields.Char()
    type = fields.Char()


    ciudad_origen = fields.Char(string='Ciudad de Origen', required=True)
    ciudad_destino = fields.Char(string='Ciudad de Destino', required=True)

    @api.depends('ciudad_origen', 'ciudad_destino')
    def _compute_suma_ciudades(self):
        for ruta in self:
            ruta.suma_ciudades = f"{ruta.ciudad_origen} - {ruta.ciudad_destino}"

    suma_ciudades = fields.Char(string='Suma de Ciudades', compute='_compute_suma_ciudades', store=True)
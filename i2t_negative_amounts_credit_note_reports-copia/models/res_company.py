# Copyright 2022 Angel Garcia de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    negative_amounts_credit_note = fields.Boolean(
        string="Show negative amounts in credit note reports.",
        help="Shows the negative amounts in the Credit Notes reports. By default, the amounts are positive.",
        default=False,
    )

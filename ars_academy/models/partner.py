from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    is_instructor = fields.Boolean(
        string='Instructor', 
        default=False,
    )

    is_student = fields.Boolean(
        string='Student', 
        default=False,
    )
    
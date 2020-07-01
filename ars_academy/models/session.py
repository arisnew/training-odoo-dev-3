from odoo import api, fields, models


class Session(models.Model):
    _name = 'ars.academy.session'
    _description = 'Data Session'

    name = fields.Char(
        string='Session Name',
        required = True,
    )

    instructor_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Instructor',
        domain = [('is_instructor', '=', True)],
    )

    course_id = fields.Many2one(
        comodel_name='ars.academy.course', 
        string='Course',
        required = True,
    )

    session_date = fields.Datetime(
        string='Session date',
        default = fields.Datetime.now,
        required = True,
    )

    description = fields.Text(
        string='Description',
    )
    
    
    

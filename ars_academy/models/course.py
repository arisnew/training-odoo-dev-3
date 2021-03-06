from odoo import api, fields, models


class Course(models.Model):
    _name = 'ars.academy.course'
    _description = 'Master Data Course'

    name = fields.Char(
        string='Course Name',
        required=True,
    )
    
    description = fields.Text(
        string='Description'
    )

    active = fields.Boolean(
        string='Active', 
        default=True,
    )

    category_id = fields.Many2one(
        comodel_name='ars.academy.course.category', 
        string='Category',
    )
    
    

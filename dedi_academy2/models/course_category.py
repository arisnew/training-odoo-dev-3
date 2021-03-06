from odoo import api, fields, models


class Course(models.Model):
    _name = 'dedi.academy2.course.category'
    _description = 'Master Data Course Category'

    name = fields.Char(
        string='Category Name',
        required=True,
    )
    
    description = fields.Text(
        string='Description'
    )

    active = fields.Boolean(
        string='Active', 
        default=True,
    )
    

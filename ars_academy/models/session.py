from odoo import api, fields, models, exceptions

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

    attendee_ids = fields.One2many(
        comodel_name='ars.academy.attendee', 
        inverse_name='session_id', 
        string='Attendees',
    )

    min_attendee = fields.Integer(
        string='Minimum Attendee',
        default = 0,
        required = True,
    )
    
    taken_seats = fields.Float(
        string="Taken seats",
        compute='_taken_seats',
        store=True,
    )

    @api.depends('min_attendee', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.min_attendee:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.min_attendee

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            person = [x.student_id.id for x in r.attendee_ids]
            if r.instructor_id and r.instructor_id.id in person:
                raise exceptions.ValidationError("A session's instructor can't be an attendee")

    
class Attendee(models.Model):
    _name = 'ars.academy.attendee'
    _description = 'Attendees of session'

    name = fields.Char(
        string = 'Reg No.',
        required = True,
    )

    reg_date = fields.Datetime(
        string='Reg Date',
        required = True,
        default = fields.Datetime.now,
    )
    
    session_id = fields.Many2one(
        comodel_name='ars.academy.session', 
        string='Session',
    )

    student_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Student',
        domain = [('is_student', '=', True)],
        required = True,
    )
    
    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "No Registrasi harus unik!!"),
    ]
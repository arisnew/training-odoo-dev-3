# -*- coding: utf-8 -*-
{
    'name': "ARS Academy",

    'summary': """
        Sebagai contoh pembuatan addon di Odoo, modul academy""",

    'description': """
        Sebagai contoh pembuatan addon di Odoo, modul academy (course, course category, session, attendee, etc.)
    """,

    'author': "ArisNew",
    'website': "https://aabc-software.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/course.xml',
        'views/course_category.xml',
        'views/partner.xml',
        'views/session.xml',

        'reports/session.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
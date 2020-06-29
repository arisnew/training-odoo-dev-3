# -*- coding: utf-8 -*-
from odoo import http

# class DediAcademy2(http.Controller):
#     @http.route('/dedi_academy2/dedi_academy2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dedi_academy2/dedi_academy2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dedi_academy2.listing', {
#             'root': '/dedi_academy2/dedi_academy2',
#             'objects': http.request.env['dedi_academy2.dedi_academy2'].search([]),
#         })

#     @http.route('/dedi_academy2/dedi_academy2/objects/<model("dedi_academy2.dedi_academy2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dedi_academy2.object', {
#             'object': obj
#         })
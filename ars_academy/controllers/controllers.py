# -*- coding: utf-8 -*-
from odoo import http

# class ArsAcademy(http.Controller):
#     @http.route('/ars_academy/ars_academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ars_academy/ars_academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ars_academy.listing', {
#             'root': '/ars_academy/ars_academy',
#             'objects': http.request.env['ars_academy.ars_academy'].search([]),
#         })

#     @http.route('/ars_academy/ars_academy/objects/<model("ars_academy.ars_academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ars_academy.object', {
#             'object': obj
#         })
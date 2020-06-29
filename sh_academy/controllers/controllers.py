# -*- coding: utf-8 -*-
from odoo import http

# class ShAcademy(http.Controller):
#     @http.route('/sh_academy/sh_academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sh_academy/sh_academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sh_academy.listing', {
#             'root': '/sh_academy/sh_academy',
#             'objects': http.request.env['sh_academy.sh_academy'].search([]),
#         })

#     @http.route('/sh_academy/sh_academy/objects/<model("sh_academy.sh_academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sh_academy.object', {
#             'object': obj
#         })
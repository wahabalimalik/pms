# -*- coding: utf-8 -*-
from odoo import http

# class PropertyManagementSystem(http.Controller):
#     @http.route('/property_management_system/property_management_system/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/property_management_system/property_management_system/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('property_management_system.listing', {
#             'root': '/property_management_system/property_management_system',
#             'objects': http.request.env['property_management_system.property_management_system'].search([]),
#         })

#     @http.route('/property_management_system/property_management_system/objects/<model("property_management_system.property_management_system"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('property_management_system.object', {
#             'object': obj
#         })
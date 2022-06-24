# -*- coding: utf-8 -*-
# from odoo import http


# class StaffdExam(http.Controller):
#     @http.route('/staffd_exam/staffd_exam/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/staffd_exam/staffd_exam/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('staffd_exam.listing', {
#             'root': '/staffd_exam/staffd_exam',
#             'objects': http.request.env['staffd_exam.staffd_exam'].search([]),
#         })

#     @http.route('/staffd_exam/staffd_exam/objects/<model("staffd_exam.staffd_exam"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('staffd_exam.object', {
#             'object': obj
#         })

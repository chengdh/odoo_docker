# -*- coding: utf-8 -*-
from odoo import http

# class WeShop(http.Controller):
#     @http.route('/we_shop/we_shop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/we_shop/we_shop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('we_shop.listing', {
#             'root': '/we_shop/we_shop',
#             'objects': http.request.env['we_shop.we_shop'].search([]),
#         })

#     @http.route('/we_shop/we_shop/objects/<model("we_shop.we_shop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('we_shop.object', {
#             'object': obj
#         })
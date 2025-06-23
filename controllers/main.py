from odoo import http
from odoo.http import request

class MosconiCategoryController(http.Controller):

    @http.route('/mosconi/categories', type='http', auth='public', website=True)
    def show_categories(self):
        categories = request.env['product.category'].sudo().search([('parent_id', '=', False)])
        return request.render('mosconi.category_cards_template', {'categories': categories})


class MosconiController(http.Controller):

    @http.route('/modal/test', type='http', auth="public", website=True)
    def test_modal_demo(self, **kw):
        return request.render('test.modal.demo')

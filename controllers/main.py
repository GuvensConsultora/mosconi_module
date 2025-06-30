from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)

class MosconiCategoryController(http.Controller):

    @http.route('/mosconi/products', type='http', auth='public', website=True)
    def mostrar_productos(self, category_id=None):
        categ_id = int(category_id)
        productos = request.env['product.template'].sudo().search([('categ_id', '=', categ_id)])
        _logger.info(f"Mostrando productos por  categoría_id={categ_id}: {productos.read()}")
        return request.render('mosconi.products_cards_template', {'products': productos})

    
    @http.route('/mosconi/categories', type='http', auth='public', website=True)
    def mostrar_categorias(self, category_id=None):
        Category = request.env['product.category'].sudo()

        if category_id:
            try:
                parent_id = int(category_id)
                categories = Category.search([('parent_id', '=', parent_id)])
                _logger.info(f"Mostrando hijos de categoría_id={parent_id}: {categories.read()}")
            except ValueError:
                _logger.warning(f"category_id inválido: {category_id}")
                categories = []
        else:
            categories = Category.search([('parent_id', '=', False)])
            _logger.info(f"Mostrando categorías raíz: {categories.read()}")

        return request.render('mosconi.category_cards_template', {'categories': categories})


class MosconiController(http.Controller):

    @http.route('/modal/test', type='http', auth="public", website=True)
    def test_modal_demo(self, **kw):
        return request.render('test.modal.demo')


from odoo import models, fields

class ProductCategory(models.Model):
    _inherit = 'product.category'

    x_card_image = fields.Binary(string='Imagen de carátula', attachment=True)
    x_video_embed = fields.Text(string='Código de video embebido (iframe)')

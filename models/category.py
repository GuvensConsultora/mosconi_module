
from odoo import models, fields

class ProductCategory(models.Model):
    _inherit = 'product.public.category'

    x_video_embed = fields.Text(string='Código de video embebido (iframe)')

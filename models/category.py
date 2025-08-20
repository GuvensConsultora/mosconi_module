
from odoo import models, fields

class ProductCategory(models.Model):
    _inherit = 'product.public.category'

    x_video_embed = fields.Text(string='Código de video embebido (iframe)')

class Producttemplate(models.Model):
    _inherit = 'product.template'

    
    altura_cm = fields.Float(string="Altura en cm.")
    ancho_cm = fields.Float(string="Ancho en cm.")
    prof_cm = fields.Float(string="Profundidad en cm.")
    peso_producto_completo = fields.Float(string="Peso Producto Completo")
    cantidad_bultos = fields.Integer(string="Cantidad de Bultos")
    codigo_ean = fields.Char(string="Código EAN")
    marca = fields.Char(string="Marca")
    garantia = fields.Char(string="Garantía")
    pais_origen = fields.Char(string="País de Origen")
    material_interno = fields.Char(string="Material Interno")
    material_externo_acabado = fields.Char(string="Material Externo / Acabado")
    cantidad_puertas = fields.Char(string="Cantidad de Puertas")
    tipo_apertura = fields.Char(string="Tipo Apertura")
    material_manija = fields.Char(string="Material Manija")
    color_manija = fields.Char(string="Color Manija")
    cantidad_cajones = fields.Char(string="Cantidad de Cajones")
    tipo_corredera = fields.Char(string="Tipo Corredera")
    material_tirador = fields.Char(string="Material Tirador")
    color_tirador = fields.Char(string="Color Tirador")
    peso_admisible = fields.Float(string="Peso Admisible")
    cantidad_tiradores = fields.Integer(string="Cantidad de Tiradores")
    tirador = fields.Char(string="Tirador")
    color = fields.Char(string="Color")
    tipo = fields.Char(string="Tipo")
    capacidad = fields.Char(string="Capacidad")
    cantidad_estantes = fields.Integer(string="Cantidad de Estantes")
    cantidad_estantes_fijos = fields.Char(string="Cantidad Estantes Fijos")
    tipo_vinculacion_fijo = fields.Char(string="Tipo Vinculación Fijos")
    peso_max_admi_fijo = fields.Float(string="Peso Máx. Admisible Fijos")
    cantidad_estantes_flotantes = fields.Char(string="Cantidad Estantes Flotantes")
    tipo_vinculacion_flotante = fields.Char(string="Tipo Vinculación Flotantes")
    peso_max_admi_flotante = fields.Float(string="Peso Máx. Admisible Flotantes")
    cantidad = fields.Integer(string="Cantidad")
    fija_o_regulable = fields.Selection([
        ('fija', 'Fija'),
        ('regulable', 'Regulable')
    ], string="Fija o Regulable")
    material = fields.Char(string="Material")
    color_general = fields.Char(string="Color")
    cant_ruedas = fields.Char(string="Cantidad de Ruedas")
    tipo_rueda = fields.Char(string="Tipo de Rueda")
    freno = fields.Boolean(string="Freno")
    requiere_ensamblado = fields.Boolean(string="Requiere Ensamblado")
    incluye_kit_instalacion = fields.Boolean(string="Incluye kit de instalación")
    medidas_peso_bulto_1 = fields.Char(string="Medidas + Peso Bulto 1")
    medidas_peso_bulto_2 = fields.Char(string="Medidas + Peso Bulto 2")
    medidas_peso_bulto_3 = fields.Char(string="Medidas + Peso Bulto 3")
    medidas_peso_bulto_4 = fields.Char(string="Medidas + Peso Bulto 4")

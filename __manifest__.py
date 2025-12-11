{
    'name': 'Mosconi Website',
    'version': '18.0',
    'summary': 'Categorías con tarjeta, imagen, video embebido y wizard visual',
    'description': 'Módulo para mostrar categorías, subcategorías y productos con soporte para videos en modales.',
    'images': ['static/description/icon.png'],
    'author': 'Guvens Consultora',
    'website': 'https://www.yaguven.com',
    'depends': ['website_sale', 'product'],
    'assets': {
        'web.assets_frontend': [
            'mosconi_module/static/src/css/hover_modal.css',
            'mosconi_module/static/src/js/hover_modal_define.js',
        ],
    },
    'data': [
        'views/templates.xml',
        'views/category_templates.xml',
        'views/products_templates.xml',
        'views/category_form.xml',
        'views/product_template_child.xml',
        'views/product_page_template.xml',
        'views/product_template_views.xml',
        'views/product_product_views.xml',
    ],
    'license':'OEEL-1',
    'installable': True,
    'application': True,
}

{
    'name': 'Mosconi Website',
    'version': '1.3',
    'summary': 'Categorías con tarjeta, imagen, video embebido y wizard visual',
    'description': 'Módulo para mostrar categorías, subcategorías y productos con soporte para videos en modales.',
    'images': ['static/description/icon.png'],
    'author': 'Guvens Consultora',
    'website': 'https://www.yaguven.com',
    'depends': ['website', 'product'],
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
    ],
    'installable': True,
    'application': True,
}

# -*- coding: utf-8 -*-

{
    'name': 'payment_weixin',
    'category': 'Website',
    'summary': 'Payment Acquirer: Weixin Implementation',
    'version': '1.0',
    'description': """Weixin Payment Acquirer""",
    'author': 'Odoo CN Community, Jeffery <jeffery9@gmail.com>',
    'depends': ['payment'],
    'data': [
        'views/weixin.xml',
        'views/payment_acquirer.xml',
        'data/weixin.xml',
    ]
}

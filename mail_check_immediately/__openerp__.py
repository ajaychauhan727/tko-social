# -*- coding: utf-8 -*-
{
    'name': 'Check mail immediately',
    'version': '1.0.1',
    'author': 'Ivan Yelizariev, ThinkOpen Solutions Brasl',
    'license': 'LGPL-3',
    "category": "Discuss",
    "support": "apps@it-projects.info",
    'website': 'https://twitter.com/yelizariev',
    'price': 9.00,
    'currency': 'EUR',
    'depends': ['base', 'web', 'fetchmail', 'mail'],
    'data': [
        'views.xml',
    ],
    'qweb': [
        "static/src/xml/main.xml",
    ],
    'installable': True
}

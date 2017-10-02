# -*- coding: utf-8 -*-
# © 2017 Phuc.nt - <phuc.nt@komit-consulting.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'web_widget_text_markdown',
    'version': '10.0.1.0.0',
    "author": "Komit, "
              "Odoo Community Association (OCA)",
    'category': 'Web',
    'license': 'AGPL-3',
    'website': 'http://www.komit-consulting.com',
    'depends': [
        'base', 'web'
    ],
    'data': [
        'views/main.xml',
    ],
    "qweb": [
        "static/src/xml/bootstrap_markdown.xml",
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}

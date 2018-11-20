# -*- coding: utf-8 -*-
{
    'name': "Property Management System",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',


    'depends': ['base','web'],
    'data': [
        'data/ir_sequence_data.xml',
        'views/menuitems.xml',
        'views/templates.xml',
        'views/society.xml',
        'views/fms.xml',
        'views/members.xml',
        'views/view.xml',
        'views/ir_sequence.xml',
        # 'security/ir.model.access.csv',
    ],
    'qweb': ['static/src/xml/*.xml'],

    'application': True,
}
{
    'name': "ToDo",

    'summary': "",

    'description': "",

    'author': "Odoo",
    'website': "TVS",

    'category': '',
    'version': '0.1',
    'application': True,
    'installable': True,


    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/todos.xml',
        'views/students.xml',
        'views/department.xml',
        'views/course.xml',
        'views/todo/templates.xml',
        'views/students/templates.xml',
        'views/add/templates.xml',
        'views/update/templates.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'todos/static/src/**/*',
        ],
        'todos.assets_todo': [
            'todos/static/src/components/todo/**/*',
        ],
        'todos.assets_students': [
            'todos/static/src/components/students/**/*',
        ],
        'todos.assets_add': [
            'todos/static/src/components/add/**/*',
        ],
        'todos.assets_update': [
            'todos/static/src/components/update/**/*',
        ],

    }
}

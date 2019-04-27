{
    'name': 'One Signal Notification Connector',
    'summary': 'The One Signal Notification Connector',
    'version': '10.0.1.0',
    'category': 'Push Notification',
    'summary': """The One Signal Notification""",
    'author': "Khudrath Ali Baig",
    'maintainer': "Khudrath Ali Baig<alibaigkhudrath@gmail.com>",

    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'views/one_signal_notification_view.xml',
        'views/res_users_view.xml',
        'views/one_signal_notification_messages.xml',
        'views/one_signal_users.xml',
        'views/menu.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install':False,
}

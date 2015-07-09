WTF_CSRF_ENABLED = True
SECRET_KEY = 'Ooh-So-Secret'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

USERS = [
	{'pin': 1271, 'firstName': 'Aaron', 'secondName': 'Griffin', 'level': 9001, 'id': 0},
	{'pin': 223355, 'firstName': 'Test', 'secondName': 'Testersson', 'level': 20, 'id': 1}
]

import requests

ss = requests.session()
ss.headers.update({
    'userAgent': 'string'
})
ss.cookies.set("cook_name",'cook_value')
resp = ss.get('url',headers=ss.headers)

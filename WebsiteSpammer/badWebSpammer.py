import requests, os, random, string, json

url = 'insert bad site here'

random.seed = (os.urandom(1024))

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
names = json.loads(open('randomNames.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@gmail.com'
    password = ''.join(random.choice(chars) for i in range(10))

requests.post(url, allow_redirects = False, data={
    'enter username web token here': username
    'enter password token here': password
})

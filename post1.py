import requests

key_dirct = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data = key_dirct)
print(r.text)
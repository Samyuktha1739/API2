import requests

cookie = {'visit-month': 'February'}
response = requests.get("https://gorest.co.in/", allow_redirects=False, cookies=cookie)

print(response.history)
print(response.status_code)

# se = requests.sessions()
# se.cookies.update({'visit-month': 'February'})
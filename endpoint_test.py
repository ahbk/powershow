import requests

token = '6eb6f069523055a339d71e5b1f6c88cc'
url = 'http://test.growatt.com/v1/'

register_endpoint = url + 'user/user_register'
register_payload = {
        'user_name': 'qtuser3',
        'user_password': '123456',
        'user_email': '770988255@qq.com',
        'user_tel': '13525653256',
        'user_country': 'China',
        'user_type': 1,
        'token': token,
        }

check_endpoint = url + 'user/check_user'
check_payload = {
        'user_name': 'admin',
        'token': token,
        }

modify_endpoint = url + 'user/modify'
modify_payload = {
        'c_user_id': 3,
        'mobile': '13525653256',
        'token': token,
        }

list_endpoint = url + 'user/c_user_list'
list_payload = {
        'page': 1,
        'perpage': 10,
        'token': token,
        }

#r = requests.post(register_endpoint , data=register_payload)
#r = requests.post(check_endpoint , data=check_payload)
#r = requests.post(modify_endpoint , data=modify_payload)
r = requests.post(list_endpoint , data=list_payload)



print(r);
print(r.text);

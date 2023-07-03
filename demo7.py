import requests
import data


def Login_Dummy_web(username,password):
    LOGIN_URL='https://the-internet.herokuapp.com/authenticate'
    SECURE_URL='https://the-internet.herokuapp.com/secure'

    ACCESS_DATA={
             'username':username,
             'password' :password
    }

    RESULT=requests.post(LOGIN_URL,data=ACCESS_DATA)
    RESULT2=requests.get(SECURE_URL)
    return RESULT2.text


print(Login_Dummy_web(data.username,data.password))
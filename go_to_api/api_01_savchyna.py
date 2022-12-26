import requests

server = "https://qauto.forstudy.space/api"

# реєстрація юзера
def authSignUp():
    endpoint = "/auth/signup"
    parameters = {
      "name": "Nastya",
      "lastName": "Savchyna",
      "email": "qwe@test.com",
      "password": "Qwerty12345",
      "repeatPassword": "Qwerty12345"
    }
    r = requests.post(server+endpoint, json=parameters)
    server_says = r.json()
    return server_says

#використовую дані юзера, якого я створила
def authSignIn():
    endpoint = '/auth/signin'
    parameters = {
        "email": "qwe@test.com",
        "password": "Qwerty12345",
        "remember": False
    }
    r = requests.post(server+endpoint, json=parameters)
    server_says = r.json()
    return server_says


#запит гет
def usersCurrent():
    endpoint = '/users/current'
    r = requests.get(server+endpoint)
    server_says = r.json()
    return server_says

def authLogOut():
    endpoint = '/auth/logout'
    r = requests.get(server+endpoint)
    server_says = r.json()
    return server_says


print(authSignUp())
print(authSignIn())
print(usersCurrent())
print(authLogOut())

'''
if "status" in server_says:
    if server_says["status"] == "ok":
        print("all ok")
    else:
        print(server_says['message'])
'''
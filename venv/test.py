import requests
BASE="http://127.0.0.1:5000/"
from pprint import pprint
# BASE="https://chatbothealthdevcprj.herokuapp.com/"


# response = requests.get(BASE + "login",{'username':"nam",'password':'123456Nam'})
# print(response.json())

# response=requests.get(BASE+"history",{"id":"000ebc858861aca26bac9b49f650ed424cf882fc"})
# print(response.json())

response=requests.get(BASE+"recommend",{"id":"000ebc858861aca26bac9b49f650ed424cf882fc"})
pprint(response.json())
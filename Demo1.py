import pytest
import requests

@pytest.mark.usefixtures("setup")

class Demo1:
    getData_response = requests.get("https://dummy.restapiexample.com/api/v1/employees")
    print(getData_response)
    print(getData_response.text)

    getData_response1 = requests.get("https://dummy.restapiexample.com/api/v1/employee/1")
    print(getData_response1)
    print(getData_response1.text)

    postData_response = requests.post("https://dummy.restapiexample.com/api/v1/create")
    print(postData_response)
    print(postData_response.text)

    putData_response = requests.put("https://dummy.restapiexample.com/public/api/v1/update/21")
    print(putData_response)
    print(putData_response.text)

    deleteData_response = requests.delete("https://dummy.restapiexample.com/public/api/v1/delete/2")
    print(deleteData_response)
    print(deleteData_response.text)
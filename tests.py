import requests

from random import randint

for i in range(100):
    params = {"x" : randint(1,10000),
              "y" : randint(1,10000)}
    add_nums = requests.get("http://127.0.0.1:5000/add_nums", params=params)
    pid = add_nums.json()["pid"]
    print "pid for celeryjob", pid

    add_result = requests.get("http://127.0.0.1:5000/get_additions/{}".format(pid))
    print add_result.json()["result"]


from multiprocessing import Process
import requests
from datetime import datetime

def do_post():
  url = "https://192.168.33.73:82/backend/service/v4

  payload = {'arg1': '1',
  'arg2': '0'}
  files=[
    ('file',('1.wav',open('/home/user/Downloads/1.wav','rb'),'audio/wav'))
  ]
  headers = {}

  print(datetime.now())
  response = requests.request("POST", url, headers=headers, data=payload, files=files, verify=False)
  print(response.status_code, response.text)

def runInParallel(*fns):
  for fn in fns:
    p = Process(target=fn)
    p.start()

runInParallel(*[do_post for _ in range(30)])

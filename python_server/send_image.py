from bottle import route, run, request, static_file
from pathlib2 import Path
import time
import os

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

@route('/img_for_api', method='GET')
def img_for_api():
    time.sleep(5)
    return static_file("img_for_api.jpg", root=dir_path)


run(host='0.0.0.0', port=8080, debug=True, reloader=True)

from bottle import route, run, request, static_file
from pathlib2 import Path
import time
import os

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)


@route('/img_for_api/<random_number>', method='GET')
def img_for_api(random_number=0):
    return static_file("img_for_api.jpg", root=dir_path)


@route('/add_img', method='GET')
def add_img():
    return static_file("add_img.jpg", root=dir_path)


run(host='0.0.0.0', port=8080, debug=True, reloader=True)

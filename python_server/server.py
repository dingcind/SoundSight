from bottle import route, run, request
from pathlib2 import Path
import time
import os
#from PIL import Image
import math
import sys
import cv2
import base64
from io import StringIO
import json

new_image_path = "img.jpg"
resulting_data_path = "result.txt"

os.chdir("../yolo-9000/darknet/python")
sys.path.append(os.getcwd())
time.sleep(0.1)
from darknet import *

os.chdir("..")
net = load_net("cfg/yolo9000.cfg", "../yolo9000-weights/yolo9000.weights", 0)
meta = load_meta("cfg/combine9k.data")
#r = detect(net, meta, "data/dog.jpg")
os.chdir("../../python_server")

class Item:
	def __init__(self, name, pos, size):
		self.name = name
		self.pos = pos
		self.size = size
		self.age = 0

	def move(self, new_pos, new_size):
		self.age = -1
		self.pos = new_pos
		self.size = new_size

	def check_age(self):
		self.age += 1
		if self.age < 5:
			return self
		else:
			return None

	def to_dict(self):
		return {"name":self.name, "pos":self.pos, "size":self.size}


def normalize(new_data):
        new_data = sorted(new_data, key=lambda k: k["prob"])
	global items_global
	for each in new_data:
		for item in items_global:
			if abs(item.pos-each["pos"]) < 0.1 and abs(item.size-each["size"]) < 0.1:
				item.move(each["pos"], each["size"])
				break
		else:
			items_global.append(Item(each["name"], each["pos"], each["size"]))
	live_items = []
	for item in items_global:
		live_items.append(item.check_age())
	while None in live_items:
		live_items.remove(None)
	return [x.to_dict() for x in live_items]


@route('/main', method='POST')
def main():
	new_image = open(new_image_path, "wb")
        #print(request.body.read())
        #print(dir(request.body.read()))
	img_data = request.body.read()
        img_data = img_data.decode()
        i = StringIO(img_data)
        dit = json.load(i)
        text = dit["img"]
        text = text.encode("ascii")
	new_image.write(base64.decodestring(text))
	new_image.close()
	r = detect(net, meta, new_image_path)
	im = cv2.imread(new_image_path)
        #print(im.shape)
	width_max, height_max = im.shape[0:2]
        #im = cv2.rectangle(im, (), (), (255,0,0,), 7)
	#os.system("rm -rf " + new_image_path)
        print(r)
	objects = []
	for obj in r:
                width = int(obj[2][2]/2)
                height = int(obj[2][3]/2)
                x = int(obj[2][0])
                y = int(obj[2][1])
		name = obj[0]
		pos = (x,y)
		size = width*height / (width_max * height_max) 
		#objects.append({"name":name, "pos":pos, "size":size, "prob":obj[1]})

                im = cv2.rectangle(im, (x+width, y+height), (x-width, y-height), (255, 0, 0), 7)
                pos = (float(x)/float(width) - 0.5, float(y)/float(height) - 0.5)
                objects.append({"name":name, "pos":pos, "size":size, "prob":obj[1]})
        cv2.imwrite("test.png", im)
        print("*********")
        print("Before Normalization")
	objects = normalize(objects)
        print("After Normalization")
        print(objects)
        print("************\n**************")
	return {"data": objects}  # NOTE: For security reasons, you CANNOT return a top level array. Send it as {"data":[array]}

@route('/get_example')
def get_example():
	return {"data": [{"pos": -0.3, "size": 0.3, "name": "Quin"}, {"pos": 0.7, "size": 0.6, "name": "Anna"}]}

run(host='0.0.0.0', port=80, debug=True, reloader=True)


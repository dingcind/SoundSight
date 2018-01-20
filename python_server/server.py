from bottle import route, run, request
from pathlib2 import Path
import time
import os
from PIL import Image
import math

new_image_path = "img.png"
resulting_data_path = "result.txt"

os.chdir("../yolo-9000/darknet/python")
from darknet import *

os.chdir("..")
net = load_net("cfg/yolo9000.cfg", "../yolo9000-weights/yolo9000.weights", 0)
meta = load_meta("cfg/combine9k.data")
#r = detect(net, meta, "data/dog.jpg")

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


items_global = []


def normalize(new_data):
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
	img_data = request.data.read()
	new_image.write(img_data.decode)
	new_image.close()
	r = detect(net, meta, new_image_path)
	im = Image.open(new_image_path)
	width, height = im.size
	os.system("rm -rf " + new_image_path)

	objects = []
	for obj in r:
		name = obj[0]
		pos = ((obj[2][0] + obj[2][2])/2/width, (obj[2][1] + obj[2][3])/2/height)
		size = (math.fabs(obj[2][0] - obj[2][2]) * math.fabs(obj[2][1] - obj[2][3]))
		objects.append({"name":name, "pos":pos, "size":size})
	objects = normalize(objects)
	return {"data": normalize(objects)}  # NOTE: For security reasons, you CANNOT return a top level array. Send it as {"data":[array]}

@route('/get_example')
def get_example():
	return {"data": [{"pos": -0.3, "size": 0.3, "name": "Quin"}, {"pos": 0.7, "size": 0.6, "name": "Anna"}]}

#run(host='0.0.0.0', port=80, debug=True, reloader=True)

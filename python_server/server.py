from bottle import route, run, request
from pathlib2 import Path
import time

new_image_path = "/Users/2017-A/Dropbox/hackathon/SoundSight/python_server/test.txt"
resulting_data_path = "/Users/2017-A/Dropbox/hackathon/SoundSight/python_server/result.txt"

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


items = []
def normalize(new_data):
	global items
	for each in new_data:
		for item in items:
			if abs(item.pos-each["pos"]) < 0.1 and abs(item.size-each["size"]) < 0.1:
				item.move(each["pos"], each["size"])
				break
		else:
			items.append(Item(each["name"], each["pos"], each["size"]))
	live_items = []
	for item in items:
		live_items.append(item.check_age())
	while None in live_items:
		live_items.remove(None)
	return [x.to_dict() for x in live_items]


@route('/main', method='POST')
def main():
	new_image_file = Path(new_image_path)
	while new_image_file.is_file():
		time.sleep(0.5)
		print("Waiting for previous image to disappear")
	new_image = open(new_image_path, "w")
	new_image.write(request.data.read())
	new_image.close()

	resulting_data_file = Path(resulting_data_path)
	while not resulting_data_file.is_file():
		time.sleep(0.5)
		print("Waiting for new results to appear")
	resulting_data = open(resulting_data_path).read()
	resulting_data_string = resulting_data.read()
	resulting_data.close()
	return {"data":resulting_data_string}  # NOTE: For security reasons, you CANNOT return a top level array. Send it as {"data":[array]}

@route('/get_example')
def get_example():
	return {"data": [{"pos": -0.3, "size": 0.3, "name": "Quin"}, {"pos": 0.7, "size": 0.6, "name": "Anna"}]}

#run(host='0.0.0.0', port=80, debug=True, reloader=True)

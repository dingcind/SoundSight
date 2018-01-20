from bottle import route, run, request
from pathlib2 import Path
import time

new_image_path = "/Users/2017-A/Dropbox/hackathon/SoundSight/python_server/test.txt"
resulting_data_path = "/Users/2017-A/Dropbox/hackathon/SoundSight/python_server/result.txt"

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

run(host='localhost', port=8080, debug=True)

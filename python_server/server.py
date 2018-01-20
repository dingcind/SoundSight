from bottle import route, run, request

@route('/main', method='POST')
def main():
	print(request.body.read())
	return {"data": "HI"}  # NOTE: For security reasons, you CANNOT return a top level array. Send it as {"data":[array]}

@route('/get_example')
def get_example():
	return {"data": [{"pos": 0, "size": 0.3, "name": "Quin"}, {"pos": 0.7, "size": 0.6, "name": "Anna"}]}

run(host='localhost', port=8080, debug=True)

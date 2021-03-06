import httplib, urllib, base64, json
import time

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = '0c723cbc14cf4d0abe07932a39484b0b'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.

def get_info():
	uri_base = 'westcentralus.api.cognitive.microsoft.com'

	# Request headers.
	headers = {
		'Content-Type': 'application/json',
		'Ocp-Apim-Subscription-Key': subscription_key,
	}

	# Request parameters.
	params = urllib.urlencode({
		'returnFaceId': 'true',
		'returnFaceLandmarks': 'false',
		'returnFaceAttributes': 'age,gender,facialHair,glasses,hair,makeup,accessories',
	})

	# The URL of a JPEG image to analyze.
	body = "{'url':'https://upload.wikimedia.org/wikipedia/commons/c/c3/RH_Louise_Lillian_Gish.jpg'}"

	try:
		# Execute the REST API call and get the response.
		conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
		conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
		response = conn.getresponse()
		data = response.read()

		# 'data' contains the JSON data. The following formats the JSON data for display.
		parsed = json.loads(data)
		print ("Response:")
		print (json.dumps(parsed, sort_keys=True, indent=2))
		conn.close()

	except Exception as e:
		print("[Errno {0}] {1}".format(e.errno, e.strerror))

def create_group():
	# Request headers.
	headers = {
		'Content-Type': 'application/json',
		'Ocp-Apim-Subscription-Key': "0c723cbc14cf4d0abe07932a39484b0b",
	}

	# Request parameters.
	params = urllib.urlencode({
		'personGroupId': 'uoft_hackathon_soundsight'
	})

	# The URL of a JPEG image to analyze.
	body = '{"name": "friends", "userData": ""}'

	try:
		# Execute the REST API call and get the response.
		conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
		conn.request("PUT", "/face/v1.0/persongroups/{personGroupId}?%s" % params, body, headers)
		response = conn.getresponse()
		data = response.read()
		# 'data' contains the JSON data. The following formats the JSON data for display.
		parsed = json.loads(data)
		print("Response:")
		print(json.dumps(parsed, sort_keys=True, indent=2))
		conn.close()
	except Exception as e:
		print(e)
		print("[Errno {0}] {1}".format(e.errno, e.strerror))


def add_person(name):
	# Request headers.
	headers = {
		'Content-Type': 'application/json',
		'Ocp-Apim-Subscription-Key': "0c723cbc14cf4d0abe07932a39484b0b",
	}

	# Request parameters.
	params = urllib.urlencode({
		'personGroupId': 'uoft_hackathon_soundsight'
	})

	# The URL of a JPEG image to analyze.
	body = '{"name": \"' + name + '\"}'

	try:
		# Execute the REST API call and get the response.
		conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
		conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/persons?%s" % params, body, headers)
		response = conn.getresponse()
		data = response.read()
		# 'data' contains the JSON data. The following formats the JSON data for display.
		parsed = json.loads(data)
		print("Response:")
		print(json.dumps(parsed, sort_keys=True, indent=2))
		conn.close()
	except Exception as e:
		print(e)
		print("[Errno {0}] {1}".format(e.errno, e.strerror))

def add_image(person_id, img_path):
	# Request headers.
	headers = {
		'Content-Type': 'application/json',
		'Ocp-Apim-Subscription-Key': "0c723cbc14cf4d0abe07932a39484b0b",
	}

	# Request parameters.
	params = urllib.urlencode({
		'personGroupId': 'uoft_hackathon_soundsight',
		'personId': person_id
	})

	# The URL of a JPEG image to analyze.
	from_file = open(img_path, "rb")
	to_file = open("add_img.jpg", "wb")
	to_file.write(from_file.read())
	to_file.close()

	body = '{"url": "http://34.214.105.118:8080/add_img"}'

	try:
		# Execute the REST API call and get the response.
		conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
		conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/persons/{personId}/persistedFaces?%s" % params, body, headers)
		response = conn.getresponse()
		data = response.read()
		# 'data' contains the JSON data. The following formats the JSON data for display.
		parsed = json.loads(data)
		print("Response:")
		print(json.dumps(parsed, sort_keys=True, indent=2))
		conn.close()
	except Exception as e:
		print(e)
		print("[Errno {0}] {1}".format(e.errno, e.strerror))


def train():
	# Request headers.
	headers = {
		'Ocp-Apim-Subscription-Key': "0c723cbc14cf4d0abe07932a39484b0b"
	}

	# Request parameters.
	params = urllib.urlencode({
		'personGroupId': 'uoft_hackathon_soundsight'
	})

	body = '{"url": "34.214.105.118:8080/add_img"}'

	try:
		# Execute the REST API call and get the response.
		conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
		conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/train?%s" % params, body, headers)
		response = conn.getresponse()
		data = response.read()
		# 'data' contains the JSON data. The following formats the JSON data for display.
		if data == "":
			print("Training command sent!")
		conn.close()
	except Exception as e:
		print(e)
		print("[Errno {0}] {1}".format(e.errno, e.strerror))


def find_faces():
	# Request headers.
	headers = {
		'Content-Type': 'application/json',
		'Ocp-Apim-Subscription-Key': "0c723cbc14cf4d0abe07932a39484b0b",
	}

	# Request parameters.
	params = urllib.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': '',
	})

	body = '{"url": "http://34.214.105.118:8080/img_for_api/' + str(int(time.time())) + '"}'
	print(body)

	try:
		# Execute the REST API call and get the response.
		conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
		conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
		response = conn.getresponse()
		data = response.read()
		# 'data' contains the JSON data. The following formats the JSON data for display.
		parsed = json.loads(data)
		conn.close()
		print("Find faces result:")
                print(parsed)
		got_data = {}
		for each in parsed:
			got_data[each["faceId"]] = {"pos":each["faceRectangle"]["left"]+each["faceRectangle"]["width"]/2, "size":each["faceRectangle"]["width"], "name":"unknown person"}
		print(got_data)
		return got_data
	except Exception as e:
		print(e)
		print("[Errno {0}] {1}".format(e.errno, e.strerror))
		return {}


def test_img():
	names = {"46785984-904d-4b78-985b-c789b9f959b1":"Anna", "2918f938-b015-4804-a760-320dca7e5b58":"Cindy", "31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33":"Morris", "2aa02459-64b1-43b6-b733-e078200890ce":"Quin"}

	headers = {
		'Content-Type': 'application/json',
		'Ocp-Apim-Subscription-Key': "0c723cbc14cf4d0abe07932a39484b0b",
	}

	# Request parameters.
	params = urllib.urlencode({
	})

	all_faces = find_faces()
        if all_faces == {}:
                return {}

	body = '{"personGroupId": "uoft_hackathon_soundsight","faceIds": [\"' + '\",\"'.join(all_faces.keys()) + '\"]}'

	try:
		# Execute the REST API call and get the response.
		conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
		conn.request("POST", "/face/v1.0/identify?%s" % params, body, headers)
		response = conn.getresponse()
		data = response.read()
		# 'data' contains the JSON data. The following formats the JSON data for display.
		parsed = json.loads(data)
		print("Test img result:")
		print(json.dumps(parsed, sort_keys=True, indent=2))
		conn.close()
		for each in parsed:
			if len(each["candidates"]) >= 1:
				all_faces[each["faceId"]]["name"] = names[each["candidates"][0]["personId"]]
		print(all_faces)
		return all_faces
	except Exception as e:
		print(e)
		print("[Errno {0}] {1}".format(e.errno, e.strerror))
		return all_faces


#create_group()
#add_person("Anna")
# Anna ID: c1d260e2-097f-409d-ac50-24042261612d
# add_person("Cindy")
# Cindy ID: 2918f938-b015-4804-a760-320dca7e5b58
#add_person("Morris")
# Morris ID: 31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33
#add_person("Quin")
# Quin ID: 2aa02459-64b1-43b6-b733-e078200890ce

#Anna
"""
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_201759.jpg')
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_201804.jpg')
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_201806.jpg')
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_201818.jpg')
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_201828.jpg')
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_201831.jpg')
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_201834.jpg')
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_201853.jpg')
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_201902.jpg')
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_201919.jpg')
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_201921.jpg')
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_201923.jpg')
time.sleep(3)
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_201929.jpg')
time.sleep(3)
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_201954.jpg')
time.sleep(3)
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_201958.jpg')
time.sleep(3)
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_201959.jpg')
time.sleep(3)
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_202002.jpg')
time.sleep(3)
add_image('46785984-904d-4b78-985b-c789b9f959b1', 'photos/anna/IMG_20180120_202039.jpg')

# Cindy
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201240.jpg')
time.sleep(3)
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201247.jpg')
time.sleep(3)
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201249.jpg')
time.sleep(3)
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201252.jpg')
time.sleep(3)
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201303.jpg')
time.sleep(3)
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201320.jpg')
time.sleep(3)
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201334.jpg')
time.sleep(3)
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201346.jpg')
time.sleep(3)
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201348.jpg')
time.sleep(3)
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201614.jpg')
time.sleep(3)
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201622.jpg')
time.sleep(3)
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201651.jpg')
time.sleep(3)
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201654.jpg')
time.sleep(3)
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201729.jpg')
time.sleep(3)
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201732.jpg')
time.sleep(3)
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201734.jpg')
time.sleep(3)
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201739.jpg')


# Morris
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204110.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204112.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204114.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204115.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204117.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204118.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204130.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204133.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204141.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204144.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204146.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204148.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204202.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204211.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204217.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204221.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204223.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204227.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204231.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204233.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204236.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204304.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204307.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204309.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204310.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204313.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204314.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204317.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204336.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204349.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204350.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204351.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204358.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204401.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204403.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204405.jpg')
time.sleep(3)
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204415.jpg')
time.sleep(3)

# Quin
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222837.jpg')
time.sleep(3)
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222846.jpg')
time.sleep(3)
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222848.jpg')
time.sleep(3)
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222849.jpg')
time.sleep(3)
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222852.jpg')
time.sleep(3)
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222854.jpg')
time.sleep(3)
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222855.jpg')
time.sleep(3)
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222857.jpg')
time.sleep(3)
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222904.jpg')
time.sleep(3)
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222909.jpg')
time.sleep(3)
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222910.jpg')
time.sleep(3)
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222911.jpg')
time.sleep(3)
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222920.jpg')
time.sleep(3)
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_233701.jpg')
time.sleep(3)
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_233705.jpg')
time.sleep(3)
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_233707.jpg')
time.sleep(3)
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_233710.jpg')
time.sleep(3)
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_233713.jpg')
"""
# "83d9f8ca-32ab-4f9d-932d-09b2542cf6c6"
#test_img()

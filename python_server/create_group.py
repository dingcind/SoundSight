import httplib, urllib, base64, json

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
		'person_id': person_id
	})

	# The URL of a JPEG image to analyze.
	from_file = open(img_path, "rb")
	to_file = open("add_img.jpg", "wb")
	to_file.write(from_file.read())
	to_file.close()

	body = '{"url": "34.214.105.118:8080/add_img"}'

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
		'Ocp-Apim-Subscription-Key': "0c723cbc14cf4d0abe07932a39484b0b",
	}

	# Request parameters.
	params = urllib.urlencode({
		'personGroupId': 'uoft_hackathon_soundsight',
	})

	# The URL of a JPEG image to analyze.
	from_file = open(img_path, "rb")
	to_file = open("add_img.jpg", "wb")
	to_file.write(from_file.read())
	to_file.close()

	body = '{"url": "34.214.105.118:8080/add_img"}'

	try:
		# Execute the REST API call and get the response.
		conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
		conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/train?%s" % params, "{body}", headers)
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


def test_img():
	# Request headers.
	headers = {
		'Content-Type': 'application/json',
		'Ocp-Apim-Subscription-Key': "0c723cbc14cf4d0abe07932a39484b0b",
	}

	# Request parameters.
	params = urllib.urlencode({
    "personGroupId":"uoft_hackathon_soundsight",
    "faceIds":[
        "c1d260e2-097f-409d-ac50-24042261612d",
        "2918f938-b015-4804-a760-320dca7e5b58",
        "31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33",
        "2aa02459-64b1-43b6-b733-e078200890ce"
    ]
	})

	body = '{"url": "34.214.105.118:8080/img_for_api"}'

	try:
		# Execute the REST API call and get the response.
		conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
		conn.request("POST", "/face/v1.0/identify?%s" % params, body, headers)
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


#create_group()
# add_person("Anna")
# Anna ID: c1d260e2-097f-409d-ac50-24042261612d
# add_person("Cindy")
# Cindy ID: 2918f938-b015-4804-a760-320dca7e5b58
#add_person("Morris")
# Morris ID: 31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33
#add_person("Quin")
# Quin ID: 2aa02459-64b1-43b6-b733-e078200890ce

#Anna
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201754.jpg')
"""
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201756.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201759.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201802.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201804.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201806.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201815.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201818.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201819.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201821.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201828.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201831.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201834.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201853.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201902.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201919.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201921.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201923.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201925.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201929.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201954.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201957.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201958.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_201959.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_202002.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_202038.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_202039.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_202041.jpg')
add_image('c1d260e2-097f-409d-ac50-24042261612d', 'photos/anna/IMG_20180120_202043.jpg')


# Cindy
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201233.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201237.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201240.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201247.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201249.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201252.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201303.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201320.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201328.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201334.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201346.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201348.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201614.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201622.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201651.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201654.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201729.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201732.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201734.jpg')
add_image('2918f938-b015-4804-a760-320dca7e5b58', 'photos/cindy/IMG_20180120_201739.jpg')

# Morris
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204103.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204104.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204106.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204107.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204108.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204110.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204112.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204114.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204115.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204117.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204118.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204130.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204133.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204141.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204144.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204146.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204148.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204202.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204211.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204217.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204221.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204223.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204227.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204231.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204233.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204236.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204304.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204307.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204309.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204310.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204313.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204314.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204317.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204336.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204339.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204346.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204349.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204350.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204351.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204353.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204355.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204358.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204401.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204403.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204405.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204408.jpg')
add_image('31e9be1e-cf21-4c53-b5f8-dd5ec9b64c33', 'photos/morris/IMG_20180120_204415.jpg')

# Quin
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222837.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222846.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222848.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222849.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222850.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222852.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222854.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222855.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222857.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222904.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222909.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222910.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222911.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_222920.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_233701.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_233705.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_233707.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_233710.jpg')
add_image('2aa02459-64b1-43b6-b733-e078200890ce', 'photos/quin/IMG_20180120_233713.jpg')

train()

test_img()
"""
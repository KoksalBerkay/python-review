from subprocess import Popen, PIPE
import requests
import webbrowser


def execute_return(cmd):
	"""
	Execute a command and return the output and error
	
	:param cmd: The command to execute
	:return: The output of the command and any errors.
	"""
	args = cmd.split()
	proc = Popen(args, stdout=PIPE, stderr=PIPE)
	out, err = proc.communicate()
	return out, err


def make_req(error):
	"""
	This function takes in an error and makes a request to the Stack Overflow API
	
	:param error: The error message you want to search for
	:return: The json object that is returned from the API call.
	"""
	resp = requests.get("https://api.stackexchange.com/" +
						"/2.2/search?order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(error))
	return resp.json()


def get_urls(json_dict):
	"""
	This function takes a dictionary of the JSON data from the Stack Overflow API and returns a list of
	the URLs of the top three questions that are answered
	
	:param json_dict: the dictionary that contains the JSON data
	"""
	url_list = []
	count = 0
	
	for i in json_dict['items']:
		if i['is_answered']:
			url_list.append(i["link"])
		count += 1
		if count == 3 or count == len(i):
			break
	
	for i in url_list:
		webbrowser.open(i)


out, err = execute_return("python D:\Repo\python-review\deneme.py")

error = err.decode("utf-8").strip().split("\r\n")[-1]
print(error)

if error:
	filter_error = error.split(":")
	json1 = make_req(filter_error[0])
	json2 = make_req(filter_error[1])
	json = make_req(error)
	get_urls(json1)
	get_urls(json2)
	get_urls(json)
	
else:
	print("No error found")

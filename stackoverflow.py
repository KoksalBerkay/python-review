from subprocess import Popen, PIPE
import requests
import webbrowser

# Debugging errors
def execute_return(cmd):
	args = cmd.split()
	proc = Popen(args, stdout=PIPE, stderr=PIPE)
	out, err = proc.communicate()
	return out, err

# Using GET Method to get answered question data
def make_req(error):
	resp = requests.get("https://api.stackexchange.com/" +
						"/2.2/search?order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(error))
	return resp.json()

# Storing urls
def get_urls(json_dict):
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

# Change this path to your python file
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

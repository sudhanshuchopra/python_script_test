import requests

try:
	k=requests.get("http://www.sudhanshuchopra.com")
	print(k.text)
except:
	print("requests not working")

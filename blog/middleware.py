import requests

class email:
	 def __init__(self, get_response):
	 	self.get_response = get_response
	 def __call__(self, request):
	 		response = self.get_response(request)
	 		if(request.method == "POST"):
	 			print(str(request.POST['content']))
	 		return response

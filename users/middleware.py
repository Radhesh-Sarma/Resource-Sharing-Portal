import requests
from django.conf import settings
from ipware import get_client_ip
import datetime

class ipaddress:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self,request):
        ip, is_routable = get_client_ip(request)
        f = open("iplog.txt","a")
        f.write("URL "  + str(request.method) + " " + str(request.path_info)+ '\n')
        f.write("USERNAME : " + str(request.user.get_username())+ '\n')
        f.write("IP ADDRESS :" + str(ip)+ '\n')
        f.write("TIMESTAMP : " + str(datetime.datetime.now())+ '\n')
        f.write("DEVICE INFO: " + str(request.headers['User-Agent']) + '\n' + '\n')
        response = self.get_response(request)
        return response
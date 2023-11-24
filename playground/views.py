from django.shortcuts import render
from .tasks import *
from django.core.mail  import BadHeaderError
from templated_mail.mail import BaseEmailMessage
import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
import logging
logger = logging.getLogger(__name__)

class HelloView(APIView):
    @method_decorator(cache_page(5*60))
    def get(self,request):
        try:
            logger.info('CAlling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': "mosh"})

   
    
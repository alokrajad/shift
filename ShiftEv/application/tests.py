from django.test import TestCase
import json
from django.urls import reverse
from rest_framework import status
# from rest_framework.test import APITestCase
import unittest
from django.test import Client
# from .serializers import *
from .models import *
import random
base_url = "http://127.0.0.1:8000/"
Authorization = 'eyJraWQiOiJcL2I1QUlWTnpVbzkweTVvYk9hc3Q2bzdhbllZVFNqK0s2OVwvMVhcL25QMTNvPSIsImFsZyI6IlJTMjU2In0.eyJvcmlnaW5fanRpIjoiNjk0YWJmNTEtNzZlNC00YjkyLThjNmUtZjkxMGY3NTEzNzAzIiwic3ViIjoiZmIyNGQwMzktYTYxMi00MGE3LTk1YWQtMWZkYzNmZTVjMjdlIiwiZXZlbnRfaWQiOiIxYTMxNWE3OS0xNjg2LTRmMzctOTIyMC01ODY3MWVmNzEzYzgiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjM3Njc0Nzg2LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuZXUtY2VudHJhbC0xLmFtYXpvbmF3cy5jb21cL2V1LWNlbnRyYWwtMV9pVjgxa25XV3YiLCJleHAiOjE2Mzc2NzgzODYsImlhdCI6MTYzNzY3NDc4NiwianRpIjoiNzE2ZGUzYjgtZjA2My00NWNlLWFmY2ItYmUzNDBjYzZhM2FlIiwiY2xpZW50X2lkIjoiNjdoYWZpaTM1MjZlcmtycWlhYW50aXV2YTEiLCJ1c2VybmFtZSI6Im5pZ2FtMjdAeW9wbWFpbC5jb20ifQ.RlfBPeXUiG5PRCMGO7sy87OdQncrkoNTTUTUMoE1OzN86aDLz2yAAb_BOcHUdkeLfs-rQjguOelTR36nZbBMMUeY4pcNQFL19SN2HAtkahsHprFrAbFhva9seZCsYID3w-2g_qtWa4-u5cYYdOuMN1NxpdP-1yfLRDHJY-lszrlUDgxuELt4QX00BcfOFTdHmadwcWT1i02teUQYAlg0M5Aa0ipRZLR51uNU6XUJPcm1KtjeWjhvS2Pycma85mUhck1hvTdtaWLU8IEaRg2w69jgJloLvvP2bQOuCrNjZCq8Pe_F_-vIswHG9xB1R3to0Maxg1XdfC3i5RymfrBx3A'
language = "en"
c = Client() #CONNECTION CREATED WITH DATABASE AS PROVIED IN SETTINGS.PY

print("_____________________________________________________________________________Starting test-cases_____________________________________________________________________________________")

ev_car_id = ''
import simplejson
import uuid
# print(uuid.uuid4()) #GENERATE UNIQUE ID


class vehicleApiTestCase(unittest.TestCase):

    def test_post_with_correct_data(self):   
        data = [{     
        "brand_en": str(uuid.uuid4()),
        "model_en": str(uuid.uuid4()),
        "brand_nl": str(uuid.uuid4()),
        "model_nl": str(uuid.uuid4()),
        "version": "Recharge Twin Pure Electric+",
        "car_type": "Standard",
        "description_en": "For more information, please contact the dealer: Broekhuis, 0341-751425 or by e-mail: merkspecialist@broekshuis.nlntowbar: 1500kg (hibited)nRange Extender: Plus Package + Heatpump",
        "description_nl": "Voor meer informatie, neem contact op met de voorkeursdealer: Broekhuis, 0341-751425 of per e-mail: merkspecialist@broekshuis.nlntrekhaak: 1500kg (geremd)nRange Extender: Pluspakket + warmtepomp",
        "wltp_range": 335,
        "additional_percentage": 16,
        "battery_capacity": 78.0,
        "tax_value": 55370.0,
        "expected_delivery_time": "3",
        "category": 8,
        "ispublished": False,
        "long_range_vehicles_category": None,
        "color": [            
            {             
                "color_name": "Denim blue metallic",
                "hex_code": "#172436",
                "r": "23",
                "g": "36",
                "b": "54",
                "img1": '',
                "img2": '',
                "img3": '',
                "img4": '',
                "img5": ''                
            }
        ],
        "choosableoptions": [
            {
              
                "option_name_en": "Trailer Hitch",
                "option_name_nl": "Trailer Hitch",
                "option_value": 123.45
             
            }
        ] }]
        
        headers = {'HTTP_LANGUAGE':language,'HTTP_AUTHORIZATION': Authorization}
        params = {}        
        data = json.dumps(data)
        response = c.post(base_url+'vehicles/',data,content_type="application/json",**headers,**params)
        response = response.json()
        print("test_post_with_correct_data-----------RESPONSE-------",response['status'])
        # self.car_id = response['data'][0]['id']
        # print('in function itself----',self.car_id)
        if response['code'] == 400:
            print(response)
        self.assertEqual(response['code'],status.HTTP_200_OK)
import datetime
import json
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.conf import settings
import requests

def getUserDetails(token):
    try:
        access_token = token
        url = 'https://0vpugiy8ih.execute-api.eu-central-1.amazonaws.com/accp/user-details'
        headers = {'Authorization': access_token, 'Content-Type': 'application/json; charset=utf-8'}
        r = requests.post(url, headers=headers)
        response = r.json()
        if response['code'] == 200:
            return response
        else:
            return False
    except:
        return False


def vs_add_car_by_user(token,data):
    try:
        access_token = token
        url = 'https://0vpugiy8ih.execute-api.eu-central-1.amazonaws.com/accp/vs/add-car-by-user'
        headers = {'Authorization': access_token, 'Content-Type': 'application/json'}
        json_object = json.dumps(data, indent = 4)
        r = requests.post(url, headers=headers,data=json_object)
        response = r.json()
        if response['code'] == 200:
            return response
        else:
            return False
    except:
        return False



def ev_definitely_my_car(token,data):
    try:
        access_token = token
        url = 'https://0vpugiy8ih.execute-api.eu-central-1.amazonaws.com/accp/my-car-email/'
        headers = {'Authorization': access_token, 'Content-Type': 'application/json'}
        json_object = json.dumps(data, indent = 4)
        r = requests.post(url, headers=headers,data=json_object)
        response = r.json()
        if response['code'] == 200:
            return response
        else:
            return False
    except:
        return False




def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("Utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None



# import pandas as pd
#
#
# def check_integer_field(x, y, i):
#     if x != " ":
#         try:
#
#             if float(x) != int(x):
#                 return ("{} in row {} must be a positive integer not float".format(y, i + 1))
#
#             elif int(x) > 0:
#                 pass
#             else:
#                 return ("{} in row {} must be a positive integer".format(y, i + 1))
#
#         except:
#
#             return ("{} in row {} must be a positive integer".format(y, i + 1))
#     else:
#         return ("{} in row {} must be a positive integer ".format(y, i + 1))





def check_float_field(x, y, i):
    if x != " ":
        try:
            if int(x) > 0:
                pass
            else:
                return ("{} in row {} must be a positive integer".format(y, i + 1))

        except:

            return ("{} in row {} must be a positive integer".format(y, i + 1))
    else:
        return ("{} in row {} must be a positive integer ".format(y, i + 1))





status = ["Standard", "Best"]

def check_option(x,y,i):
    if x == " ":
        return ("{} in row {} only 'Standard' or 'Best' ".format(y, i + 1))
    else:
        try:
            option_val = (x.strip()).capitalize()
            if option_val not in status:
                return ("{} in row {} only 'Standard' or 'Best' ".format(y,i + 1))
        except:
            return ("{} in row {} only 'Standard' or 'Best' ".format(y, i + 1))


status1 = [True, False]
def check_option1(x,y,i):
    if x ==" ":
        return ("{} in row {} only 'True' or 'False' ".format(y, i + 1))
    else:
        try:
            option_val = x
            if option_val not in status1:
                return ("{} in row {} only 'true' or 'false' ".format(y,i + 1))
        except:
            return ("{} in row {} only 'true' or 'false' ".format(y, i + 1))



def not_empty(x,y,i):
    if x == " ":
        return ("{} in row {} can't be empty".format(y,i + 1))


def set_if_not_none(mapping, key, value):
    if value is not None:
        value = eval(value)

        if key=="category__in":
            value=[int(i) for i in value]
            value=list(range(1,max(value)+1))
        if key == "long_range_vehicles_category__in":
            value = [int(i) for i in value]
            value = list(range(1, max(value) + 1))

        mapping[key] = value

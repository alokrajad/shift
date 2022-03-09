import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import electric_vehicles,ev_vehicles_order
from .serializers import VehicleDataSerializer, EVDataSerializer,\
    EvNlDataSerializer,EvBrandEnSerializer, EvVersionSerializer, EvmodelEnSerializer ,VsBasicDataSerializer,order_serializer
from .mypagination import PaginationHandlerMixin
from .function import  set_if_not_none,getUserDetails,vs_add_car_by_user,ev_definitely_my_car,render_to_pdf
from rest_framework.pagination import PageNumberPagination
from django.db.models import F
from .models import vs_vehicles
from io import BytesIO
from django.conf import settings
from django.core.files import File
from django.core.mail import EmailMessage
import datetime



class BasicPagination(PageNumberPagination):
    page_size = 21
    page_size_query_param = 'limit'


class VehiclesApi(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination
    def get(self,request,pk=None, format=None,*args,**kwargs):
        id = pk
        access_token = self.request.META.get('HTTP_AUTHORIZATION')
        language = self.request.META.get('HTTP_LANGUAGE')
        page_number = self.request.query_params.get('page', 1)


        response = getUserDetails(access_token)
        if response:
            role = response['data']['role']
            ev_category = response['data']['category']
        else:
            if language == 'en':
                message = {"message": "UnAuthorized User", "code": status.HTTP_401_UNAUTHORIZED,
                           "status": "UnAuthorized"}
            else:
                message = {"message": "Ongeautoriseerde gebruiker", "code": status.HTTP_401_UNAUTHORIZED,
                           "status": "UnAuthorized"}
            return Response(message)
        if language == "en":
            serializer_class = VehicleDataSerializer
            if id is not None:
                try:
                    vehicle = electric_vehicles.objects.get(id=id)
                    serializer = EVDataSerializer(vehicle)
                    data = serializer.data

                    color = data['color']
                    for cl in color:
                        images = []
                        if cl['img1']:
                            images.append(cl['img1'])
                        if cl['img2']:
                            images.append(cl['img2'])
                        if cl['img3']:
                            images.append(cl['img3'])
                        if cl['img4']:
                            images.append(cl['img4'])
                        if cl['img5']:
                            images.append(cl['img5'])
                        cl['images'] = images

                    data = {'status': 'success', 'code': status.HTTP_200_OK, 'data': serializer.data}
                    return Response(data)
                except:
                    message={'status': 'success',"message": "data does'nt exist","code":status.HTTP_404_NOT_FOUND}
                    return Response(message)

            vehicle = electric_vehicles.objects.all().order_by('brand_en')
            count = vehicle.count()
            number_of_page=int(count/21)
            if count%21!=0:
                number_of_page+=1

            page = self.paginate_queryset(vehicle)
            if page is not None:
                serializer = self.get_paginated_response(EVDataSerializer(page,many=True).data)

            else:
                serializer = EVDataSerializer(vehicle, many=True)

            data = serializer.data
            result = data['results']
            if len(result)!=0:
                for res in result:
                    color = res['color']
                    for cl in color:
                        images = []
                        if cl['img1']:
                            images.append(cl['img1'])
                        if cl['img2']:
                            images.append(cl['img2'])
                        if cl['img3']:
                            images.append(cl['img3'])
                        if cl['img4']:
                            images.append(cl['img4'])
                        if cl['img5']:
                            images.append(cl['img5'])
                        cl['images'] = images
            data = {'status': 'success', 'code': status.HTTP_200_OK,'Total_page':number_of_page,'current_page':page_number,'data': serializer.data}
            return Response(data)

        elif language == "nl":
            if id is not None:
                try:
                    vehicle = electric_vehicles.objects.get(id=id)
                    serializer = EvNlDataSerializer(vehicle)
                    data = serializer.data
                    color = data['color']
                    for cl in color:
                        images = []
                        if cl['img1']:
                            images.append(cl['img1'])
                        if cl['img2']:
                            images.append(cl['img2'])
                        if cl['img3']:
                            images.append(cl['img3'])
                        if cl['img4']:
                            images.append(cl['img4'])
                        if cl['img5']:
                            images.append(cl['img5'])
                        cl['images'] = images
                    data = {'status': 'success', 'code': status.HTTP_200_OK, 'data': serializer.data}
                    return Response(data)
                except:
                    message = {'status': 'success', "message": "data does'nt exist", "code": status.HTTP_404_NOT_FOUND}
                    return Response(message)

            vehicle = electric_vehicles.objects.all()
            count = vehicle.count()

            number_of_page = int(count / 21)
            if count % 21 != 0:
                number_of_page += 1
            page = self.paginate_queryset(vehicle)
            if page is not None:
                serializer = self.get_paginated_response(EvNlDataSerializer(page,
                                                                               many=True).data)
            else:
                serializer = EvNlDataSerializer(vehicle, many=True)

            data = serializer.data
            result = data['results']
            if len(result)!=0:
                for res in result:
                    color = res['color']
                    for cl in color:
                        images = []
                        if cl['img1']:
                            images.append(cl['img1'])
                        if cl['img2']:
                            images.append(cl['img2'])
                        if cl['img3']:
                            images.append(cl['img3'])
                        if cl['img4']:
                            images.append(cl['img4'])
                        if cl['img5']:
                            images.append(cl['img5'])
                        cl['images'] = images
            data = {'status': 'success', 'code': status.HTTP_200_OK,'Total_page':number_of_page,'current_page':page_number, 'data': serializer.data}
            return Response(data)
        else:
            if id is not None:
                try:
                    vehicle = electric_vehicles.objects.get(id=id)

                    serializer = VehicleDataSerializer(vehicle)
                    data = serializer.data
                    color = data['color']
                    for cl in color:
                        images = []
                        if cl['img1']:
                            images.append(cl['img1'])
                        if cl['img2']:
                            images.append(cl['img2'])
                        if cl['img3']:
                            images.append(cl['img3'])
                        if cl['img4']:
                            images.append(cl['img4'])
                        if cl['img5']:
                            images.append(cl['img5'])
                        cl['images'] = images
                    data = {'status': 'success', 'code': status.HTTP_200_OK, 'data': serializer.data}
                    return Response(data)
                except:
                    message = {'status': 'success', "message": "gegevens bestaan niet", "code": status.HTTP_404_NOT_FOUND}
                    return Response(message)

            vehicle = electric_vehicles.objects.all()
            count = vehicle.count()
            number_of_page = int(count / 21)
            if count%21 != 0:
                number_of_page += 1
            page = self.paginate_queryset(vehicle)
            if page is not None:
                serializer = self.get_paginated_response(VehicleDataSerializer(page,
                                                                   many=True).data)
            else:
                serializer = VehicleDataSerializer(vehicle, many=True)
            data = serializer.data
            result = data['results']
            if len(result)!=0:
                for res in result:
                    color = res['color']
                    for cl in color:
                        images = []
                        if cl['img1']:
                            images.append(cl['img1'])
                        if cl['img2']:
                            images.append(cl['img2'])
                        if cl['img3']:
                            images.append(cl['img3'])
                        if cl['img4']:
                            images.append(cl['img4'])
                        if cl['img5']:
                            images.append(cl['img5'])
                        cl['images'] = images
            # serializer = VehicleDataSerializer(vehicle, many=True)
            data = {'status': 'success', 'code': status.HTTP_200_OK,'Total_page':number_of_page,'current_page':page_number,'data': serializer.data}
            return Response(data)

    def post(self, request, format=None):
        access_token = self.request.META.get('HTTP_AUTHORIZATION')
        language = self.request.META.get('HTTP_LANGUAGE')

        response = getUserDetails(access_token)
        if response:
            role = response['data']['role']
            ev_category = response['data']['category']
        else:
            if language == 'en':
                message = {"message": "UnAuthorized User", "code": status.HTTP_401_UNAUTHORIZED,"status":"UnAuthorized"}
            else:
                message = {"message": "Ongeautoriseerde gebruiker", "code": status.HTTP_401_UNAUTHORIZED,"status":"UnAuthorized"}
            return Response(message)
        if role != "Admin":
            if language == 'en':
                message = {'status': "failed", 'code': status.HTTP_401_UNAUTHORIZED, 'message': 'Admin Credential Required'}
                return Response(message)
            else:
                message = {'status': "failed", 'code': status.HTTP_401_UNAUTHORIZED, 'message': 'Beheerdersreferentie vereist'}
                return Response(message)
        serializer = VehicleDataSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            if language == 'en':
                data = {'status': 'success', 'message': 'Car saved successfully', 'code': status.HTTP_200_OK,
                        'data': serializer.data}
            else:
                data = {'status': 'success', 'message': 'Auto succesvol opgeslagen', 'code': status.HTTP_200_OK,
                        'data': serializer.data}
            return Response(data)
        message = {'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors}
        return Response(message)

    def put(self, request, pk=None, format=None):
        id = pk
        access_token = self.request.META.get('HTTP_AUTHORIZATION')
        language = self.request.META.get('HTTP_LANGUAGE')

        response = getUserDetails(access_token)
        if response:
            role = response['data']['role']
            ev_category = response['data']['category']
        else:
            if language == 'en':
                message = {"message": "UnAuthorized User", "code": status.HTTP_401_UNAUTHORIZED,"status":"UnAuthorized"}
            else:
                message = {"message": "Ongeautoriseerde gebruiker", "code": status.HTTP_401_UNAUTHORIZED,"status":"UnAuthorized"}
            return Response(message)
        if role != "Admin":
            if language == 'en':
                message = {'status': "failed", 'code': status.HTTP_401_UNAUTHORIZED, 'message': 'Admin Credential Required'}
            else:
                message = {'status': "failed", 'code': status.HTTP_401_UNAUTHORIZED, 'message': 'Beheerdersreferentie vereist'}
            return Response(message)
        vehicle = electric_vehicles.objects.get(id=id)
        serializer = VehicleDataSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'status': 'success', 'code': status.HTTP_200_OK, 'data': serializer.data}
            return Response(data)
        message = {'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors}
        return Response(message)

    def patch(self, request, pk=None, format=None):
        id = pk
        access_token = self.request.META.get('HTTP_AUTHORIZATION')
        language = self.request.META.get('HTTP_LANGUAGE')
        response = getUserDetails(access_token)
        if response:
            role = response['data']['role']
            ev_category = response['data']['category']
        else:
            if language == 'en':
                message = {"message": "UnAuthorized User", "code": status.HTTP_401_UNAUTHORIZED,"status":"UnAuthorized"}
            else:
                message = {"message": "Ongeautoriseerde gebruiker", "code": status.HTTP_401_UNAUTHORIZED,"status":"UnAuthorized"}
            return Response(message)
        if role != "Admin":
            if language == 'en':
                message = {'status': "failed", 'code': status.HTTP_401_UNAUTHORIZED, 'message': 'Admin Credential Required'}
            else:
                message = {'status': "failed", 'code': status.HTTP_401_UNAUTHORIZED, 'message': 'Beheerdersreferentie vereist'}
            return Response(message)
        vehicle = electric_vehicles.objects.get(id=id)
        serializer = VehicleDataSerializer(vehicle, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {'status': 'success', 'code': status.HTTP_200_OK, 'data': serializer.data}
            return Response(data)
        message = {'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors}
        return Response(message)

    def delete(self, request, pk=None, format=None):
        id = pk
        access_token = self.request.META.get('HTTP_AUTHORIZATION')
        language = self.request.META.get('HTTP_LANGUAGE')
        response = getUserDetails(access_token)
        if response:
            role = response['data']['role']
            ev_category = response['data']['category']
        else:
            if language == 'en':
                message = {"message": "UnAuthorized User", "code": status.HTTP_401_UNAUTHORIZED,"status":"UnAuthorized"}
            else:
                message = {"message": "Ongeautoriseerde gebruiker", "code": status.HTTP_401_UNAUTHORIZED,"status":"UnAuthorized"}
            return Response(message)
        if role != "Admin":
            if language == 'en':
                message = {'status': "failed", 'code': status.HTTP_401_UNAUTHORIZED, 'message': 'Admin Credential Required'}
            else:
                message = {'status': "failed", 'code': status.HTTP_401_UNAUTHORIZED, 'message': 'Beheerdersreferentie vereist'}
            return Response(message)
        try:
            vehicle = electric_vehicles.objects.get(id=id)
            vehicle.delete()
            if language == 'en':
                message = {'status': "failed", 'code': status.HTTP_200_OK,"message": "Car deleted successfully"}
            else:
                message = {'status': "failed", 'code': status.HTTP_200_OK,"message": "Auto succesvol verwijderd"}
            return Response(message)
        except:
            if language == 'en':
                message = {'status': "failed", 'code': status.HTTP_404_NOT_FOUND, "message": "No detail found"}
            else:
                message = {'status': "failed", 'code': status.HTTP_404_NOT_FOUND, "message": "Geen detail gevonden"}
            return Response(message)





class ev_filter_standard_vehicle(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination

    def get(self, request, pk=None, format=None, *args, **kwargs):
        try:
            language = request.META.get('HTTP_LANGUAGE')

            access_token = self.request.META.get('HTTP_AUTHORIZATION')
            response = getUserDetails(access_token)
            if response:
                role = response['data']['role']
                ev_category = response['data']['category']
            else:
                if language == 'en':
                    message = {"message": "Unauthorized User", "code": status.HTTP_401_UNAUTHORIZED,
                               "status": "Unauthorized"}
                else:
                    message = {"message": "Ongeautoriseerde gebruiker", "code": status.HTTP_401_UNAUTHORIZED,
                               "status": "Unauthorized"}
                return Response(message)
            # if role=="Admin":
            #
            #     message = {"message": "Invalid User", "code": status.HTTP_400_BAD_REQUEST}
            #     return Response(message)

            brand = self.request.query_params.get('brand', None)
            model = self.request.query_params.get('model', None)
            version = self.request.query_params.get('version', None)
            category = self.request.query_params.get('category', None)
            category_type = self.request.query_params.get('category_type', "")  # new param for category type admin
            page_number = self.request.query_params.get('page', 1)
            sort_params = {}
            if category:
                if len(category) <= 2:
                    category=str([ev_category])
            else:
                category=str([ev_category])
            if brand:
                if len(brand) <= 2:
                    brand = None
            if model:
                if len(model) <= 2:
                    model = None
            if version:
                if len(version) <= 2:
                    version = None
            if category_type:
                if len(category_type) <= 2 :
                    category_type = None

            if language == "en":
                set_if_not_none(sort_params, 'brand_en__in', brand)
                set_if_not_none(sort_params, 'model_en__in', model)
                set_if_not_none(sort_params, 'version__in', version)
                # set_if_not_none(sort_params, 'category__in', category)

                if role == "Admin":
                    if "long_range" in category_type :
                        set_if_not_none(sort_params, 'long_range_vehicles_category__in', category)
                    else:
                        set_if_not_none(sort_params, 'category__in', category)
                elif role == "long_range_user":
                    set_if_not_none(sort_params, 'long_range_vehicles_category__in', category)
                else:
                    set_if_not_none(sort_params, 'category__in', category)
                sort_params["ispublished"] = True
                sort_params["car_type"] = "Standard"

                vehicle = electric_vehicles.objects.filter(**sort_params)
                count = vehicle.count()
                number_of_page = int(count / 21)
                if count % 21 != 0:
                    number_of_page += 1

                page = self.paginate_queryset(vehicle)
                if page is not None:
                    serializer = self.get_paginated_response(EVDataSerializer(page, many=True).data)
                else:
                    serializer = EVDataSerializer(vehicle, many=True)
                data = serializer.data
                result = data['results']
                if len(result) != 0:
                    for res in result:
                        color = res['color']
                        for cl in color:
                            images = []
                            if cl['img1']:
                                images.append(cl['img1'])
                            if cl['img2']:
                                images.append(cl['img2'])
                            if cl['img3']:
                                images.append(cl['img3'])
                            if cl['img4']:
                                images.append(cl['img4'])
                            if cl['img5']:
                                images.append(cl['img5'])
                            cl['images'] = images
                # serializer = EVDataSerializer(vehicle, many=True)
                data = {'status': 'success', 'code': status.HTTP_200_OK,'Total_page':number_of_page,'current_page':page_number,
                        'data': serializer.data}
                return Response(data)

            elif language == "nl":
                set_if_not_none(sort_params, 'brand_nl__in', brand)
                set_if_not_none(sort_params, 'model_nl__in', model)
                set_if_not_none(sort_params, 'version__in', version)
                # set_if_not_none(sort_params, 'category__in', category)
                if role == "Admin":
                    if "long_range" in category_type:
                        set_if_not_none(sort_params, 'long_range_vehicles_category__in', category)
                    else:
                        set_if_not_none(sort_params, 'category__in', category)
                elif role == "long_range_user":
                    set_if_not_none(sort_params, 'long_range_vehicles_category__in', category)
                else:
                    set_if_not_none(sort_params, 'category__in', category)
                sort_params["ispublished"] = True
                sort_params["car_type"] = "Standard"

                vehicle = electric_vehicles.objects.filter(**sort_params)
                count = vehicle.count()
                number_of_page = int(count / 21)
                if count % 21 != 0:
                    number_of_page += 1
                page = self.paginate_queryset(vehicle)
                if page is not None:
                    serializer = self.get_paginated_response(EvNlDataSerializer(page, many=True).data)
                else:
                    serializer = EvNlDataSerializer(vehicle, many=True)
                data = serializer.data
                result = data['results']
                if len(result) != 0:
                    for res in result:
                        color = res['color']
                        for cl in color:
                            images = []
                            if cl['img1']:
                                images.append(cl['img1'])
                            if cl['img2']:
                                images.append(cl['img2'])
                            if cl['img3']:
                                images.append(cl['img3'])
                            if cl['img4']:
                                images.append(cl['img4'])
                            if cl['img5']:
                                images.append(cl['img5'])
                            cl['images'] = images
                # serializer = EvNlDataSerializer(vehicle, many=True)
                data = {'status': 'success', 'code': status.HTTP_200_OK,'Total_page':number_of_page,'current_page':page_number,
                        'data': serializer.data}
                return Response(data)
            else:
                message = {"message": "Enter language in Headers", "code": status.HTTP_400_BAD_REQUEST}
                return Response(message)
        except Exception as e:
            message = {"message": str(e), "code": status.HTTP_400_BAD_REQUEST}
            return Response(message)


class ev_filter_best_vehicle(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination

    def get(self, request, pk=None, format=None, *args, **kwargs):
        try:
            access_token = self.request.META.get('HTTP_AUTHORIZATION')
            language = request.META.get('HTTP_LANGUAGE')
            response = getUserDetails(access_token)
            if response:
                role = response['data']['role']
                ev_category = response['data']['category']
            else:
                if language == 'en':
                    message = {"message": "Unauthorized User", "code": status.HTTP_401_UNAUTHORIZED,
                               "status": "Unauthorized"}
                else:
                    message = {"message": "Ongeautoriseerde gebruiker", "code": status.HTTP_401_UNAUTHORIZED,
                               "status": "Unauthorized"}
                return Response(message)

            brand = self.request.query_params.get('brand', None)
            model = self.request.query_params.get('model', None)
            version = self.request.query_params.get('version', None)
            category = self.request.query_params.get('category', None)
            category_type = self.request.query_params.get('category_type', "")  # new param for category type admin
            page_number = self.request.query_params.get('page', 1)
            sort_params = {}
            if category:
                if len(category) <= 2:
                    category=str([ev_category])
            else:
                category=str([ev_category])
            if brand:
                if len(brand) <= 2:
                    brand = None
            if model:
                if len(model) <= 2:
                    model = None
            if version:
                if len(version) <= 2:
                    version = None
            if category_type:
                if len(category_type) <= 2:
                    category_type = None
            if language == "en":
                set_if_not_none(sort_params, 'brand_en__in', brand)
                set_if_not_none(sort_params, 'model_en__in', model)
                set_if_not_none(sort_params, 'version__in', version)
                # set_if_not_none(sort_params, 'category__in', category)
                if role == "Admin":
                    if "long_range" in category_type:
                        set_if_not_none(sort_params, 'long_range_vehicles_category__in', category)
                    else:
                        set_if_not_none(sort_params, 'category__in', category)
                elif role == "long_range_user":
                    set_if_not_none(sort_params, 'long_range_vehicles_category__in', category)
                else:
                    set_if_not_none(sort_params, 'category__in', category)
                sort_params["ispublished"] = True
                sort_params["car_type"] = "Best"

                vehicle = electric_vehicles.objects.filter(**sort_params)
                count = vehicle.count()
                number_of_page = int(count / 21)
                if count % 21 != 0:
                    number_of_page += 1
                page = self.paginate_queryset(vehicle)
                if page is not None:
                    serializer = self.get_paginated_response(EVDataSerializer(page, many=True).data)
                else:
                    serializer = EVDataSerializer(vehicle, many=True)
                data = serializer.data
                result = data['results']
                if len(result) != 0:
                    for res in result:
                        color = res['color']
                        for cl in color:
                            images = []
                            if cl['img1']:
                                images.append(cl['img1'])
                            if cl['img2']:
                                images.append(cl['img2'])
                            if cl['img3']:
                                images.append(cl['img3'])
                            if cl['img4']:
                                images.append(cl['img4'])
                            if cl['img5']:
                                images.append(cl['img5'])
                            cl['images'] = images
                # vehicle = electric_vehicles.objects.filter(**sort_params)
                # serializer = EVDataSerializer(vehicle, many=True)
                data = {'status': 'success', 'code': status.HTTP_200_OK,'Total_page':number_of_page,'current_page':page_number,
                        'data': serializer.data}
                return Response(data)

            elif language == "nl":
                set_if_not_none(sort_params, 'brand_nl__in', brand)
                set_if_not_none(sort_params, 'model_nl__in', model)
                set_if_not_none(sort_params, 'version__in', version)
                # set_if_not_none(sort_params, 'category__in', category)
                if role == "Admin":
                    if "long_range" in category_type:
                        set_if_not_none(sort_params, 'long_range_vehicles_category__in', category)
                    else:
                        set_if_not_none(sort_params, 'category__in', category)
                elif role == "long_range_user":
                    set_if_not_none(sort_params, 'long_range_vehicles_category__in', category)
                else:
                    set_if_not_none(sort_params, 'category__in', category)
                sort_params["ispublished"] = True
                sort_params["car_type"] = "Best"

                vehicle = electric_vehicles.objects.filter(**sort_params)
                count = vehicle.count()
                number_of_page = int(count / 21)
                if count % 21 != 0:
                    number_of_page += 1
                page = self.paginate_queryset(vehicle)
                if page is not None:
                    serializer = self.get_paginated_response(EvNlDataSerializer(page, many=True).data)
                else:
                    serializer = EvNlDataSerializer(vehicle, many=True)
                data = serializer.data
                result = data['results']
                if len(result) != 0:
                    for res in result:
                        color = res['color']
                        for cl in color:
                            images = []
                            if cl['img1']:
                                images.append(cl['img1'])
                            if cl['img2']:
                                images.append(cl['img2'])
                            if cl['img3']:
                                images.append(cl['img3'])
                            if cl['img4']:
                                images.append(cl['img4'])
                            if cl['img5']:
                                images.append(cl['img5'])
                            cl['images'] = images
                # serializer = EvNlDataSerializer(vehicle, many=True)
                data = {'status': 'success', 'code': status.HTTP_200_OK, 'data': serializer.data}
                return Response(data)
            else:
                message = {"message": "Voer taal in Headers in", "code": status.HTTP_400_BAD_REQUEST}
                return Response(message)
        except Exception as e:
            message = {"message": str(e), "code": status.HTTP_400_BAD_REQUEST}
            return Response(message)


class ev_filter_all_best_vehicle(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination

    def get(self, request, pk=None, format=None, *args, **kwargs):
        try:
            access_token = self.request.META.get('HTTP_AUTHORIZATION')
            language = request.META.get('HTTP_LANGUAGE')
            response = getUserDetails(access_token)
            if response:
                role = response['data']['role']
                # ev_category = response['data']['category']
            else:
                if language == 'en':
                    message = {"message": "Unauthorized User", "code": status.HTTP_401_UNAUTHORIZED,
                               "status": "Unauthorized"}
                else:
                    message = {"message": "Ongeautoriseerde gebruiker", "code": status.HTTP_401_UNAUTHORIZED,
                               "status": "Unauthorized"}
                return Response(message)

            if role != 'Admin':
                message = {"message": "invalid User", "code": status.HTTP_401_UNAUTHORIZED, "status": "Unauthorized"}
                return Response(message)

            brand = self.request.query_params.get('brand', None)
            model = self.request.query_params.get('model', None)
            version = self.request.query_params.get('version', None)
            category = self.request.query_params.get('category', None)
            category_type = self.request.query_params.get('category_type', "")  # new param for category type admin
            page_number = self.request.query_params.get('page', 1)
            sort_params = {}
            if category:
                if len(category) <= 2:
                    category = None
            if brand:
                if len(brand) <= 2:
                    brand = None
            if model:
                if len(model) <= 2:
                    model = None
            if version:
                if len(version) <= 2:
                    version = None
            if category_type:
                if len(category_type) <= 2:
                    category_type = None
            if language == "en":
                set_if_not_none(sort_params, 'brand_en__in', brand)
                set_if_not_none(sort_params, 'model_en__in', model)
                set_if_not_none(sort_params, 'version__in', version)
                # set_if_not_none(sort_params, 'category__in', category)
                if "long_range" in category_type:
                    set_if_not_none(sort_params, 'long_range_vehicles_category__in', category)
                else:
                    set_if_not_none(sort_params, 'category__in', category)
                sort_params["car_type"] = "Best"

                vehicle = electric_vehicles.objects.filter(**sort_params)
                count = vehicle.count()
                number_of_page = int(count / 21)
                if count % 21 != 0:
                    number_of_page += 1
                page = self.paginate_queryset(vehicle)
                if page is not None:
                    serializer = self.get_paginated_response(EVDataSerializer(page, many=True).data)
                else:
                    serializer = EVDataSerializer(vehicle, many=True)
                data = serializer.data
                result = data['results']
                if len(result) != 0:
                    for res in result:
                        color = res['color']
                        for cl in color:
                            images = []
                            if cl['img1']:
                                images.append(cl['img1'])
                            if cl['img2']:
                                images.append(cl['img2'])
                            if cl['img3']:
                                images.append(cl['img3'])
                            if cl['img4']:
                                images.append(cl['img4'])
                            if cl['img5']:
                                images.append(cl['img5'])
                            cl['images'] = images
                # serializer = EVDataSerializer(vehicle, many=True)
                data = {'status': 'success', 'code': status.HTTP_200_OK,'Total_page':number_of_page,'current_page':page_number,
                        'data': serializer.data}
                return Response(data)

            elif language == "nl":
                set_if_not_none(sort_params, 'brand_nl__in', brand)
                set_if_not_none(sort_params, 'model_nl__in', model)
                set_if_not_none(sort_params, 'version__in', version)
                if "long_range" in category_type:
                    set_if_not_none(sort_params, 'long_range_vehicles_category__in', category)
                else:
                    set_if_not_none(sort_params, 'category__in', category)
                sort_params["car_type"] = "Best"

                vehicle = electric_vehicles.objects.filter(**sort_params)
                # vehicle = electric_vehicles.objects.filter(**sort_params)
                count = vehicle.count()
                number_of_page = int(count / 21)
                if count % 21 != 0:
                    number_of_page += 1
                page = self.paginate_queryset(vehicle)
                if page is not None:
                    serializer = self.get_paginated_response(EvNlDataSerializer(page, many=True).data)
                else:
                    serializer = EvNlDataSerializer(vehicle, many=True)
                data = serializer.data
                result = data['results']
                if len(result) != 0:
                    for res in result:
                        color = res['color']
                        for cl in color:
                            images = []
                            if cl['img1']:
                                images.append(cl['img1'])
                            if cl['img2']:
                                images.append(cl['img2'])
                            if cl['img3']:
                                images.append(cl['img3'])
                            if cl['img4']:
                                images.append(cl['img4'])
                            if cl['img5']:
                                images.append(cl['img5'])
                            cl['images'] = images

                data = {'status': 'success', 'code': status.HTTP_200_OK,'Total_page':number_of_page,'current_page':page_number,
                        'data': serializer.data}
                return Response(data)
            else:
                message = {"message": "Enter language in Headers", "code": status.HTTP_400_BAD_REQUEST}
                return Response(message)
        except:
            message = {"message": "", "code": status.HTTP_400_BAD_REQUEST}
            return Response(message)


class ev_filter_all_standard_vehicle(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination

    def get(self, request, pk=None, format=None, *args, **kwargs):
        try:
            access_token = self.request.META.get('HTTP_AUTHORIZATION')
            language = request.META.get('HTTP_LANGUAGE')
            response = getUserDetails(access_token)
            if response:
                role = response['data']['role']
                # ev_category = response['data']['category']
            else:
                if language == 'en':
                    message = {"message": "Unauthorized User", "code": status.HTTP_401_UNAUTHORIZED,
                               "status": "Unauthorized"}
                else:
                    message = {"message": "Ongeautoriseerde gebruiker", "code": status.HTTP_401_UNAUTHORIZED,
                               "status": "Unauthorized"}
                return Response(message)

            if role != 'Admin':
                message = {"message": "Unauthorized User", "code": status.HTTP_401_UNAUTHORIZED,
                           "status": "Unauthorized",
                           'status': 'UnAuthorized'}
                return Response(message, status.HTTP_401_UNAUTHORIZED)

            brand = self.request.query_params.get('brand', None)
            model = self.request.query_params.get('model', None)
            version = self.request.query_params.get('version', None)
            category = self.request.query_params.get('category', None)
            category_type = self.request.query_params.get('category_type', "")  # new param for category type admin
            page_number = self.request.query_params.get('page', 1)
            sort_params = {}
            if category:
                if len(category) <= 2:
                    category = None
            if brand:
                if len(brand) <= 2:
                    brand = None
            if model:
                if len(model) <= 2:
                    model = None
            if version:
                if len(version) <= 2:
                    version = None
            if category_type:
                if len(category_type) <= 2:
                    category_type = None
            if language == "en":
                set_if_not_none(sort_params, 'brand_en__in', brand)
                set_if_not_none(sort_params, 'model_en__in', model)
                set_if_not_none(sort_params, 'version__in', version)
                # set_if_not_none(sort_params, 'category__in', category)
                # ___________________NEW________________________
                if "long_range" in category_type:
                    set_if_not_none(sort_params, 'long_range_vehicles_category__in', category)
                else:
                    set_if_not_none(sort_params, 'category__in', category)
                # ___________________NEW________________________

                sort_params["car_type"] = "Standard"
                vehicle = electric_vehicles.objects.filter(**sort_params)
                count = vehicle.count()
                number_of_page = int(count / 21)
                if count % 21 != 0:
                    number_of_page += 1
                page = self.paginate_queryset(vehicle)
                if page is not None:
                    serializer = self.get_paginated_response(EVDataSerializer(page, many=True).data)
                else:
                    serializer = EVDataSerializer(vehicle, many=True)
                data = serializer.data
                result = data['results']
                if len(result) != 0:
                    for res in result:
                        color = res['color']
                        for cl in color:
                            images = []
                            if cl['img1']:
                                images.append(cl['img1'])
                            if cl['img2']:
                                images.append(cl['img2'])
                            if cl['img3']:
                                images.append(cl['img3'])
                            if cl['img4']:
                                images.append(cl['img4'])
                            if cl['img5']:
                                images.append(cl['img5'])
                            cl['images'] = images
                # serializer = EVDataSerializer(vehicle, many=True)
                data = {'status': 'success', 'code': status.HTTP_200_OK,'Total_page':number_of_page,'current_page':page_number,
                        'data': serializer.data}
                return Response(data)

            elif language == "nl":
                set_if_not_none(sort_params, 'brand_nl__in', brand)
                set_if_not_none(sort_params, 'model_nl__in', model)
                set_if_not_none(sort_params, 'version__in', version)
                # set_if_not_none(sort_params, 'category__in', category)
                # ___________________NEW________________________
                if "long_range" in category_type:
                    set_if_not_none(sort_params, 'long_range_vehicles_category__in', category)
                else:
                    set_if_not_none(sort_params, 'category__in', category)
                # ___________________NEW________________________
                sort_params["car_type"] = "Standard"
                vehicle = electric_vehicles.objects.filter(**sort_params)
                count = vehicle.count()
                number_of_page = int(count / 21)
                if count % 21 != 0:
                    number_of_page += 1
                page = self.paginate_queryset(vehicle)
                if page is not None:
                    serializer = self.get_paginated_response(EvNlDataSerializer(page, many=True).data)
                else:
                    serializer = EvNlDataSerializer(vehicle, many=True)
                data = serializer.data
                result = data['results']
                if len(result) != 0:
                    for res in result:
                        color = res['color']
                        for cl in color:
                            images = []
                            if cl['img1']:
                                images.append(cl['img1'])
                            if cl['img2']:
                                images.append(cl['img2'])
                            if cl['img3']:
                                images.append(cl['img3'])
                            if cl['img4']:
                                images.append(cl['img4'])
                            if cl['img5']:
                                images.append(cl['img5'])
                            cl['images'] = images
                # serializer = EvNlDataSerializer(vehicle, many=True)
                data = {'status': 'success', 'code': status.HTTP_200_OK,'Total_page':number_of_page,'current_page':page_number,
                        'data': serializer.data}
                return Response(data)
            else:
                message = {"message": "Enter language in Headers", "code": status.HTTP_400_BAD_REQUEST}
                return Response(message)
        except Exception as e:
            message = {"message": e, "code": status.HTTP_400_BAD_REQUEST}
            return Response(message)


class ev_vehicle_dropdown(APIView):
    def get(self, request, pk=None, format=None, *args, **kwargs):
        language = request.META.get('HTTP_LANGUAGE')
        brand = self.request.query_params.get('brand', None)
        if language == "en":
            data1 = electric_vehicles.objects.order_by('brand_en').values(brand=F('brand_en')).distinct()
            data2 = electric_vehicles.objects.order_by('version').values('version').distinct()
            serializer1 = EvBrandEnSerializer(data1, many=True)
            serializer2 = EvVersionSerializer(data2, many=True)
            sort_params = {}
            set_if_not_none(sort_params, 'brand_en__in', brand)
            if brand != None:
                data3 = electric_vehicles.objects.order_by('model_en').values(model=F('model_en')).filter(
                    **sort_params).distinct()
                serializer3 = EvmodelEnSerializer(data3, many=True)
                data = {'status': 'success', 'code': status.HTTP_200_OK, 'brand_data': serializer1.data,
                        'version_data': serializer2.data, 'model_data': serializer3.data}
                return Response(data)
            data = {'status': 'success', 'code': status.HTTP_200_OK, 'brand_data': serializer1.data,
                    'version_data': serializer2.data}
            return Response(data)
        if language == "nl":
            data1 = electric_vehicles.objects.order_by('brand_nl').values(brand=F('brand_nl')).distinct()
            data2 = electric_vehicles.objects.order_by('version').values('version').distinct()
            serializer1 = EvBrandEnSerializer(data1, many=True)
            serializer2 = EvVersionSerializer(data2, many=True)
            sort_params = {}
            set_if_not_none(sort_params, 'brand_nl__in', brand)
            if brand != None:
                data3 = electric_vehicles.objects.order_by('model_nl').values(model=F('model_nl')).filter(
                    **sort_params).distinct()
                serializer3 = EvmodelEnSerializer(data3, many=True)
                data = {'status': 'success', 'code': status.HTTP_200_OK, 'brand_data': serializer1.data,
                        'version_data': serializer2.data, 'model_data': serializer3.data}
                return Response(data)
            data = {'status': 'success', 'code': status.HTTP_200_OK, 'brand_data': serializer1.data,
                    'version_data': serializer2.data}
            return Response(data)
        data = {'status': 'success', 'code': status.HTTP_200_OK, 'message': "Enter language in Headers"}
        return Response(data)


# --------------------------------vs car-------------------------------------------
# --------------------------------vs car-------------------------------------------
# --------------------------------vs car-------------------------------------------


class vs_car_list(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination
    def get(self, request, pk=None, format=None, *args, **kwargs):
        try:
            language = request.META.get('HTTP_LANGUAGE')

            access_token = self.request.META.get('HTTP_AUTHORIZATION')
            response = getUserDetails(access_token)
            if response:
                role = response['data']['role']
                ev_category = response['data']['category']
            else:
                if language == 'en':
                    message = {"message": "Unauthorized User", "code": status.HTTP_401_UNAUTHORIZED,
                               "status": "Unauthorized"}
                elif language == 'nl':
                    message = {"message": "Ongeautoriseerde gebruiker", "code": status.HTTP_401_UNAUTHORIZED,
                               "status": "Unauthorized"}
                else:
                    message = {"message": "Unauthorized User", "code": status.HTTP_401_UNAUTHORIZED,
                               "status": "Unauthorized"}
                return Response(message)
            page_number = self.request.query_params.get('page', 1)
            brand = self.request.query_params.get('brand', None)
            model = self.request.query_params.get('model', None)
            color = self.request.query_params.get('color', None)
            category = self.request.query_params.get('category', None)
            door = self.request.query_params.get('door', None)
            transition = self.request.query_params.get('transition', None)
            ispublished = self.request.query_params.get('ispublished', None)

            sort_params = {}
            if category:
                if len(category) <= 2:
                    if role == "Admin":
                        category = None
                    else:
                        category = str([ev_category])


            else:
                if role == "Admin":
                    category = None
                else:
                    category = str([ev_category])
            if brand:
                if len(brand) <= 2:
                    brand = None
            if model:
                if len(model) <= 2:
                    model = None
            if door:
                if len(door) <= 2:
                    door = None
            if transition:
                if len(transition) <= 2:
                    transition = None
            if color:
                if len(color) <= 2:
                    color = None
            set_if_not_none(sort_params, 'doors__in', door)
            set_if_not_none(sort_params, 'transition__in', transition)
            if role != 'Admin':
                sort_params["ispublished"] = True
            if ispublished == 'true':
                sort_params["ispublished"] = True

            if not pk:
                set_if_not_none(sort_params, 'category__in', category)

            if language == "en":
                set_if_not_none(sort_params, 'brand__in', brand)
                set_if_not_none(sort_params, 'model__in', model)
                set_if_not_none(sort_params, 'color_en__in', color)

                if category == None:
                    if pk:
                        vehicle = vs_vehicles.objects.filter(id=pk, **sort_params).order_by('-category', 'brand')

                    else:
                        vehicle = vs_vehicles.objects.filter(**sort_params).order_by('-category', 'brand')
                    count = vehicle.count()
                    number_of_page = int(count / 21)
                    if count % 21 != 0:
                        number_of_page += 1

                    page = self.paginate_queryset(vehicle)
                    if page is not None:

                        serializer = self.get_paginated_response(VsBasicDataSerializer(page, many=True).data)
                    else:

                        serializer = VsBasicDataSerializer(vehicle, many=True)
                    data = serializer.data
                    if 'results' in data.keys():
                        result = data['results']
                        for data in data['results']:
                            if data['images']:
                                data['images'] = eval(data['images'])
                    data = {'status': 'success', 'code': status.HTTP_200_OK
                        , 'Total_page': number_of_page, 'current_page': int(page_number), 'data': serializer.data}
                    return Response(data)
                if pk:
                    vehicle = vs_vehicles.objects.filter(id=pk, **sort_params).order_by('-category', 'brand')
                else:
                    vehicle = vs_vehicles.objects.filter(**sort_params).order_by('-category', 'brand')
                count = vehicle.count()
                number_of_page = int(count / 21)
                if count % 21 != 0:
                    number_of_page += 1
                page = self.paginate_queryset(vehicle)
                if page is not None:
                    if language == 'en':
                        serializer = self.get_paginated_response(VsBasicDataSerializer(page, many=True).data)
                    else:
                        serializer = self.get_paginated_response(VsBasicDataSerializer(page, many=True).data)
                else:
                    if language == 'en':
                        serializer = VsBasicDataSerializer(vehicle, many=True)
                    else:
                        serializer = VsBasicDataSerializer(vehicle, many=True)
            elif language == "nl":
                set_if_not_none(sort_params, 'brand__in', brand)
                set_if_not_none(sort_params, 'model__in', model)
                set_if_not_none(sort_params, 'color_nl__in', color)

                # if role == "Admin":
                #     set_if_not_none(sort_params, 'category__in', category)
                # else:
                #     set_if_not_none(sort_params, 'category__in', category)
                # sort_params["ispublished"] = True
                if category == None:
                    if pk:
                        vehicle = vs_vehicles.objects.filter(id=pk, **sort_params).order_by('-category', 'brand')
                    else:
                        vehicle = vs_vehicles.objects.filter(**sort_params).order_by('-category', 'brand')
                    count = vehicle.count()
                    number_of_page = int(count / 21)
                    if count % 21 != 0:
                        number_of_page += 1
                    page = self.paginate_queryset(vehicle)
                    if page is not None:
                        #     if language == 'en':
                        #         serializer = self.get_paginated_response(VsEnSerializer(page, many=True).data)
                        #     else:
                        serializer = self.get_paginated_response(VsBasicDataSerializer(page, many=True).data)
                    else:
                        # if language == 'en':
                        #     serializer = VsEnSerializer(vehicle, many=True)
                        # else:
                        serializer = VsBasicDataSerializer(vehicle, many=True)
                    data = serializer.data
                    if 'results' in data.keys():
                        for data in data['results']:
                            if data['images']:
                                data['images'] = eval(data['images'])

                    data = {'status': 'success', 'code': status.HTTP_200_OK
                        , 'Total_page': number_of_page, 'current_page': int(page_number), 'data': serializer.data}
                    return Response(data)

                if pk:
                    vehicle = vs_vehicles.objects.filter(id=pk, **sort_params).order_by('-category', 'brand')
                else:
                    vehicle = vs_vehicles.objects.filter(**sort_params).order_by('-category', 'brand')
                count = vehicle.count()
                number_of_page = int(count / 21)
                if count % 21 != 0:
                    number_of_page += 1
                page = self.paginate_queryset(vehicle)
                if page is not None:

                    serializer = self.get_paginated_response(VsBasicDataSerializer(page, many=True).data)
                else:

                    serializer = VsBasicDataSerializer(vehicle, many=True)
            else:
                message = {"message": "Enter language in Headers", "code": status.HTTP_400_BAD_REQUEST}
                return Response(message)
            data = serializer.data
            if 'results' in data.keys():
                result = data['results']
                for data in data['results']:
                    if data['images']:
                        data['images'] = eval(data['images'])
            data = {'status': 'success', 'code': status.HTTP_200_OK
                , 'Total_page': number_of_page, 'current_page': int(page_number), 'data': serializer.data}
            return Response(data)
        except Exception as e:
            message = {"message": str(e), "code": status.HTTP_400_BAD_REQUEST}
            return Response(message)

    def post(self, request, format=None):
        access_token = self.request.META.get('HTTP_AUTHORIZATION')
        language = self.request.META.get('HTTP_LANGUAGE')

        response = getUserDetails(access_token)
        if response:
            role = response['data']['role']
            ev_category = response['data']['category']
        else:
            if language == 'en':
                message = {"message": "Unauthorized User", "code": status.HTTP_401_UNAUTHORIZED,
                           "status": "Unauthorized"}
            else:
                message = {"message": "Ongeautoriseerde gebruiker", "code": status.HTTP_401_UNAUTHORIZED,
                           "status": "Unauthorized"}
            return Response(message)
        if role != "Admin" and role != "Uploader":
            if language == 'en':
                message = {'status': "failed", 'code': status.HTTP_401_UNAUTHORIZED, 'message': 'Admin Credential Required'}
                return Response(message)
            else:
                message = {'status': "failed", 'code': status.HTTP_401_UNAUTHORIZED, 'message': 'Beheerdersreferentie vereist'}
                return Response(message)
        data = request.data

        if type(data) != type([]):
            message = {'status': "failed", 'code': status.HTTP_400_BAD_REQUEST,
                       'message': "Expected a list of items but got type \"dict\"."}
            return Response(message)
        for data in data:
            if 'pitch' in data.keys():
                if language == 'en':
                    data['pitch_en'] = data['pitch']
                else:
                    data['pitch_nl'] = data['pitch']

            if 'images' in data.keys():
                if data['images'] != None and len(data['images']) > 0:
                    data['images'] = str(data['images'])
                else:
                    data['images'] = None
            if role == 'Uploader':
                if 'pictures' in data.keys():
                    if data['pictures'] != None and len(data['pictures']) > 0:
                        data['images'] = str(data['pictures'])
                    else:
                        data['images'] = None
                else:
                    data['images'] = None
                # if 'license_plate' in data.keys():
                #     data['licence_plate'] = data['license_plate']
                if 'licence_plate' in data.keys():
                    data['license_plate'] = data['licence_plate']
                if 'options' in data.keys():
                    for option in data['options']:
                        if 'trekhaak' in option:
                            data['trailer_hitch'] = 'Yes'
                        if 'navigatie' in option:
                            data['navigation'] = 'Yes'
                        if 'airco' in option:
                            data['air_conditioning'] = 'Yes'
                        if 'Automaat/Semi-Automaat' in option:
                            data['transition'] = 'Yes'
                        if 'Trailer Hitch' in option:
                            data['trailer_hitch'] = 'Yes'
                        if 'Navigation' in option:
                            data['navigation'] = 'Yes'
                        if 'Air Conditioning' in option:
                            data['air_conditioning'] = 'Yes'


        serializer = VsBasicDataSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            if role == 'Uploader':
                email = vs_add_car_by_user(access_token, (request.data)[0])
                if email == False:
                    message = {'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST, 'message': "Email Not Sent"}
                    return Response(message)
            data = serializer.data
            for data in data:
                if data['images'] != None and len(data['images']) >= 2:
                    data['images'] = eval(data['images'])
            # data = vs_language_filter(language,data)
            if language == 'en':
                data = {'status': 'success', 'message': 'Car saved successfully', 'code': status.HTTP_200_OK,
                        'data': serializer.data}
            else:
                data = {'status': 'success', 'message': 'Auto succesvol opgeslagen', 'code': status.HTTP_200_OK,
                        'data': serializer.data}
            return Response(data)
        message = {'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors}
        return Response(message)
    def delete(self, request, pk=None, format=None):
        id = pk
        access_token = self.request.META.get('HTTP_AUTHORIZATION')
        language = self.request.META.get('HTTP_LANGUAGE')
        response = getUserDetails(access_token)
        if response:
            role = response['data']['role']
            ev_category = response['data']['category']
        else:
            if language == 'en':
                message = {"message": "Unauthorized User", "code": status.HTTP_401_UNAUTHORIZED,
                           "status": "Unauthorized"}
            else:
                message = {"message": "Ongeautoriseerde gebruiker", "code": status.HTTP_401_UNAUTHORIZED,
                           "status": "Unauthorized"}
            return Response(message)
        if role != "Admin":
            if language == 'en':
                message = {'status': "failed", 'code': status.HTTP_401_UNAUTHORIZED, 'message': 'Admin Credential Required'}
            else:
                message = {'status': "failed", 'code': status.HTTP_401_UNAUTHORIZED, 'message': 'Beheerdersreferentie vereist'}
            return Response(message)
        try:
            vehicle = vs_vehicles.objects.get(id=id)

            vehicle.delete()
            if language == 'en':
                message = {'status': "success", 'code': status.HTTP_200_OK, "message": "Car deleted successfully"}
            else:
                message = {'status': "success", 'code': status.HTTP_200_OK, "message": "Auto succesvol verwijderd"}
            return Response(message)
        except:
            if language == 'en':
                message = {'status': "failed", 'code': status.HTTP_404_NOT_FOUND, "message": "No detail found"}
            else:
                message = {'status': "failed", 'code': status.HTTP_404_NOT_FOUND, "message": "Geen detail gevonden"}
            return Response(message)

    def patch(self, request, pk=None, format=None):
        id = pk
        access_token = self.request.META.get('HTTP_AUTHORIZATION')
        language = self.request.META.get('HTTP_LANGUAGE')
        response = getUserDetails(access_token)
        if response:
            role = response['data']['role']
            ev_category = response['data']['category']
        else:
            if language == 'en':
                message = {"message": "Unauthorized User", "code": status.HTTP_401_UNAUTHORIZED,
                           "status": "Unauthorized"}
            else:
                message = {"message": "Ongeautoriseerde gebruiker", "code": status.HTTP_401_UNAUTHORIZED,
                           "status": "Unauthorized"}
            return Response(message)
        if role != "Admin":
            if language == 'en':
                message = {'status': "failed", 'code': status.HTTP_401_UNAUTHORIZED, 'message': 'Admin Credential Required'}
            else:
                message = {'status': "failed", 'code': status.HTTP_401_UNAUTHORIZED, 'message': 'Beheerdersreferentie vereist'}
            return Response(message)
        try:
            vehicle = vs_vehicles.objects.get(id=id)
        except:
            if language == 'en':
                message = {'status': "failed", 'code': status.HTTP_404_NOT_FOUND, "message": "No detail found"}
            else:
                message = {'status': "failed", 'code': status.HTTP_404_NOT_FOUND, "message": "Geen detail gevonden"}
            return Response(message)
        data = request.data
        if "images" in data.keys() :
            data['images'] = str(data['images'])
        serializer = VsBasicDataSerializer(vehicle, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            try:
                data['images'] = eval(data['images'])
            except:
                pass

            data = {'status': 'success', 'code': status.HTTP_200_OK, 'data': serializer.data}
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        id = pk
        access_token = self.request.META.get('HTTP_AUTHORIZATION')
        language = self.request.META.get('HTTP_LANGUAGE')

        response = getUserDetails(access_token)
        if response:
            role = response['data']['role']
            ev_category = response['data']['category']
        else:
            if language == 'en':
                message = {"message": "Unauthorized User", "code": status.HTTP_401_UNAUTHORIZED}
            else:
                message = {"message": "Ongeautoriseerde gebruiker", "code": status.HTTP_401_UNAUTHORIZED}
            return Response(message)
        if role != "Admin":
            if language == 'en':
                message = {'status': "failed", 'code': status.HTTP_401_UNAUTHORIZED, 'message': 'Admin Credential Required'}
            else:
                message = {'status': "failed", 'code': status.HTTP_401_UNAUTHORIZED, 'message': 'Beheerdersreferentie vereist'}
            return Response(message)
        vehicle = vs_vehicles.objects.get(id=id)
        data = request.data

        if "images" in data.keys():
            data['images'] = str(data['images'])
        serializer = VsBasicDataSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            try:
                data['images'] = eval(data['images'])
            except:
                pass
            data = {'status': 'success', 'code': status.HTTP_200_OK, 'data': serializer.data}
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




from .serializers import DoorSerializer,ColorSerializer,TransitionSerializer

class vs_vehicle_dropdown(APIView):
    def get(self, request, pk=None, format=None, *args, **kwargs):
        language = request.META.get('HTTP_LANGUAGE')
        access_token = self.request.META.get('HTTP_AUTHORIZATION')
        response = getUserDetails(access_token)
        if response:
            role = response['data']['role']
            ev_category = response['data']['category']
        else:
            if language == 'en':
                message = {"message": "Unauthorized User", "code": status.HTTP_401_UNAUTHORIZED}
            else:
                message = {"message": "Ongeautoriseerde gebruiker", "code": status.HTTP_401_UNAUTHORIZED}
            return Response(message)
        brand = self.request.query_params.get('brand', None)
        if language == "en":
            if role=='Admin':
                data1 = vs_vehicles.objects.order_by('brand').filter(brand__isnull=False).values('brand').distinct()
                door = vs_vehicles.objects.order_by('doors').filter(doors__isnull=False).values('doors').distinct()
                transition = vs_vehicles.objects.order_by('transition').filter(transition__isnull=False).values('transition').distinct()
                color=vs_vehicles.objects.order_by('color_en').filter(color_en__isnull=False).values(color=F('color_en')).distinct()
            else:
                data1 = vs_vehicles.objects.order_by('brand').filter(brand__isnull=False,ispublished=True).values('brand').distinct()
                door = vs_vehicles.objects.order_by('doors').filter(doors__isnull=False,ispublished=True).values('doors').distinct()
                transition = vs_vehicles.objects.order_by('transition').filter(transition__isnull=False,ispublished=True).values(
                    'transition').distinct()
                color = vs_vehicles.objects.order_by('color_en').filter(color_en__isnull=False,ispublished=True).values(
                    color=F('color_en')).distinct()

            serializer1 = EvBrandEnSerializer(data1, many=True)
            serializer2 = DoorSerializer(door, many=True)
            serializer3 = TransitionSerializer(transition, many=True)
            serializer4= ColorSerializer(color, many=True)
            sort_params = {}
            set_if_not_none(sort_params, 'brand__in', brand)
            if brand != None:
                model = vs_vehicles.objects.order_by('model').values('model').filter(
                    **sort_params).distinct()
                serializer5= EvmodelEnSerializer(model, many=True)
                data = {'status': 'success', 'code': status.HTTP_200_OK, 'brand_data': serializer1.data,
                        'door_data': serializer2.data,'transition_data':serializer3.data,'color_data':serializer4.data, 'model_data': serializer5.data}
                return Response(data)
            data = {'status': 'success', 'code': status.HTTP_200_OK, 'brand_data': serializer1.data,
                    'door_data': serializer2.data,'transition_data':serializer3.data,'color_data':serializer4.data}
            return Response(data)
        if language == "nl":
            if language == "en":
                if role == 'Admin':
                    data1 = vs_vehicles.objects.order_by('brand').filter(brand__isnull=False).values(brand=F('brand')).distinct()
                    door = vs_vehicles.objects.order_by('doors').filter(doors__isnull=False).values('doors').distinct()
                    transition = vs_vehicles.objects.order_by('transition').filter(transition__isnull=False).values('transition').distinct()
                    color = vs_vehicles.objects.order_by('color_nl').filter(color_nl__isnull=False).values(color=F('color_nl')).distinct()
            else:
                data1 = vs_vehicles.objects.order_by('brand').filter(brand__isnull=False, ispublished=True).values(
                    'brand').distinct()
                door = vs_vehicles.objects.order_by('doors').filter(doors__isnull=False, ispublished=True).values(
                    'doors').distinct()
                transition = vs_vehicles.objects.order_by('transition').filter(transition__isnull=False,
                                                                               ispublished=True).values('transition').distinct()
                color = vs_vehicles.objects.order_by('color_nl').filter(color_nl__isnull=False,
                                                                        ispublished=True).values(
                    color=F('color_nl')).distinct()

            serializer1 = EvBrandEnSerializer(data1, many=True)
            serializer2 = DoorSerializer(door, many=True)
            serializer3 = TransitionSerializer(transition, many=True)
            serializer4 = ColorSerializer(color, many=True)
            sort_params = {}
            set_if_not_none(sort_params, 'brand__in', brand)
            if brand != None:
                model = vs_vehicles.objects.order_by('model').values(model=F('model')).filter(
                    **sort_params).distinct()
                serializer5 = EvmodelEnSerializer(model, many=True)
                data = {'status': 'success', 'code': status.HTTP_200_OK, 'brand_data': serializer1.data,
                        'door_data': serializer2.data,'transition_data':serializer3.data,'color_data':serializer4.data, 'model_data': serializer5.data}
                return Response(data)
            data = {'status': 'success', 'code': status.HTTP_200_OK, 'brand_data': serializer1.data,
                    'door_data': serializer2.data,'transition_data':serializer3.data,'color_data':serializer4.data}
            return Response(data)
        data = {'status': 'success', 'code': status.HTTP_200_OK, 'message': "Enter language in Headers"}
        return Response(data)
# --------------------------------vs car-------------------------------------------
# --------------------------------vs car-------------------------------------------
# --------------------------------vs car-------------------------------------------






class ev_car_agreement(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination
    def get(self, request, pk=None, format=None, *args, **kwargs):
        access_token = self.request.META.get('HTTP_AUTHORIZATION')
        language = self.request.META.get('HTTP_LANGUAGE')
        response = getUserDetails(access_token)
        if response:
            role = response['data']['role']
            ev_category = response['data']['category']
            user_id = response['data']['id']
        else:
            if language == 'en':
                message = {"message": "Unauthorized User", "code": status.HTTP_401_UNAUTHORIZED,
                           "status": "Unauthorized"}
            else:
                message = {"message": "Ongeautoriseerde gebruiker", "code": status.HTTP_401_UNAUTHORIZED,
                           "status": "Unauthorized"}
            return Response(message)
        if role != 'Admin':
            message = {"message": "Unauthorized User", "code": status.HTTP_401_UNAUTHORIZED,
                       "status": "Unauthorized",
                       'status': 'UnAuthorized'}
            return Response(message, status.HTTP_401_UNAUTHORIZED)

        data=ev_vehicles_order.objects.all()
        serializer = order_serializer(data,many=True)
        data = serializer.data
        return Response({"data":data})


    def post(self, request, format=None):
        access_token = self.request.META.get('HTTP_AUTHORIZATION')
        language = self.request.META.get('HTTP_LANGUAGE')
        response = getUserDetails(access_token)
        if response:
            role = response['data']['role']
            ev_category = response['data']['category']
            user_id=response['data']['id']
        else:
            if language == 'en':
                message = {"message": "Unauthorized User", "code": status.HTTP_401_UNAUTHORIZED,
                           "status": "Unauthorized"}
            else:
                message = {"message": "Ongeautoriseerde gebruiker", "code": status.HTTP_401_UNAUTHORIZED,
                           "status": "Unauthorized"}
            return Response(message)

        context = request.data
        option = context['option']
        option1 = option[0]

        if language == 'en':
            option1['option'] = option1['option_name_en']
        else:
            option1['option'] = option1['option_name_nl']
        context['option1'] = option1
        if len(option) > 1:
            other_options = option[1:len(option)]
            if language == 'en':
                for option in other_options:
                    option['option'] = option['option_name_en']
            else:
                for option in other_options:
                    option['option'] = option['option_name_nl']
            context['other_options'] = other_options

        baseurl = settings.BASE_DIR
        pdf = render_to_pdf('agreement.html', {'context': context, 'url': baseurl})
        receipt_file = BytesIO(pdf.content)

        filename =str(datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S_%f'))+".pdf"
        file = File(receipt_file, filename)
        try:
            order = ev_vehicles_order()
            order.user_id = user_id  # have to make it dynamic as per user id context['user_id']
            order.agreement_pdf = File(receipt_file, filename)
            order.save()
            agreement_file=order.agreement_pdf
            email_filename ='https://sm-car-images.s3-eu-central-1.amazonaws.com/' + str(agreement_file)
        except Exception as e:
            message = {"message": "order failed: "+str(e), "code": status.HTTP_400_BAD_REQUEST,
                       "status": "failed"}
            return Response(message)
        try:
            ev_definitely_my_car(access_token,context)
        except:
            message = {"message": "email has not been sent ", "code": status.HTTP_200_OK,
                       "status": "failed"}
            return Response(message)

        # try:
        #     subject = 'Agreements'
        #     message = 'Vehicle Agreement pdf document'
        #     message = EmailMessage(
        #         subject,
        #         message,
        #         settings.DEFAULT_FROM_EMAIL,
        #         [],)
        #     response = requests.get(email_filename)
        #     name='Attachment'
        #     message.attach(name,response.content, mimetype="application/pdf")
        #     message.send(fail_silently=False)
        #
        # except Exception as e:
        #     message = {"message":str(e), "code": status.HTTP_400_BAD_REQUEST,
        #                "status": "failed"}
        #     return Response(message)
        message = {"message": "email has been sent successfully", "code": status.HTTP_200_OK,
                   "status": "success"}
        return Response(message)



























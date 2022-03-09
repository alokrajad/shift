from rest_framework import serializers
# from .models import ShiftEvData, ShiftEvColor, ShiftEvChoosableOption,ShiftEvUploadExcel
from .models import electric_vehicles, colors_ev, choosable_options_ev,ShiftEvUploadExcel,ev_vehicles_order

from .models import vs_vehicles

class VehicleColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = colors_ev
        fields = ('id', 'color_name', 'hex_code', 'r', 'g', 'b',
                  'img1', 'img2', 'img3', 'img4', 'img5', 'created_at', 'updated_at')



class ChoosableOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = choosable_options_ev
        fields = ('id', 'option_name_en', 'option_name_nl', 'option_value',  'created_at', 'updated_at')



class VehicleDataSerializer(serializers.ModelSerializer):
    color = VehicleColorSerializer(many=True,partial=True)
    choosableoptions=ChoosableOptionSerializer(many=True,partial=True)

    class Meta:
        model = electric_vehicles
        fields = ('id', 'brand_en', 'model_en',
        'brand_nl', 'model_nl', 'version', 'car_type', 'description_en',
        'description_nl', 'wltp_range', 'additional_percentage',
        'battery_capacity', 'tax_value', 'expected_delivery_time',
        'category','ispublished','long_range_vehicles_category', 'created_at',
        'updated_at', 'color', 'choosableoptions')

    # def to_representation(self, instance):
    #     rep = super(EVDataSerializer, self).to_representation(instance)
    #     rep.pop('brand_en')
    #     rep['brand'] = instance.brand_en
    #
    #     rep.pop('model_en')
    #     rep['model'] = instance.model_en
    #
    #     rep.pop('description_en')
    #     rep['description'] = instance.description_en
    #     rep.pop['option_name_en']
    #     rep['description'] = instance.description_en
    #     # rep

    #     return rep




    def validate(self, data):
        if self.partial:
            return data
        else:
            brand_en = data.get('brand_en')
            model_en = data.get('model_en')
            version = data.get('version')
            # long_range_vehicles_category = data.get('long_range_vehicles_category')
            # if long_range_vehicles_category:
            #     long_range_list = long_range_vehicles_category.split(",")
            #     long_range_vehicles_category = min(long_range_list)
            #
            #     long_range_vehicles_category= long_range_vehicles_category


            availble = electric_vehicles.objects.filter(brand_en=brand_en, model_en=model_en, version=version)
            if availble.exists():
                raise serializers.ValidationError('This  Electric Vehicles data is already exist')
        return data

    def create(self, validated_data):
        data = validated_data.pop('color')

        options = validated_data.pop('choosableoptions')
        # long_range_vehicles_category = validated_data['long_range_vehicles_category']
        # if long_range_vehicles_category:
        #     long_range_list=long_range_vehicles_category.split(",")
        #     long_range_vehicles_category=min(long_range_list)
        #     validated_data['long_range_vehicles_category']=long_range_vehicles_category




        vehicle = electric_vehicles.objects.create(**validated_data)

        for datum in data:
            colors_ev.objects.create(vehicledata=vehicle, **datum)
        for datum in options:
            choosable_options_ev.objects.create(vehicledata=vehicle, **datum)
        return vehicle

    def update(self, instance, validated_data):
        if 'color' not in validated_data.keys():
            validated_data["color"] = []
        else:
            (instance.color).all().delete()

        if 'choosableoptions' not in validated_data.keys():
            validated_data["choosableoptions"] = []
        else:
            (instance.choosableoptions).all().delete()






        data = validated_data.pop('color')
        if len(data) != 0:
            color1 = (instance.color).all().delete()

        # color1 = list(color1)

        options = validated_data.pop('choosableoptions')
        if len(options) != 0:
            option1 = (instance.choosableoptions).all().delete()
        # option1 = list(option1)

        instance.brand_en = validated_data.get('brand_en', instance.brand_en)
        instance.model_en = validated_data.get('instance.model_en', instance.model_en)
        instance.brand_nl = validated_data.get('brand_nl', instance.brand_nl)
        instance.model_nl = validated_data.get('model_nl', instance.model_nl)
        instance.version = validated_data.get('version', instance.version)
        instance.description_en = validated_data.get('description_en', instance.description_en)
        instance.description_nl = validated_data.get('description_nl', instance.description_nl)
        instance.wltp_range = validated_data.get('wltp_range', instance.wltp_range)
        instance.additional_percentage = validated_data.get('additional_percentage', instance.additional_percentage)
        instance.battery_capacity = validated_data.get('battery_capacity', instance.battery_capacity)
        instance.tax_value = validated_data.get('tax_value', instance.tax_value)
        instance.expected_delivery_time = validated_data.get('expected_delivery_time', instance.expected_delivery_time)
        instance.category = validated_data.get('category', instance.category)
        instance.car_type = validated_data.get('car_type', instance.car_type)
        instance.ispublished = validated_data.get('ispublished', instance.ispublished)
        instance.long_range_vehicles_category = validated_data.get('long_range_vehicles_category',
                                                                   instance.long_range_vehicles_category)
        instance.save()

        # for datum in data:
        # color2 = color1.pop(0)
        # color2.color_name = datum.get('color_name', color2.color_name)
        # color2.hex_code = datum.get('hex_code', color2.hex_code)
        # color2.r = datum.get('r', color2.r)
        # color2.g = datum.get('g', color2.g)
        # color2.b = datum.get('b', color2.b)
        # color2.img1 = datum.get('img1', color2.img1)
        # color2.img2 = datum.get('img2', color2.img2)
        # color2.img3 = datum.get('img3', color2.img3)
        # color2.img4 = datum.get('img4', color2.img4)
        # color2.img5 = datum.get('img5', color2.img5)
        # color2.save()
        if len(data) != 0:
            for datum in data:
                colors_ev.objects.create(vehicledata=instance, **datum)

        if len(options) != 0:
            for datum in options:
                choosable_options_ev.objects.create(vehicledata=instance, **datum)

        return instance

        # for option in options:
        # option2 = option1.pop(0)
        # option2.option_name_en = option.get('option_name_en', option2.option_name_en)
        # option2.option_name_nl = option.get('option_name_nl', option2.option_name_nl)
        # option2.option_value = option.get('option_value', option2.option_value)
        # option2.save()



    # def update(self, instance, validated_data):
    #     if 'color' not in validated_data.keys():
    #         validated_data["color"]=[]
    #
    #     if 'choosableoptions' not in validated_data.keys():
    #         validated_data["choosableoptions"]=[]
    #
    #     data = validated_data.pop('color')
    #
    #     if len(validated_data["color"])!=0:
    #         color1 = (instance.color).all().delete()
    #
    #
    #     # color1 = list(color1)
    #
    #     options = validated_data.pop('choosableoptions')
    #     if len(validated_data["choosableoptions"]) != 0:
    #         option1 = (instance.choosableoptions).all().delete()
    #     # option1 = list(option1)
    #
    #
    #     instance.brand_en = validated_data.get('brand_en', instance.brand_en)
    #     instance.model_en = validated_data.get('instance.model_en', instance.model_en)
    #     instance.brand_nl = validated_data.get('brand_nl', instance.brand_nl)
    #     instance.model_nl = validated_data.get('model_nl', instance.model_nl)
    #     instance.version = validated_data.get('version', instance.version)
    #     instance.description_en = validated_data.get('description_en', instance.description_en)
    #     instance.description_nl = validated_data.get('description_nl', instance.description_nl)
    #     instance.wltp_range = validated_data.get('wltp_range', instance.wltp_range)
    #     instance.additional_percentage = validated_data.get('additional_percentage', instance.additional_percentage)
    #     instance.battery_capacity = validated_data.get('battery_capacity', instance.battery_capacity)
    #     instance.tax_value = validated_data.get('tax_value', instance.tax_value)
    #     instance.expected_delivery_time = validated_data.get('expected_delivery_time', instance.expected_delivery_time)
    #     instance.category = validated_data.get('category', instance.category)
    #     instance.car_type = validated_data.get('car_type', instance.car_type)
    #     instance.ispublished = validated_data.get('ispublished', instance.ispublished)
    #     instance.long_range_vehicles_category = validated_data.get('long_range_vehicles_category', instance.long_range_vehicles_category)
    #     instance.save()
    #
    #
    #     # for datum in data:
    #         # color2 = color1.pop(0)
    #         # color2.color_name = datum.get('color_name', color2.color_name)
    #         # color2.hex_code = datum.get('hex_code', color2.hex_code)
    #         # color2.r = datum.get('r', color2.r)
    #         # color2.g = datum.get('g', color2.g)
    #         # color2.b = datum.get('b', color2.b)
    #         # color2.img1 = datum.get('img1', color2.img1)
    #         # color2.img2 = datum.get('img2', color2.img2)
    #         # color2.img3 = datum.get('img3', color2.img3)
    #         # color2.img4 = datum.get('img4', color2.img4)
    #         # color2.img5 = datum.get('img5', color2.img5)
    #         # color2.save()
    #     if len(validated_data["color"]) != 0:
    #         for datum in data:
    #             colors_ev.objects.create(vehicledata=instance, **datum)
    #
    #     if len(validated_data["choosableoptions"]) != 0:
    #         for datum in options:
    #             choosable_options_ev.objects.create(vehicledata=instance, **datum)
    #
    #     # for option in options:
    #         # option2 = option1.pop(0)
    #         # option2.option_name_en = option.get('option_name_en', option2.option_name_en)
    #         # option2.option_name_nl = option.get('option_name_nl', option2.option_name_nl)
    #         # option2.option_value = option.get('option_value', option2.option_value)
    #         # option2.save()
    #
    #     return instance
    #


#for en language

class EvColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = colors_ev
        fields = ('id', 'color_name', 'hex_code', 'r', 'g', 'b',
                  'img1', 'img2', 'img3', 'img4', 'img5', 'created_at', 'updated_at')



class EvOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = choosable_options_ev
        fields = ('id', 'option_name_en',  'option_value',  'created_at', 'updated_at')

    def to_representation(self, instance):
        rep = super(EvOptionSerializer, self).to_representation(instance)
        rep.pop('id')
        rep['id'] = instance.id

        rep.pop('option_name_en')
        rep['option_name'] = instance.option_name_en

        rep.pop('option_value')
        rep['option_value'] = instance.option_value

        rep.pop('created_at')
        rep['created_at'] = instance.created_at
        rep.pop('updated_at')
        rep['updated_at'] = instance.updated_at
        return rep


class EVDataSerializer(serializers.ModelSerializer):
    color = EvColorSerializer(many=True,partial=True)
    choosableoptions=EvOptionSerializer(many=True,partial=True)

    class Meta:
        model = electric_vehicles
        fields = ('id', 'brand_en', 'model_en',
        'version', 'car_type', 'description_en',
       'wltp_range', 'additional_percentage',
        'battery_capacity', 'tax_value', 'expected_delivery_time',
        'category','ispublished','long_range_vehicles_category','created_at',
        'updated_at', 'color', 'choosableoptions')

    def to_representation(self, instance):
        rep = super(EVDataSerializer, self).to_representation(instance)
        rep.pop('id')
        rep['id'] = instance.id

        rep.pop('brand_en')
        rep['brand'] = instance.brand_en

        rep.pop('model_en')
        rep['model'] = instance.model_en

        rep.pop('version')
        rep['version'] = instance.version

        rep.pop('description_en')
        rep['description'] = instance.description_en

        rep.pop('wltp_range')
        rep['wltp_range'] = instance.wltp_range

        rep.pop('additional_percentage')
        rep['additional_percentage'] = instance.additional_percentage

        rep.pop('battery_capacity')
        rep['battery_capacity'] = instance.battery_capacity

        rep.pop('tax_value')
        rep['tax_value'] = instance.tax_value

        rep.pop('expected_delivery_time')
        rep['expected_delivery_time'] = instance.expected_delivery_time

        rep.pop('category')
        rep['category'] = instance.category

        rep.pop('ispublished')
        rep['ispublished'] = instance.ispublished

        rep.pop('long_range_vehicles_category')
        rep['long_range_vehicles_category'] = instance.long_range_vehicles_category

        rep.pop('car_type')
        rep['car_type'] = instance.car_type

        rep.pop('created_at')
        rep['created_at'] = instance.created_at

        rep.pop('updated_at')
        rep['updated_at'] = instance.updated_at

        # rep['color'] = instance.color
        # rep['choosableoptions'] = instance.choosableoptions
        return rep





#for nl language

class EvNlColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = colors_ev
        fields = ('id', 'color_name', 'hex_code', 'r', 'g', 'b',
                  'img1', 'img2', 'img3', 'img4', 'img5', 'created_at', 'updated_at')


class EvNlOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = choosable_options_ev
        fields = ('id',  'option_name_nl', 'option_value',  'created_at', 'updated_at')
    def to_representation(self, instance):
        rep = super(EvNlOptionSerializer, self).to_representation(instance)
        rep.pop('id')
        rep['id'] = instance.id

        rep.pop('option_name_nl')
        rep['option_name'] = instance.option_name_nl

        rep.pop('option_value')
        rep['option_value'] = instance.option_value

        rep.pop('created_at')
        rep['created_at'] = instance.created_at
        rep.pop('updated_at')
        rep['updated_at'] = instance.updated_at

        return rep


class EvNlDataSerializer(serializers.ModelSerializer):
    color = EvNlColorSerializer(many=True,partial=True)
    choosableoptions=EvNlOptionSerializer(many=True,partial=True)

    class Meta:
        model = electric_vehicles
        fields = ('id',
        'brand_nl', 'model_nl', 'version', 'car_type',
        'description_nl', 'wltp_range', 'additional_percentage',
        'battery_capacity', 'tax_value', 'expected_delivery_time',
        'category','ispublished','long_range_vehicles_category', 'created_at',
        'updated_at', 'color', 'choosableoptions')

    def to_representation(self, instance):
        rep = super(EvNlDataSerializer, self).to_representation(instance)
        rep.pop('brand_nl')
        rep['brand'] = instance.brand_nl

        rep.pop('model_nl')
        rep['model'] = instance.model_nl

        rep.pop('version')
        rep['version'] = instance.version

        rep.pop('description_nl')
        rep['description'] = instance.description_nl

        rep.pop('wltp_range')
        rep['wltp_range'] = instance.wltp_range

        rep.pop('additional_percentage')
        rep['additional_percentage'] = instance.additional_percentage

        rep.pop('battery_capacity')
        rep['battery_capacity'] = instance.battery_capacity

        rep.pop('tax_value')
        rep['tax_value'] = instance.tax_value

        rep.pop('expected_delivery_time')
        rep['expected_delivery_time'] = instance.expected_delivery_time

        rep.pop('category')
        rep['category'] = instance.category

        rep.pop('ispublished')
        rep['ispublished'] = instance.ispublished

        rep.pop('long_range_vehicles_category')
        rep['long_range_vehicles_category'] = instance.long_range_vehicles_category

        rep.pop('car_type')
        rep['car_type'] = instance.car_type

        rep.pop('created_at')
        rep['created_at'] = instance.created_at

        rep.pop('updated_at')
        rep['updated_at'] = instance.updated_at
        return rep


class ExcelpageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftEvUploadExcel
        fields = ('id', 'ev_file')
#
#

class EvBrandEnSerializer(serializers.Serializer):
    brand = serializers.CharField(max_length=200)

class EvmodelEnSerializer(serializers.Serializer):
    model = serializers.CharField(max_length=200)

class EvVersionSerializer(serializers.Serializer):
    version = serializers.CharField(max_length=200)


class DoorSerializer(serializers.Serializer):
    doors = serializers.IntegerField()

class ColorSerializer(serializers.Serializer):
    color = serializers.CharField()


class TransitionSerializer(serializers.Serializer):
    transition = serializers.CharField(max_length=200)




#______________________________________________________________


class VsBasicDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = vs_vehicles
        fields = ('id', 'brand', 'model',
                  'color_en', 'color_nl', 'version', 'licence_plate', 'transition','pitch_en' , 'pitch_nl',
                  'doors','category','mileage', 'construction_year',
                  'fuel',  'price','ispublished','trailer_hitch','navigation','air_conditioning',
                  'tax_value','first_registration','power_pk','power_kw','tax_addition','end_date',
                  'images', 'created_at', 'updated_at')

    def create(self, validated_data):
        basic_data = vs_vehicles.objects.create(**validated_data)
        return basic_data

    def update(self, instance, validated_data):
        instance.brand = validated_data.get('brand', instance.brand)
        # instance.brand_nl = validated_data.get('brand_nl', instance.brand_nl)
        instance.model = validated_data.get('model', instance.model)
        # instance.model_nl = validated_data.get('model_nl', instance.model_nl)
        instance.color_en = validated_data.get('color_en', instance.color_en)
        instance.color_nl = validated_data.get('color_nl', instance.color_nl)
        instance.version = validated_data.get('version', instance.version)
        instance.licence_plate = validated_data.get('licence_plate', instance.licence_plate)
        instance.transition = validated_data.get('transition', instance.transition)
        instance.pitch_en = validated_data.get('pitch_en', instance.pitch_en)
        instance.pitch_nl = validated_data.get('pitch_nl', instance.pitch_nl)
        instance.doors = validated_data.get('doors', instance.doors)
        instance.category = validated_data.get('category', instance.category)
        instance.mileage = validated_data.get('mileage', instance.mileage)
        instance.construction_year = validated_data.get('construction_year', instance.construction_year)
        instance.fuel = validated_data.get('fuel', instance.fuel)
        instance.price = validated_data.get('price', instance.price)
        instance.trailer_hitch = validated_data.get('trailer_hitch', instance.trailer_hitch)
        instance.navigation = validated_data.get('navigation', instance.navigation)
        instance.air_conditioning = validated_data.get('air_conditioning', instance.air_conditioning)
        instance.tax_value = validated_data.get('tax_value', instance.tax_value)
        instance.first_registration = validated_data.get('first_registration', instance.first_registration)
        instance.power_pk = validated_data.get('power_pk', instance.power_pk)
        instance.power_kw = validated_data.get('power_kw', instance.power_kw)
        instance.images = validated_data.get('images', instance.images)
        instance.ispublished = validated_data.get('ispublished', instance.ispublished)
        instance.tax_addition = validated_data.get('tax_addition', instance.tax_addition)
        instance.end_date = validated_data.get('end_date', instance.end_date)



        instance.save()

        return instance



class VsEnSerializer(serializers.ModelSerializer):

    class Meta:
        model = vs_vehicles
        fields = ('id', 'brand_en',  'model_en',
                  'color_en',  'version', 'licence_plate', 'transition', 'pitch_en',
                  'doors', 'category', 'mileage', 'construction_year',
                  'fuel', 'price', 'ispublished', 'trailer_hitch', 'navigation', 'air_conditioning',
                  'tax_value', 'first_registration', 'power_pk', 'power_kw', 'tax_addition', 'end_date',
                  'images', 'created_at', 'updated_at')

    def to_representation(self, instance):
        rep = super(VsEnSerializer, self).to_representation(instance)
        rep.pop('id')
        rep['id'] = instance.id

        rep.pop('brand_en')
        rep['brand'] = instance.brand_en

        rep.pop('model_en')
        rep['model'] = instance.model_en

        rep.pop('color_en')
        rep['color'] = instance.color_en

        rep.pop('pitch_en')
        rep['pitch'] = instance.pitch_en

        return rep


class VsNlSerializer(serializers.ModelSerializer):
    class Meta:
        model = vs_vehicles
        fields = ('id', 'brand_nl', 'model_nl',
                  'color_nl', 'version', 'licence_plate', 'transition', 'pitch_nl',
                  'doors', 'category', 'mileage', 'construction_year',
                  'fuel', 'price', 'ispublished', 'trailer_hitch', 'navigation', 'air_conditioning',
                  'tax_value', 'first_registration', 'power_pk', 'power_kw', 'tax_addition', 'end_date',
                  'images', 'created_at', 'updated_at')

    def to_representation(self, instance):
        rep = super(VsNlSerializer, self).to_representation(instance)
        rep.pop('id')
        rep['id'] = instance.id

        rep.pop('brand_nl')
        rep['brand'] = instance.brand_nl

        rep.pop('model_nl')
        rep['model'] = instance.model_nl

        rep.pop('color_nl')
        rep['color'] = instance.color_nl

        rep.pop('pitch_nl')
        rep['pitch'] = instance.pitch_nl

        return rep




class order_serializer(serializers.ModelSerializer):
    class Meta:
        model=ev_vehicles_order
        fields=('id','agreement_pdf', 'user_id','created_at')





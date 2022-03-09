from django.db import models
from datetime import datetime, date
# import datetime
from django.core.validators import FileExtensionValidator
from django.contrib.postgres.fields import ArrayField
# class Board(models.Model):
#     pieces = ArrayField(ArrayField(models.IntegerField()))
# from django.utils import timezone

class electric_vehicles(models.Model):
    brand_en = models.CharField(max_length=200)
    model_en = models.CharField(max_length=200)
    brand_nl = models.CharField(max_length=200)
    model_nl = models.CharField(max_length=200)
    version = models.CharField(max_length=200,blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    description_nl = models.TextField(blank=True, null=True)
    wltp_range = models.IntegerField(blank=True, null=True)
    expected_delivery_time = models.CharField(max_length=200,blank=True, null=True)
    km_range=models.IntegerField(blank=True, null=True)
    Manufacturer_specification_km_range=models.IntegerField(blank=True, null=True)
    charging_speed_fast_charging_kwh=models.IntegerField(blank=True, null=True)
    fast_charge_ten_to_eigthy_percent_in_minutes=models.IntegerField(blank=True, null=True)
    ten_minutes_of_fast_charging_is_km=models.IntegerField(blank=True, null=True)
    heat_pump=models.FloatField(blank=True, null=True)
    lease_ex_fuel=models.FloatField(blank=True, null=True)
    fuel=models.FloatField(blank=True, null=True)
    lease_incl_fuel=models.FloatField(blank=True, null=True)
    towbar_contribution=models.FloatField(blank=True, null=True)
    towbar_explanation=models.CharField(max_length=200,blank=True, null=True)
    additional_percentage = models.IntegerField(blank=True, null=True)
    battery_capacity = models.FloatField(blank=True, null=True)
    tax_value = models.FloatField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    car_type = models.CharField(max_length=10, choices=(('Standard', 'Standard_Car'), ('Best', 'Best_Buys')))  # increase a column car type in excel sheet
    ispublished = models.BooleanField(default=False)
    long_range_vehicles_category = models.IntegerField(blank=True, null=True) #[1,4,8,7,6]"1,2,3"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand_en





class colors_ev(models.Model):
    vehicledata=models.ForeignKey(electric_vehicles, on_delete=models.CASCADE,related_name='color')
    color_name = models.CharField(max_length=200,blank=True, null=True)
    hex_code = models.CharField(max_length=20,blank=True, null=True)
    r=models.CharField(max_length=5,blank=True, null=True)
    g=models.CharField(max_length=5,blank=True, null=True)
    b=models.CharField(max_length=5,blank=True, null=True)
    img1=models.CharField(max_length=200,blank=True, null=True)
    img2=models.CharField(max_length=200,blank=True, null=True)
    img3=models.CharField(max_length=200,blank=True, null=True)
    img4=models.CharField(max_length=200,blank=True, null=True)
    img5=models.CharField(max_length=200,blank=True, null=True)

    # img1=models.ImageField(blank=True, null=True)
    # img2=models.ImageField(blank=True, null=True)
    # img3=models.ImageField(blank=True, null=True)
    # img4=models.ImageField(blank=True, null=True)
    # img5=models.ImageField( blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.color_name
   



class choosable_options_ev(models.Model):
    option_name_en = models.CharField(max_length=200, blank=True, null=True)
    option_name_nl = models.CharField(max_length=200, blank=True, null=True)
    option_value = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    vehicledata=models.ForeignKey(electric_vehicles, on_delete=models.CASCADE, related_name='choosableoptions')

    def __str__(self):
        return self.option_name_en




class ShiftEvUploadExcel(models.Model):
    ev_file = models.FileField(upload_to='excel',default=None,blank=True,validators=[FileExtensionValidator(allowed_extensions=['ods','xls','xlsx','xlsm','xlsb','xltx','xltm'])])
    created_at = models.DateTimeField(auto_now_add=True)

    # validators = [FileExtensionValidator(allowed_extensions=['ods', 'xlr', 'xlw'
    #     , 'xla', 'xlam', 'xml', 'xml', 'xls', 'xlsx', 'xlsm', 'xlsb', 'xltx', 'xltm'])]








#_________________________________MODEL FOR VIRTUAL SHOWROOM________________________________________________

class vs_vehicles(models.Model):
    brand= models.CharField(max_length=200)
    # brand_nl = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    # model_nl = models.CharField(max_length=200)
    color_en = models.CharField(max_length=200,blank=True, null=True)
    color_nl = models.CharField(max_length=200,blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    licence_plate = models.CharField(max_length=200, unique=True)
    transition = models.CharField(max_length=100,blank=True, null=True)
    pitch_en = models.TextField(default=None,blank=True, null=True)
    pitch_nl = models.TextField(default=None,blank=True, null=True)
    doors = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    construction_year = models.IntegerField(blank=True, null=True)
    fuel = models.CharField(max_length=200,blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    trailer_hitch = models.CharField(max_length=10,choices=(('Yes', 'Yes'), ('No', 'No')),default="No")
    navigation = models.CharField(max_length=10,choices=(('Yes', 'Yes'), ('No', 'No')),default="No")
    air_conditioning = models.CharField(max_length=10,choices=(('Yes', 'Yes'), ('No', 'No')),default="No")
    tax_value = models.FloatField(blank=True, null=True)
    first_registration = models.IntegerField(blank=True, null=True)
    power_pk = models.IntegerField(blank=True, null=True)
    power_kw = models.IntegerField(blank=True, null=True)
    tax_addition = models.FloatField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    images=models.TextField(blank=True, null=True)
    ispublished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand








class ev_vehicles_order(models.Model):
    agreement_pdf= models.FileField(upload_to='agreements/')
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)








# class CarVsOptions(models.Model):


    # ispublished = models.BooleanField(default=False)
    # long_range_vehicles_category = models.CharField(max_length=10,blank=True, null=True)
    # img1=models.URLField(blank=True, null=True)
    # img2=models.URLField(blank=True, null=True)
    # img3=models.URLField(blank=True, null=True)
    # img4=models.URLField(blank=True, null=True)
    # img5=models.URLField( blank=True, null=True)

#     specific_version = models.CharField(max_length=100)
#     trailer_hitch = models.CharField(max_length=10,choices=(('Yes', 'Yes'), ('No', 'No'),))
#     navigation = models.CharField(max_length=10,choices=(('Yes', 'Yes'), ('No', 'No'),))
#     air_conditioning = models.CharField(max_length=10,choices=(('Yes', 'Yes'), ('No', 'No'),))
#     car_details = models.OneToOneField(CarVsBasicData, on_delete=models.CASCADE, related_name='option')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.specific_version


# class CarVsTaxData(models.Model):
#     tax_value = models.FloatField()
#     first_registration = models.IntegerField()
#     power_pk = models.IntegerField()
#     power_kw = models.IntegerField()
#     co2_emission_wtlp = models.IntegerField()
#     co2_emission_nedc = models.IntegerField()
#     tax_addition = models.FloatField()
#     energie_label = models.CharField(max_length=100)
#     car_details = models.OneToOneField(CarVsBasicData, on_delete=models.CASCADE, related_name='tax')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.energie_label
# class carVsContractDetails(models.Model):
#     contract_reference = models.CharField(max_length=100,blank=True, null=True)
#     start_date = models.DateField(default=date.today())
#     end_date = models.DateField()
#     owner = models.CharField(max_length=100,blank=True, null=True)
#     lease_amount = models.FloatField()
#     car_details = models.OneToOneField(CarVsBasicData, on_delete=models.CASCADE, related_name='contract')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.contract_reference


# class employee_organisation(models.Model):
#     company_name = models.CharField(max_length=200)
#     employee_category=models.IntegerField()
#     ninety_percent = models.CharField(max_length=200)
#     eighty_percent = models.CharField(max_length=200)
#     seventy_percent = models.CharField(max_length=200)
#     sixty_percent = models.CharField(max_length=200)
#     fifty_percent = models.CharField(max_length=200)


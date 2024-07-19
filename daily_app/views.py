from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import *
from django.core import serializers
import datetime,ast,json

# Create your views here.
def index(request):
    res_obj = DayWiseData.objects.filter(date=datetime.date.today())
    res_obj_json = serializers.serialize('json', res_obj)
    return render(request,'index.html',{'res_obj':res_obj_json})

def save_record(request):
    req_data = ast.literal_eval(request.POST['postData'])[0]
    try:
        res_obj = DayWiseData.objects.get(date=request.POST['date_'],sub_category=req_data[1])
        res_obj.reason = req_data[3]
        res_obj.input = req_data[2]
        res_obj.time_0800 = req_data[4]
        res_obj.time_0900 = req_data[5]
        res_obj.time_1000 = req_data[6]
        res_obj.time_1100 = req_data[7]
        res_obj.time_1200 = req_data[8]
        res_obj.time_1300 = req_data[9]
        res_obj.time_1400 = req_data[10]
        res_obj.time_1500 = req_data[11]
        res_obj.time_1600 = req_data[12]
        res_obj.time_1700 = req_data[13]
        res_obj.time_1800 = req_data[14]
        res_obj.time_1900 = req_data[15]
        res_obj.time_2000 = req_data[16]
        res_obj.time_2100 = req_data[17]
        res_obj.time_2200 = req_data[18]
        res_obj.time_2300 = req_data[19]
        res_obj.time_0000 = req_data[20]
        res_obj.time_0100 = req_data[21]
        res_obj.time_0200 = req_data[22]
        res_obj.time_0300 = req_data[23]
        res_obj.time_0400 = req_data[24]
        res_obj.time_0500 = req_data[25]
        res_obj.time_0600 = req_data[26]
        res_obj.time_0700 = req_data[27]
        res_obj.save()
    except:
        res_obj = DayWiseData()
        res_obj.sub_category = SubCategory.objects.get(sub_category_id=req_data[1])
        res_obj.date = request.POST['date_']
        res_obj.time_0800 = req_data[4]
        res_obj.time_1000 = req_data[5]
        res_obj.time_1200 = req_data[6]
        res_obj.time_1400 = req_data[7]
        res_obj.time_1600 = req_data[8]
        res_obj.time_1800 = req_data[9]
        res_obj.time_2000 = req_data[10]
        res_obj.time_2200 = req_data[11]
        res_obj.time_0000 = req_data[12]
        res_obj.time_0200 = req_data[13]
        res_obj.time_0400 = req_data[14]
        res_obj.save()
        
    return JsonResponse({'msg':'okkkk'})

def filterDate(request):
    res_obj = DayWiseData.objects.filter(date=request.POST['filterDate'])
    res_obj_json = serializers.serialize('json', res_obj)
    return render(request,'table_ajax.html',{'res_obj':res_obj_json})
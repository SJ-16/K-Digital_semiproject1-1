import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from projectdata_pre.myanalysis.preprocess import preprocess


def home(request):
    return render(request, 'home.html');
def gamgi(request):
    return render(request, 'gamgi.html');
def gamgis(request):
    data = preprocess().gamgi();
    return HttpResponse(json.dumps(data), content_type='applicaiton/json');
def gamgi_new(request):
    return render(request, 'gamgi_new.html');
def gamgi_news(request):
    data = preprocess().gamgi_new();
    return HttpResponse(json.dumps(data), content_type='applicaiton/json');
def chunsik(request):
    return render(request, 'chunsik.html');
def chunsiks(request):
    data = preprocess().chunsik();
    return HttpResponse(json.dumps(data), content_type='applicaiton/json');
def smartwork(request):
    return render(request, 'smartwork.html');
def smartworks(request):
    data = preprocess().smartwork();
    return HttpResponse(json.dumps(data), content_type='applicaiton/json');
def hospital(request):
    return render(request, 'hospital.html');
def hospitals(request):
    data = preprocess().hospital();
    return HttpResponse(json.dumps(data), content_type='applicaiton/json');
def hospital_m(request):
    return render(request, 'hospital_m.html');
def hospital_ms(request):
    data = preprocess().hospital_m();
    return HttpResponse(json.dumps(data), content_type='applicaiton/json');
def hospital_h(request):
    return render(request, 'hospital_h.html');
def hospital_hs(request):
    data = preprocess().hospital_h();
    return HttpResponse(json.dumps(data), content_type='applicaiton/json');
def hospital_p(request):
    return render(request, 'hospital_p.html');
def hospital_ps(request):
    data = preprocess().hospital_p();
    return HttpResponse(json.dumps(data), content_type='applicaiton/json');
def hospital_pm(request):
    return render(request, 'hospital_pm.html');
def hospital_pms(request):
    data = preprocess().hospital_pm();
    return HttpResponse(json.dumps(data), content_type='applicaiton/json');
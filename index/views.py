from django.shortcuts import render,redirect
from index.models import Contact
from index.models import Service
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def company(request):
    return render(request,'company.html')
def meet_the_team(request):
    return render(request,'meet_the_team.html')

def privacy_policy(request):
    return render(request,'privacy_policy.html')

def work(request):
    return render(request,'work.html')

def contact(request):
    if request.method=="GET":
        return render(request,'contact.html')
    if request.method=="POST":
        try:
            data=request.POST
            full_name=data.get('full_name',"")
            email=data.get('email',"")
            phone_number=data.get("phone_number")
            help=data.get("help","")
            company=data.get('company','')
            Contact.objects.create(full_name=full_name,email=email,phone_number=phone_number,help=help,company=company)
            messages.success(request,"Your request has been submited.Our Team will contact You Soon")
            referer = request.POST.get('referer', '/')
            print(referer)
            return redirect(referer)
        except Exception as e:
            print(e)
            return render(request,'contact.html',{"error":str(e)})

def services(request):
    return render(request,'services.html')

def service(request,service_slug):
    try:
        service=Service.objects.get(title_slug=service_slug)
        context={
            'service':service
            }
        if service_slug=="web-design-and-development" or service_slug=="e-commerce-development" or service_slug=="web-maintenance-and-support":
            context['website']=True
        return render(request,'service.html',context)
    except Exception as e:
        print(e)
        return JsonResponse({"error":"page doesnot exists"},status=400)


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def run_service_script(request):
    try:
        data=json.loads(request.body)
        Service.objects.create(title=data.get('title'),top_header=data.get('top_header'),content_header_1=data.get('content_header_1'),content_header_2=data.get('content_header_2'),content_header_3=data.get('content_header_3'),content_header_4=data.get('content_header_4'),content_text_1=data.get('content_text_1'),content_text_2=data.get('content_text_2'),content_text_3=data.get('content_text_3'),content_text_4=data.get('content_text_4'))

        print(data)
        return JsonResponse({"status":"OK"},status=200)
    except Exception as e:
        print(e)
        return JsonResponse({"error":f"{str(e)}"},status=400)



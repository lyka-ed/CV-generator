from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse 
from django.template import loader 
import io

# Create your views here.
def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        role = request.POST.get("role","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        github = request.POST.get("github","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        university = request.POST.get("university","")
        work_experience = request.POST.get("work_experience","")
        technical_skills = request.POST.get("technical_skills","")
        soft_skills = request.POST.get("soft_skills","")

        profile =Profile(name=name,role=role,email=email,phone=phone,github=github,summary=summary,degree=degree,university=university,work_experience=work_experience,technical_skills=technical_skills,soft_skills=soft_skills)
        profile.save()

    return render(request, 'cvgen/accept.html')


def cv(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('cvgen/cv.html')
    html = template.render({'user_profile':user_profile})
    options ={
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    filename = "cv.pdf"
    response['Content-Disposotion']='attachment; filename=' + filename
    
    return response

def list(request):
    profiles = Profile.objects.all()
    return render(request,'cvgen/list.html',{'profiles':profiles})


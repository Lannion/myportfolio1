from django.shortcuts import render

def about_me(request):
    return render(request, 'AboutMe.html')

def skill_s(request):
    return render(request, 'Skills.html')

def project_s(request):
    return render(request, 'Projects.html')
    
def cha_lea(request):
    return render(request, 'ChaLea.html')

def fut_ure(request):
    return render(request, 'Future.html')

def res_ume(request):
    return render(request, 'Resume.html')

def con_tact(request):
    return render(request, 'Contact.html')    

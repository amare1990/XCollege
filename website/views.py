from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html', {})


def admission(request):
    return render(request, 'website/admission.html', {})

def csBSc(request):
    return render(request, 'website/cs_bsc.html')

def seBSc(request):
    return render(request, 'website/se_bsc.html')

def csMSc(request):
    return render(request, 'website/cs_bsc.html')

def seMSc(request):
    return render(request, 'website/cs_bsc.html')

def courses(request):
    return render(request, 'website/courses_list.html')


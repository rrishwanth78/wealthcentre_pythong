from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'pages-login.html')

def alerts(request):
    return render(request, 'components-alerts.html')

def forms_elements(request):
    return render(request, 'forms-elements.html')

def forms_layouts(request):
    return render(request, 'forms-layouts.html')

def forms_layouts(request):
    return render(request, 'forms-layouts.html')

def forms_validation(request):
    return render(request, 'forms-validation.html')

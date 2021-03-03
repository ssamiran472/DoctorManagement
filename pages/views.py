from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def todayOpdPatients(request):
    return render(request, 'todayOPDPatients.html')


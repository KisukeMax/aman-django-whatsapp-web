from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json




# Create your views here.

# Create your views here.
def home(request):
    # return HttpResponse("Hellaao World2")
    return render(request, "business/index.html")
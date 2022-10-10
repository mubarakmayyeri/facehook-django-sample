from django.shortcuts import render
from .forms import SigninForm
# Create your views here.

def home(request):
  return render(request, 'index.html', {'form': SigninForm})
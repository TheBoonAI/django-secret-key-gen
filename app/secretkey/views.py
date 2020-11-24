from django.shortcuts import render
from django.core.management.utils import get_random_secret_key


# Create your views here.
def generate_secret_key(request):
  return render(request, 'secretkey/index.html', {'secret_key': get_random_secret_key()})
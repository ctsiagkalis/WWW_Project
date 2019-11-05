from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def signup(request):
#     return render(request, 'signup.html')
    # form_class = UserCreationForm
    # return HttpResponse(form_class)
    # success_url = reverse_lazy('login')
    # template_name = 'signup.html'

# def login(request):
#     return HttpResponse("Log in using the form below:")

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def generate_qrcode():
    import qrcode
    img = qrcode.make('bitcoincash:qqy7g6p2eyyf7xk4h2j0t8lxq38sj57ga5n8xshhfn')
    img.save('test.png')
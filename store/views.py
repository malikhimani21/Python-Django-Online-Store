from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from store.forms.authforms import CustomerCreationForms

# Create your views here.


def home(request):
    return render(request, template_name='store/home.html')


def cart(request):
    return render(request, template_name="store/cart.html")


def orders(request):
    return render(request, template_name="store/orders.html")


def login(request):
    return render(request, template_name="store/login.html")


def signup(request):

    if (request.method == 'GET'):
        form = CustomerCreationForms()
        context = {
            "form": form
        }
        return render(request, template_name="store/signup.html", context=context)

    else:
        form = CustomerCreationForms(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()
            print(user)
            return render(request, template_name="store/login.html")

        context = {
            "form": form
        }
        return render(request, template_name="store/signup.html", context=context)


def signout(request):
    return render(request, template_name="store/home.html")

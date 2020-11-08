from django.shortcuts import render
from myapp.models import Employee
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect


def upload(request):
    return render(request, "uploadfile.html")


def home(request):
    messages.info(request, f"You are now logged in as ")
    return render(request, 'home.html', {"messages": messages})


def logout_method(request):
    logout(request)
    messages.info(request, "logged out ")
    return login_request(request)


def login_request(request):
    print("i am heres")
    if request.method == 'POST':
        print("i am heres post")
        form = AuthenticationForm(request=request, data=request.POST)
        print("i am heres is valid")
        if form.is_valid():
            print("i am heres is valid")
            username = form.cleaned_data.get('username')
            print(username)
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome  {username}")
                return render(request, "home.html")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="signup.html",
                  context={"form": form})


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = "/myapp"
    template_name = 'signup.html'

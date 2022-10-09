from django.shortcuts import render
from django.http import HttpResponse
from my_app1.models import Users, Signup, UserProfileInfo
from my_app1.forms import NewUserForm, UserProfileInfoForm, UserForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def index(request):
    template_name = 'my_app1/index.html'
    context = {'insert_me':"You are in the right place where you can get help easily without asking."}
    return render(request, template_name)

def help(request):
    my_dict = {'help_me':"This is help me 2"}
    return render(request, 'my_app1/help.html', context=my_dict)

def users(request):
    data_user = Signup.objects.order_by('first_name')
    #fisrt_name = Users.objects.order_by('first_name')
    #last_name = Users.objects.order_by('last_name')
    #email = Users.objects.order_by('email')

    my_dict = {
        #'f_name':fisrt_name,
        #'l_name':last_name,
        #'email_user':email,
        'user_data': data_user
    }

    return render(request,'my_app1/users.html', context=my_dict)

def signup(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            #return to to the index page/Home page.
            return index(request)
        else:
            print("ERROR FORM INVALID!")

    return render(request, 'my_app1/signup.html', {'form': form})

def about(request):

    my_text = {'text':"it's within the Dictionary.", 'number':28}
    
    return render(request, 'my_app1/about.html', my_text)

def base(request):
    return render(request, 'my_app1/base.html')

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'my_app1/registration.html', {
        'user_form':user_form,
        'profile_form':profile_form,
        'registered':registered,
    })

@login_required
def special():
    return HttpResponse("You are logged in!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(special))

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:

              login(request, user)
              return HttpResponseRedirect(reverse('index.html'))

            else:
                return HttpResponse("ACCOUNT NOT FOUND!")
        else:
            print('Someone tried to login and failed!')
            print('Username: {} and password: {}'.format(username,password))
            return HttpResponse('Invalid login details supplied!')

    else:
        return render(request, 'my_app1/login.html', {})



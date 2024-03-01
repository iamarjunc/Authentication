from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Check form validity
            print("Form is valid")
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # Print username and password
            print(f"New user created - Username: {username}, Password: {password}")
            return redirect('/login/')
        else:
            # Print form errors if any
            print("Form errors:", form.errors)
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})




def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def home(request):
    # Assuming you have authentication enabled and the user is logged in
    # You can access the logged-in user's name like this
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None
    
    context = {
        'username': username
    }
    return render(request, 'home.html', context)
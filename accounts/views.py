from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, get_user_model


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Use AuthenticationForm for login
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a desired page after login
                return redirect('homepage')  # Example redirect
            else:
                # Handle invalid authentication
                return render(request, 'accounts/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    user = request.user  # Get the currently logged-in user
    # Implement your logging logic here, e.g., using a logger or database
    # Example using the built-in logger:
    import logging
    logger = logging.getLogger(__name__)
    logger.info(f"User with ID {user.id} logged out.")

    logout(request)  # Log the user out
    return redirect('login')  # Assuming your login view has a name 'login' in urls.py
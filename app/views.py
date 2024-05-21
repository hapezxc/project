
def home(request):
    return render(request, 'home.html')
def about_view(request):

    message = [""]  # Example list of messages


    context = {

    }
    return render(request, 'about.html', context)
def room_view(request):
    # Your logic to fetch data or perform operations for the room page

    context = {

    }




    return render(request, 'room.html', context)


from django.http import HttpResponseRedirect
from .forms import ContactForm

def contact(request):
    message = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message = ['Your message has been sent successfully.']
            return HttpResponseRedirect(request.path_info)
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'message': message})


def update_user_view(request):

    return render(request, 'update_user.html', context)

def booking_view(request):

    return render(request, 'booking.html', context)












from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration.html', {'form': form})


from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if username == 'admin':
                    return redirect('admin_dashboard')  # Change to your admin dashboard URL name
                else:
                    return redirect('home')  # Change to your home page URL name
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def admin_dashboard_view(request):
    return render(request, 'admin_dashboard.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')














def dashboard(request):
    # Your dashboard logic here
    return render(request, 'home.html')



def basic_view(request):

    context = {

    }

    return render(request, 'basic.html', context)




from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def checkout_view(request):
    user = request.user
    context = {}  # Initialize context for both GET and POST requests

    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        method = request.POST.get('method')
        address = request.POST.get('city')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        room_quantity = int(request.POST.get('room_quantity', 1))
        message = []

        try:
            # Validate check-in and check-out dates
            check_in_date = datetime.strptime(check_in, '%Y-%m-%d')
            check_out_date = datetime.strptime(check_out, '%Y-%m-%d')
            if check_in_date >= check_out_date:
                message.append('Check-out date should be after the check-in date.')

            # Calculate total price
            room_price_per_night = 1700  # Set your room price per night
            total_days = (check_out_date - check_in_date).days
            total_price = total_days * room_price_per_night * room_quantity

            # Check if the room is fully booked
            if is_room_fully_booked(check_in_date, check_out_date, room_quantity):
                message.append('Sorry, the room is fully booked. Please choose another room or date.')

            # If the room is not fully booked and dates are valid, proceed with the order
            if not message:
                # Create booking object
                Booking.objects.create(
                    user=user,
                    name=name,
                    number=number,
                    email=email,
                    method=method,
                    address=address,
                    total_price=total_price,
                    room_type='Basic Room',
                    check_in=check_in,
                    check_out=check_out,
                    room_quantity=room_quantity
                )
                message.append('Booked Successfully!')
        except Exception as e:
            message.append(str(e))

        context['message'] = message

    return render(request, 'checkout_basic.html', context)

def is_room_fully_booked(check_in, check_out, room_quantity):
    room_type = 'Basic Room'
    room_capacity = 16

    # Check if there are overlapping bookings for the given room and dates
    booked_rooms = Booking.objects.filter(
        room_type=room_type,
        check_in__lte=check_out,
        check_out__gte=check_in
    ).count()

    # Check if the total booked rooms plus the current room quantity exceed the room capacity
    return booked_rooms + room_quantity > room_capacity




from django.contrib.auth import authenticate, login


from django.contrib.auth.decorators import login_required

@login_required
def update_profile(request):
    context = {
    }

    return render(request, 'update_user.html', context)





from django.contrib.auth.decorators import login_required
from .models import Booking

@login_required
def booking_view(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)
    context = {
        'user': user,
        'bookings': bookings
    }
    return render(request, 'bookings.html', context)



from django.shortcuts import render, redirect
from django.contrib.auth import logout




def dashboard_view(request):
    admin = request.user

    if request.method == "POST":
        if 'logout' in request.POST:
            logout(request)
            return redirect('login')

    context = {
        'admin': admin,
        'messages': ["Welcome to the dashboard!"],
    }
    return render(request, 'admin_dashboard.html', context)

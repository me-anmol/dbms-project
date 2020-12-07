
from django.shortcuts import render, redirect
from .models import destination,userinfo,hotel,travel,registerations
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# use the index html
def index(request):
    dest = destination.objects.all()
    return render(request, 'index.html', {'dest': dest})

# just call it when u don't know where to go
def home(request):
    return redirect("/")

# Login fuction from everywhere if needed
def loginP(request):
    email = request.POST.get('email',False)
    pwd = request.POST.get('password',False)
    print(email, pwd)
    if not pwd:
        return render(request,'login.html',{ 'flag': False ,'msg':'Invalid login' })
    user = authenticate(request,username = email ,password = pwd)
    if user is not None:
        login(request,user)
        print(request.POST.get('next'))
        if request.POST.get('next',False):

            return redirect(request.POST.get('next'))
    else:
        return render(request,'login.html',{ 'flag': True ,'msg':'Invalid login' })

    return redirect('/')

#This is just to create a url to load the request to register
def register(request):
    return render(request,'register.html')

# This is to create a new user and save their data that is needed
def sign(request):
    email = request.POST.get('email',False)
    password = request.POST.get('password',False)
    repass = request.POST.get('repassword',False)
    fname = request.POST.get('fname',False)
    lname = request.POST.get('lname',False)
    address = request.POST.get('address',False)
    phone = request.POST.get('phone',False)
    city = request.POST.get('city',False)
    country = request.POST.get('country',False)
    dob = request.POST.get('dob',False)
    if repass != password:
        return render(request,'register.html',{'flag':True ,'msg':'Password Incorrect'})
    if User.objects.filter(username = email).exists():
        return render(request,'register.html',{'flag':True ,'msg':'Email Already registerd'})
    user = User.objects.create_user(username =email ,password =password, email =email, first_name = fname ,last_name = lname)

    if user is not None and address and phone and dob and city and country:
        user.save()
        info = userinfo()
        info.user = user
        info.address = address
        info.phone = phone
        info.dob = dob
        info.city = city
        info.country = country
        info.save()
        login(request,user)
        return redirect('/')
    return render(request,'register.html',{'flag':True ,'msg':'Internal Error occured'})

#This is the destination page
def desti(request,oid):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % ('/login', request.path))

    data = destination.objects.filter(id = oid).first()
    hotel_list = list(hotel.objects.values('id','name','per_day_cost').filter(address = data.name))
    travel_list = list(travel.objects.values('id','name','rtc').filter(loc = data.name))
    send = { 'data': data, 'hotel_list': hotel_list, 'travel_list':travel_list}
    print(hotel_list)
    return render(request,'destination.html',send)

# This is to just logout from the current user
def logoutp(request):
    logout(request)
    return redirect('/')

#This is a post request fuction to just create a Booking
def book(request,oid):
    hotel_id = request.POST.get('hotel_id',False)
    travel_id = request.POST.get('travel_id',False)
    enddate = request.POST.get('enddate',False)
    startdate  = request.POST.get('startdate',False)
    #Create booking
    if (hotel_id and travel and enddate and startdate):
        booking = registerations()
        booking.user = request.user
        booking.hotel = hotel.objects.filter(id = hotel_id).first()
        booking.travel = travel.objects.filter(id = travel_id).first()
        booking.destination = destination.objects.filter(id =oid).first()
        booking.end_date = enddate
        booking.start_date = startdate
        booking.save()

        #Updating the hotel
        data = hotel.objects.filter(id = hotel_id).first()
        data.update_res()
        data.save()
        data = travel.objects.filter(id = hotel_id).first()
        data.update_res()
        data.save()
        messages.success(request,"Booking Successfully done !!!!!")
        print(request.path)
    else:
        messages.error(request,"Fill the Fields correctly")
    return redirect('/desti/'+oid)


#change phone number in user Information
def changePhone(request):
    uinfo = userinfo.objects.filter(user = request.user).first()
    phone = request.POST.get('phone',False)
    uinfo.phone = phone
    uinfo.save()
    messages.success(request ,"Phone number Changed")
    return redirect('/account/')

#Change Address in the user Information
def changeAddress(request):
    uinfo = userinfo.objects.filter(user = request.user).first()
    Address = request.POST.get('address',False)
    city = request.POST.get('city',False)
    country = request.POST.get('country',False)
    if Address and city and country:
        uinfo.address = Address
        uinfo.city = city
        uinfo.country = country
        uinfo.save()
        messages.success(request, "Address is updated")
    else:
        messages.error(request, "Invalid Entry")
    return redirect('/account/')

#This is to load the user info template
def account(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % ('/login', request.path))

    user = request.user
    info = userinfo.objects.filter(user = user).first()
    reser = list(registerations.objects.filter(user = user).values())
    data = {'info':info,'reser':reser }
    return render(request,'profile.html',data)

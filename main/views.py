
from django.shortcuts import render, redirect
from .models import destination,userinfo,hotel,travel,registeration
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout

def index(request):
    dest = destination.objects.all()
    return render(request, 'index.html', {'dest': dest})


def home(request):
    return redirect("/")

def loginP(request):
    email = request.POST.get('email',False)
    pwd = request.POST.get('password',False)
    print(email, pwd)
    if not pwd:
        return render(request,'login.html',{ 'flag': False ,'msg':'Invalid login' })
    user = authenticate(request,username = email ,password = pwd)
    if user is not None:
        login(request,user)
        return redirect('/')
    else:
        return render(request,'login.html',{ 'flag': True ,'msg':'Invalid login' })
        
    return redirect('/')

def register(request):
    return render(request,'register.html')

def sign(request):
    email = request.POST.get('email',False)
    password = request.POST.get('password',False)
    repass = request.POST.get('repassword',False)
    fname = request.POST.get('fname',False)
    lname = request.POST.get('lname',False)
    address = request.POST.get('address',False)
    phone = request.POST.get('phone',False)
    dob = request.POST.get('dob',False)
    if repass != password:
        return render(request,'register.html',{'flag':True ,'msg':'Password Incorrect'})
    if User.objects.filter(username = email).exists():
        return render(request,'register.html',{'flag':True ,'msg':'Email Already registerd'})
    user = User.objects.create_user(username =email ,password =password, email =email, first_name = fname ,last_name = lname)
    if user is not None:
        user.save()
        info = userinfo()
        info.user = user
        info.address = address
        info.phone = phone
        info.dob = dob
        info.save()
        login(request,user)
        return redirect('/')
    return render(request,'register.html',{'flag':True ,'msg':'Internal Error occured'})

@login_required(login_url ='login')
def desti(request,oid):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % ('/login', request.path))
    
    data = destination.objects.filter(id = oid).first()
    hotel_list = list(hotel.objects.values('id','name','per_day_cost').filter(address = data.name))
    travel_list = list(travel.objects.values('id','name','rtc').filter(loc = data.name))
    send = { 'data': data, 'hotel_list': hotel_list, 'travel_list':travel_list}
    print(hotel_list)
    return render(request,'destination.html',send)


def logoutp(request):
    logout(request)
    return redirect('/')

def book(request):
    #Create a booking 
    hotel_id = request.POST['hotel']
    travel_id = request.POST['travel']
    enddate = request.POST['enddate']
    startdate  = request.POST['startdate']
    booking = registeration()
    #booking.hotel = hotel
    #booking.travel = travel
    #booking.end_date = enddate
    #booking.start_date = startdate
        
    #Updating the hotel
    data = hotel.objects.filter(id = hotel_id).first()
    data.update_res()
    data.save()

    print(data)
    
    return redirect('/')
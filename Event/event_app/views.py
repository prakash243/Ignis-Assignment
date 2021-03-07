from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.
def home(request):
    all_event = Event.objects.all().order_by('-event_id')
    total = all_event.count()

    context = {'all_event': all_event, 'total':total, }
    return render(request, 'home.html', context)


def create_event(request):
    if request.method== "POST":
        event_name = request.POST['event_name']
        image = request.FILES['image']
        description = request.POST['data']
        venue = request.POST['location']
        date_time = request.POST['date_time']
        

        event = Event(event_name=event_name, image=image, data=description,
                    location=venue, date_time=date_time)
        
        event.save()
        return redirect('/')
    return render(request, 'create_event.html')

def like(request):
    
    if request.method == 'POST':
        user = request.user
        print("user : " , user)
        liked_id = request.POST['liked_id']
        
        liked_user = Like.objects.filter(user=user)
        for like in liked_user:
            if liked_id == like.liked_id:
                message = "Already in playlist "
                break
        else:
            liked = Like(user=user, liked_id=liked_id)
            liked.save()
            message = "Added Successfully"
    
        return redirect('/like')
    
    liked_user = Like.objects.filter(user=request.user)
    # print(watchlater_user)
    liked_id_list = []
    for i in liked_user:
        liked_id_list.append(i.liked_id)
    if not liked_id_list:
        empty_message = "Nothing to show , Please Add Event to favourite list By hitting the Heart button"
        return render(request, 'like.html', {'empty_message':empty_message})
    print(liked_id_list)

    liked_event = Event.objects.filter(event_id__in=liked_id_list)
    print(liked_event)
    context = {'liked_event': liked_event ,}
    return render(request, 'like.html',context)



def unlike(request):
    unliked_id = request.GET['unliked_id']
    print("unliked_id : ", unliked_id)
    user = request.user
    if request.method == "POST":
        liked_user = Like.objects.filter(user=user)
        print("unlike : ", liked_user)
        for i in liked_user:
            print("unlike : ", i.liked_id)
            
    return render(request, 'like.html', {})

def login(request):
    if request.method == "POST":
        
        username = request.POST['username']
        
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)
        from django.contrib.auth import login
        login(request, user)

        return redirect(home)

    return render(request, 'signin.html')

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        user = authenticate(username=username, password=password1)
        from django.contrib.auth import login
        login(request, user)
        

        return redirect(home)
    return render(request, 'signup.html')


def user_logout(request):
    logout(request)
    return redirect('/')
     

def search(request):
    search_event = request.GET['search']
    print(search_event)
    searched_event = Event.objects.all().filter(event_name__icontains=search_event)
    
    return render(request, 'search.html', {'searched_event':searched_event, 'search_event':search_event,})

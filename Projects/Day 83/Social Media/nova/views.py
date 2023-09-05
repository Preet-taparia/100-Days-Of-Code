from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm
from .models import Profile, Posts

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.success(request, ("Your post has been posted"))
                return redirect("home")
        
        posts = Posts.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"posts" : posts ,"form":form}) 
    else:
        posts = Posts.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"posts" : posts})


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles":profiles})
    else:
        messages.success(request, ("You must be Logged In to view this page"))
        return redirect('home')
    

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id = pk)
        posts = Posts.objects.filter(user_id = pk).order_by("-created_at")

        if request.method == 'POST':
            current_user_profile = request.user.profile
            action = request.POST['follow']
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            else:
                current_user_profile.follows.add(profile)
            current_user_profile.save()

        return render(request, "profile.html", {"profile":profile, "posts" : posts})
    
    else:
        messages.success(request, ("You must be Logged In to view this page"))
        return redirect('home')
    


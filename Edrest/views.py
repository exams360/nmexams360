from django.shortcuts import render,redirect, get_object_or_404
from Edrest.forms import CustomLoginForm
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from Edrest.models import Course, Video
from django.db.models import Q
from django.contrib.auth.views import LoginView ,PasswordResetView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
# Create your views here.
def Home(request):
    course1 = Course.objects.all()
    
    return render(request,'index.html',{'course':course1})
def AboutUs(request):
    return render(request, 'aboutus.html')
def Vedios(request, id):
    course_id = id
    course = get_object_or_404(Course, id=course_id)
    videos = course.videos.all()
    print(videos)
    
    return render(request, 'vedios.html',{'a':videos})


class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'registration/login.html'
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            print(request.POST)
            user = form.save()
            login(request, user)
            return redirect(Vedios)
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
def Modal(request):
    return render(request,'modals.html')
class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'password_reset_email.html'
def search(request):
    query = request.GET.get('q')
    courses = Course.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request, 'search.html', {'courses': courses, 'query': query})
class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'
@login_required(login_url='/login/')
def StudentView(request):
    return render(request,'studentdashboard.html')
def MocktestView(request):
    return render(request,'studentmocktests.html')
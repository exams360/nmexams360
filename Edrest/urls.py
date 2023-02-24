from django.urls import path
from Edrest import views
from .views import CustomLoginView,signup,Modal,search, CourseDetailView

urlpatterns = [path('courses/', views.Home),
               path('videos/<int:id>', views.Vedios),
               path('login/', CustomLoginView.as_view(), name='login'),
                path('signup/', signup, name='signup'),
                path('modal/', Modal),
                path('search/', search, name='search'),
                path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
                path('',views.AboutUs),
                path('StudentDashboard',views.StudentView),
                path('studentmocktest', views.MocktestView),




]
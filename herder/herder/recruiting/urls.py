from django.urls import path
from .views import RecruitingView, CreateApplicationView


app_name = "recruiting"
urlpatterns = [
    # Recruitingview
    path("", RecruitingView.as_view(), name="home"),
    # CreateApplicationView
    path("create_application/", CreateApplicationView.as_view(), name="create_application"),

    
]

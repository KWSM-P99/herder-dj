from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Application
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import ApplicationForm

# Create your views here.

# create a view for the recruiting page that lists all the recruiting criteria and process
class RecruitingView(TemplateView):
    """
    View for the recruiting page that lists all the recruiting criteria and processes.
    """

    template_name = "recruiting/recruiting.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    

# view to create a new application
class CreateApplicationView(CreateView):
    """
    View to create a new application.
    """

    model = Application
    form_class = ApplicationForm
    template_name = "recruiting/create_application.html"
    success_url = "/recruiting/"



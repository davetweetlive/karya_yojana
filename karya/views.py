from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from django.urls import reverse_lazy
from django.views import generic
from . forms import RegistrationForm



class IndexView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        # return render(request, 'karya/index.html', {})
        return render(request, 'base.html', {})

    def post(self, request, *kwargs):
        pass

class CreateAccountView(generic.CreateView):
    form_class  = RegistrationForm
    success_url = reverse_lazy('logout_url')
    template_name = 'karya/register.html'


class DisplayProfileView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'karya/profile.html', {})


    def post():
        pass

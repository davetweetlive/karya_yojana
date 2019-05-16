from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

class IndexView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        # return render(request, 'karya/index.html', {})
        return render(request, 'base.html', {})

    def post(self, request, *kwargs):
        pass

class CreateAccountView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'karya/register.html', {})

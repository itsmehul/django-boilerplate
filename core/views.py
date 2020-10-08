from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import TemplateView

def Home(request):
  return render(request, 'home.html')

class Signup(TemplateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    initial={}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        return render(request, self.template_name, {'form': form})
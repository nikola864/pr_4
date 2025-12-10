from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login

def home(request):
    return render(request, 'accounts/home.html')

@login_required
def protected_view(request):
    return render(request, 'accounts/protected.html')

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/registr.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # Автоматический вход после регистрации
        return response
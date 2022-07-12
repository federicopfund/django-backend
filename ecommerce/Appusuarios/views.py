# Create your views here.
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *
from Appcarro.views import limpiar_carro

def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()          
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

#def logout(request):
#    try:
#        limpiar_carro()
#    except KeyError:
#        pass
#    return HttpResponseRedirect(reverse('Productos'))

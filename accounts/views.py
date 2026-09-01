from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 

def registro(request):
    if request.method == 'POST':
        #Guardar user
        pass
    else:
        form = UserCreationForm()
        return render(request, 'registro.html', {'form': form})
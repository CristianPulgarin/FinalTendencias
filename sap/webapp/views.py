from django.http import HttpResponse
from django.shortcuts import render, redirect
from usuarios.models import Usuario



def inicio(request):
    return render(request,'index.html')

def bienvenidohtml(request):
    no_usuarios = Usuario.objects.count()
    usuarios = Usuario.objects.all()
    DicMensajes= {'msg1': 'Valor mensaje 1'}
    return render(request, 'gimnasio.html', {'no_usuarios':no_usuarios, 'usuarios':usuarios})



from .forms import UsuarioForm

def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario_list.html', {'usuarios': usuarios})

def usuario_register(request):
    """if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(usuario_list)
        else:
            form = UsuarioForm()
        return render(request,'usuario_register.html', {'form': form})
        """
    usuarios = Usuario.objects.all()
    if request.method == 'POST':
        form =UsuarioForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form= UsuarioForm()
    return render(request, 'usuario_register.html',{'form':form})

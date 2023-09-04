from django.shortcuts import render
from app_cad_usuarios.models import Usuario


# Create your views here.
def home(request):
    return render(request, 'usuarios/home.html')


def submit_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        
       
        novo_usuario = Usuario(
        nome = nome,
        idade = idade,
        email = email,
        telefone = telefone,)
        
        novo_usuario.save()

    return render(request, 'usuarios/home.html')

    

def lista_de_usuarios(request):
    usuario = Usuario.objects.all()
    dados = {'usuarios': usuario}
    return render(request, 'usuarios/usuarios.html', dados)

    
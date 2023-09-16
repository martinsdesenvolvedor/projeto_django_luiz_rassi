from django.shortcuts import render, redirect
from app_cad_usuarios.models import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app_cad_usuarios.forms import FormularioCadastroUsuario


# Create your views here.
def login_user(request):
    return render(request, 'usuarios/login.html')

def login_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username,
                               password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou Senha Inválidos!')
        
    return redirect('/login/')    

def logout_user(request):
    return redirect('/login/')

def home(request):
    return render(request, 'usuarios/home.html')

@login_required(login_url='/login/')
def submit_usuario(request):
    if request.method == 'POST':
       form = FormularioCadastroUsuario(request.POST)
       if form.is_valid():
           novo_usuario = Usuario(
               nome = form.cleaned_data['nome'],
               idade = form.cleaned_data['idade'],
               email = form.cleaned_data['email'],
               telefone = form.cleaned_data['telefone']
           )
           novo_usuario.save()
           return redirect('/sucesso/')

    else:
        form = FormularioCadastroUsuario()
    return render(request, 'usuarios/home.html')

@login_required(login_url='/login/')
def pagina_de_sucesso(request):
    return render(request, 'usuarios/sucesso.html')
    
@login_required(login_url='/login/')
def lista_de_usuarios(request):
    usuario = Usuario.objects.all()
    dados = {'usuarios': usuario}
    return render(request, 'usuarios/usuarios.html', dados)

    
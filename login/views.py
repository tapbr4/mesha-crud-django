from django.shortcuts import render, redirect
from login.models import Usuarios
from login.forms import UsuariosForm
from django.core.paginator import Paginator


user = {}
superuser = 0
invaliduser = {'check':0}

# Create your views here.
def login(request):
    global invaliduser
    global user
    userdata = {}
    userdata['db'] = Usuarios.objects.all()
    for usuario in userdata['db']:
        user[usuario.login] = usuario.senha

    return render(request, 'login.html', invaliduser)

def authentication(request):
    global invaliduser
    global user
    form = request.POST
    if(form['login'] in user and form['password'] == user[form['login']]):
        invaliduser['check'] = 0
        if(form['login'] == 'admin'):
            request.session['admin'] = 1
        else:
            request.session['admin'] = 0
        return redirect('home')
    else:
        request.session['admin'] = 0
        invaliduser['check'] = 1
        return redirect('login')

def register(request):
    dados = {}
    dados['form'] = UsuariosForm()
    return render(request, 'userform.html', dados)

def create_new_user(request):
    form = UsuariosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def userlist(request):
    dados = {} 
    # Paginação
    all = Usuarios.objects.all()
    paginator = Paginator(all, 5)
    pages = request.GET.get('page')
    dados['db'] = paginator.get_page(pages)
    
    return render(request, 'userlist.html', dados)

def delete_user(request, pk):
    db = Usuarios.objects.get(pk=pk)
    db.delete()
    return redirect('userlist')
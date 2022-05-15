from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from recursos.forms import RecursosForm
from recursos.models import Recursos

# Create your views here.
def home(request):
    dados = {} 
    # Paginação
    all = Recursos.objects.all()
    paginator = Paginator(all, 5)
    pages = request.GET.get('page')
    dados['db'] = paginator.get_page(pages)
    # Busca
    search = request.GET.get('search')
    if search:
       dados['db'] = Recursos.objects.filter(nome__icontains=search) 
    else:
       dados['db'] = paginator.get_page(pages)
    
    return render(request, 'index.html', dados)


def form(request):
    dados = {}
    dados['form'] = RecursosForm()
    
    return render(request, 'form.html', dados)


def create(request):
    form = RecursosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    dados = {}
    dados['db'] = Recursos.objects.get(pk=pk)
    
    return render(request, 'view.html', dados)


def edit(request, pk):
    dados = {}
    dados['db'] = Recursos.objects.get(pk=pk)
    dados['form'] = RecursosForm(instance=dados['db'])
    
    return render(request, 'form.html', dados)


def update(request, pk):
    data = {}
    data['db'] = Recursos.objects.get(pk=pk)
    form = RecursosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Recursos.objects.get(pk=pk)
    db.delete()
    
    return redirect('home')
from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm

# Create your views here.
def index(request):  
    pessoas = Pessoa.objects.all()  
    return render(request,"index.html",{"pessoas": pessoas})  

def criar(request):  
    if request.method == "POST":  
        form = PessoaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('index')  
            except:  
                pass  
    else:  
        form = PessoaForm()  
    return render(request,'criar.html',{'form':form})  

def editar(request, id):  
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(initial={'id': pessoa.id, 'nome': pessoa.nome})
    if request.method == "POST":  
        form = PessoaForm(request.POST, instance=pessoa)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('index')  
            except Exception as e: 
                pass    
    return render(request,'editar.html',{'form':form})  

def deletar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    try:
        pessoa.delete()
    except:
        pass
    return redirect('index')
from django.shortcuts import render
from .models import Symbol
from .forms import SymbolForm

def add_symbol(request):
    symbols = Symbol.objects.all()
    form = SymbolForm(request.POST)
    if form.is_valid():
        new_symbol = form.save(commit=False)
        new_symbol.save()
    return render(request, 'home.html', { 'symbols':symbols,'form':form})




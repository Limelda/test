from .models import Pokemon
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PokemonForm
from django.utils import timezone

def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'plist/pokemon_list.html', {'pokemons' : pokemons})

def pokemon_detail(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    return render(request, 'plist/pokemon_detail.html', {'pokemon': pokemon})

def pokemon_new(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            pokemon = form.save(commit=False)
            pokemon.created_date = timezone.now()
            pokemon.save()
            return redirect('plist.views.pokemon_detail', pk=pokemon.pk)
    else:
        form = PokemonForm()
    return render(request, 'plist/pokemon_edit.html', {'form': form})

def pokemon_edit(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == "POST":
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            pokemon = form.save(commit=False)
            pokemon.created_date = timezone.now()
            pokemon.save()
            return redirect('plist.views.pokemon_detail', pk=pokemon.pk)
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'plist/pokemon_edit.html', {'form': form})

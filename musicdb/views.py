from django.shortcuts import render, redirect, get_object_or_404
from musicdb.forms import *
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def view_composers(request):
    composers_list = Compozitori.objects.order_by('stil')
    name_dict = {'composers': composers_list}
    return render(request, 'composer/composers.html', context=name_dict)


def add_composer(request):
    if request.method == 'POST':
        composer_form = ComposerForm(request.POST)
        if composer_form.is_valid():
            composer_form.save()
            messages.success(request, 'Composer added')
        else:
            messages.error(request, 'Error saving form')

        return redirect('/composers')

    composer_form = ComposerForm()
    composers = Compozitori.objects.all()
    return render(request, 'composer/addcomposer.html',
                  context={'composer_form': composer_form,
                           'composers': composers})


def update_composer(request, id):
    composer = get_object_or_404(Compozitori, id=id)
    if request.method == 'POST':
        update_form = ComposerForm(request.POST, instance=composer)
        if update_form.is_valid():
            update_form.save()
            return redirect('/composers')
    else:
        update_form = ComposerForm(instance=composer)

    update_form = ComposerForm()
    return render(request, 'composer/updatecomposer.html',
                  {
                      'form': update_form,
                      'composer': composer,
                  })


def delete_composer(request, id):
    composer = get_object_or_404(Compozitori, id=id)
    if request.method == 'POST':
        delete_form = ComposerDeleteForm(request.POST, instance=composer)
        if delete_form.is_valid():
            composer.delete()
            return redirect('/composers')
    else:
        delete_form = ComposerDeleteForm(instance=composer)

    delete_form = ComposerDeleteForm()
    return render(request, 'composer/composers.html',
                  {
                      'form': delete_form,
                      'composer': composer,
                  })


def view_compositions(request):
    compositions_list = Compozitii.objects.order_by('an_aparitie')
    name_dict = {'composition': compositions_list}
    return render(request, 'compositions/compositions.html',
                  context=name_dict)


def add_composition(request):
    if request.method == 'POST':
        composition_form = CompositionForm(request.POST)
        if composition_form.is_valid():
            composition_form.save()
            messages.success(request, 'Composition added')
        else:
            messages.error(request, 'Error saving form')

        return redirect("/compositions")
    composition_form = CompositionForm()
    return render(request, 'compositions/addcompositions.html',
                  context={'composition_form': composition_form})


def update_composition(request, id):
    composition = get_object_or_404(Compozitii, id=id)
    if request.method == 'POST':
        update_form = CompositionForm(request.POST, instance=composition)
        if update_form.is_valid():
            update_form.save()
            return redirect('/compostions')
    else:
        update_form = CompositionForm(instance=composition)

    update_form = CompositionForm()
    return render(request, 'compositions/updatecompositions.html',
                  {
                      'form': update_form,
                      'composition': composition,
                  })


def delete_composition(request, id):
    composition = get_object_or_404(Compozitii, id=id)
    if request.method == 'POST':
        delete_form = CompositionDeleteForm(request.POST, instance=composition)
        if delete_form.is_valid():
            composition.delete()
            return redirect('/compositions')
    else:
        delete_form = CompositionDeleteForm(instance=composition)

    delete_form = CompositionDeleteForm()
    return render(request, 'compositions/compositions.html',
                  {
                      'form': delete_form,
                      'composition': composition,
                  })


def view_catalogues(request):
    catalogues_list = Cataloage.objects.order_by('compozitor')
    name_dict = {'catalogues': catalogues_list}
    return render(request, 'catalogues/catalogues.html', context=name_dict)


def add_catalogue(request):
    if request.method == 'POST':
        catalogue_form = CatalogueForm(request.POST)
        if catalogue_form.is_valid():
            catalogue_form.save()
            messages.success(request, 'Catalogue added')
        else:
            messages.error(request, 'Error saving form')
        return redirect('/catalogues')
    catalogue_form = CatalogueForm()
    return render(request, 'catalogues/addcatalogues.html',
                  context={'catalogue_form': catalogue_form})


def update_catalogue(request,id):
    catalogue = get_object_or_404(Cataloage, id=id)
    if request.method == 'POST':
        update_form = CatalogueForm(request.POST, instance=catalogue)
        if update_form.is_valid():
            update_form.save()
            return redirect('/catalogues')
    else:
        update_form = CatalogueForm(instance=catalogue)

    update_form = CatalogueForm()
    return render(request, 'catalogues/updatecatalogues.html',
                  {
                      'form': update_form,
                      'catalogue': catalogue,
                  })


def delete_catalogue(request, id):
    catalogue = get_object_or_404(Cataloage, id=id)
    if request.method == 'POST':
        delete_form = CatalogueDeleteForm(request.POST, instance=catalogue)
        if delete_form.is_valid():
            catalogue.delete()
            return redirect('/catalogues')
    else:
        delete_form = CatalogueDeleteForm(instance=catalogue)

    delete_form = CatalogueDeleteForm()
    return render(request, 'catalogues/catalogues.html',
                  {
                      'form': delete_form,
                      'catalogue': catalogue,
                  })


def view_composer_compositions(request, id):
    composition_list = Compozitii.objects.filter(
        cataloage__compozitor=id).order_by('an_aparitie')
    composition_dict = {'composition': composition_list}
    return render(request, 'composer/composer_compositions.html',
                  context=composition_dict)


def view_composer_catalogues(request, id):
    catalogue_list = Cataloage.objects.filter(
        compozitie__cataloage__compozitor_id=id).order_by('simbol')
    catalogue_dict = {'catalogues': catalogue_list}
    return render(request, 'composer/composer_catalogues.html',
                  context=catalogue_dict)
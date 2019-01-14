from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import *
from .models import *
from .forms import *



@login_required
def vendorView(request):
    return render(request, 'inv/vendorInventory.html')

@login_required
def consumerView(request):
    return render(request, 'inv/consumerInventory.html')

def unauthenticatedView(request):
    return render(request, 'inv/unauthenticatedInventory.html')

def display_drinks(request):
    items = Drinks.objects.all()
    context = {
        'items': items,
        'header': 'Drinks',
    }
    if not request.user.is_authenticated: #user not logged in
        items = Drinks.objects.filter(status='AVAILABLE')
        context = {
            'items': items,
            'header': 'Drinks',
        }
        return render(request, 'inv/unauthenticatedInventory.html', context)

    elif request.user.profile.vendor: #user is vendor
        items = Drinks.objects.filter(donator__username=request.user.username)
        context = {
            'items': items,
            'header': 'Drinks',
        }
        if request.GET:
            form = DrinkForm()
        if request.POST:
            form = DrinkForm(request.POST)
            if form.is_valid():
                drinks = form.save(commit=False)
                drinks.donator = request.user.username
                drinks.save()
        return render(request, 'inv/vendorInventory.html', context)

    elif not request.user.profile.vendor: #user is consumer
        items = Drinks.objects.filter(status='AVAILABLE')
        context = {
            'items': items,
            'header': 'Drinks',
        }
        return render(request, 'inv/consumerInventory.html', context)


def display_foods(request):
    items = Foods.objects.all()
    context = {
        'items': items,
        'header': 'Foods',
    }
    if not request.user.is_authenticated:
        items = Foods.objects.filter(status='AVAILABLE')
        context = {
            'items': items,
            'header': 'Foods',
        }
        return render(request, 'inv/unauthenticatedInventory.html', context)

    elif request.user.profile.vendor: #
        items = Foods.objects.filter(donator__username=request.user.username)
        context = {
            'items': items,
            'header': 'Foods',
        }
        if request.GET:
            form = FoodForm()
        if request.POST:
            form = FoodForm(request.POST)
            if form.is_valid():
                foods = form.save(commit=False)
                foods.donator = request.user.username
                foods.save()
        return render(request, 'inv/vendorInventory.html', context)

    elif not request.user.profile.vendor:
        items = Foods.objects.filter(status='AVAILABLE')
        context = {
            'items': items,
            'header': 'Foods',
        }
        return render(request, 'inv/consumerInventory.html', context)

def display_miscObjects(request):
    items = MiscObjects.objects.all()
    context = {
        'items': items,
        'header': 'MiscObjects',
    }
    if not request.user.is_authenticated:
        items = MiscObjects.objects.filter(status='AVAILABLE')
        context = {
            'items': items,
            'header': 'MiscObjects',
        }
        return render(request, 'inv/unauthenticatedInventory.html', context)

    elif request.user.profile.vendor: #attempt with stackvoerflow comment
        items = MiscObjects.objects.filter(donator__username=request.user.username)
        context = {
            'items': items,
            'header': 'MiscObjects',
        }
        if request.GET:
            form = MiscObjectForm()
        if request.POST:
            form = MiscObjectForm(request.POST)
            if form.is_valid():
                miscObjects = form.save(commit=False)
                miscObjects.donator = request.user.username
                miscObjects.save()
        return render(request, 'inv/vendorInventory.html', context)

    elif not request.user.profile.vendor:
        items = MiscObjects.objects.filter(status='AVAILABLE')
        context = {
            'items': items,
            'header': 'MiscObjects',
        }
        return render(request, 'inv/consumerInventory.html', context)

################################################################################

@login_required
def add_item(request, cls):
    if not request.user.profile.vendor:
        return redirect('consumerIndex')
    else:
        if request.method == "POST":
            form = cls(request.POST)

            if form.is_valid():
                form.save()
                return redirect('vendorIndex')

        else:
            form = cls()
            return render(request, 'inv/add_new.html', {'form' : form})

@login_required
def add_drink(request):
    if not request.user.profile.vendor:
        return redirect('consumerIndex')
    else:
        return add_item(request, DrinkForm)

@login_required
def add_food(request):
    if not request.user.profile.vendor:
        return redirect('consumerIndex')
    else:
        return add_item(request, FoodForm)

@login_required
def add_miscObject(request):
    if not request.user.profile.vendor:
        return redirect('consumerIndex')
    else:
        return add_item(request, MiscObjectForm)

################################################################################

@login_required
def edit_item(request, pk, model, cls):
    if not request.user.profile.vendor:
        return redirect('consumerIndex')
    else:
        item = get_object_or_404(model, pk=pk)

        if request.method == "POST":
            form = cls(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('vendorIndex')
        else:
            form = cls(instance=item)

            return render(request, 'inv/edit_item.html', {'form': form})


@login_required
def edit_drink(request, pk):
    if not request.user.profile.vendor:
        return redirect('consumerIndex')
    else:
        return edit_item(request, pk, Drinks, DrinkForm)

@login_required
def edit_food(request, pk):
    if not request.user.profile.vendor:
        return redirect('consumerIndex')
    else:
        return edit_item(request, pk, Foods, FoodForm)

@login_required
def edit_miscObject(request, pk):
    if not request.user.profile.vendor:
        return redirect('consumerIndex')
    else:
        return edit_item(request, pk, MiscObjects, MiscObjectForm)


################################################################################

@login_required
def reserve_item(request, pk, model, cls):
    if request.user.profile.vendor:
        return redirect('vendorIndex')
    else:
        item = get_object_or_404(model, pk=pk)

        if request.method == "POST":
            form = cls(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('vendorIndex')
        else:
            form = cls(instance=item)

            return render(request, 'inv/reserve_item.html', {'form': form})


@login_required
def reserve_drink(request, pk):
    if request.user.profile.vendor:
        return redirect('vendorIndex')
    else:
        return reserve_item(request, pk, Drinks, ReserveDrinkForm)

@login_required
def reserve_food(request, pk):
    if request.user.profile.vendor:
        return redirect('vendorIndex')
    else:
        return reserve_item(request, pk, Foods, ReserveFoodForm)

@login_required
def reserve_miscObject(request, pk):
    if request.user.profile.vendor:
        return redirect('vendorIndex')
    else:
        return reserve_item(request, pk, MiscObjects, ReserveMiscObjectForm)

################################################################################

@login_required
def delete_drink(request, pk):
    if not request.user.profile.vendor:
        return redirect('consumerIndex')
    else:
        template = 'inv/vendorInventory.html'
        Drinks.objects.filter(id=pk).delete()

        items = Drinks.objects.all()

        context = {
            'items': items,
        }

        return render(request, template, context)

@login_required
def delete_food(request, pk):
    if not request.user.profile.vendor:
        return redirect('consumerIndex')
    else:
        template = 'inv/vendorInventory.html'
        Foods.objects.filter(id=pk).delete()

        items = Foods.objects.all()

        context = {
            'items': items,
        }

        return render(request, template, context)

@login_required
def delete_miscObject(request, pk):
    if not request.user.profile.vendor:
        return redirect('consumerIndex')
    else:
        template = 'inv/vendorInventory.html'
        MiscObjects.objects.filter(id=pk).delete()

        items = MiscObjects.objects.all()

        context = {
            'items': items,
        }

        return render(request, template, context)

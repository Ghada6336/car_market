from django.shortcuts import render , redirect
from .models import Car
from .forms import CarForm
from django.contrib import messages

def car_list(request):
    cars = Car.objects.all()
    context = {
    "cars": cars,
    }
    return render(request, 'car_list.html', context)


def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    context = {
    "car": car,
    }
    return render(request, 'car_detail.html', context)


def car_create(request):
    form = CarForm()
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #messages.success(request, ' created successfully!')
            #messages.add_message(request, messages.DEBUG, 'Total records updated {0}'.format(count))
            messages.success(request, 'Your password was updated successfully!')

            return redirect('car-list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)

def car_update(request, car_id):
    car = Car.objects.get(id=car_id)
    form = CarForm(instance = car)
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            #messages.success(request, ' updated successfully!')
            #messages.add_message(request, messages.DEBUG, 'Total records updated {0}'.format(count))
            messages.success(request, 'Your password was updated successfully!')
            return redirect('car-list')
    context = {
        "car":car,
        "form":form,
    }
    return render(request, 'update.html', context)


def car_delete(request, car_id):
    car= Car.objects.get(id=car_id)
    car.delete()
    messages.success(request, 'Your password was updated successfully!')
    return redirect('car-list')

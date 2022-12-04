from django.shortcuts import render, redirect
from .models import Vehicle

from .forms import VehicleForm


# Create your views here.

#homepage view
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    vehicles = Vehicle.objects.filter(regNo__icontains=q)
    context = {"vehicles":vehicles}

    return render(request, 'home.html', context)


#redirect to search page
def searchVehiclePage(request):
    return render(request, 'search_vehicle.html')


#save accident information
def reportVehicle(request):
    form = VehicleForm
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    context = {'form': form}
    return render(request, 'report_vehicle_form.html', context)



#search vehicle from database
def vehicle(request, pk):
    vehicles = Vehicle.objects.filter(id=pk)

    context = {'vehicle': vehicles}
    return render(request, 'fetch_vehicle.html', context)




def vehicleDetails(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    vehicles = Vehicle.objects.filter(regNo__icontains=q)
    if (vehicles == None):
        return False
    else:
        context = {"vehicles":vehicles}

    return render(request, 'fetch_vehicle.html', context)
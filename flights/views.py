from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Airport, Passenger
from . import forms

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all(),
    })


# flight/show page
def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    # alternative way to handle error is as follows, with a specified error code
    # flight = get_object_or_404(Flight, pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        # exclude if passenger is already on the flight
        "non_passengers": Passenger.objects.exclude(flights=flight).all(),
    })


# airport/show page
def airport(request, airport_id):
    airport = Airport.objects.get(pk=airport_id)
    return render(request, "flights/airport.html", {
        "airport": airport,
        "departures": airport.departures.all(),
        "arrivals": airport.arrivals.all(),
    })

# book a flight. POST request for Flight model
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        # request.POST["passenger"] is user input from the form
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights:flight", args=(flight.id,)))


# remove passenger from flight. DELETE request for Passenger model
def remove_passenger(request, flight_id, passenger_id):
    if request.method == 'POST' or request.POST.get('_method') == 'DELETE':
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flights.remove(flight)
        messages.success(request, f"Removed {passenger.first_name} from flight {flight_id}.")
        return HttpResponseRedirect(reverse("flights:flight", args=(flight.id,)))


def edit_flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)

    if request.method == 'POST':
        form = forms.FlightEditForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('flights:flight', args=(flight.id,)))
    else:
        form = forms.FlightEditForm(instance=flight)

    return render(request, 'flights/edit_flight.html', {'form': form, 'flight': flight})

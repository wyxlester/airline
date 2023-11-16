from django.urls import path

from . import views

app_name = "flights"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("airport/<int:airport_id>", views.airport, name="airport"),
    path("<int:flight_id>/book", views.book, name="book"),
    path("<int:flight_id>/remove_passenger/<int:passenger_id>", views.remove_passenger, name="remove_passenger"),
    path('<int:flight_id>/edit/', views.edit_flight, name='edit_flight'),
]

# handler404 = 'flights.views.error_404'
# handler500 = 'flights.views.error_500'
# handler403 = 'flights.views.error_403'
# handler400 = 'flights.views.error_400'

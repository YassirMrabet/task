from django.shortcuts import render
from typing import List, Union

from rentals.models import Reservation

def get_previous_reservation(rental_reservation: Union[Reservation, None], all_rental_reservations: List[Reservation]) -> Union[int, None]:
    reservation = None
    for rr in reversed(all_rental_reservations):
        if rr.checkin < rental_reservation.checkin:
            reservation = rr.id
            break
    return reservation


def rentals_with_previous(request):
    reservations: List[Reservation] = Reservation.objects.all()
    reservations_representation = [
        (reservation.rental.name, reservation.id, reservation.checkin, reservation.checkout, get_previous_reservation(reservation, list(filter(lambda r: r.rental_id == reservation.rental_id, reservations)))) for reservation in reservations
    ]
    return render(request, 'rentals/index.html', {"reservations": reservations_representation})
from django.test import TestCase
from datetime import datetime

from rentals.views import get_previous_reservation
from rentals.models import Reservation, Rental

class RentalsTests(TestCase):
    def test_no_rental_reservation_before_when_reservations_empty(self):
        self.assertIsNone(get_previous_reservation(None, []))

    def test_no_rental_reservation_before_when_one_reservation(self):
        rental = Rental(name="rental")
        reservation = Reservation(rental=rental, checkin=datetime(2022, 8, 10), checkout=datetime(2022, 8, 11))
        self.assertIsNone(get_previous_reservation(reservation, [reservation]))

    def test_no_rental_reservation_before_when_asking_first_reservation(self):
        rental = Rental(name="rental")
        reservation1 = Reservation(rental=rental, checkin=datetime(2022, 8, 10), checkout=datetime(2022, 8, 11))
        reservation2 = Reservation(rental=rental, checkin=datetime(2022, 8, 11), checkout=datetime(2022, 8, 12))
        self.assertIsNone(get_previous_reservation(reservation1, [reservation1, reservation2]))

    def test_rental_reservation_given_when_querying_second_rental(self):
        rental = Rental(name="rental")
        reservation1 = Reservation(rental=rental, checkin=datetime(2022, 8, 10), checkout=datetime(2022, 8, 11))
        reservation2 = Reservation(rental=rental, checkin=datetime(2022, 8, 11), checkout=datetime(2022, 8, 12))
        self.assertIsNone(get_previous_reservation(reservation2, [reservation1, reservation2]))

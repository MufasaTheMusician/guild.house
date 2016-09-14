# -*- coding: utf-8 -*-
import datetime
from datetime import time, timedelta
from django.conf import settings


BOOKINGS_PAGINATE_BY = getattr(settings, 'BOOKINGS_BOOKING_PAGINATE_BY', 100)

BOOKINGS_FEED = getattr(settings, 'BOOKINGS_BOOKING_FEED', 10)

# If a booking is greater or equal to this number it is treated as a larger sized booking.
BIG_BOOKING = getattr(settings, 'BOOKINGS_BIG_BOOKING', 7)

TIME_ZONE = settings.TIME_ZONE

DEFAULT_BOOKING_TIME = getattr(settings, 'BOOKINGS_DEFAULT_BOOKING_TIME', "18:00")

DEFAULT_CALENDAR_LENGTH = getattr(settings, 'BOOKINGS_DEFAULT_CALENDAR_LENGTH', 42)

FROM_EMAIL = getattr(settings, 'DEFAULT_FROM_EMAIL')

TO_EMAILS = getattr(settings, 'BOOKINGS_TO_EMAILS')

STATUS_CHOICE = [
    ('Booked', 'Booked'),
    ('Confirmed', 'Confirmed'),
    ('Numbers Confirmed', 'Numbers Confirmed'),
    ('Big Booking', 'Big Booking'),
    ('Cancelled', 'Cancelled'),
]

DEFAULT_BOOKING_METHOD = getattr(settings, 'BOOKINGS_DEFAULT_BOOKING_METHOD',
                                 'website')

AREA_CHOICE = (
    ('inside', 'Inside'),
    ('outside', 'Outside'),
)

METHOD_CHOICE = [
    ('phone', 'Phone'),
    ('email', 'Email'),
    ('website', 'Online'),
    ('facebook', 'Facebook Messenger'),
    ('person', 'In Person'),
    ('other', 'Other'),
]

SERVICE_CHOICE = (
    ('lunch', 'Lunch'),
    ('afternoon', 'Afternoon'),
    ('main', 'Main'),
)

SERVICE_TIMES = (
    (time(12,0), 'lunch'),
    (time(14,30), 'afternoon'),
    (time(17,30), 'main'),
)

BOOKING_TIMES = (time(12), time(23))
BOOKING_INTERVAL = timedelta(minutes=30)


def generate_times():
    temp_date, time_list = datetime.date(2000,1,1), []
    this_time = BOOKING_TIMES[0]
    while this_time<=BOOKING_TIMES[1]:
        time_list.append((
            this_time,
            "{}:{:0>2}".format(this_time.hour, this_time.minute)
        ))
        # hack around timedelta not allowing time addition (on purpose)
        # http://bugs.python.org/issue1487389
        # http://bugs.python.org/issue1118748
        temp_time = datetime.datetime.combine(temp_date, this_time)+BOOKING_INTERVAL
        this_time = time(temp_time.hour, temp_time.minute)
    return time_list


BOOKING_TIMES_CHOICES = generate_times()

DEFAULT_BOOKING_DURATION = getattr(settings, 'BOOKINGS_DEFAULT_BOOKING_DURATION',
                                   '04:00:00')

DURATION_SELECTION = [
    ('00:30:00', '30 minutes'),
    ('00:45:00', '45 minutes'),
    ('01:00:00', '1 hour'),
    ('01:30:00', '1 and a half hours'),
    ('02:00:00', '2 hours'),
    ('02:30:00', '2 and a half hours'),
    ('03:00:00', '3 hours'),
    ('04:00:00', '4 hours'),
    ('06:00:00', 'more than 4 hours')
]

HEAT = {
    60: 'warm',
    85: 'hot',
    105: 'full',
}

# Note: hardcoded in booking_form.html
HEAR_CHOICE = [
    ("event", "event"),
    ("facebook", "facebook"),
    ("friends", "friends"),
    ("newspaper", "newspaper"),
    ("search", "search"),
    ("other", "other")
]
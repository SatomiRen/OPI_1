#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def select_flights(flights, airplane_type):
    count = 0
    res = []
    for flight in flights:
        if flight.get('airplane_type') == airplane_type:
            count += 1
            res.append(flight)
    if count == 0:
        print("рейсы не найдены")

    return res

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Individual.IDZ_1.Modules import i1_sample

if __name__ == "__main__":
    sample_string = (
         "Добро пожаловать, %N% %S%!"
    )
    name, surname = input("Введите имя и фамилию: ").split()
    print(i1_sample.sample(sample_string, name, surname))

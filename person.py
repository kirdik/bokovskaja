from typing import List, Any


class Person:

    do_birth = '1920-01-01'
    do_death = '1941-01-01'
    mtr_unit = 'Неизвестно'
    ro_death = 'Неизвестно'
    rip_loc = 'Неизвестно'
    village = 'Неизвестно'
    name = 'Неизвестно'
    surname = 'Неизвестно'
    patronymic = 'Неизвестно'
    address = 'Неизвестно'
    godfather = 'Неизвестно'
    godmother = 'Неизвестно'
    father = 'Неизвестно'
    mother = 'Неизвстно'
    priest = 'Неизвестно'

    def fio(self, village, name, surname, patronymic, do_birth, address):
        self.village = village
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.do_birth = do_birth
        self.address = address
        fio_tuple = (self.village, self.name, self.surname, self.patronymic, self.do_birth, self.address)
        return fio_tuple

    def info(self):
        print(f'Боец: {self.name} {self.surname} {self.patronymic} дата рождения: {self.do_birth} \n'
              f'Адрес проживания:{self.address}')


class Soldier(Person):
    def data_soldier(self, mtr_unit, do_death, ro_death, rip_loc):
        self.mtr_unit = mtr_unit
        self.do_death = do_death
        self.ro_death = ro_death
        self.rio_loc = rip_loc


class Church(Person):
    def metrika(self, godfather, godmother, father, mother, priest):
        self.godfather = godfather
        self.godmother = godmother
        self.father = father
        self.mother = mother
        self.priest = priest


class Person:
    do_birth = '1920-01-01'
    do_death = '1941-01-01'
    mtr_unit = 'Неизвестно'
    ro_death = 'Неизвестно'
    village = 'Неизвестно'
    name = 'Неизвестно'
    surname = 'Неизвестно'
    patronymic = 'Неизвестно'
    address = 'Неизвестно'

    def fio(self, village, name, surname, patronymic, do_birth, address):
        self.village = village
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.do_birth = do_birth
        self.address = address

    def info(self):
        print(f'Боец: {self.name} {self.surname} {self.patronymic} дата рождения: {self.do_birth} \n'
              f'Адрес проживания:{self.address}')


class Soldier(Person):
    def data_soldier(self,  mtr_unit, do_death, ro_death):
        self.mtr_unit = mtr_unit
        self.do_death = do_death
        self.ro_death = ro_death



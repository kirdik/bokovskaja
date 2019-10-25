import sqlite3

con = sqlite3.connect('base.sqlite')
curs = con.cursor()


class Queries:
    # sql_c_person = 'CREATE TABLE person (village, name, surname, patronymic, do_birth, address)'
    # sql_c_soldier = ' CREATE TABLE soldier (mtr_unit, do_death, ro_death, rip_loc)'
    # sql_c_church = ' CREATE TABLE churching ( goodfather, goodmother, father, mother, priest ) '
    sql_add_v = 'INSERT INTO villages VALUES (NULL ,?)'
    sql_add_p = ' INSERT INTO person VALUES (?, ?, ?, ?, ?, ?, NULL)' # village(int), name, surname, patronymic, do_birth, address,
    sql_add_s = 'INSERT INTO soldier VALUES (?, ?, ?, ?, ?)'  # mtr_unit, do_death, ro_death, rip_loc, id (int)
    sql_add_c = 'INSERT INTO churching VALUES (?, ?, ?, ?, ?, ? )' # goodfather, goodmother, father, mother, priest, id (int)
    sql_upd_p = 'UPDATE person SET village = ?, name = ?, surname = ?, patronymic = ?, do_birth = ?, address = ?  WHERE id = ?'
    sql_upd_s = 'UPDATE soldier SET mtr_unit = ?, do_death = ?, ro_death = ?, rip_loc = ? WHERE id = ?'







# 1,'Иванов', 'Иван', 'Иванович', '3-5-1930', 'Пооспект Мира 29 34', 1

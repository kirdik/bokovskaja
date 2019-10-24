import sqlite3

con = sqlite3.connect('base.sqlite')
curs = con.cursor()
sql_c_person = 'CREATE TABLE person (village, name, surname, patronymic, do_birth, address)'
sql_c_soldier = ' CREATE TABLE soldier (mtr_unit, do_death, ro_death, rip_loc)'
sql_c_church = ' CREATE TABLE churching ( goodfather, goodmother, father, mother, priest ) '
sql_add_person = ' INSERT INTO person VALUES (?, ?, ?, ?, ?, ?), person '






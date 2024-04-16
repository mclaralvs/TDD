import pytest
from employee import Employee

def test_desenvolvedor_salary_above_3000():
    emp = Employee("Maria Clara", "maria@example.com", 3500, "DESENVOLVEDOR")
    assert emp.calculate_net_salary() == 2800

def test_desenvolvedor_salary_below_3000():
    emp = Employee("Maria Clara", "maria@example.com", 2500, "DESENVOLVEDOR")
    assert emp.calculate_net_salary() == 2250

def test_dba_salary_above_2000():
    emp = Employee("Maria Clara", "maria@example.com", 2500, "DBA")
    assert emp.calculate_net_salary() == 1875

def test_dba_salary_below_2000():
    emp = Employee("Maria Clara", "maria@example.com", 1500, "DBA")
    assert emp.calculate_net_salary() == 1275

def test_testador_salary_above_2000():
    emp = Employee("Maria Clara", "maria@example.com", 2500, "TESTADOR")
    assert emp.calculate_net_salary() == 1875

def test_testador_salary_below_2000():
    emp = Employee("Maria Clara", "maria@example.com", 1500, "TESTADOR")
    assert emp.calculate_net_salary() == 1275

def test_gerente_salary_above_5000():
    emp = Employee("Maria Clara", "maria@example.com", 6000, "GERENTE")
    assert emp.calculate_net_salary() == 4200

def test_gerente_salary_below_5000():
    emp = Employee("Maria Clara", "maria@example.com", 4000, "GERENTE")
    assert emp.calculate_net_salary() == 3200
import pytest
from employee import Employee

def test_invalid_position():
    with pytest.raises(TypeError) as excinfo:
        emp = Employee("Maria Clara", "maria@example.com", 3000, "CARGO_INVALIDO")
        emp.calculate_net_salary()
    assert str(excinfo.value) == "Cargo inválido"

def test_unspecified_position():
    with pytest.raises(TypeError) as excinfo:
        emp = Employee("Maria Clara", "maria@example.com", 3000, "")
        emp.calculate_net_salary()
    assert str(excinfo.value) == "Cargo inválido"

def test_desenvolvedor_boundary_salary():
    emp = Employee("Maria Clara", "maria@example.com", 3000, "DESENVOLVEDOR")
    assert emp.calculate_net_salary() == 2400

def test_dba_boundary_salary():
    emp = Employee("Maria Clara", "maria@example.com", 2000, "DBA")
    assert emp.calculate_net_salary() == 1500

def test_testador_boundary_salary():
    emp = Employee("Maria Clara", "maria@example.com", 2000, "TESTADOR")
    assert emp.calculate_net_salary() == 1500

def test_gerente_boundary_salary():
    emp = Employee("Maria Clara", "maria@example.com", 5000, "GERENTE")
    assert emp.calculate_net_salary() == 3500

def test_desenvolvedor_minimum_salary():
    emp = Employee("Maria Clara", "maria@example.com", 1000, "DESENVOLVEDOR")
    assert emp.calculate_net_salary() == 900

def test_dba_minimum_salary():
    emp = Employee("Maria Clara", "maria@example.com", 1000, "DBA")
    assert emp.calculate_net_salary() == 850

def test_testador_minimum_salary():
    emp = Employee("Maria Clara", "maria@example.com", 1000, "TESTADOR")
    assert emp.calculate_net_salary() == 850

def test_gerente_minimum_salary():
    emp = Employee("Maria Clara", "maria@example.com", 1000, "GERENTE")
    assert emp.calculate_net_salary() == 800
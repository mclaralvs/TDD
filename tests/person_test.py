import pytest
from person import Person, Email

# Data
@pytest.fixture
def valid_person():
    emails = [Email("mariaclara@gmail.com")]
    return Person("Maria Clara", 25, emails)

@pytest.fixture
def invalid_person():
    emails = [Email("mariclaraa@gmail")]
    return Person("Maria", 30, emails)

@pytest.fixture
def person_without_email():
    return Person("Maria Clara", 35, [])

# Tests
def test_valid_name(valid_person):
    assert valid_person.isValidToInclude() == []

def test_invalid_name(invalid_person):
    assert invalid_person.isValidToInclude() == ["Nome deve ter ao menos 2 partes", "Formato de email inválido"]

def test_age_range():
    person = Person("Maria Clara", 0, [Email("mariaclara@gmail.com")])
    assert "Idade deve estar entre 1 e 200" in person.isValidToInclude()

def test_person_without_email(person_without_email):
    assert "Pessoa deve ter pelo menos um email associado" in person_without_email.isValidToInclude()
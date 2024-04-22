import pytest
from person import Person, Email

# Data
@pytest.fixture
def valid_person():
    emails = [Email("mariaclara@gmail.com")]
    return Person("Maria Clara", 25, emails)

@pytest.fixture
def invalid_person():
    emails = [Email("mariaclara@gmail")]
    return Person("Maria", 30, emails)

@pytest.fixture
def person_without_email():
    return Person("Maria Clara", 35, [])

@pytest.fixture
def person_with_non_alphabetic_name():
    emails = [Email("mariaclara@gmail.com")]
    return Person("Maria 123", 25, emails)

@pytest.fixture
def person_with_out_of_range_age():
    emails = [Email("mariaclara@gmail.com")]
    return Person("Maria Clara", 201, emails)

@pytest.fixture
def person_with_invalid_emails():
    emails = [Email("mariaclara@gmail.com"), Email("invalidemail")]
    return Person("Maria Clara", 25, emails)

@pytest.fixture
def person_with_single_name():
    emails = [Email("mariaclara@gmail.com")]
    return Person("Maria", 25, emails)

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

def test_age_range():
    person = Person("Maria Clara", 0, [Email("mariaclara@gmail.com")])
    assert "Idade deve estar entre 1 e 200" in person.isValidToInclude()

def test_non_alphabetic_name(person_with_non_alphabetic_name):
    assert "Nome deve ser composto apenas por letras" in person_with_non_alphabetic_name.isValidToInclude()

def test_out_of_range_age(person_with_out_of_range_age):
    assert "Idade deve estar entre 1 e 200" in person_with_out_of_range_age.isValidToInclude()

def test_invalid_emails(person_with_invalid_emails):
    assert "Formato de email inválido" in person_with_invalid_emails.isValidToInclude()

def test_single_name(person_with_single_name):
    assert "Nome deve ter ao menos 2 partes" in person_with_single_name.isValidToInclude()
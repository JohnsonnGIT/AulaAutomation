import pytest
from pytest_bdd import scenarios, given, when, then,  parsers
from pom.action_page import DemoPage

scenarios('features/suit.feature')

@pytest.fixture
def demo_page(browser):
    return DemoPage(browser)

@given('Estou no webapp TDD Detroit homepage')
def open_homepage(demo_page):
    demo_page.open()

@when(parsers.parse('Eu adiciono o estudante "{nome_estudant}"'))
def add_student(demo_page, nome_estudant):
    demo_page.add_student(nome_estudant)

@then(parsers.parse('Eu devo ver o texto "INFO Added student id: {id_num}, Name: {nome_estudant}"'))
def check_student_added(demo_page, nome_estudant):
    text =  "INFO Added student id: 1, Name: " + nome_estudant
    assert text in demo_page.get_message()

# Add cursos ----------------------------------------------
@when(parsers.parse('Eu adiciono um curso com o nome "{nome_curso}"'))
def add_course(demo_page, nome_curso):
    demo_page.add_course(nome_curso)

@then(parsers.parse('Eu devo ver "INFO Curso adicionado com sucesso. id: {id}, Nome: {nome_curso}"'))
def check_course_added(demo_page, id, nome_curso):
    text = "INFO Added course id: "+ id +", Nome: "+ nome_curso
    assert  text in demo_page.get_message()

#adicionar materia --------------------------------------------
@when(parsers.parse('Eu adiciono a matéria "{nome_materia}" no curso de id "{id_curso}"'))
def add_discipline(demo_page, nome_materia, id_curso):
    demo_page.add_discipline(nome_materia, id_curso)

@then(parsers.parse('Eu devo ver "INFO Matéria {nome_materia} adicionada com sucesso ao curso de id {id_curso}"'))
def check_discipline_added(demo_page, nome_materia, id_curso):
    text = "Added discipline id: " + id_curso + ", Name: " + nome_materia + ", Course: 1"
    assert text in demo_page.get_message()

# ----------------------------------------------------
@when(parsers.parse('Eu inscrevo o aluno com id "{id_aluno}" na disciplina de id "{id_disciplina}"'))
def enroll_student_in_discipline(demo_page, id_aluno, id_disciplina):
    demo_page.subscribe_student(id_aluno, id_disciplina)

@then(parsers.parse('Eu devo ver "INFO Aluno de id {id_aluno} inscrito com sucesso na disciplina de id {id_disciplina}"'))
def check_enrollment_discipline(demo_page, id_aluno, id_disciplina):
    assert f"INFO Aluno de id {id_aluno} inscrito com sucesso na disciplina de id {id_disciplina}" in demo_page.get_message()

@when(parsers.parse('Eu inscrevo o aluno com id "{id_aluno}" no curso de id "{id_curso}"'))
def enroll_student_in_course(demo_page, id_aluno, id_curso):
    demo_page.subscribe_student_to_course(id_aluno, id_curso)

@then(parsers.parse('Eu devo ver "INFO Aluno de id {id_aluno} inscrito com sucesso no curso de id {id_curso}"'))
def check_enrollment_course(demo_page, id_aluno, id_curso):
    assert f"INFO Student id {id_aluno} subscribed to course id {id_curso}" in demo_page.get_message()

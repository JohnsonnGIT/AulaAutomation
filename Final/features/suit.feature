Feature: Testar funcionalidades de adição de estudantes

Scenario: Adicionar estudante
    Given Estou no webapp TDD Detroit homepage
    When Eu adiciono o estudante "Werner"
    Then Eu devo ver o texto "INFO Added student id: 1, Name: Werner"

Scenario: Adicionar 3 cursos
    Given Estou no webapp TDD Detroit homepage
    When Eu adiciono um curso com o nome "Exatas"
    Then Eu devo ver "INFO Curso adicionado com sucesso. id: 1, Nome: Exatas"
    When Eu adiciono um curso com o nome "Letras"
    Then Eu devo ver "INFO Curso adicionado com sucesso. id: 2, Nome: Letras"
    When Eu adiciono um curso com o nome "Humanas"      
    Then Eu devo ver "INFO Curso adicionado com sucesso. id: 3, Nome: Humanas"


Scenario: Adicionar 3 materias
    Given Estou no webapp TDD Detroit homepage
    When Eu adiciono um curso com o nome "Humanas" 
    And Eu adiciono um curso com o nome "Letras"
    And Eu adiciono um curso com o nome "Exatas"
    When  Eu adiciono a matéria "Sociologia" no curso de id "1"
    Then  Eu devo ver "INFO Matéria Sociologia adicionada com sucesso ao curso de id 1"
    When  Eu adiciono a matéria "Filosofia" no curso de id "1"
    Then  Eu devo ver "INFO Matéria Filosofia adicionada com sucesso ao curso de id 2"    
    When  Eu adiciono a matéria "Teologia" no curso de id "1"
    Then  Eu devo ver "INFO Matéria Teologia adicionada com sucesso ao curso de id 3"     


Scenario: cadastrar aluno na materia e curso
    Given Estou no webapp TDD Detroit homepage
    When Eu adiciono um curso com o nome "Humanas" 
    And Eu adiciono um curso com o nome "Letras"
    And Eu adiciono um curso com o nome "Exatas"
    And Eu adiciono a matéria "Sociologia" no curso de id "1"
    And Eu adiciono a matéria "Filosofia" no curso de id "1"
    And Eu adiciono a matéria "Teologia" no curso de id "1"
    And Eu adiciono o estudante "Werner"
    And Eu inscrevo o aluno com id "1" no curso de id "1"
    Then Eu devo ver "INFO Aluno de id 1 inscrito com sucesso no curso de id 1"
    When Eu inscrevo o aluno com id "1" na disciplina de id "1"
    Then Eu devo ver "INFO Aluno de id 1 inscrito com sucesso na disciplina de id 1" 

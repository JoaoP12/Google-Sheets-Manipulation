from enum import Enum

class Situation(Enum):
    APPROVED = 1
    FAILED_BY_ABSENCE = 2
    FAILED_BY_GRADES = 3
    FINAL_EXAM = 4

situation_strings = {
    Situation.APPROVED: 'Aprovado',
    Situation.FAILED_BY_ABSENCE: 'Reprovado por Falta',
    Situation.FAILED_BY_GRADES: 'Reprovado por Nota',
    Situation.FINAL_EXAM: 'Exame Final'
} 
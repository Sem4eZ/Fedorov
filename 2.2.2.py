from contest.report import InputConnect

VACANCIES = 'вакансии'
STATISTICS = 'статистика'
ALLOW_INPUTS = (VACANCIES, STATISTICS)
TEXT_INPUT = 'Выводим вакансии или статистику? Введите одно значение из 2 вариантов: '
TEXT_ERROR = 'Некорректное значение ввода, попробуйте, пожалуйста, ещё раз.'
FILE_NAME = '../data/vacancies_by_year.csv'
VACANCY_NAME = 'Работающий программист'

if __name__ == '__main__':
    while True:
        result = str(input(TEXT_INPUT)).lower()
        if result.lower() in ALLOW_INPUTS:
            break
        print(TEXT_ERROR)

    input_connect = InputConnect(FILE_NAME, VACANCY_NAME)

    if result == STATISTICS:
        input_connect.generate_statistics(True)
    elif result == VACANCIES:
        stats1, stats2, stats3, stats4, stats5, stats6 = input_connect.generate_statistics()
        input_connect.generate_vacancies(stats1, stats2, stats3, stats4, stats5, stats6)

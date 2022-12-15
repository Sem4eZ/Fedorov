import cProfile
from contest.main import DataSet
import datetime
from dateutil.parser import parse


def profile(func):
    """Декоратор для профилирования какой-либо функции"""
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        print('Статистика по методу «{0}»\n'.format(args[1].__name__))
        profiler.print_stats()
        return result
    return wrapper


# def first_date_parser(original_date):
#     changed_date = datetime.datetime.strptime(original_date[:10], '%Y-%m-%d').date()
#     return '{0.day}.{0.month}.{0.year}'.format(changed_date)


# def second_date_parser(original_date):
#     changed_date = parse(original_date)
#     return '{0.day}.{0.month}.{0.year}'.format(changed_date)


# def third_date_parser(original_date):
#     changed_date = str(original_date).split('T')[0]
#     changed_date = changed_date.split('-')
#     return '{0[2]}.{0[1]}.{0[0]}'.format(changed_date)


def fourth_date_parser(original_date):
    changed_date = original_date[:10].split('-')
    return '{0[2]}.{0[1]}.{0[0]}'.format(changed_date)


# def fifth_date_parser(original_date):
#     changed_date = original_date[:10].split('-')
#     changed_date.reverse()
#     return '.'.join(changed_date)


# def sixth_date_parser(original_date):
#     changed_date = str(original_date).split('T')[0].split('-')
#     changed_date.reverse()
#     return '.'.join(changed_date)


class DateRepository:
    def __init__(self):
        self.original_dates = []
        self.finished_dates = []

    @profile
    def parse_date(self, date_parser):
        self.finished_dates = [date_parser(original_date) for original_date in self.original_dates]


if __name__ == '__main__':
    dataset = DataSet('./data/vacancies_big.csv', '')
    date_repository = DateRepository()
    date_repository.original_dates = [vacancy['published_at'] for vacancy in dataset.csv_reader()]

    # date_repository.parse_date(first_date_parser)
    # print(date_repository.finished_dates[:10])

    # date_repository.parse_date(second_date_parser)
    # print(date_repository.finished_dates[:10])

    # date_repository.parse_date(third_date_parser)
    # print(date_repository.finished_dates[:10])

    date_repository.parse_date(fourth_date_parser)
    print(date_repository.finished_dates[:10])

    # date_repository.parse_date(fifth_date_parser)
    # print(date_repository.finished_dates[:10])

    # date_repository.parse_date(sixth_date_parser)
    # print(date_repository.finished_dates[:10])

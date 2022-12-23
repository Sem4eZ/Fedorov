import pandas as pd
from datetime import datetime
from functools import partial
import concurrent.futures as pool

from Task232 import DataSet, InputConectStatistics


def get_statistic_by_year(f, vacancy, statistics):
    df = pd.read_csv(f)
    df["salary"] = df[['salary_from', 'salary_to']].mean(axis=1)
    year = int(f[15:19])
    statistics[0] = (year, int(df["salary"].mean()))
    statistics[1] = (year, int(df[df['name'] == vacancy]['salary'].mean()))
    statistics[2] = (year, len(df))
    statistics[3] = (year, len(df[df["name"] == vacancy]))
    return statistics

def get_statistic_by_city(file):
    df = pd.read_csv(file)
    df["salary"] = df[['salary_from', 'salary_to']].mean(axis=1)
    cities = df["area_name"].unique()
    stat1 = {city: [] for city in cities}
    stat2 = {city: 0 for city in cities}
    for city in cities:
        stat1[city] = int(df[df['area_name'] == city]['salary'].mean())
        stat2[city] = round(len(df[df['area_name'] == city]) / len(df), 4)
    return [stat1, stat2]


if __name__ == '__main__':
    file = input('Название файла:')
    vacancy = input('Название вакансии:')
    df = pd.read_csv(file)
    df["years"] = df["published_at"].apply(lambda s: datetime.strptime(s, "%Y-%m-%dT%H:%M:%S%z").year)
    years = df["years"].unique()
    salary_by_years = {year: [] for year in years}
    vac_salary_by_year = {year: [] for year in years}
    vac_by_years = {year: 0 for year in years}
    vac_count_by_years = {year: 0 for year in years}
    statistics = [salary_by_years, vac_salary_by_year, vac_by_years, vac_count_by_years]
    files = []
    for year in years:
        files.append(f"csv_files\\year_{year}.csv")
    executor = pool.ProcessPoolExecutor()
    output = list(executor.map(partial(get_statistic_by_year, vacancy=vacancy, statistics=statistics), files))
    salary_by_years = {stat[0][0]: stat[0][1] for stat in output}
    vac_salary_by_year = {stat[1][0]: stat[1][1] for stat in output}
    vac_by_years = {stat[2][0]: stat[2][1] for stat in output}
    vac_count_by_years = {stat[3][0]: stat[3][1] for stat in output}

    dataSet = DataSet(file)
    outputer = InputConectStatistics()
    dict_city_count = {}
    for vac in dataSet.vacancies_objects:
        if vac.area_name not in dict_city_count.keys():
            dict_city_count[vac.area_name] = 0
        dict_city_count[vac.area_name] += 1
    new_vacancies_objects = list(
        filter(lambda vac: int(len(dataSet.vacancies_objects) * 0.01) <= dict_city_count[vac.area_name],
               dataSet.vacancies_objects))
    res_city = dict(sorted(outputer.get_salary_level(new_vacancies_objects, "area_name").items(), key=lambda x: x[1],
                           reverse=True)[:10])
    res_city_vac = dict(
        sorted(outputer.get_count_vacancy(new_vacancies_objects, "area_name", dataSet).items(), key=lambda x: x[1],
               reverse=True)[:10])

    print("Динамика уровня зарплат по годам:", salary_by_years)
    print("Динамика уровня зарплат по годам для выбранной профессии:", vac_salary_by_year)
    print("Динамика количества вакансий по годам:", vac_by_years)
    print("Динамика количества вакансий по годам для выбранной профессии:", vac_count_by_years)
    print(f'Уровень зарплат по городам (в порядке убывания): {res_city}')
    print(f'Доля вакансий по городам (в порядке убывания): {res_city_vac}')




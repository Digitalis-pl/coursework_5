from src_mvp.classes.DB_managerf import DBManager
from simpleconfig import HOST, DB_USER, PASS
import psycopg2

dbm = DBManager


def form_vac_info(comp_info, get_ex1):
    all_vac_info = []  #
    for el in comp_info:
        vac_info = get_ex1.get_vac_info(el[3])
        all_vac_info.append(vac_info)
    return all_vac_info


def work_with_bd(obj):
    try:
        function = {'получить список всех компаний с количеством вакансий': obj.get_companies_and_vacancies_count,
                    'получить информацию по всем вакансиям': obj.get_all_vacancies,
                    'получить среднюю зарплату по вакансиям': obj.get_avg_salary,
                    'получить список всех вакансий, с зарплатой выше средней': obj.get_vacancies_with_higher_salary,
                    'получить список всех вакансий по ключевому слову': obj.get_vacancies_with_keyword,
                    'добавить данные в базу': obj.return_to_get,
                    'завершить работу': obj.exit_and_say_bye}
        print('\nукажите необходимое действие')
        key_list = list(function.keys())
        for el in key_list:
            print(f'{key_list.index(el) + 1}) {el}')
        user_answer = int(input()) - 1
        answer = key_list[user_answer]
        return function[answer]()
    except IndexError:
        print("Выберите из доступных вариантов действий")
        work_with_bd(obj)


def create_db(name):
    conn = psycopg2.connect(dbname="postgres",
                            host=HOST,
                            user=DB_USER,
                            password=PASS)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f'DROP DATABASE {name}')
    cur.execute(f'CREATE DATABASE {name}')

    cur.close()
    conn.close()

    conn = psycopg2.connect(dbname=name,
                            host=HOST,
                            user=DB_USER,
                            password=PASS)
    with conn.cursor() as cur:
        cur.execute('''CREATE TABLE company(
        company_id int NOT NULL UNIQUE PRIMARY KEY,
        company_name varchar(60),
        open_vacancies int,
        vacancies_url varchar(60)
        );''')

    with conn.cursor() as cur:
        cur.execute('''CREATE TABLE vacancies(
        vacancy_id int NOT NULL UNIQUE PRIMARY KEY,
        vacancy_name varchar(100),
        published_at date,
        salary int,
        salary_currency varchar(30),
        schedule varchar(30),
        experience varchar(30),
        company_id int
        REFERENCES company(company_id),
        contacts_mail varchar(30) DEFAULT 'none'
        );''')

    conn.commit()
    conn.close()



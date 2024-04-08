import psycopg2
from ..simpleconfig import HOST, PASS, DB_USER


class DBManager:

    def __init__(self):
        self.str = 0
        self.stop_word = True

    def get_companies_and_vacancies_count(self):
        self.str = f'SELECT company_name, open_vacancies FROM public.company'
        return self.str

    def get_all_vacancies(self):
        self.str = f'''SELECT vacancy_name, company_name, concat(salary, ' ', salary_currency)
        FROM public.company
        join public.vacancies on vacancies.company_id = company.company_id'''
        return self.str

    def get_avg_salary(self):
        self.str = f'SELECT AVG(salary) FROM vacancies'
        return self.str

    def get_vacancies_with_higher_salary(self):
        self.str = f'''SELECT vacancy_name, concat(salary, ' ', salary_currency)
        FROM vacancies where salary > (select AVG(salary) from vacancies)'''
        return self.str

    def get_vacancies_with_keyword(self):
        where_list = []
        frase = input("через пробел опишите ключевые слова\n")
        word_list = frase.split()
        for x in word_list:
            where_list.append(f"vacancy_name like '{x}%' or")
        where_str = ' '.join(where_list)
        self.str = f"""SELECT vacancy_name FROM vacancies WHERE
            {where_str[:-3]};"""
        return self.str

    def work(self):
        conn = psycopg2.connect(dbname='hh_data',
                                host=HOST,
                                user=DB_USER,
                                password=PASS)
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(f'{self.str}')
                    rows = cur.fetchall()

                    for row in rows:
                        print(str(row))
        except psycopg2.Error:
            return 'nовторный запрос'
        finally:
            conn.close()

    def return_to_get(self):
        self.stop_word = 'stop'
        return self.stop_word

    def exit_and_say_bye(self):
        print("До новых встреч")
        self.stop_word = 'exit'
        return self.stop_word

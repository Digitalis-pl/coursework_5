import psycopg2
from ..simpleconfig import HOST, PASS, DB_USER


class DBMaker:

    def __init__(self, info):
        self.info = info

    def create_db(self):
        pass

    def fill_db(self):
        con = psycopg2.connect(dbname='hh_data',
                               host=HOST,
                               user=DB_USER,
                               password=PASS)
        try:
            with con:
                with con.cursor() as cur:
                    for el in self.info[0]:
                        val_num = '%s, ' * len(el)
                        cur.execute(f'INSERT INTO company VALUES ({val_num[:-2]})', el)
                    for some in self.info[1]:
                        for lm in some:
                            val_num = '%s, ' * len(lm)
                            cur.execute(f'INSERT INTO vacancies VALUES ({val_num[:-2]})', lm)
        except psycopg2.Error:
            return 'nовторный запрос'
        finally:
            con.close()

    @staticmethod
    def truncate_db():
        con = psycopg2.connect(dbname='hh_data',
                               host=HOST,
                               user=DB_USER,
                               password=PASS)
        try:
            with con:
                with con.cursor() as cur:
                    cur.execute('TRUNCATE table vacancies cascade;')
                    cur.execute('TRUNCATE table company cascade;')
        except psycopg2.Error:
            return 'nовторный запрос'
        finally:
            con.close()


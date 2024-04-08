from src_mvp.classes.real_get_class import GetResponse
from src_mvp.classes.for_user import ForUser
from src_mvp.classes.DB_maker import DBMaker
from src_mvp.classes.DB_managerf import DBManager
from utils import form_vac_info, work_with_bd, create_db


params = []


def main():
    #create_db('hh_data')
    print("Для поиска интересующих вакансий введите название в поиск\nдля завершения работы введите ~")
    name = input("поиск\n")
    while name != '~':
        foru = ForUser(name)
        get_ex1 = GetResponse(name, 10)

        get_ex1.get_information()
        a = get_ex1.sort_info()
        foru.lets_talk_are_you_sure(a)
        comp_info = foru.lets_talk_choose_comp(a)
        all_vac_info = form_vac_info(comp_info, get_ex1)
        all_needed_info = [comp_info, all_vac_info]

        maker = DBMaker(all_needed_info)
        maker.fill_db()
        name = '~'
        while True:
            dbm = DBManager()

            work_with_bd(dbm)

            dbm.work()
            if dbm.stop_word == 'stop':
                main()
                break
            elif dbm.stop_word == 'exit':
                break
            else:
                continue


main()

DBMaker.truncate_db()

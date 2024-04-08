class ForUser:
    """Взаимодействуем с пользователем, проверяем правильность введенных данных"""
    def __init__(self, name):
        self.name = name
        self.comp_name_list = []
        self.say = str

    def lets_talk_are_you_sure(self, comp_list):
        counter = 0
        for c in comp_list:
            if c["company_name"] == self.name:
                self.say = f'\nПо вашему запросу найдены следующие варианты {c["company_name"]}\n'
            else:
                counter += 1
                self.comp_name_list.append(f"{counter})" + " " + c["company_name"])
        if len(self.comp_name_list) > 0:
            res = '\n'.join(self.comp_name_list)
            self.say = f'\nЗапрос {self.name} не обнаружен\nвозможно вы имели ввиду что то из\n{res}\n'
        print(self.say)

    @staticmethod
    def lets_talk_choose_comp(comp_list):
        sol1 = input("Добавить в базу одну из доступных компаний: нажмите 1\nдобавить все: нажмите 2\n")
        values_list = []
        if int(sol1) == 1:
            sol2 = input("\nукажите номер интересующей компании\n")
            comp_info = list(comp_list[int(sol2)-1].values())
            values_list.append(comp_info)
        else:
            for el in comp_list:
                val = list(el.values())
                values_list.append(val)
        return values_list

    def __del__(self):
        print("Запрос выполнен")

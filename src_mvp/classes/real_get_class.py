from src_mvp.classes.abc_class_get import Get
import requests


class GetResponse(Get):
    """Класс для запроса к сайту"""
    def __init__(self, company_name, top):
        self.name = company_name
        self.top = top
        self.get_information()
        self.hh_comp_list = []

    def sort_info(self) -> list:
        """Сортируем данные"""
        useful_inf = []
        counter = 0
        while counter < self.top:
            cell = {}
            counter += 1
            try:
                cell["id"] = self.hh_comp_list[counter - 1]["id"]
                cell["company_name"] = self.hh_comp_list[counter - 1]["name"]
                cell["open_vacancies"] = self.hh_comp_list[counter - 1]["open_vacancies"]
                cell["vacancies_url"] = self.hh_comp_list[counter - 1]["vacancies_url"]
            except IndexError:
                print(f"""по вашему запросу найдено только {len(useful_inf)} компаний""")

                return useful_inf
            useful_inf.append(cell)
        return useful_inf

    def get_information(self) -> dict or str:
        try:
            params = {"text": f'{self.name}',
                      "sort_by": "by_name",
                      "only_with_vacancies": "true",
                      "per_page": self.top}
            response = requests.get("https://api.hh.ru/employers", params=params)
            if response.status_code == 200:
                self.hh_comp_list = response.json()['items']
                if len(self.hh_comp_list) == 0:
                    print("Кажется что то пошло не так, попробуйте ввести запрос заново")
                    self.name = input("Поиск\n")
                    self.get_information()
                    return self.name
                return self.hh_comp_list
            else:
                raise UserWarning
        except UserWarning:
            print("Что то пошло не так введите запрос заново")

    def __str__(self):
        return f'По вашему запросу были найдены следующие компании\n{self.hh_comp_list}'

    @staticmethod
    def get_vac_info(link):
        inf = []
        resp = requests.get(link).json()["items"]
        for el in resp:
            el_list = []
            el_list.append(el['id'])
            el_list.append(el['name'])
            el_list.append(el['published_at'])
            try:
                el_list.append(el['salary']['from'])
                el_list.append(el['salary']['currency'])
            except TypeError:
                el_list.append(None)
                el_list.append(None)
            el_list.append(el['schedule']['name'])
            el_list.append(el['experience']['name'])
            el_list.append(el['employer']['id'])
            try:
                el_list.append(el['contacts'])
            except KeyError:
                el_list.append(None)
            inf.append(el_list)
        return inf

from tools.dbloader import DBLoader


def main_theme():
    print('введите название организации')
    name_org = input()
    s = DBLoader()
    res = s.data_preparation_and_load_in_db(s.get_vacancies(name_org))



# s = DBLoader()
# s.big_red_button('corporations')
# s.big_red_button('vacancies')

# main_theme()

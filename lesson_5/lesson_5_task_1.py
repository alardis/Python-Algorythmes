# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import namedtuple


Company_data = namedtuple('Company_data', ['season_1', 'season_2', 'season_3', 'season_4'])
count_companies = input('Введите количество предприятий:\n')
try:
    # заносим информацию о компаниях
    count_companies = int(count_companies)
    company_dict = {}
    for i in range(count_companies):
        company_name = input('Введите название компании:\n')
        season_1_income = input(f'Введите прибыль за 1 квартал:\n')
        season_2_income = input(f'Введите прибыль за 2 квартал:\n')
        season_3_income = input(f'Введите прибыль за 3 квартал:\n')
        season_4_income = input(f'Введите прибыль за 4 квартал:\n')
        company_dict.update({company_name: Company_data(season_1=int(season_1_income), season_2=int(season_2_income),
                                                        season_3=int(season_3_income), season_4=int(season_4_income))})

    print(company_dict)
    # считаем их денежки
    mean_sum = 0
    mean_dict = {}
    for name, data in company_dict.items():
        mean_income = (data.season_1 + data.season_2 + data.season_3 + data.season_4) / 4
        print(f'Прибыль компании {name} в среднем за год: {mean_income}')

except ValueError:
    print('Что-то не так с вводом, будьте аккуратнее!')

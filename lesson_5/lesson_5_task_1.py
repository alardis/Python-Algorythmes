# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import namedtuple


Company_data = namedtuple('Company_data', ['quater_1', 'quater_2', 'quater_3', 'quater_4'])
count_companies = input('Введите количество предприятий:\n')
try:
    count_companies = int(count_companies)
    company_dict = {}
    for i in range(count_companies):
        company_name = input('Введите название компании:\n')
        quater_1_income = input(f'Введите прибыль за 1 квартал:\n')
        quater_2_income = input(f'Введите прибыль за 2 квартал:\n')
        quater_3_income = input(f'Введите прибыль за 3 квартал:\n')
        quater_4_income = input(f'Введите прибыль за 4 квартал:\n')
        company_dict.update({company_name: Company_data(quater_1=quater_1_income, quater_2=quater_2_income,
                                                        quater_3=quater_3_income, quater_4=quater_4_income)})

    print(company_dict)

except ValueError:
    print('Что-то не так с вводом, будьте аккуратнее!')

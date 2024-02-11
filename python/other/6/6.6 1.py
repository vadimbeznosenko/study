"""
Внести изменения в написанные в предыдущем разделе программы с иерархией классов
“Квадрат” - ”Правильная квадратная призма”
следующим образом:
- каждый класс должен быть оформлен в виде отдельного модуля;
- демонстрация работы с классами должна осуществляться в главном модуле программы;
- демонстрация работы с классами должна осуществляться только в случае автономного
запуска главного модуля.
"""
from RegularSqPrism import RegualrSqPrism


if __name__ == "__main__":
    prisms = [RegualrSqPrism(3, 5), RegualrSqPrism(2, 8), RegualrSqPrism(9, 15)]
    max_s_prism = max(prisms, key=lambda pr: pr.calc_square())
    min_d_prism = min(prisms, key=lambda pr: pr.calc_diagonal())

    print('*'*50)
    print(f'The prism with max sqiare: {max_s_prism.get_info()}')
    print(f'The prism with min diagonal: {min_d_prism.get_info()}')

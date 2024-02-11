"""
Внести изменения в написанные в предыдущем разделе программы с иерархией классов
“Треугольник” - ”Равносторонний треугольник”
следующим образом:
- каждый класс должен быть оформлен в виде отдельного модуля;
- демонстрация работы с классами должна осуществляться в главном модуле программы;
- демонстрация работы с классами должна осуществляться только в случае автономного
запуска главного модуля.
"""
from Triangle import Triangle
from EquilateralTriangle import EquilateralTriangle


if __name__ == "__main__":
    tr = [Triangle(2, 5, 6), Triangle(2, 2, 2), Triangle(5, 2, 4), Triangle(7, 7, 7), Triangle(7, 3, 6), Triangle(4, 4, 4)]

    p_max = 0
    tr_p_max = None

    for i in range(0, len(tr)):
        if tr[i].is_equilateral():
            tr[i] = EquilateralTriangle(tr[i].get_sides()[0])
            print(f'Triangle {tr[i].get_info()} is equilateral.')
            p = tr[i].get_perimeter()
            if p > p_max:
                p_max = p
                tr_p_max = tr[i]

    print('*'*50)
    print(f'Max perimeter: {p_max}')
    print(f'Equilateral Triangle with max perimeter: {tr_p_max.get_info()}')

    print()
    print(tr[0].get_info())
    tr[0].is_equilateral()
    tr[0].get_angles()
    print(tr[1].get_info())
    tr[1].is_equilateral()
    tr[1].get_angles()
"""
Спортивный обозреватель хранит записи о каждой спортивной команде следующим образом:
первым в списке идет имя тренера команды, затем - капитана, и далее имена всех участников
в соответствии с их порядковым номером игрока. Также у него имеется список всех спортивных команд,
первое место в котором занимает лучшая команда, и далее по убывающей к самой худшей.
Выведите на экран имя капитана худшей команды.
"""

team1 = ['Alex', 'Mark', 'Player1', 'Player2', 'Player3', 'Player4', 'Player5']
team2 = ['Antony', 'Tom', 'Player1', 'Player2', 'Player3', 'Player4', 'Player5']
team3 = ['Michael', 'Noam', 'Player1', 'Player2', 'Player3', 'Player4', 'Player5']

common_list = [team2, team1, team3]

print(common_list[-1][1])
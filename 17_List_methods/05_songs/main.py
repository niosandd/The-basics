violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

count = int(input('ВВедите сколько вам нужнно: '))
plaing_time = 0

for i in range(count):
    print('Введите', i + 1, 'фильм', end=' ')
    word = input()
    if violator_songs[i][0] == word:
        plaing_time += violator_songs[i][1]
        print(plaing_time)
    else:
        print('gg')

print(plaing_time)
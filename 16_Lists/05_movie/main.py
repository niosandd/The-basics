
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favorite_films = []
while True:
    film_name = input('Введите название фильма: ')
    if film_name == 'end':

        break
    if film_name in favorite_films:

        print('Этот фильм уже есть в списке любимых.')
    elif film_name in films:
        favorite_films.append(film_name)
    else:
        print('Этого фильма нет в списке.')
print('Список любимых фильмов:', favorite_films)
from random import choice

categories = ['Храна', 'Цвят', 'Спорт', 'Животни']

categories_map = {
    'храна': ['Банан', 'Ориз', 'Ябълка', 'Картофи', 'Сандвич'],
    'цвят': ['Зелено', 'Синьо', 'Червено', 'Жълто', 'Оранжево'],
    'спорт': ['Борба', 'Бокс', 'Баскетбол', 'Футбол', 'Ръгби'],
    'животни': ['Жерав', 'Крава', 'Вълк', 'Овца', 'Камила'],
}

def join_current_word_state_with_space(word_list):
    return ' '.join(word_list)

def join_current_word_state_without(word_list):
    return ''.join(word_list)

categorie_choosen = input('Изберете си категория моля: Храна, Цвят, Спорт, Животни\n').lower()

random_word = choice(categories_map[categorie_choosen])

current_word_state = ['_' for x in range(len(random_word))]

chances_left = 8

print(join_current_word_state_with_space(current_word_state))

while join_current_word_state_with_space(current_word_state) != random_word:
    letter_choosen = input('Изберете буква.')

    if letter_choosen in random_word:
        letter_place = [x for x in range(len(random_word)) if random_word[x] == letter_choosen][0]
        current_word_state[letter_place] = letter_choosen
        print(f'Думата в момента е: {join_current_word_state_with_space(current_word_state)}')

    else:
        chances_left -= 1
        print(f'Грешна буква, остават Ви {chances_left} опита')


    if join_current_word_state_without(current_word_state) == random_word:
        print('Познахте!!!')
        break

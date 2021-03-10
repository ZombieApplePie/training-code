

word = (input('Enter the word to guess: ')).lower()

while True:

    word_letters = list(word)
    visible_word = list('_' * len(word_letters))
    tries = 8

    print(''.join(visible_word))

    while visible_word != word_letters and tries > 0:
        letter = input('Enter a letter: ')

        if letter in word_letters:
            for count, let in enumerate(word_letters):
                if let == letter:
                    visible_word[count] = letter
            print(''.join(visible_word))
        else:
            tries -= 1
            print(f'Wrong letter, {tries} tries left')
        continue

    if visible_word == word_letters:
        print(f'Hurray! You won with {tries} tries left!')
    else:
        print('GAME OVER')

    break

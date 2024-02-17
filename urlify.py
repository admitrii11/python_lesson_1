def urlify(text: list[str]) -> int:
    """Заменяем пробелы на %20 и возвращаем новую длину массива символов"""
    fast = slow = space_counter = 0

    while fast < len(text):
      if text[fast] == '':
        break
      if text[fast] == ' ':
        space_counter += 1
      fast += 1

    del text[fast:]
    text.extend([''] * (space_counter)*2)

    slow = fast + (space_counter*2) - 1
    fast -= 1

    while fast >= 0:
      if text[fast] == ' ':
        text[slow] = '0'
        slow -= 1
        text[slow] = '2'
        slow -= 1
        text[slow] = '%'
        slow -= 1
        fast -= 1
      else:
        text[slow] = text[fast]
        fast -= 1
        slow -= 1
    print(len(text))
    print(text)
    return len(text)

#Тесты

text = list('my url')
new_len = urlify(text)

assert new_len == 8
assert text[:new_len] == list('my%20url')

text = list('my url') + [''] * 21
new_len = urlify(text)

assert new_len == 8
assert text[:new_len] == list('my%20url')

text = list(' te st ')
new_len = urlify(text)

assert new_len == 13
assert text[:new_len] == list('%20te%20st%20')

text = list('')
new_len = urlify(text)

assert new_len == 0
assert text[:new_len] == list('')

text = list('     ')
new_len = urlify(text)

assert new_len == 15
assert text[:new_len] == list('%20%20%20%20%20')

text = list('a   b   c   d')
new_len = urlify(text)

assert new_len == 31
assert text[:new_len] == list('a%20%20%20b%20%20%20c%20%20%20d')

text = list('Finally, I did this! ')
new_len = urlify(text)

assert new_len == 29
assert text[:new_len] == list('Finally,%20I%20did%20this!%20')

text = list(' ')
new_len = urlify(text)

assert new_len == 3
assert text[:new_len] == list('%20')

text = list(' One more test, give me one more TEEEEEST!')
new_len = urlify(text)

assert new_len == 58
assert text[:new_len] == list('%20One%20more%20test,%20give%20me%20one%20more%20TEEEEEST!')

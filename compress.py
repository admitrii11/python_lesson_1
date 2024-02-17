def compress(text: list[str]) -> int:

    fast = slow = 0
    char_counter = 1
    if len(text) != 0:
      for fast in range(1, len(text)):
          if text[fast] == text[fast - 1]:
              char_counter += 1
          else:
              text[slow] = text[fast - 1]
              slow += 1
              if char_counter > 1:
                  for every_number in str(char_counter):
                      text[slow] = every_number
                      slow += 1
              char_counter = 1

      text[slow] = text[fast]
      slow += 1
      if char_counter > 1:
          for every_number in str(char_counter):
              text[slow] = every_number
              slow += 1
    
    else:
      slow = 0

    return slow

#Tests

text = list('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')
new_len = compress(text)

assert new_len == 20
assert text[:new_len] == list('A4B3C2XYZD4E3F3A6B28')

text = list('')
new_len = compress(text)

assert new_len == 0
assert text[:new_len] == list('')

text = list('   ')
new_len = compress(text)

assert new_len == 2
assert text[:new_len] == list(' 3')

text = list('A')
new_len = compress(text)

assert new_len == 1
assert text[:new_len] == list('A')

text = list('ABCDEFG')
new_len = compress(text)

assert new_len == 7
assert text[:new_len] == list('ABCDEFG')

text = list('AAAAAAAAAAAAAAA')
new_len = compress(text)

assert new_len == 3
assert text[:new_len] == list('A15')

text = list('AABBCCCDDDDEEEEE')
new_len = compress(text)

assert new_len == 10
assert text[:new_len] == list('A2B2C3D4E5')

def remove_zeroes(numbers: list[int]) -> int:
    fast = slow = zero_counter = 0

    while fast < len(numbers):
        if numbers[fast] != 0:
            numbers[slow] = numbers[fast]
            slow += 1
        else:
            zero_counter += 1
        fast += 1

    for i in range(zero_counter):
        numbers[slow + i] = 0

    return slow

#Tests

nums = [0,42,21,0,100,0,5,1,0,7,3,0,404,0]
new_len = remove_zeroes(nums)

assert new_len == 8
assert nums[:new_len] == [42,21,100,5,1,7,3,404]

print(new_len)
print(nums[:new_len])
print()

nums = []
new_len = remove_zeroes(nums)

assert new_len == 0
assert nums[:new_len] == []

print(new_len)
print(nums[:new_len])
print()

nums = [0]
new_len = remove_zeroes(nums)

assert new_len == 0
assert nums[:new_len] == []

print(new_len)
print(nums[:new_len])
print()

nums = [00000]
new_len = remove_zeroes(nums)

assert new_len == 0
assert nums[:new_len] == []

print(new_len)
print(nums[:new_len])
print()

nums = [0,0,0,0,42,21,0,100,0,5,1,0,7,3,0,404,0,0,0,0]
new_len = remove_zeroes(nums)

assert new_len == 8
assert nums[:new_len] == [42,21,100,5,1,7,3,404]

print(new_len)
print(nums[:new_len])
print()

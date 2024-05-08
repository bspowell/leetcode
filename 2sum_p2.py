def twoSum(self, numbers, target):
    a = 0
    r = len(numbers) - 1

    while a < r:
        sum = numbers[a] + numbers[r]
        if sum == target:
            return [a + 1, r + 1]
        elif sum < target:
            a += 1
        else:
            r -= 1
            
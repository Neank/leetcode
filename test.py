def deleteSpace(str):
    nums = list(str)
    start = 0
    while nums[start] == '#':
        start += 1
    find = back = start
    while find < len(nums):
        if nums[find] == '#':
            back -= 1
        else:
            back = back if back >= start else start
            nums[back] = nums[find]
            back += 1
        find += 1
    return ''.join(nums[start:back])

if __name__ == '__main__':
    nums = [-4,-1,0,3,10]
    result = [0] * len(nums)
    min = 0
    for i in range(len(nums)):
        if abs(nums[i]) < abs(nums[min]):
            min = i
    if min == 0:
        print([x ** 2 for x in result])
    else:
        forward = min
        back = min - 1
        result = [0] * len(nums)
        print(forward, back)
        i = 0
        while i < len(nums):
            if abs(nums[back]) >= abs(nums[forward]):
                result[i] = nums[forward]
                if forward + 1 < len(nums):
                    forward += 1
            else:
                result[i] = nums[back]
                if back - 1 >= 0:
                    back -= 1
            i += 1
        print([x ** 2 for x in result])

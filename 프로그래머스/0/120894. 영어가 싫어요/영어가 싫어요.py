def solution(numbers):
    num_eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    nums = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(10):
        numbers = numbers.replace(num_eng[i],nums[i])
    return int(numbers)
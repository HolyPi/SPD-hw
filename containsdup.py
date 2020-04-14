#Given a list of n numbers, determine if it contains any duplicate numbers.

def containsDuplicate(nums):
    dic = {}
    for num in nums:
        if num in dic:
            return True
        else:
            dic[num] = 1
    return False


nums = [1, 2, 3, 1]
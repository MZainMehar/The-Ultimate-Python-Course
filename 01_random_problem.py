# Type: Random problem


def solution (numbers, pivot):
    new_list = []

    for number in numbers:
        if (number == 0):
            new_list.append(0)
        elif (number < 0 and pivot < 0 ):
            new_list.append(1) 

        elif (number > 0 and pivot > 0 ):
            new_list.append(1)

        else:
            new_list.append(0)

    return new_list


# Test cases

numbers = [1, 2, -3, 4, 5]
pivot = -2

print(solution(numbers, pivot)) # [0, 0, 1, 0, 0]
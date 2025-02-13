
def rec_list_sum(numbers: list[int]) -> int:
    if len(numbers) == 1:
        return numbers[0]
    return numbers.pop() + rec_list_sum(numbers)

# def rec_list_sum2(numbers: list[int]) ->int:
#     if not numbers:
#         return 0
#     return numbers[0] + rec_list_sum2(numbers[1:])


def count_char_rec(string: str, char: str) -> int:
    if len(string) == 0:
        return 0
    # result = 0
    # if string[0] == char:
    #     result = 1
    return (string[0] == char) + count_char_rec(string[1:], char)


def fibonachi_rec(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n < 1:
        return "cislo n musi byt vetsi nez 0"
    else:
        return fibonachi_rec(n-1) + fibonachi_rec(n-2)


if __name__ == "__main__":
    print(f"sum list[5, 3, 6, 9]: {rec_list_sum([5, 3, 6, 9])}")
    print(f"sum list[5, 3, 6, 9]: {rec_list_sum([5, 3, 6, 9])}")
    print(f'count char: {count_char_rec("Ahoj, a a a nic", "a")}')
    print(f'count char: {count_char_rec("Ahoj, a a a nic", "A")}')
    print(f'count char: {count_char_rec("Ahoj, a a a nic", "n")}')
    print(f'count char: {count_char_rec("Hello", "l")}')
    print(f'fibonachi: {fibonachi_rec(5)}')


def find_max_occurred_alphabet(string):

    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        # index 0 -> alphabet_occurrence 3
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence
    # print(max_alphabet_index)
    # a의 인덱스를 구했던 방법
    # a -> 0을 구하기 위해
    # a -> ord(a) -> 97 - ord(a) = 0
    # 그렇다면 다시 0을 a로 보내려면??
    # 0 -> a
    # 0 -> 0 + ord(a) -> 97 -> chr(97) -> a

    max_alphabet = chr(max_alphabet_index + ord("a"))

    return max_alphabet


print("정답 = a 현재 풀이 값 =", find_max_occurred_alphabet("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", find_max_occurred_alphabet("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", find_max_occurred_alphabet("best of best sparta"))
def is_palindrome(word):
    # 코드를 입력하세요.
    word_list = list(word)
    # word_list.reverse()
    revers_list = word_list[::-1]

    if word_list == revers_list:
        return True
    else:
        return False

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
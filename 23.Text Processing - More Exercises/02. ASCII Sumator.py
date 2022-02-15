ch1_ascii_num = ord(input())
ch2_ascii_num = ord(input())
input_string = input()

sum_of_ascii = sum([ord(x) for x in input_string if ch1_ascii_num < ord(x) < ch2_ascii_num])

print(sum_of_ascii)
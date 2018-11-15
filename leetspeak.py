leet_chars = ['A', 'E', 'G', 'I', 'O', 'S', 'T', 'B']
leet_nums = ['4', '3', '6', '1', '0', '5', '7', '8']

string = raw_input('gimme a phrase to leet: ')
string_to_upper = string.upper()
leeted_string = list(string_to_upper)
string_list = list(string_to_upper)

for i in range(0, len(string_list)):
    for j in range(0, len(leet_nums)):
        if string_list[i] == leet_chars[j]:
            leeted_string[i] = leet_nums[j]
print ''.join(leeted_string)

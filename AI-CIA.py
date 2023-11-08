def manipulate_strings(string, string_list):
    while string_list:
        found = False
        for i, s in enumerate(string_list):
            if s in string and s != string_list[-1]:
                continue
            else:
                if string.endswith(s[:2]):
                    string += s[2:]
                    string_list.pop(i)
                    found = True
                    break
                elif s.endswith(string[:2]):
                    string = s + string[2:]
                    string_list.pop(i)
                    found = True
                    break
                elif string == '':
                    string = s
                    string_list.pop(i)
                    found = True
                    break

        if not found:
            missing_items = [item for item in string_list if item not in string]
            return string, missing_items

    return string, []

resultant_string = ''
string_list = ['U_CH', 'CHEN', 'NAI.', 'SNU_', 'ENNA', 'ANY']
result, missing = manipulate_strings(resultant_string, string_list)
print(result, missing)

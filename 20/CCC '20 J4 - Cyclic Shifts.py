text = input()
string = input()
yes_or_no = False

# for x in range(len(text)-(len(string)-1)):
#     if sorted(text[x:len(string)+x]) == sorted(string):
#         print("yes")
#         yes_or_no = True
#         break
#
# if yes_or_no == False:
#     print("no")

string_len = len(string)
for x in range(string_len):
    if string in text:
        print("yes")
        yes_or_no = True
        break
    string = string[1:] + string[0]

if not yes_or_no:
    print("no")
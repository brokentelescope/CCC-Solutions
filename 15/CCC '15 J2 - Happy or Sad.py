text = input()
if text.count(":-)") + text.count(":-(") > 0:
    if text.count(":-)") > text.count(":-("):
        print("happy")
    elif text.count(":-)") < text.count(":-("):
        print("sad")
    elif text.count(":-)") == text.count(":-("):
        print("unsure")
    else: 
        print("none")
else:
    print("none")
your_name  = input("enter your name: ")
lover_name = input("enter your lover name: ")
combine_name = (your_name + lover_name)
lower_case_string = combine_name.lower()
t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')
true = t+r+u+e
l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')
love = l+o+v+e
lower_case_string = combine_name.upper()
t = lower_case_string.count('T')
r = lower_case_string.count('R')
u = lower_case_string.count('U')
e = lower_case_string.count('E')
true = t+r+u+e
l = lower_case_string.count('L')
o = lower_case_string.count('O')
v = lower_case_string.count('V')
e = lower_case_string.count('E')
love = l+o+v+e
love_score =  int(str(true)+str(love))
if love_score >= 80 or love_score > 90:
    print(f" your love pecentage is {love_score}\n you both are loyal relatioship")
elif love_score >= 50 and love_score <= 80:
    print(f" your love percentage is {love_score}\n you both are happy")
else:
    print(f" no love you need {love_score}\n breakup")

    



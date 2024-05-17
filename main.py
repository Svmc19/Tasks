# Task1
# string = input("Enter a word:")
# def stutter(string):
#     lower = string.lower()
#     for x in lower:
#         if len(string) != 1:
#             join_word = lower[:2] + "... " + lower[:2] + "... "
#             join_word += lower + "?"
#             return join_word
#         else:
#             return "It's just only letter and easy to read!"
# print(stutter(string))


# Task2
# input1 = input("Darth Vader / Leia / Han / R2D2\n""Who can't you remember?:")
# def relation_to_luke(input1):
#     relations = {
#         "Darth Vader": "father",
#         "Leia": "sister",
#         "Han": "brother in law",
#         "R2D2": "droid"
#     }
#     for x in relations:
#         if x == input1:
#             return f"Luke, I'm your {relations[x]}."
#     return "Luke hasn't got a relation with this name?!"
#
# print(relation_to_luke(input1))

#Task3
# mood = input("mood:")
# def moods(mood):
#     if mood == "":
#         return "Today i'm feeling neutral!"
#     return "Today i'm feeling {}!".format(mood)
# print(moods(mood))

# # #Task4
# word = input("Enter a word:")
# def count_vowels(word):
#     m = "aeiou"
#     word_lower = word.lower()
#     count = 0
#     for letter in word_lower:
#         if letter in m:
#             count += 1
#     return f"This word has {count} vowel(s)!"
#
# print(count_vowels(word))

# Task5
# input1 = input("Enter a single character:")
# def counterpartCharCode(input1):
#     upper = 65
#     lower = 97
#     if input1.isupper():
#         return lower
#     elif input1.islower():
#         return upper
#     else:
#         return input1
#
# print(counterpartCharCode(input1))

# # Task6
# word = input("enter:")
# def replace(word):
#     vowels = "a,e,i,o,u"
#     word_lower = word.lower()
#     strip = word_lower.strip()
#     for z in vowels:
#         if z in strip:
#             j = "#"
#             return strip.replace(z,j)
# print(replace(word))

# # Task7----------------------------------------
# card_num = input("Enter your credit card number:")
# def card_hide(card_num):
#      if card_num.isdigit():
#          strip = card_num.strip()
#          if len(strip) == 16:
#              sim = "*"
#              o = strip[:12]
#              return strip.replace(o,sim)
#          else:
#              return "Error!"
#
# print(card_hide(card_num))

# Task8
# def hamming_distance(str1,str2):
#     lst = []
#     for x in str1:
#         if len(str1) == len(str2):
#             if x in str2:
#                 lst.append(str1.count(x))
#     return len(str1) - sum(lst)
#
# print(hamming_distance('abcdeg','bcdefi'))
# print(hamming_distance('strong','strung'))
# print(hamming_distance('cut','cut'))


# Task9----------------------------------------

# def string(string1):
#    lst = []
#    l = list(string1)
#    lst.append(l)
#    p = lst.pop(-1)
#    lst.append(p)
#
# print(string("Donald Trump"))
# print(string("Milly Bobby"))

# Task10------------------------------
# def double_char(string):
#    for x in string:
#         return x*2
#
# print(double_char("String"))
# print(double_char("Hello world!"))
# print(double_char("1234!_"))

# Task11
# def st(lst):
#     result = 0
#     for x in lst:
#         d = len(x)
#         result+=d
#     return result

# print(st(["###","###","###"]))
# print(st(["222222","222222","222222"]))
# Task12
# def string(up):
#     lst = []
#     for x in up:
#         if x.isupper():
#             lst.append(up.index(x))
#     return lst
#
# print(string("eDaBiT"))
# print(string("sUn"))
# print(string("UeStenO"))
# print(string("determine"))







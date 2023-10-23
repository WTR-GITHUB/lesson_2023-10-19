text = "In this lecture we will review some additional functionalities of python built-in data structures."
# i = 0
# for leter in text:
#     if leter == "e":
#         i += 1
# print(f"Radziu 'e' tekste yra: {i}")

my_leters = [i for i, v in enumerate(text, start=1) if v == "e"]
print(f"Radziu 'e' tekste yra: {len(my_leters)}")

# word_list = text.split(" ")

# my_words = [i for i, v in enumerate(text.split(" "), start=1) if len(v) > 5]
my_words = [word for word in text.split() if len(word) > 5]
print(f"Zodziu ilgesniu nei 5 simboliai yra: {len(my_words)}") 

# text = text.replace(" ", "")
# text = text.replace("-", "")
# text = text.replace(".", "")
text = text.lower()
my_dict = {}

for leter in text:
    if leter.isalpha():
        if leter in my_dict.keys():
            my_dict[leter] += 1
        else:
            my_dict[leter] = 1
# my_dict = sorted(my_dict.items())

# print({key : value for key, value in my_dict})
maximum = max(my_dict, key=my_dict.get)
print(maximum, my_dict[maximum])
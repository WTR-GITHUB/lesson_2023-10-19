from typing import List, Dict
import random

sentences = "A bridge is a structure built to span a physical obstacle (such as a body of water, valley, road, or railway) without blocking the way underneath. It is constructed for the purpose of providing passage over the obstacle, which is usually something that is otherwise difficult or impossible to cross. There are many different designs of bridges, each serving a particular purpose and applicable to different situations."

def split_object(text: str, char: str) -> List[str]:
    separate = [item for item in text.split(char) if item !=""]
    return separate

def clear_words(text: str) -> List[str]:
    unique_chars: List[str] = ["!","@","#","$","%","^","&","*","_","+","-","(",")","[","]","{","}",
                               "?","<",">",",",".","1","2","3","4","5","6","7","8","9","0"]   
    return [word for word in split_object(text, " ") if not any(simb in word for simb in unique_chars)]
    
def creat_dictionary(sentence: List[str]) -> Dict[str, List[str]]:
    sort_iteration = {"long_word" : [word for word in sentence if len(word) > 9],
                      "medium_word" : [word for word in sentence if len(word) <= 9 and len(word) >=5],
                      "short_word": [word for word in sentence if len(word) < 5]}
    return sort_iteration

def sort_words(few_sentences: List[str], position: int) -> List[Dict[str, List[str]]]:
    i = 0
    for sentence in few_sentences:        
        few_sentences[i] = creat_dictionary(clear_words(sentence))
        i +=1 
    return few_sentences[position]

def most_common_letter(text: str) -> str:
    my_dict = {}
    for leter in text:
        if leter.isalpha():
            if leter in my_dict.keys():
                my_dict[leter] += 1
            else:
                my_dict[leter] = 1
    maximum = max(my_dict, key=my_dict.get)
    return (maximum, my_dict[maximum])

# quantity_sentences = len(split_object(sentences, "."))
# if quantity_sentences >= 3:
#     a = 0
#     while a < quantity_sentences:        
#         test: Dict = sort_words(split_object(sentences, "."), a)
#         sk = 0
#         for key, value in test.items():
#             sk = sk + len([item for item in value])
#         s1 = (len(test["long_word"]) / sk)
#         s2 = (len(test["medium_word"]) / sk)
#         s3 = (len(test["short_word"]) / sk)
#         print("{:.0%}".format(s1), "{:.0%}".format(s2), "{:.0%}".format(s3))
#         print(most_common_letter(split_object(sentences, ".")[a]), "\n")
#         a += 1
# else:
#     print(f"You entered {quantity_sentences} sentences it is not enaught")


test_dikt = creat_dictionary(clear_words(sentences))
print(test_dikt)
fdgf = []
random.choice()
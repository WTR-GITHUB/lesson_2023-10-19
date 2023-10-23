from typing import List, Dict
import random

sentences = "A bridge is a structure built to span a physical obstacle (such as a body of water, valley, road, or railway) without blocking the way underneath. It is constructed for the purpose of providing passage over the obstacle, which is usually something that is otherwise difficult or impossible to cross. There are many different designs of bridges, each serving a particular purpose and applicable to different situations."

def split_object(text: str, char: str) -> List[str]:
    separate = [item for item in text.split(char) if item !=""]
    return separate

def split_clear_words(text: str) -> List[str]:
    unique_chars: List[str] = ["!","@","#","$","%","^","&","*","_","+","-","(",
                               ")","[","]","{","}","?","<",">",",",".","1","2",
                               "3","4","5","6","7","8","9","0"]
       
    return [word for word in split_object(text, " ")
            if not any(simb in word for simb in unique_chars)]
    
def creat_dictionary(sentence: List[str]) -> Dict[str, List[str]]:
    sort_sentence = {"long_word" : [word for word in sentence 
                                     if len(word) > 9],
                      "medium_word" : [word for word in sentence 
                                       if len(word) <= 9 and len(word) >=5],
                      "short_word": [word for word in sentence 
                                     if len(word) < 5]}
    return sort_sentence

def most_common_letter(text: str) -> str:
    letter_dict = {}
    for leter in text:
        if leter.isalpha():
            if leter in letter_dict.keys():
                letter_dict[leter] += 1
            else:
                letter_dict[leter] = 1
    maximum = max(letter_dict, key=letter_dict.get)
    return (maximum, letter_dict[maximum])

def count_word_statistics(sentence_dict: Dict):
    total_words = 0
    for key, value in sentence_dict.items():
            total_words = total_words + len([item for item in value])
    return total_words
   
# def data_store(one_sent, i, in_data):
#     data = {"Sentence": i+1,
#             "long_word": len(one_sent["long_word"]),
#             "medium_word": len(one_sent["medium_word"]),
#             "short_word": len(one_sent["short_word"])}
#     return out_data

#================= THIS IS THE END OF FUNCTION DEFINITION =====================

quantity_sentences = len(split_object(sentences, "."))
if quantity_sentences >= 3:

    iterator = 0
    for sentence in split_object(sentences, "."):
        one_sentence = (creat_dictionary(split_clear_words(sentences)))
        total_words = count_word_statistics(one_sentence)
        s1 = len(one_sentence["long_word"]) / total_words
        s2 = len(one_sentence["medium_word"]) / total_words
        s3 = len(one_sentence["short_word"]) / total_words
        print(f"Sentence {iterator+1} has: ")
        print(" Long words: {:.0%}\n".format(s1),
              "Medium words: {:.0%}\n".format(s2),
              "Short words: {:.0%}".format(s3))
        print("Most common letter: ",most_common_letter(split_object(sentences, ".")[iterator]),"\n")
        # sentence_data = data_store(one_sentence, iterator, data)
        # iterator += 1

def data_store(one_sent, i, in_data):
    data = {"Sentence": i+1,
            "long_word": len(one_sent["long_word"]),
            "medium_word": len(one_sent["medium_word"]),
            "short_word": len(one_sent["short_word"])}
    return out_data


full_dictionary = (creat_dictionary(split_clear_words(sentences)))
    # print(full_dictionary)
else:
    print(f"You entered {quantity_sentences} sentences it is not enaught")



# random.choice()
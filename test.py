from typing import List, Dict

sentences = "A bridge is a structure built to span a physical obstacle (such as a body of water, valley, road, or railway) without blocking the way underneath. It is constructed for the purpose of providing passage over the obstacle, which is usually something that is otherwise difficult or impossible to cross. There are many different designs of bridges, each serving a particular purpose and applicable to different situations."

def split_opject(txt: str, char: str):
    separate = [item for item in txt.split(char) if item !=""]
    return separate

def sort_words(few_sentences: List[str]) -> List[Dict[str, List[str]]]:
    unique_chars: List[str] = ["!","@","#","$","%","^","&","*","_","+","-","(",")","[","]","{","}",
                               "?","<",">",",","1","2","3","4","5","6","7","8","9","0"]
    i = 0
    for sentence in few_sentences:        
        few_sentences[i] = [word for word in split_opject(sentence, " ") if not any(simb in word for simb in unique_chars)]
        few_sentences[i]:Dict[str, List[str]] = {"long_word" : [word for word in few_sentences[i] if len(word) > 9],
                                                 "medium_word" : [word for word in few_sentences[i] if len(word) <= 9 and len(word) >=5],
                                                 "short_word": [word for word in few_sentences[i] if len(word) < 5]}
        i +=1 
    return few_sentences


  


# if len(split_sentence(sentences, ".")) >= 3:
#     print(f"You entered {len(split_sentence(sentences, "."))} sentences")
# else:
#     print(f"You entered {len(split_sentence(sentences, "."))} sentences it is not enaught")

print(sort_words(split_opject(sentences, ".")))
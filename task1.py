from typing import List

simbol = input("Please enter words with spec simbol: ")

def find_word(in_text: str) -> List[str]:
    unique_chars: List[str] = ["!","@","#","$","%","^","&","*","_","+","-"]
    splited_words: List[str] = in_text.split(" ")
    unique_words: List[str] = [word for word in splited_words if any(simb in word for simb in unique_chars)]
    return unique_words

print(find_word(simbol))

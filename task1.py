from typing import Optional, List

simbol = input("Please enter string with spec simbol: ")

def pick_spec_simb(in_string: str) -> Optional(str):
    spec_simb = ""
    chars: List[str] = ["!","@","#","$","%","^","&","*","_","+","-"]
    for simb in in_string:
        for char in chars:
            if simb == char:
                spec_simb: Optional(str) = str(spec_simb) + str(simb)
    return spec_simb

print(pick_spec_simb(simbol))
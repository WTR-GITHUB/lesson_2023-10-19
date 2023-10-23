quantity_sentences = len(split_object(sentences, "."))
if quantity_sentences >= 3:
    iterator = 0
    all_sentences = []
    for sentence in split_object(sentences, "."):
        all_sentences.append(creat_dictionary(split_clear_words(sentences)))
    while iterator < quantity_sentences:        
        one_sentence: Dict = all_sentences[iterator]
        total_words = count_word_statistics(one_sentence)
        s1 = len(one_sentence["long_word"]) / total_words
        s2 = len(one_sentence["medium_word"]) / total_words
        s3 = len(one_sentence["short_word"]) / total_words
        print(f"Sentence {iterator+1} has: ")
        print(" Long words: {:.0%}\n".format(s1),
              "Medium words: {:.0%}\n".format(s2),
              "Short words: {:.0%}".format(s3))
        print("Most common letter: ",most_common_letter(split_object(sentences, ".")[iterator]),"\n")
        iterator += 1
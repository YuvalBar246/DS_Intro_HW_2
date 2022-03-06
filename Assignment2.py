#Yuval Bar
#206011355

##Task 1
def reverse(sentence, word):
    if type(word) == str:
        new = ""
        new_word = word[::-1]
        if word in sentence.split():
            word_index = sentence.find(word)
            before = sentence[:word_index]
            after = sentence[(word_index + len(word)):]
            new = before + new_word + after
            sentence = sentence[word_index + len(word):]
            return new.lstrip()
        else:
            return "The word was not found"
    else:
        return "invalid input"

# Exercice 1

###############################################################################
# Question 1
###############################################################################

def the_word_is_here(text, word, i):
    """ Précondition : i <= len(t) - len(w)
        Returns True if w[0] == t[i] et w[1] == t[i + 1] and ... and w[len(w) - 1] == t[i + len(w) - 1]
        else, retruns False
    """
    j = 0
    while j < len(word) and word[j] == text[i + j]:
        j = j + 1
    if j == len(word):
        return True
    else:
        return False






def look_for_word(text, word):
    """ Returns the smallest index i so that :
                     t[i] == w[0] et t[i + 1] == w[1] et ... et t[i + len(w) - 1] == w[len(w) - 1]
        Returns -1 if this index doesn't exist
    """
    i = 0
    while i <= len(text) - len(word) and not le_word_est_ici(text, word, i):
        i += 1
    if i > len(text) - len(word):
        return -1
    else:
        return i

#  tests

text = list('Je suis en BCPST en 1ère année')
word = list('en')
word2 = list('easdf')

assert look_for_word_word(text, word) == 8
assert look_for_word(text, word2) == -1


###############################################################################
# Question 2
###############################################################################

def modify_word(text, word, i):
    """ Precondition : index <= len(text) - len(word)
        Returns text2, a copy of text, except for:
        text2[index] == word[0], text2[index+1] == word[1], etc
    """

    a=0
    b=0
    while a <= len(text)-len(word):
        a+=1
        while b < len(word):
            text[i]=word[b]
            b+=1
            i+=1
    return text



#  tests
text = list('Je suis en BCPST en 1ère année')
word = list('ne')
text2 = list('Je suis ne BCPST en 1ère année')

assert modify_word(text, word, 8) == text2



###############################################################################
# Question 3
###############################################################################


def look_for_and_replace(text, word1, word2):
    """ Précondition : len(word1) == len(word2)
        Returns text where word1 has been replaced by word2
        Returns text if word1 is not in the text"""










#Test
text = list('Je suis en BCPST en 1ère année')
word2 = list('ne')
word1 = list('en')
text2 = list('Je suis ne BCPST en 1ère année')





assert look_for_and_replace(text, word2, word2) == text
#assert look_for_and_replace(text, word1, word2) == text2


###############################################################################
# Question 4
###############################################################################


def look_for_and_replace_all(text, word1, word2):
    """ Returns a liste of caractères where all the word1 have been replaced by word2
    """









# Test

text = list('Je suis en BCPST en 1ère année')
word2 = list('ne')
word1 = list('en')
text2 = list('Je suis ne BCPST ne 1ère année')

#assert look_for_and_replace_all(text, word1, word2) == text2

###############################################################################
# Question 5
###############################################################################


def modify_word2(text, word, index1, taille):
    """ Précondition : index <= len(text) - taille
        Returns text2, a copy of text,
        where the list of characters of the lenght 'lenght' by the list of the chains of caracters word''










# Test

text = list('Je suis en BCPST en 1ère année')
word = list('encore en')
text2 = list('Je suis encore en BCPST en 1ère année')

#assert modify_word2(text, word, 8, 2) == text2


###############################################################################
# Question 6
###############################################################################

def look_for_and_replace_all2 (text, word1, word2):
    """ Retourne a list of chains of caracters where the occurrences of word1
        have been replaced by the occurrences of word2
    """







# Tests
text = list('Je suis en BCPST en 1ère année')
word2 = list('none')
word1 = list('en')
text1 = list('Je suis en BCPST en 1ère année')
text2 = list('Je suis none BCPST none 1ère année')

#assert look_for_and_replace_all2(text1, word1, word2) == text2

word3 = list('encore en')
text3 = list('Je suis encore en BCPST encore en 1ère année')

#assert look_for_and_replace_all2(text1, word1, word3) == text3





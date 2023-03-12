

import spacy

file1 = open("mostcommon.txt", "r")
nlp = spacy.load("en_core_web_sm")
doc = nlp(file1.read())

thisdic = {}
for token in doc:
    if("SPACE" not in token.text and "\n" not in token.text ):
        thisdic = {
        token.text.lower() : [token.lemma_.lower(), token.pos_.lower(), token.tag_.lower(), token.dep_.lower(), token.shape_, token.is_alpha, token.is_stop]
        }
        # print(thisdic)
string = "8:00AM"
string2 = "8:00"
string3 = "12:00PM"

print(string.isdigit())
print(string2.isdigit())
print(string3.isdigit())


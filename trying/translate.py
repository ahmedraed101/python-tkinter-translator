from googletrans import Translator
from sys import argv

ts = Translator()
word = ts.translate(argv[1], dest="ar")

# print(word)
print(word.text)
# print(word.src)
# print(word.dest)
# print(word.pronunciation)
# print(word.origin)
# print(word.extra_data)

what_lang = ts.detect("تعالى إلى هنا")
print(what_lang)
print(dir(what_lang))

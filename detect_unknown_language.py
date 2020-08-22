# pip install langdetect

from langdetect import detect

text= input("Enter text to detect Language: ")
detect_lang= detect(text)

print(f'Your Type is {detect_lang} Language')

input()
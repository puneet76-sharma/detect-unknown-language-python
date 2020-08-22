# pip install langdetect

# detect-unknown-language-python
Language detection algorithm is non-deterministic, which means that if you try to run it on a text which is either too short or too ambiguous, you might get different results everytime you run it.


from langdetect import detect
detect("War doesn't show who's right, just who's left.")
'en'
detect("Ein, zwei, drei, vier")
'de'


To enforce consistent results, call following code before the first language detection:

from langdetect import DetectorFactory
DetectorFactory.seed = 0

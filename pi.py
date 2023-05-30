text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

words = text.split()
wordss = list(map(len, words))
wordsss = map(str, wordss)
wordssss = ''.join(wordsss)
print(wordssss)
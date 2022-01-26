import time
from spellchecker import SpellChecker
spell = SpellChecker() 

# load dictionary words from file
def load_words():
  all_words = []
  start_time = time.time()
  
  with open('safedict_simple.txt', 'r') as f:
    for line in f:
      all_words.append(line.rstrip())
  end_time = time.time()

  elapsed_time = end_time - start_time
  # log words loaded and elapsed time
  print('Loaded ' + str(len(all_words)) + ' words in ' + f'{elapsed_time:.2f}' + ' seconds.')

  return all_words


def suggest(text, all_words):
  # YOUR CODE HERE. This currently doesn't suggest a correction, just checks if the input is already a word. You'll want to change that
  word_split = text.split(" ")
  if len(word_split) > 1:
    for word in word_split: 
      if word in all_words:
        print(text + ' is correctly spelled!')
      else:
        misspelled = word
        print("Do you mean " + str(spell.candidates(misspelled)) + " ?")  
  else:
    if text in all_words:
      print(text + ' is correctly spelled!')
    else:
      misspelled = text
      print("Do you mean " + str(spell.candidates(misspelled)) + " ?")  


def main():
  print("Hello")
  all_words = load_words()
  print('Type some text, or type \"quit\" to stop')
  while True:
      text = input(':> ')
      if ('quit' == text):
        break
      suggest(text, all_words)

if __name__ == "__main__":
  print("Hello")
  main()

#Resource - https://www.geeksforgeeks.org/spelling-checker-in-python/
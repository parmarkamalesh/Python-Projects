# Word replacement app

def replace_word():

  str = "Hi guys, I am kamalesh, and I like to make you my buddy"
  word_to_replace = input("Enter the word to replace: ")
  word_replacement = input("Enter the word replacement: ")
  print(str.replace(word_to_replace, word_replacement))


replace_word()
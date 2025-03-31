#Use Python's re module to find all occurrences of the word "Python" in a given text.

import re

def find_python_occurrences(text):
  
  pattern = r'\bPython\b' 
  matches = re.finditer(pattern, text)
  return [match.start() for match in matches]

text = "I love learning Python. Python is a powerful language. Let's learn Python!"
occurrences = find_python_occurrences(text)

if occurrences:
  print(f"Found {len(occurrences)} occurrences of 'Python':")
  for index in occurrences:
    print(f" - at index {index}")
else:
  print("No occurrences of 'Python' found.")

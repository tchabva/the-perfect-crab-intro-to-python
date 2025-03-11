# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging than the example.

# Write a function that takes a list of words and returns a report of all the
# words that are longer than 10 characters but don't contain a hyphen. If those
# words are longer than 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  list_one = words_with_at_least_ten_characters(words)
  list_two = remove_words_with_hyphens(list_one)
  list_three = shorten_words_greater_than_fifteen_chars(list_two)
  result_string = concatenate_final_string(list_three)
  return result_string

def words_with_at_least_ten_characters(words):
  filtered_words = []
  for word in words:
    if len(word) > 9:
      filtered_words.append(word)
  return filtered_words

def remove_words_with_hyphens(words):
  filtered_words = []
  for word in words:
    if "-" not in word:
      filtered_words.append(word)
  return filtered_words

def shorten_words_greater_than_fifteen_chars(words):
  filtered_words = []
  for word in words:
    if len(word) < 16:
      filtered_words.append(word)
    else:
      filtered_words.append(word[0:15] + "...")
  return filtered_words

def concatenate_final_string(words):
  final_string = "These words are quite long: "
  return final_string + ", ".join(words)

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
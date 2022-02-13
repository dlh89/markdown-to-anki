import markdown
import os
import re

# questions = re.match('(?<!#)(###) (.*?)\n')
# (?<!#)(###)(?s)(.*)
# '(?<!#)(###[^###]*)'
# questions = re.match('(?s)(?<!#)(### )(.*?)(?=\n###)', css_markdown)
# questions[0]

# questions = re.match('(?<!#)(### )(.*)(?s)(.*?)(?=\n###)', css_markdown)
# questions[0]

def get_questions_and_answers(source_markdown_path):
  if not os.path.isfile(source_markdown_path):
    print('Error: file not found')
    return

  f = open(source_markdown_path, 'r')
  source_markdown = f.read()
  reference_links = re.findall('(- )(https.*)', source_markdown)
  for index, reference_link in enumerate(reference_links):
    source_markdown = source_markdown.replace(reference_link[1], f'[{reference_link[1]}]({reference_link[1]})')

  questions = re.findall('(?<!#)(### )(.*)', source_markdown)
  questions_and_answers = []

  for index, question in enumerate(questions):
    part = source_markdown.split(question[0] + question[1])
    index = index + 1 if index + 1 < len(questions) else index
    answer = part[1].split(questions[index][1])
    markdown_question = markdown.markdown(question[1], extensions=['codehilite', 'fenced_code'])
    markdown_answer = markdown.markdown(answer[0], extensions=['codehilite', 'fenced_code'])
    markdown_answer = markdown_answer.replace('href="#table-of-contents"', 'href="#answer"')
    questions_and_answers.append([markdown_question, markdown_answer])

  return questions_and_answers
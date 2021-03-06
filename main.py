import genanki
import random
import os
from parse_question_text import get_questions_and_answers

model_id = 1372816901 # generated with random.randrange(1 << 30, 1 << 31)

css = open('./css/style.css').read()
css += open('./css/third-party/pygments.css').read()

my_model = genanki.Model(
	model_id,
	'Simple Model',
	fields = [
		{'name': 'Question'},
		{'name': 'Answer'},
	],
	templates = [
		{
			'name': 'Card 1',
			'qfmt': '<div class="question" id="question"{{Question}}</div>',
			'afmt': '{{FrontSide}}<hr id="answer-hr"><div class="answer" id="answer">{{Answer}}<div>',
		},
	],
	css = css
)

basepath = 'questions-source'

questions_source_filenames = os.listdir(basepath)

for filename in questions_source_filenames:
	path = os.path.join(basepath, filename)
	if not filename.endswith('.md'):
		continue

	questions_and_answers = get_questions_and_answers(path)

	deck_id = random.randrange(1 << 30, 1 << 31) # deck ID must be unique
	print('Building a deck from ' + filename)
	deck_name = input('Please enter a name for your deck: ')

	my_deck = genanki.Deck(
		deck_id,
		deck_name
	)
	
	for question in questions_and_answers:
		note = genanki.Note(
			model = my_model,
			fields = question
		)

		my_deck.add_note(note)

	genanki.Package(my_deck).write_to_file('./generated-decks/' + deck_name + '.apkg')
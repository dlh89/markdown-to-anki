import genanki
import random
import os
from parse_question_text import get_questions_and_answers

model_id = random.randrange(1 << 30, 1 << 31) # model ID must be unique

css = """
	.card {
		font-size: 16px;
	}
"""

css_file = open('./css/pygments.css')
css += css_file.read()

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
			'qfmt': '{{Question}}',
			'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
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

	my_deck = genanki.Deck(
		deck_id,
		filename
	)
	
	for question in questions_and_answers:
		note = genanki.Note(
			model = my_model,
			fields = question
		)

		my_deck.add_note(note)

	genanki.Package(my_deck).write_to_file(filename + '.apkg')
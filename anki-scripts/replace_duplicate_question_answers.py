import collections
import anki.find

"""

Replace answers for duplicate questions with the more recent version found and delete
the more recent note entirely.

The purpose of this script is to update answer data for existing notes while maintaining
review data.

This script can be run by pasting into the Anki desktop debug console
You can open the debug console by pressing ctrl+shift+; on Windows (UK keyboard)

WARNING: Please be careful using this script as you risk losing your data. Always export
a backup of your Anki decks before using the script.

"""

noteType = 'Simple Model'
question_field = 'Question'
answer_field = 'Answer'

noteInfo = {}

duplicate_questions = anki.find.findDupes(mw.col, question_field)

print('Found {} duplicate questions'.format(len(duplicate_questions)))
answers_replaced_count = 0

for duplicate_question in duplicate_questions:
	original = mw.col.getNote(duplicate_question[1][0])
	replacement = mw.col.getNote(duplicate_question[1][1])

	# Replace original answer with replacement answer
	original[answer_field] = replacement[answer_field]
	original.flush()

	mw.col.remNotes([duplicate_question[1][1]])

	answers_replaced_count += 1

print('Replaced {} answers for duplicate questions'.format(answers_replaced_count))
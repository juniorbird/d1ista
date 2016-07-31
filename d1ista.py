import ui

qs = (
	{'question': "How was today", 'contents': "Review your day", 'questionType': "TEXTBOX"},
	{'question': "Rate Your Day", 'contents': ('☆☆☆☆☆', '★☆☆☆☆', '★★☆☆☆', '★★★☆☆', '★★★★☆', '★★★★★'), 'questionType': "PICK"},
	)
	
class TEXTBOX (ui.View):
	def __init___(self):
		text_question = 'question'
		text_entry = 'prompt'
		
	def set_question(self, questionText):
		text_question = questionText
		
	def set_contents(self, questionPrompt):
		text_entry = questionPrompt
		
	def draw(self):
		txtBox = ui.TextView
		print(txtBox)
			
theQ = qs[0]['question']
thePrompt = qs[0]['contents']
v = TEXTBOX()
#v.set_question(theQ)
v.set_contents(thePrompt)

v.present('sheet')

#v = dialogs.text_dialog(qs[0]['question'], qs[0]['contents'], spellchecking=True)

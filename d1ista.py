import dialogs

qs = (
	{'question': "How was today", 'contents': "Review your day", 'questionType': "TEXTBOX"},
	{'question': "Rate Your Day", 'contents': ('☆☆☆☆☆', '★☆☆☆☆', '★★☆☆☆', '★★★☆☆', '★★★★☆', '★★★★★'), 'questionType': "PICK"},
	)

v = dialogs.text_dialog(qs[0]['question'], qs[0]['contents'], spellchecking=True)

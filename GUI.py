from tkinter import *

#GUI
root = Tk()
window_title = root.title('Chess Engine')
title_frame = Frame(root)
button_frame = Frame(root)
welcome_text = Label(title_frame, text = 'Chess Engine')
easy_AI_button = Button(button_frame, text = 'Start Easy AI Game', bg = 'blue', fg = 'white')
medium_AI_button = Button(button_frame, text = 'Start Medium AI Game', bg = 'blue', fg = 'white')
hard_AI_button = Button(button_frame, text = 'Start Hard AI Game', bg = 'blue', fg = 'white')
title_frame.pack(side = TOP)
button_frame.pack(side = BOTTOM)
welcome_text.pack()
easy_AI_button.pack()
medium_AI_button.pack()
hard_AI_button.pack()

root.mainloop()

from tkinter import *

root = Tk()
window_title = root.title('Chess Engine')

main_window = Frame(root, height = 500, width = 750, bg = 'dodger Blue')
main_window.pack()

welcome_text = Label(main_window, text = 'TORAHZERO', font = ('Impact', 20), bg = 'dodger Blue', fg = 'Red')
welcome_text.place(relx=0.5, rely=0.1, anchor = CENTER)

easy_AI_button = Button(main_window, text = 'Start Easy AI Game', padx = 100, pady = 10, relief = FLAT, bg = 'blue', fg = 'white')
easy_AI_button.place(relx=0.5, rely=0.3, anchor = CENTER)

medium_AI_button = Button(main_window, text = 'Start Medium AI Game', padx = 100, pady = 10, relief = FLAT, bg = 'blue', fg = 'white')
medium_AI_button.place(relx=0.5, rely=0.55, anchor = CENTER)

hard_AI_button = Button(main_window, text = 'Start Hard AI Game', padx = 100, pady = 10, relief = FLAT, bg = 'blue', fg = 'white')
hard_AI_button.place(relx=0.5, rely=0.8, anchor = CENTER)


root.mainloop()
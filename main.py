from tkinter import *
from tkinter import messagebox
import pyowm
import sys
from PIL import ImageTk, Image
from pathlib import Path
import requests
import os
import urllib.request

BASE_URL = 'https://cubamia.ru/wp-content/uploads/2018/02/Kuba-avto-Almendrones-01-600x300.jpg'
BASE_SAVE_PATH = Path('./pars')
if not os.path.exists(BASE_SAVE_PATH):
	os.makedirs(BASE_SAVE_PATH)

new_file_path = BASE_SAVE_PATH / 'image.jpg'
resource = urllib.request.urlretrieve(BASE_URL, new_file_path)

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = "ru")

root = Tk() # создание главного окна
root.resizable(False, False) # сделать синхронизацию
root.title("First_program") 
root.geometry('600x300')

# создание холста
canvas = Canvas(root, width = 600, height = 300, bg = 'blue')
canvas.pack() # отображение холста

#image = Image.open('C:\\Users\\admin\Desktop\image.jpg')
image = ImageTk.PhotoImage(file = 'pars/image.jpg') # or (file = new_file_path)
canvas.create_image(300, 150, image = image, anchor = CENTER)

# виджет ввода
enter = Entry(root, width = 30)
enter.place(x = 210, y = 150)
enter.focus_set()
#enter.insert(0, 'Введите название города')

def weather(place):

	# кнопка не возвращается исправить!!!
	#button.config(state = 'normal', foreground = 'black')# почему disabled не работает

	try:
		observation = owm.weather_at_place(place)
		
		w = observation.get_weather()
		gtemp = w.get_temperature('celsius')["temp"]

		temp = Label(root, text = 'Сейчас в городе ' + place + ' ' + str(gtemp) + ' градусов', width = 50)
		temp.place(x = 125, y = 70)

	except:
		messagebox.showerror('Ошибка', 'Попробуй другой город!')
		enter.delete(0, END)

#	button.config(state = 'normal')

button = Button(root, text = 'Узнать погоду', width = 20)
#button.focus_set()
#button.focus_force()
#button.after(100, lambda: button.focus_force())
button.place(x = 230, y = 200)
button.bind('<ButtonRelease-1>', lambda event: weather(enter.get()))# западает только для <button-1>
root.bind('<Return>', lambda event: weather(enter.get()))

root.mainloop()
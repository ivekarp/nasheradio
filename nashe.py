#! /usr/bin/env python
# -*- coding: utf-8 -*-

import vlc
import time
import json
import urllib
import requests
import webbrowser
from termcolor import colored
import logo
try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk
from tkinter import messagebox

#VERSION
VERSION = '1.1'

#FUNCTIONS
#----------------------------------------
#Play the media
def play():
	player.play()
	print('Вы слушаете "НАШЕ Радио"')

#Stop the media
def stop():
	player.stop()
	print('Радио остановлено')

#Closing app
def close():
	if messagebox.askyesno("Выход","Выйти из программы?"):
		root.destroy()

#About
def about():
	#singer and name of song
	singer_url = 'https://metanashe.hostingradio.ru/current.json'
	try:
		response = urllib.urlopen(singer_url)
		data = json.loads(response.read())
	except AttributeError:
		response = requests.get(singer_url)
		data = json.loads(response.text)
	singer = data["artist"]
	song = data["title"]
	messagebox.showinfo("Кто поёт?",singer+" - "+song)
	who_sings(singer,song)
	
def who_sings(singer,song):
	print(colored("В эфире: ",'green'))
	print(colored(singer+" - "+song,'white','on_green',attrs=['bold']))

#email_link
def callback(url):
	webbrowser.open_new(url)
	
#----------------------------------------

#creating window
root = tk.Tk()
root.title('НАШЕ Радио '+VERSION)
root.geometry('428x114+708+238')
root.resizable(False,False)

#icon

#Logo
logo.print_logo()

#radio url
radio_url = 'http://nashe1.hostingradio.ru:80/nashe-128.mp3'

#menubar
menubar = tk.Menu()
root.config(menu=menubar)
appmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Меню",menu=appmenu)
appmenu.add_command(label="Кто поёт?",command=about)
appmenu.add_command(label="Выйти",command=close)

#define VLC instance
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

#Define VLC player
player=instance.media_player_new()

#Define VLC media
media=instance.media_new(radio_url)

#Set player media
player.set_media(media)
	
#Buttons
#----------------------------------------
button_play = tk.Button(text='Включить',command=play)
button_play.grid(row=0,column=0)

button_stop = tk.Button(text='Остановить',command=stop)
button_stop.grid(row=0,column=1)
#----------------------------------------

#Text
#----------------------------------------
about_app = tk.Label(root,text='Онлайн-радио радиостанции "НАШЕ Радио"\n\nРазработчик - Иван Карпов') 
about_app.grid(row=2,column=0)
email = 'vanhelsing66677@gmail.com'
email_label = tk.Label(root,text=email,fg="green",cursor="hand2")
email_label.grid(row=3,column=0)
email_label.bind("<Button-1>",lambda e: callback("mailto:vanhelsing66677@gmail.com"))


#----------------------------------------

#Sleep for 5 sec for VLC to complete retries.
time.sleep(5)

#Get current state.
state = str(player.get_state())

#Find out if stream is working.
if state == "vlc.State.Error" or state == "State.Error":
	print('Stream is dead. Current state = {}'.format(state))
	player.stop()
else:
	print('Stream is working. Current state = {}'.format(state))

root.mainloop()

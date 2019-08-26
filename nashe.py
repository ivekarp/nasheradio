#! /usr/bin/env python
# -*- coding: utf-8 -*-

import vlc
import time
import json
import urllib
import requests
import webbrowser
from termcolor import colored
from bs4 import BeautifulSoup as bs
from random import choice
import logo

try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk
from tkinter import messagebox

#VERSION
VERSION = '1.2'

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
	try:
		singer = data["artist"]
		song = data["title"]
		singer_and_song = str(singer)+' - '+str(song)
		messagebox.showinfo("Кто поёт?",singer_and_song)
		who_sings(singer_and_song)
	except KeyError:
		print('"Московский" сервер не передал информацию!')
		print('Подключаемся к Питеру...')
		singer_url = 'https://meta.fmgid.com/stations/nashespb/current.json'
		try:
			response = urllib.urlopen(singer_url)
			data = json.loads(response.read())
		except AttributeError:
			response = requests.get(singer_url)
			data = json.loads(response.text)
			try:
				singer = data["artist"]
				song = data["title"]
				singer_and_song = str(singer)+' - '+str(song)
				messagebox.showinfo("Кто поёт?",singer_and_song)
				who_sings(singer_and_song)
			except KeyError:
				pass

def who_sings(singer_and_song):
	print(colored("В эфире: ",'green'))
	print(colored(singer_and_song,'white','on_green',attrs=['bold']))

#email_link
def callback(url):
	webbrowser.open_new(url)

#news
def show_news():
	news_color = ['green','magenta','cyan','white']
	news_back_color = ['on_red','on_yellow','on_blue']
	news_window = tk.Tk()
	news_window.title('Новости')
	url = 'https://www.nashe.ru/news/'
	news_list = []
	html = requests.get(url).text
	soup = bs(html,'lxml')
	news = soup.find_all('div',{'class':'b__item b__item_with_overlay'})
	for n in news:
		news_title = n.find('div',{'class':'post__title'})
		news_link = n.find('a',{'class':'post'})
		print(colored(news_title.text,choice(news_color),choice(news_back_color),attrs=['bold']))
		print(colored(news_link.get('href'),choice(news_color),choice(news_back_color),attrs=['bold']))
		news_list.append({'title':news_title.text,'link':news_link.get('href')})
	for i in range(len(news_list)):
		text = tk.Label(news_window,text=news_list[i].get('title'))
		text.grid(row=i,column=0)
		#href = tk.Label(news_window,text=str(news_list[i].get('link')),fg="green",cursor="hand2")
		#href.bind("<Button-1>",lambda e: callback(str(news_list[i].get('link'))))
		#href.grid(row=i,column=1)
		#print(news_list[i].get('link'))

		#tk.Label(news_window,text=news_list[i].get('link')).grid(row=i+1,column=0)
	news_window.mainloop()


#----------------------------------------

#creating window
root = tk.Tk()
root.title('НАШЕ Радио '+VERSION)
root.geometry('428x114+708+238')
root.resizable(False,False)

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
appmenu.add_command(label="Новости",command=show_news)
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
button_play = tk.Button(text='Включить',command=play,cursor="hand2")
button_play.grid(row=0,column=0)

button_stop = tk.Button(text='Остановить',command=stop,cursor="hand2")
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

from kivy.lang import Builder
from kivymd.app import MDApp
import csv
import random
import geocoder
import folium
from geopy.geocoders import Nominatim
from geopy.point import Point
main_database = []


with open("data_randomized.csv","r",encoding="UTF-8") as f:
	for i in f:
		main_database.append(i.strip().split(";"))


class MainApp(MDApp):

	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('swiper2.kv')
	# Swipe Left
	def on_swipe_left(self):
		self.root.ids.label_widget.text = "You Swiped yes!"
		# put the data in the right database
		self.go_next()

	# Swipe Right
	def on_swipe_right(self):
		self.root.ids.label_widget.text = "You Swiped No!"
		#put the data in the right database
		self.go_next()


	def go_next(self):
		#if database is not empty, load next data
		self.root.ids.data.text = "\n".join(random.choice(main_database))

	def find_location_auto(self):
		geolcator = Nominatim(user_agent="test")
		my_ip = geocoder.ip('me')
		my_adress = my_ip.latlng
		location = geolcator.reverse(Point(my_adress[0],my_adress[1]))
		self.find_location()

	def find_location(self):
		loc ="Rév utca 13/b, Tiszatardos, Magyarország, 3928"
		geolocator = Nominatim(user_agent="test")
		location = geolocator.geocode(loc)
		print(location.address)
		print(self.root.ids.address_input.text)
MainApp().run()
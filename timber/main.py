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
		# put the data in the right database
		self.go_next()

	# Swipe Right
	def on_swipe_right(self):
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

	def find_location(self):
		loc =self.root.ids.address_input.text
		geolocator = Nominatim(user_agent="test")
		location = geolocator.geocode(loc)
		geocode = (location.latitude,location.longitude)

	def display_location(self,address, location = ""):
		self.root.ids.label_widget.text = f"you're swiping from:\n{address[0]},{address[1]}, {address[7]},{address[6]}"

		# fmap = folium.Map(location=location,zoom_start=12)
		# folium.CircleMarker(location=location,radius=50).add_to(fmap)
		# fmap.save("mymap.html")


MainApp().run()
from kivy.lang import Builder
from kivymd.app import MDApp
import random
import geocoder
import folium
from geopy.geocoders import Nominatim
from geopy.point import Point
from geopy.distance import great_circle as GD

main_database = []


with open("data_randomized.csv","r",encoding="UTF-8") as f:
	for i in f:
		main_database.append(i.strip().split(";"))


class MainApp(MDApp):
	own_geocode = ()
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('swiper2.kv')


	# Swipe Left
	def on_swipe_left(self):
		# put the data in the right database
		#if MATCH put it in MATCHES
		#if person swiped no, ignore,
		#if persone yet to swipe like
		#then go to the next person
		can_go_next = self.go_next()

	# Swipe Right
	def on_swipe_right(self):
		#put the data in the right database

		can_go_next = self.go_next()


	def go_next(self):
		if main_database!= []:
			#if database is not empty, load next data
			self.root.ids.data.text = main_database[0][0]+'\n'+main_database[0][1]
			print(main_database[0][1])
			person_geocode = self.find_location(main_database[0][1])[0]
			main_database.pop(0)
			return True
		return False


	def user_location_auto(self):
		geolcator = Nominatim(user_agent="test")
		my_ip = geocoder.ip('me')
		my_adress = my_ip.latlng
		location = geolcator.reverse(Point(my_adress[0],my_adress[1]))
		address = location.address.split(",")
		geocode = (location.latitude, location.longitude)
		self.display_location(address, geocode)
		self.own_geocode = geocode


	def user_location(self):


		loc = self.root.ids.address_input.text
		try:
			returned = self.find_location(loc)
			self.own_geocode = returned[0]
			self.display_location(returned[1], self.own_geocode)
		except:
			self.root.ids.label_widget.text = "Couldn't find address, please try again"


	def display_location(self,address, location = ""):
		if len(address) == 8:
			self.root.ids.label_widget.text = f"you're swiping from:\n{address[0]},{address[1]}, {address[-1]},{address[-2]}"
		else:
			self.root.ids.label_widget.text = f"you're swiping from:\n{address[0]},{address[2]}, {address[-1]},{address[-2]}"



	def find_location(self, loc):

		geolocator = Nominatim(user_agent="test")
		location = geolocator.geocode(loc)
		geocode = (location.latitude, location.longitude)
		address = location.address.split(',')
		return geocode,address


	def loc_tester(self):
		location = (36.9593639, 140.0478093)
		fmap = folium.Map(location=location, zoom_start=12)
		folium.CircleMarker(location=location, radius=50).add_to(fmap)
		fmap.save("mymap.html")

MainApp().run()
MainApp().loc_tester()
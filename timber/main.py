from kivy.lang import Builder
from kivymd.app import MDApp
import geocoder
import folium
from geopy.geocoders import Nominatim
from geopy.point import Point
from geopy.distance import great_circle as GC
import pandas as pd
import math as m




class MainApp(MDApp):
	WANTS = "female"
	GENDER = "male"
	NAME = "Zack"
	own_address = ""
	own_geocode = ()
	id = 0
	started = False

	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('swiper2.kv')


	def load_database(self):
		df = pd.read_csv("data_randomized.csv", sep=';', index_col=False,encoding = "ISO-8859-1")

		self.dict_of_df = df.to_dict(orient="records")
		self.filtered_df = []

		self.id = int(df.iloc[-1:]['id'])+1
		self.root.ids.toolbar.title = f"your id:{int(self.id)}"
		self.started = True

	def create_account(self):
		with open(f"users\{self.id}.txt", "w") as f:
			pass
		with open("data_randomized.csv", "a") as f:
			print(f"{self.id};{self.NAME};{self.own_address};{self.own_geocode[0]};{self.own_geocode[1]};{self.GENDER};{self.WANTS}\n",file=f)


	# Swipe Left
	def on_swipe_left(self):
		# put the data in the right database
		if self.started:
			with open(f"users\{self.id}.txt"):
				pass

			can_go_next = self.go_next(True)


	# Swipe Right
	def on_swipe_right(self):
		#put the data in the right database
		if self.started:

			can_go_next = self.go_next(False)


	def go_next(self,right):
		all_data= {}
		with open(f'users\{self.id}.txt','a') as f:
			for i in f:
				i = i.split(";")
				all_data[i[0]] = i[2]
				if self.started:
					if self.filtered_df[0]["id"]!= self.id and self.filtered_df[0]["id" not in all_data.keys()]:
						print('asd')


	def filter_database(self):


		if self.root.ids.radius.text != '':
			print(self.root.ids.radius.text)
			self.radius = int(self.root.ids.radius.text)

		else:
			self.radius = m.inf

		if self.started:
			self.filtered_df = []
			for i in self.dict_of_df:
				if GC(self.own_geocode,(i["Latitude"],i["Longitude"])) < self.radius and i["Gender"] == self.WANTS and i["Wants"] == self.GENDER:
					self.filtered_df.append(i)



	def user_location_auto(self):
		self.load_database()
		geolcator = Nominatim(user_agent="test")
		my_ip = geocoder.ip('me')
		my_adress = my_ip.latlng
		location = geolcator.reverse(Point(my_adress[0],my_adress[1]))
		address = location.address.split(",")
		geocode = (location.latitude, location.longitude)
		self.display_location(address)
		self.own_geocode = geocode
		self.own_address = address


	def user_location(self):

		self.load_database()
		loc = self.root.ids.address_input.text
		try:
			returned = self.find_location(loc)
			self.own_geocode = returned[0]
			self.display_location(returned[1])
			self.own_address = returned[1]
		except:
			self.root.ids.label_widget.text = "Couldn't find address, please try again"


	def display_location(self,address):
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


	def loc_tester(self, location):
		fmap = folium.Map(location=location, zoom_start=12)
		folium.CircleMarker(location=location, radius=50).add_to(fmap)
		fmap.save("mymap.html")



MainApp().run()

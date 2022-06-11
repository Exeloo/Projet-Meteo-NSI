import json
from tkinter import *
from PIL import Image, ImageTk
import os

from src.system.features.location.Location import get_location, Location
from src.system.features.map.Map import get_map_temp, get_map_wind
from src.system.interface.weather.Weather import get_weather
from src.utils.Config import GetConfig


class App:

    def __init__(self):

        self.map_type = "TEMP"
        self.map_time = "CURRENT"
        self.map_content = None
        self.canvas_map_type = None

        self.location_city = ""
        self.location_time = "DAY"
        self.location_content = get_weather(None)
        self.canvas_NW = None
        self.entry = None
        self.search_button = None

        self.precise_window = None
        self.precise_text = None
        self.precise_canvas = None

        self.window = Tk()
        self.window.title("Windi méteo")
        self.window.geometry("1400x750")
        self.window.iconbitmap("src/icons/windi.ico")
        img = Image.open('src/icons/map_france.png')
        self.x, self.y = 596, 550
        resized_img = img.resize((self.x, self.y), Image.ANTIALIAS)
        self.map_image = ImageTk.PhotoImage(resized_img)

        self.window.config(background='#7FD9E3')

        self.canvas = Canvas(self.window, width=self.x + 10, height=self.y + 10, bg='#355A5E', bd=5)
        self.canvas.place(x=15, y=20)
        self.canvas.create_image(310, 287, image=self.map_image)

        self.wind_img = {i.rstrip(".png"): get_image(i, "wind") for i in os.listdir("src/icons/wind")}
        self.weather_img = {i.rstrip(".png"): get_image(i, "weather") for i in os.listdir("src/icons/weather")}
        self.location_img = {i.rstrip(".png"): get_image(i, "weather", (40, 40)) for i in
                             os.listdir("src/icons/weather")}

        arrow_low = self.wind_img.get("low-E")
        arrow_mid = self.wind_img.get("mid-E")
        arrow_hard = self.wind_img.get("hard-E")

        canvas_legend = Canvas(self.window, width=606, height=35, bg='#355A5E', bd=5)
        canvas_legend.place(x=15, y=600)

        canvas_legend.create_image(50, 25, image=arrow_low)
        canvas_legend.create_image(225, 25, image=arrow_mid)
        canvas_legend.create_image(430, 25, image=arrow_hard)
        canvas_legend.create_text(70, 25, text="Vent faible", fill='#BEDBDE', font=("Courrier", 18), anchor='w')
        canvas_legend.create_text(245, 25, text="Vent modéré", fill='#BEDBDE', font=("Courrier", 18), anchor='w')
        canvas_legend.create_text(450, 25, text="Vent fort", fill='#BEDBDE', font=("Courrier", 18), anchor='w')

        canvas_set_map = Canvas(self.window, width=606, height=60, bg='#355A5E', bd=5)
        canvas_set_map.place(x=15, y=656)

        canvas_set_map.create_text(15, 38, text="Type de carte :", font='Courrier 18 underline', fill='#BEDBDE',
                                   anchor='w')
        Button(self.window, text="Vent", font=("Courrier", 20), bg='#7FD9E3',
               command=self.set_map_wind).place(y=665, x=220)
        Button(self.window, text="Météo et température", font=("Courrier", 20), bg='#7FD9E3',
               command=self.set_map_weather).place(y=665, x=330)

        canvas_mid = Canvas(self.window, width=150, height=560, bg='#355A5E', bd=5)
        canvas_mid.place(x=650, y=20)
        Button(self.window, text="Maintenant", font=("Courrier", 18), bg='#7FD9E3',
               command=self.set_map_current).place(y=32, x=662)
        Button(self.window, text="Aujourd'hui\nmatin", font=("Courrier", 18), bg='#7FD9E3',
               command=self.set_map_today_morn).place(y=86, x=662)
        Button(self.window, text="Aujourd'hui\naprès midi", font=("Courrier", 18), bg='#7FD9E3',
               command=self.set_map_today_after).place(y=166, x=662)
        Button(self.window, text="Demain\nmatin", font=("Courrier", 19), height=2, width=9, bg='#7FD9E3',
               command=self.set_map_tomorrow_morn).place(y=250, x=660)
        Button(self.window, text="Demain\naprès midi", font=("Courrier", 19), bg='#7FD9E3',
               command=self.set_map_tomorrow_after).place(y=334, x=662)
        Button(self.window, text="Après\ndemain", font=("Courrier", 19), height=2, width=9, bg='#7FD9E3',
               command=self.set_map_after_tomorrow).place(y=420, x=660)
        Button(self.window, text="Après après\ndemain", font=("Courrier", 17), height=2, width=10, bg='#7FD9E3',
               command=self.set_map_after_after_tomorrow).place(y=510, x=663)

        canvas_w = Canvas(self.window, width=450, height=500, bg='#355A5E', bd=5)
        canvas_w.place(x=900, y=200)

        Button(self.window, text="Aujourd'hui", font=("Courrier", 18), bg='#7FD9E3',
               command=self.set_location_day).place(y=215, x=920)
        Button(self.window, text="3 jours", font=("Courrier", 18), bg='#7FD9E3',
               command=self.set_location_three_day).place(y=215, x=1100)
        Button(self.window, text="Semaine", font=("Courrier", 18), bg='#7FD9E3',
               command=self.set_location_week).place(y=215, x=1230)

        Button(self.window, text="Informations plus précises", font=("Courrier", 18), bg='#7FD9E3',
               command=self.set_precise_location_window).place(y=660, x=920)

        self.set_map()
        self.set_location()

        self.window.mainloop()

    def set_location(self):
        contents, city = None, None
        if self.location_content is not None:
            contents, city = get_location(self.location_content.value, self.location_time)
        if self.canvas_NW is not None:
            self.canvas_NW.destroy()

        self.canvas_NW = Canvas(self.window, width=450, height=150, bg='#355A5E', bd=5)
        self.canvas_NW.place(x=900, y=20)
        self.entry = Entry(self.canvas_NW, font=("Courrier", 20), bg='#7FD9E3')
        self.entry.place(x=147, y=15)
        self.canvas_NW.create_text(6, 35, text="Localisation :", fill='#BEDBDE', font='Courrier 18 underline',
                                   anchor='w')

        if self.search_button is not None:
            self.search_button.destroy()
        self.search_button = Button(self.window, text="Rechercher", font=("Courrier", 17), bg='#7FD9E3',
                                    command=self.search_location).place(y=100, x=910)
        if city is not None:
            self.canvas_NW.create_text(250, 100, text=city, fill='#BEDBDE', font='Courrier 20 bold', anchor='w')
        else:
            self.canvas_NW.create_text(220, 100, text="Erreur, \nla ville n'éxiste pas", fill="#900603",
                                       font='Courrier 17', anchor='w')
        self.window.update()
        if contents is None:
            return
        for i in range(7):
            content: Location = contents[i]
            canvas = Canvas(self.window, width=410, height=35, bg='#7FD9E3', bd=5)
            canvas.place(x=920, y=275 + i * 55)
            day, hour = get_format_time(content)

            canvas.create_text(15, 23, text=day + hour, font='Courrier 10', anchor='w')
            canvas.create_image(80, 23, image=self.location_img.get(content.weather))
            canvas.create_text(110, 23, text=f"Température :\n{content.temp}°C", font='Courrier 9', anchor='w')
            canvas.create_text(195, 23, text=f"Ressenti :\n{content.feel}°C", font='Courrier 9', anchor='w')
            canvas.create_text(
                260, 23, font='Courrier 9', anchor='w',
                text=f"Direction et vitesse du vent :\n{content.wind_dir} - {content.wind_speed} km/h")

    def set_precise_location_window(self):
        if self.location_content is None:
            return
        self.precise_window = Toplevel()
        self.precise_window.grab_set()
        self.precise_window.focus_set()
        self.precise_window.title("Informations précises")
        self.precise_window.geometry("1080x680")
        self.precise_window.iconbitmap("src/icons/windi.ico")
        self.precise_window.config(background='#355A5E')
        Button(self.precise_window, text="Quitter", font=("Courrier", 18), bg='#7FD9E3',
               command=lambda: self.precise_window.destroy()).place(x=10, y=10)
        Button(self.precise_window, text="Aujourd'hui", font=("Courrier", 18), bg='#7FD9E3',
               command=self.set_precise_day).place(x=650, y=10)
        Button(self.precise_window, text="3 jours", font=("Courrier", 18), bg='#7FD9E3',
               command=self.set_precise_three_day).place(x=800, y=10)
        Button(self.precise_window, text="Semaine", font=("Courrier", 18), bg='#7FD9E3',
               command=self.set_precise_week).place(x=900, y=10)
        self.set_precise_location()

    def set_precise_location(self):
        contents, city = get_location(self.location_content.value, self.location_time)
        time = \
            "Aujourd'hui" if self.location_time == "DAY" else \
                "3 Jours" if self.location_time == "THREE_DAY" else "Semaine"
        if self.precise_text is not None:
            self.precise_text.destroy()
        self.precise_text = Canvas(self.precise_window, width=450, height=60, bg='#355A5E', bd=-1)
        self.precise_text.place(x=170, y=10)
        self.precise_text.create_text(20, 30, text=f"{city} - {time}", fill='#BEDBDE', font='Courrier 20 bold',
                                      anchor='w')
        if self.precise_canvas is not None:
            for canvas in self.precise_canvas:
                canvas.destroy()
        self.precise_canvas = []
        for i in range(7):
            content: Location = contents[i]
            canvas = Canvas(self.precise_window, width=1050, height=60, bg='#7FD9E3', bd=5)
            canvas.place(x=10, y=80 + i * 85)
            day, hour = get_format_time(content)

            canvas.create_text(15, 35, text=day + hour, font='Courrier 13', anchor='w')
            canvas.create_image(95, 35, image=self.weather_img.get(content.weather))
            canvas.create_text(130, 35, text=f"Température :\n{content.temp}°C", font='Courrier 12', anchor='w')
            canvas.create_text(240, 35, text=f"Ressenti :\n{content.feel}°C", font='Courrier 12', anchor='w')
            canvas.create_text(
                320, 35, font='Courrier 12', anchor='w',
                text=f"Direction et vitesse du vent :\n{content.wind_dir} - {content.wind_speed} km/h")
            canvas.create_text(530, 35, font='Courrier 12', anchor='w',
                               text=f"Pression : {content.pressure}\nHumiditée : {content.humidity}"
                               if content.humidity is not None else f"Pression : {content.pressure}")
            canvas.create_text(670, 35, font='Courrier 12', anchor='w',
                               text=f"Soleil : Levée -> {content.sunrise}\n            Couché -> {content.sunset}")

            rain = "" if content.precipprob == 0 else \
                f"Pluie : Probabilité -> {content.precipprob}%" if content.precip == 0 else \
                    f"Pluie : Probabilité -> {content.precipprob}%\n         Précipitation -> {content.precip}cm"
            snow = "" if content.snow == 0 else \
                f"Neige : Quantité -> {content.snow}" if content.snowdepth == 0 else \
                    f"Neige : Quantité -> {content.snow}\n              Couche -> {content.snowdepth}cm"
            canvas.create_text(880, 35, font='Courrier 9', anchor='w', text=f"{rain}\n{snow}")
            self.precise_canvas.append(canvas)

        self.precise_window.update()

    def set_map_type(self):

        if isinstance(self.canvas_map_type, Canvas):
            self.canvas_map_type.destroy()

        self.canvas_map_type = Canvas(self.window, width=150, height=116, bg='#355A5E', bd=5)
        self.canvas_map_type.place(x=650, y=600)
        map_time = "Aujourd'hui \n  matin" if self.map_time == "TODAY_MORN" else \
            "Aujourd'hui \n  après midi" if self.map_time == "TODAY_AFTER" else \
            "Demain matin" if self.map_time == "TOMORROW_MORN" else \
            "Demain \n  après midi" if self.map_time == "TOMORROW_AFTER" else \
            "Après demain" if self.map_time == "AFTER_TOMORROW" else \
            "Après après\n  demain" if self.map_time == "AFTER_AFTER_TOMORROW" else \
            "Maintenant"

        map_type = "Vent" if self.map_type == "WIND" else "Météo"
        self.canvas_map_type.create_text(10, 33, text="Actuellement\naffiché :", fill='#BEDBDE',
                                         font='Courrier 18 underline', anchor='w', )
        self.canvas_map_type.create_text(10, 92, text=f"- {map_time}\n- {map_type}", fill='#BEDBDE',
                                         font=("Courrier", 14, 'bold'), anchor='w')
        self.window.update()

    def set_map(self):
        if self.map_content is None:
            self.map_content = {city: get_weather(city).value for city in GetConfig().cities.keys()}

        map_info, up, down = get_map_temp(self.map_content, self.map_time) if self.map_type == "TEMP" else \
            get_map_wind(self.map_content, self.map_time)
        if map_info.__getattribute__(list(GetConfig().cities.keys())[0]).__getattribute__(up) is None:
            self.window.update()
            return

        self.canvas.destroy()
        self.canvas = Canvas(self.window, width=self.x + 10, height=self.y + 10, bg='#355A5E', bd=5)
        self.canvas.place(x=15, y=20)
        self.canvas.create_image(310, 287, image=self.map_image)
        max_temp = None
        min_temp = None
        if self.map_type == "TEMP":
            for key, value in GetConfig().cities.items():
                weather = map_info.__getattribute__(key)
                up_value = weather.__getattribute__(up)
                if max_temp is None or up_value > max_temp:
                    max_temp = up_value
                if min_temp is None or up_value < min_temp:
                    min_temp = up_value

        for key, value in GetConfig().cities.items():
            weather = map_info.__getattribute__(key)
            up_value = weather.__getattribute__(up)
            down_value = weather.__getattribute__(down)
            if self.map_type == "TEMP":
                self.canvas.create_image(value.get("x") - 15, value.get("y") + 10, image=self.weather_img.get(
                    down_value) if self.weather_img.get(down_value) is not None else self.weather_img.get("cloudy"))
                self.canvas.create_text(value.get("x"), value.get("y") - 5, text=f"{up_value}°",
                                        fill='#bc2734' if max_temp == up_value else '#0048ba' if min_temp == up_value
                                        else '#000000',
                                        font=("Courrier", 14), anchor='w')
            else:
                self.canvas.create_image(value.get("x"), value.get("y"),
                                         image=self.wind_img.get(f"{up_value}-{down_value}"))

        self.set_map_type()
        self.window.update()

    def set_map_current(self):
        if self.map_time != "CURRENT":
            self.map_time = "CURRENT"
            self.set_map()

    def set_map_today_morn(self):
        if self.map_time != "TODAY_MORN":
            self.map_time = "TODAY_MORN"
            self.set_map()

    def set_map_today_after(self):
        if self.map_time != "TODAY_AFTER":
            self.map_time = "TODAY_AFTER"
            self.set_map()

    def set_map_tomorrow_morn(self):
        if self.map_time != "TOMORROW_MORN":
            self.map_time = "TOMORROW_MORN"
            self.set_map()

    def set_map_tomorrow_after(self):
        if self.map_time != "TOMORROW_AFTER":
            self.map_time = "TOMORROW_AFTER"
            self.set_map()

    def set_map_after_tomorrow(self):
        if self.map_time != "AFTER_TOMORROW":
            self.map_time = "AFTER_TOMORROW"
            self.set_map()

    def set_map_after_after_tomorrow(self):
        if self.map_time != "AFTER_AFTER_TOMORROW":
            self.map_time = "AFTER_AFTER_TOMORROW"
            self.set_map()

    def set_map_weather(self):
        if self.map_type != "TEMP":
            self.map_type = "TEMP"
            self.set_map()

    def set_map_wind(self):
        if self.map_type != "WIND":
            self.map_type = "WIND"
            self.set_map()

    def set_location_day(self):
        if self.location_time != "DAY":
            self.location_time = "DAY"
            self.set_location()

    def set_location_three_day(self):
        if self.location_time != "THREE_DAY":
            self.location_time = "THREE_DAY"
            self.set_location()

    def set_location_week(self):
        if self.location_time != "WEEK":
            self.location_time = "WEEK"
            self.set_location()

    def set_precise_day(self):
        if self.location_time != "DAY":
            self.location_time = "DAY"
            self.set_precise_location()

    def set_precise_three_day(self):
        if self.location_time != "THREE_DAY":
            self.location_time = "THREE_DAY"
            self.set_precise_location()

    def set_precise_week(self):
        if self.location_time != "WEEK":
            self.location_time = "WEEK"
            self.set_precise_location()

    def search_location(self):
        if self.location_city != self.entry.get():
            self.location_city = self.entry.get()
            try:
                self.location_content = get_weather(None if self.location_city == "" else self.location_city)
            except json.decoder.JSONDecodeError:
                self.location_content = None
            self.set_location()


def get_image(name: str, folder: str, size: (int, int) = (50, 50)) -> PhotoImage:
    img = Image.open(f"src/icons/{folder}/{name}")
    resized_img = img.resize(size, Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_img)


def get_format_time(content: Location) -> (str, str):
    return f"{content.day[-2:]} - {content.day[-5:-3]}", \
           f"\n{content.hour[:2]}h" if content.hour is not None and content.day is not None else \
            f"{content.hour[:2]}h" if content.hour is not None else ""

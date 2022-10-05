from helium import *
import time
import sys

class bot_C():
    def __init__(self):
        self.name = "driver"
        self.results = []

    def launch(self):
        start_firefox(headless=True) #silent mode


    def ZipCode(self, city_S):
        tmp_city = city_S.upper()
        try:
            file = open("./cities.csv", "r")
        except:
            sys.exit("no file found")

        contentFile = file.readlines()
        
        results = []
        for line in contentFile:
            if(tmp_city in line):
                parsed_line = line.split(";")
                results.append(parsed_line)

        if(len(results) == 1):
            return parsed_line[1]
        elif(len(results) == 0):
            sys.exit("City not found ! ("+str(city_S)+")")
        else: #have to choose only one city
            print("multiple cities found. Choose only one : ")
            for i in range(len(results)-1):
                print(str(i)+". "+str(results[i]))

            choice = input("city index > ")
            tmp_city = results[int(choice)]
            print(tmp_city)
            return tmp_city[1].strip()

    def browse_weather(self, city):
        zip_city = self.ZipCode(city)
        
        go_to("https://meteofrance.com/previsions-meteo-france/"+city+"/"+zip_city)

        if Text('Continuer sans accepter').exists():
            click("Continuer sans accepter")

        temperature = S(".temp")
        self.results.append("Current weather at "+city+" : "+temperature.web_element.text)


    def browse_waze(self, src, dst):
        go_to("https://www.waze.com/fr/live-map?utm_source=waze_website&utm_campaign=waze_website&utm_medium=website_menu")

        time.sleep(2)

        if Text("Modifiez votre heure d'arrivée").exists():
            click("OK")
        if Text("Waze & Cookies").exists():
            click("Non merci")

        write(src, into='Choisissez un point de départ')
        time.sleep(1)
        press(ENTER)
        write(dst, into='Choisissez une destination')
        time.sleep(1)
        press(ENTER)

        time.sleep(2)
        if Text("Enregistrez votre trajet dans l'application").exists():
            click("OK")

        time.sleep(2)
        if Text("Modifiez votre heure d'arrivée").exists():
            click("OK")

        goal = S(".wm-routes-item-desktop__hint")
        self.results.append(goal.web_element.text)
        

    def kill(self):
        kill_browser()

    def run(self, src, dst):
        self.launch()
        self.browse_weather(src)
        self.browse_weather(dst)
        self.browse_waze(src, dst)

        print("\n\n")
        for result in self.results:
            print(result)

        self.kill()
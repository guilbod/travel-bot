# travel-bot

A python bot to get some informations on a planned trip (a city to another one).


Principle :
- specify starting city and destination city (only french cities are supported)
- the bot connects to forecast website
	- get the actual starting city weather
	- get the actual destination city weather
- the bot connects to waze
	- get the amount of time needed to reach the destination city

Usage :
- python3 main.py city_src city_dest
(install helium before)


Files :
- requirements.txt : the module needed
- cities.csv : a file containing french cities and their ZIP code
- bot.py : the bot itself
- help.py : display the help
- main.py : for starting the project

History : 
- version 1 (now) : retrieve the weather and time to reach the destination city


Upgrades :
- save parameters for faster research
- make a cron to automatically run the program
- retrieve the weather for a given period
- retrieve more details about traffic (jam, work...) 

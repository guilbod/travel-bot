import bot
import help
import sys

if(("-h" in sys.argv)):
    help.Help()
elif(len(sys.argv) != 3):
    help.Help()
else:
    myBot = bot.bot_C()
    myBot.run(sys.argv[1], sys.argv[2])

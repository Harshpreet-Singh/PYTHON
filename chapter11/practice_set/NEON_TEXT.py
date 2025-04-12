import time
import os

# Define the neon styles
colors = [
    "\033[1;92m",  # Bright Green
    "\033[1;95m",  # Bright Magenta
    "\033[1;96m",  # Bright Cyan
    "\033[1;93m",  # Bright Yellow
    "\033[1;91m",  # Bright Red
    "\033[1;94m"   # Bright Blue
]
reset = "\033[0m"

ascii_art = r"""
 ██████╗  ██████╗ ██╗    ██╗     ██████╗  ██████╗ ██╗    ██╗
██╔════╝ ██╔═══██╗██║    ██║    ██╔═══██╗██╔════╝ ██║    ██║
██║  ███╗██║   ██║██║ █╗ ██║    ██║   ██║██║  ███╗██║ █╗ ██║
██║   ██║██║   ██║██║███╗██║    ██║   ██║██║   ██║██║███╗██║
╚██████╔╝╚██████╔╝╚███╔███╔╝    ╚██████╔╝╚██████╔╝╚███╔███╔╝
 ╚═════╝  ╚═════╝  ╚══╝╚══╝      ╚═════╝  ╚═════╝  ╚══╝╚══╝

"""

# Flashing loop (Ctrl+C to stop)
try:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
        color = colors[int(time.time() * 5) % len(colors)]
        print(color + ascii_art + reset)
        time.sleep(0.2)
except KeyboardInterrupt:
    print("\n\033[1;90mNeon party over. 🕺💤\033[0m")


'''
Color	            Code	             Example
Bright Black	 \033[90m	    print("\033[90mBright Black\033[0m")
Bright Red	     \033[91m	    print("\033[91mBright Red\033[0m")
Bright Green	 \033[92m	    print("\033[92mBright Green\033[0m")
Bright Yellow	 \033[93m	    print("\033[93mBright Yellow\033[0m")
Bright Blue	     \033[94m	    print("\033[94mBright Blue\033[0m")
Bright Magenta	 \033[95m	    print("\033[95mBright Magenta\033[0m")
Bright Cyan      \033[96m	    print("\033[96mBright Cyan\033[0m")
Bright White	 \033[97m	    print("\033[97mBright White\033[0m")
Black	         \033[30m	    print("\033[30mBlack Text\033[0m")
Red	             \033[31m	    print("\033[31mRed Text\033[0m")
Green	         \033[32m	    print("\033[32mGreen Text\033[0m")
Yellow	         \033[33m	    print("\033[33mYellow Text\033[0m")
Blue	         \033[34m	    print("\033[34mBlue Text\033[0m")
Magenta	         \033[35m	    print("\033[35mMagenta Text\033[0m")
Cyan	         \033[36m	    print("\033[36mCyan Text\033[0m")
White	         \033[37m	    print("\033[37mWhite Text\033[0m")


'''

print("\n \n")
print("\033[1;93m💛 ✨ BOW BOW ✨ 💛\033[0m")
print("\033[1;92mBOW \033[1;95mBOW \033[1;96mIS \033[1;93mHERE! 💥\033[0m")
print("\033[5;95mBOW BOW NEON ALERT!\033[0m")
print("\033[1;92m💚 ~~~ BOW BOW ~~~ 💚\033[0m")

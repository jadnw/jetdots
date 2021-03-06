from classes.module import Module

def gen_template(theme):
    pal = theme["palette"]
    template = f"""ignore-empty-password
disable-caps-lock-text
image=$HOME/.config/wallpapers/lockscreen.jpg
font=Jolly Lodger

text-ver-color=00000000
text-wrong-color=00000000
text-clear-color=00000000
inside-color=00000000
inside-ver-color=00000000
inside-wrong-color=00000000
inside-clear-color=00000000
inside-caps-lock-color=00000000
ring-color=00000000
ring-ver-color=00000000
ring-wrong-color=00000000
ring-clear-color=00000000
line-color=00000000
line-clear-color=00000000
line-ver-color=00000000
key-hl-color=00000000
bs-hl-color=00000000
caps-lock-bs-hl-color=00000000
caps-lock-key-hl-color=00000000
separator-color=00000000

scaling=fill
indicator
clock
timestr=%H:%M
datestr=%A | %d %B %y
indicator-x-position=20
indicator-y-position=930
indicator-radius=320
font-size=192
text-color={pal["fg1"]}
    """
    return template

swaylock = Module("swaylock", gen_template)

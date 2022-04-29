from classes.module import Module

def gen_template(theme):
    pal = theme["palette"]
    template = f"""# ▄▄▄▄· ▄▄▄ .▄▄▄▄▄▄▄▄▄▄▄▄▄ .▄▄▄  ▄▄▌         ▄▄· ▄ •▄ .▄▄ ·  ▄▄· ▄▄▄  ▄▄▄ .▄▄▄ . ▐ ▄ 
# ▐█ ▀█▪▀▄.▀·•██  •██  ▀▄.▀·▀▄ █·██•  ▪     ▐█ ▌▪█▌▄▌▪▐█ ▀. ▐█ ▌▪▀▄ █·▀▄.▀·▀▄.▀·•█▌▐█
# ▐█▀▀█▄▐▀▀▪▄ ▐█.▪ ▐█.▪▐▀▀▪▄▐▀▀▄ ██▪   ▄█▀▄ ██ ▄▄▐▀▀▄·▄▀▀▀█▄██ ▄▄▐▀▀▄ ▐▀▀▪▄▐▀▀▪▄▐█▐▐▌
# ██▄▪▐█▐█▄▄▌ ▐█▌· ▐█▌·▐█▄▄▌▐█•█▌▐█▌▐▌▐█▌.▐▌▐███▌▐█.█▌▐█▄▪▐█▐███▌▐█•█▌▐█▄▄▌▐█▄▄▌██▐█▌
# ·▀▀▀▀  ▀▀▀  ▀▀▀  ▀▀▀  ▀▀▀ .▀  ▀.▀▀▀  ▀█▄▀▪·▀▀▀ ·▀  ▀ ▀▀▀▀ ·▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀ ▀▀ █▪
# Created by: Jaden Wu
# Github: @j4d3nw
# Email: jadenwu137@protonmail.com

# default options
display_on=0
span_image=false
lock_timeout=300
fx_list=(dim blur dimblur pixel dimpixel color)
dim_level=40
blur_level=1
pixel_scale=10,1000
solid_color={pal["bg1"]}
wallpaper_cmd="feh --bg-fill"
# i3lockcolor_bin="i3lock-color" # Manually set command for i3lock-color

# default theme
loginbox=00000000
loginshadow=00000000
locktext="Type password to unlock..."
font="Nerko One"
ringcolor=00000000
insidecolor=00000000
separatorcolor=00000000
ringvercolor=00000000
insidevercolor=00000000
ringwrongcolor=00000000
insidewrongcolor=00000000
timecolor={pal["fg1"]}ff
time_format="%H:%M"
greetercolor={pal["fg1"]}ff
layoutcolor=00000000
keyhlcolor=00000000
bshlcolor=00000000
verifcolor=00000000
wrongcolor=00000000
modifcolor=00000000
bgcolor=00000000
    """
    return template

betterlockscreen = Module("betterlockscreen", gen_template)

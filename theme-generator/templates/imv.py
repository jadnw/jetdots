from classes.module import Module

def gen_template(theme):
    pal = theme["palette"]
    template = f"""# ▪  • ▌ ▄ ·.  ▌ ▐·
# ██ ·██ ▐███▪▪█·█▌
# ▐█·▐█ ▌▐▌▐█·▐█▐█•
# ▐█▌██ ██▌▐█▌ ███ 
# ▀▀▀▀▀  █▪▀▀▀. ▀  
# Created by: Jaden Wu
# Github: @jadnw
# Email: jadenwu137@protonmail.com

# ~/.config/imv/config

# styling
[options]
background = {pal["bg0"]}
fullscreen = false
overlay = true
overlay_text_color = {pal["fg1"]}
overlay_background_color = {pal["bg2"]}
overlay_background_alpha = ff
overlay_font = Josevka Curly:11
overlay_position_bottom = false

# bindings
[binds]
j = next
k = prev
    """
    return template

imv = Module("imv", gen_template)

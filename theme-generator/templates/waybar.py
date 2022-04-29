from classes.module import Module

def gen_template(theme):
    pal = theme["palette"]
    template = f"""/* {theme["name"]} Colorscheme for GTK CSS */

 /* ~/.config/waybar/colors.css */

@define-color accent {pal["accent"]};
@define-color bg0 {pal["bg0"]};
@define-color bg1 {pal["bg1"]};
@define-color bg2 {pal["bg2"]};
@define-color bg3 {pal["bg3"]};
@define-color bg4 {pal["bg4"]};

@define-color fg0 {pal["fg0"]};
@define-color fg1 {pal["fg1"]};
@define-color fg2 {pal["fg2"]};
@define-color fg3 {pal["fg3"]};
@define-color black {pal["black"]};
@define-color red {pal["red"]};
@define-color orange {pal["orange"]};
@define-color yellow {pal["yellow"]};
@define-color green {pal["green"]};
@define-color teal {pal["teal"]};
@define-color cyan {pal["cyan"]};
@define-color blue {pal["blue"]};
@define-color magenta {pal["magenta"]};
@define-color purple {pal["purple"]};
@define-color white {pal["white"]};
@define-color gray {pal["gray"]};"""

    return template

waybar = Module("waybar", gen_template)

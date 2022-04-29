from classes.module import Module

def gen_template(theme):
    pal = theme["palette"]
    template = f"""#!/bin/fish

# ~/.config/bspwm/theme

bspc config normal_border_color "{pal["bg0"]}"
bspc config focused_border_color "{pal["accent"]}"
bspc config presel_feedback_color "{pal["bg3"]}"
    """
    return template

bspwm = Module("bspwm", gen_template)

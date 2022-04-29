from classes.module import Module
from lib.util import remove_hash_from_pal

def gen_template(theme):
    pal = remove_hash_from_pal(theme["palette"])
    template = f"""# {theme["name"]} colorscheme for foot term
# ~/.config/foot/theme.ini
[cursor]
style=block
color={pal["bg1"]} {pal["accent"]}
blink=no

[mouse]
hide-when-typing=yes

[colors]
alpha=1.0
foreground={pal["fg1"]}
background={pal["bg1"]}

# Normal/regular colors (color palette 0-7)
regular0={pal["black"]}  # black
regular1={pal["red"]}  # red
regular2={pal["green"]}  # green
regular3={pal["yellow"]}  # yellow
regular4={pal["blue"]}  # blue
regular5={pal["magenta"]}  # magenta
regular6={pal["cyan"]}  # cyan
regular7={pal["white"]}  # white

# Bright colors (color palette 8-15)
bright0={pal["black"]}  # black
bright1={pal["red"]}  # red
bright2={pal["green"]}  # green
bright3={pal["yellow"]}  # yellow
bright4={pal["blue"]}  # blue
bright5={pal["magenta"]}  # magenta
bright6={pal["cyan"]}  # cyan
bright7={pal["white"]}  # white
    """
    return template

foot = Module("foot", gen_template)

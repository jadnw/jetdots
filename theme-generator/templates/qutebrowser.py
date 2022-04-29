from classes.module import Module

def gen_template(theme):
    pal = theme["palette"]
    template = f"""# {theme["name"]} colorscheme for QuteBrowser
# ~/.config/qutebrowser/theme.py

colors = {{
    'accent': '{pal["accent"]}',
    'bg0': '{pal["bg0"]}',
    'bg1': '{pal["bg1"]}',
    'bg2': '{pal["bg2"]}',
    'bg3': '{pal["bg3"]}',
    'bg4': '{pal["bg4"]}',
    'fg0': '{pal["fg0"]}',
    'fg1': '{pal["fg1"]}',
    'fg2': '{pal["fg2"]}',
    'fg3': '{pal["fg3"]}',
    'black': '{pal["black"]}',
    'red': '{pal["red"]}',
    'orange': '{pal["orange"]}',
    'yellow': '{pal["yellow"]}',
    'green': '{pal["green"]}',
    'teal': '{pal["teal"]}',
    'cyan': '{pal["cyan"]}',
    'blue': '{pal["blue"]}',
    'magenta': '{pal["magenta"]}',
    'purple': '{pal["purple"]}',
    'white': '{pal["white"]}',
    'gray': '{pal["gray"]}',
}}
    """
    return template

qutebrowser = Module("qutebrowser", gen_template)

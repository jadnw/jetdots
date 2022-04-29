from classes.module import Module
name = "sway"

filename = "theme"

def gen_template(theme):
    pal = theme["palette"]
    template = f"""# window decorations
# class                 border              background          text                indicator           child_border
client.focused          {pal["accent"]}     {pal["bg4"]}        {pal["fg1"]}        {pal["red"]}        {pal["accent"]}
client.focused_inactive {pal["bg4"]}        {pal["bg4"]}        {pal["fg1"]}        {pal["red"]}        {pal["bg4"]}
client.unfocused        {pal["bg1"]}        {pal["bg1"]}        {pal["fg1"]}        {pal["red"]}        {pal["bg1"]}
client.urgent           {pal["red"]}        {pal["red"]}        {pal["bg1"]}        {pal["red"]}        {pal["red"]}
    """
    return template

sway = Module("sway", gen_template)

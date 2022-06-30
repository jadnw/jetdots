from classes.module import Module

def gen_template(theme):
    pal = theme["palette"]
    template = f"""# {theme["name"]} for Alacritty
# ~/.config/alacritty/theme.yml
colors:
  primary:
    background: '{pal["bg1"]}'
    foreground: '{pal["fg1"]}'
    dim_foreground: '{pal["fg2"]}'
    bright_foreground: '{pal["fg0"]}'
  cursor:
    text: '{pal["bg1"]}'
    cursor: '{pal["accent"]}'
  vi_mode_cursor:
    text: '{pal["bg1"]}'
    cursor: '{pal["accent"]}'
  search:
    matches:
      foreground: '{pal["bg3"]}'
      background: '{pal["purple"]}'
    focused_match:
      foreground: '{pal["purple"]}'
      background: '{pal["bg3"]}'
    bar:
      foreground: '{pal["bg3"]}'
      background: '{pal["purple"]}'
  hints:
    start:
      foreground: '{pal["bg3"]}'
      background: '{pal["yellow"]}'
    end:
      foreground: '{pal["yellow"]}'
      background: '{pal["bg3"]}'
  line_indicator:
    foreground: None
    background: None
  selection:
    text: '{pal["fg1"]}'
    background: '{pal["bg4"]}'
  normal:
    black: '{pal["gray"]}'
    red: '{pal["red"]}'
    green: '{pal["green"]}'
    yellow: '{pal["yellow"]}'
    blue: '{pal["blue"]}'
    magenta: '{pal["magenta"]}'
    cyan: '{pal["cyan"]}'
    white: '{pal["white"]}'
  bright:
    black: '{pal["gray"]}'
    red: '{pal["red"]}'
    green: '{pal["green"]}'
    yellow: '{pal["yellow"]}'
    blue: '{pal["blue"]}'
    magenta: '{pal["magenta"]}'
    cyan: '{pal["cyan"]}'
    white: '{pal["white"]}'"""

    return template

alacritty = Module("alacritty", gen_template)

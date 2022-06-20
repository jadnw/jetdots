import os
from os import path
import json

from templates.alacritty import alacritty
from templates.betterlockscreen import betterlockscreen
from templates.bspwm import bspwm
from templates.btop import btop 
from templates.dunst import dunst_wl, dunst_x
from templates.fish import fish
from templates.foot import foot
from templates.imv import imv
from templates.polybar import polybar
from templates.qutebrowser import qutebrowser
from templates.river import river
from templates.rofi import rofi
from templates.sugar_candy import sddm_sugar_candy
from templates.sway import sway
from templates.swaylock import swaylock
from templates.waybar import waybar
from templates.zathura import zathura

modules = [ alacritty, betterlockscreen, bspwm, btop, dunst_wl, dunst_x, fish, foot, imv, polybar, qutebrowser, river, rofi, sddm_sugar_candy, sway, swaylock, waybar, zathura ]

def read_theme_from_schema(schema_path):
    f = open(schema_path, "r")
    theme = json.loads(f.read())
    f.close()
    return theme

def write_template(theme, module, dest_path):
    template = module.gen_template(theme)
    with open(dest_path, "w") as f:
        f.write(template)
        f.close()

def generate(modules):
    SCHEMA_NAME = "nightwing"
    SCHEMA_PATH = path.abspath("theme-generator/schemas/" + SCHEMA_NAME + ".json")
    theme = read_theme_from_schema(SCHEMA_PATH)
    GEN_DIRNAME = "themes/" + theme["name"].lower()
    os.makedirs(path.abspath(GEN_DIRNAME))

    for module in modules:
        dest_path = path.abspath(GEN_DIRNAME + "/" + module.name)
        write_template(theme, module, dest_path)


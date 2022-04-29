from classes.module import Module
from lib.util import remove_hash_from_pal

def gen_template(theme):
    pal = remove_hash_from_pal(theme["palette"])
    template = f"""#!/bin/fish

riverctl background-color 0x{pal["bg1"]}
riverctl border-color-focused 0x{pal["accent"]}
riverctl border-color-unfocused 0x{pal["bg3"]}
    """
    return template

river = Module("river", gen_template)

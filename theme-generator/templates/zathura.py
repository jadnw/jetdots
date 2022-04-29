from classes.module import Module

def gen_template(theme):
    pal = theme["palette"]
    template = f"""set default-fg "{pal["fg1"]}"
set default-bg "{pal["bg0"]}"

set completion-bg "{pal["bg1"]}"
set completion-fg "{pal["fg1"]}"
set completion-highlight-bg "{pal["bg4"]}"
set completion-highlight-fg "{pal["fg1"]}"
set completion-group-bg "{pal["bg1"]}"
set completion-group-fg "{pal["accent"]}"

set statusbar-fg "{pal["fg1"]}"
set statusbar-bg "{pal["bg1"]}"

set notification-bg "{pal["bg1"]}"
set notification-fg "{pal["fg1"]}"
set notification-error-bg "{pal["bg1"]}"
set notification-error-fg "{pal["red"]}"
set notification-warning-bg "{pal["bg1"]}"
set notification-warning-fg "{pal["yellow"]}"

set inputbar-fg "{pal["fg1"]}"
set inputbar-bg "{pal["bg1"]}"

set recolor-lightcolor "{pal["bg0"]}"
set recolor-darkcolor "{pal["fg1"]}"

set index-fg "{pal["fg1"]}"
set index-bg "{pal["bg0"]}"
set index-active-fg "{pal["fg1"]}"
set index-active-bg "{pal["bg1"]}"

set render-loading-bg "{pal["bg0"]}"
set render-loading-fg "{pal["fg1"]}"

set highlight-color "{pal["bg4"]}"
set highlight-fg "{pal["accent"]}"
set highlight-active-color "{pal["accent"]}"
    """
    return template

zathura = Module("zathura", gen_template)

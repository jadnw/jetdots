from classes.module import Module
from lib.util import remove_hash_from_pal

def gen_template(theme):
    pal = remove_hash_from_pal(theme["palette"])
    template = f"""# {theme["name"]} colorscheme for Fish
# ~/.config/fish/conf.d/theme.fish

# --> special
set -l fg {pal["fg1"]}
set -l sel {pal["bg4"]}

# --> palette
set -l red {pal["red"]}
set -l green {pal["green"]}
set -l yellow {pal["yellow"]}
set -l orange {pal["orange"]}
set -l blue {pal["blue"]}
set -l magenta {pal["magenta"]}
set -l purple {pal["purple"]}
set -l cyan {pal["cyan"]}
set -l gray {pal["gray"]}

# Syntax Highlighting
set -g fish_color_normal $fg
set -g fish_color_command $blue
set -g fish_color_param $fg
set -g fish_color_keyword $red
set -g fish_color_quote $green
set -g fish_color_redirection $purple
set -g fish_color_end $orange
set -g fish_color_error $red
set -g fish_color_gray $gray
set -g fish_color_selection --background=$sel
set -g fish_color_search_match --background=$sel
set -g fish_color_operator $purple
set -g fish_color_escape $magenta
set -g fish_color_autosuggestion $gray
set -g fish_color_cancel $red

# Prompt
set -g fish_color_cwd $yellow
set -g fish_color_user $cyan
set -g fish_color_host $blue

# Completion Pager
set -g fish_pager_color_progress $gray
set -g fish_pager_color_prefix $purple
set -g fish_pager_color_completion $fg
set -g fish_pager_color_description $gray
    """
    return template

fish = Module("fish", gen_template)

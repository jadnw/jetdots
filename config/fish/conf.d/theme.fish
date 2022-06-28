# Batwing colorscheme for Fish
# ~/.config/fish/conf.d/theme.fish

# --> special
set -l fg c1c5cf
set -l sel 414754

# --> palette
set -l red df8284
set -l green 93c68c
set -l yellow e8ce9b
set -l orange f4a582
set -l blue 75a8f9
set -l magenta e397bb
set -l purple 9d95f2
set -l cyan 7be0ec
set -l gray 768195

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
    

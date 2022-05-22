# ·▄▄▄▪  .▄▄ ·  ▄ .▄
# ▐▄▄·██ ▐█ ▀. ██▪▐█
# ██▪ ▐█·▄▀▀▀█▄██▀▐█
# ██▌.▐█▌▐█▄▪▐███▌▐▀
# ▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ ·
# Created by: Jaden Wu
# Github: @jadnw
# Email: jadenwu137@protonmail.com

# Disable fish_greeting
set -U fish_greeting

# Add paths
fish_add_path -g ~/.local/bin

if status is-interactive
    # Commands to run in interactive sessions can go here
end

# Alias
alias ll "ls -la"
alias ga "git add -A"
alias gp "git push"
alias z "zvim"

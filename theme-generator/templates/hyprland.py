from classes.module import Module
from lib.util import remove_hash_from_pal

def gen_template(theme):
    pal = remove_hash_from_pal(theme["palette"])
    template = f"""# VARIABLES
$term=foot
$browser=qutebrowser
$devbrowser=MOZ_ENABLE_WAYLAND=1 firefox-developer-edition
$launcher=$HOME/.config/hypr/scripts/launcher toggle
$colorpicker=$HOME/.config/hypr/scripts/colorpicker toggle
$documents=$HOME/.config/hypr/scripts/documents toggle
$recorder=$HOME/.config/hypr/scripts/recorder toggle
$screenshot=$HOME/.config/hypr/scripts/screenshot toggle
$powermenu=$HOME/.config/waybar/scripts/power-hyprland toggle

# MONITORS
monitor=HDMI-A-1,1920x1080@60,0x0,1
workspace=HDMI-A-1,1

input {{
  kb_layout=us
  kb_variant=
  kb_model=
  kb_options=
  kb_rules=
  follow_mouse=0
  repeat_delay=450
  repeat_rate=60
}}

general {{
  sensitivity=1.0 # for mouse cursor
  main_mod=SUPER
  gaps_in=2
  gaps_out=2
  border_size=2
  col.active_border=0xff{pal["accent"]}
  col.inactive_border=0xff{pal["bg3"]}
  apply_sens_to_raw=0 # whether to apply the sensitivity to raw input (e.g. used by games where you aim using your mouse)
  damage_tracking=full # leave it on full unless you hate your GPU and want to make it suffer
}}

decoration {{
  rounding=1
  blur=0
  blur_size=8 # minimum 1
  blur_passes=1 # minimum 1, more passes = more resource intensive.
  # Your blur "amount" is blur_size * blur_passes, but high blur_size (over around 5-ish) will produce artifacts.
  # if you want heavy blur, you need to up the blur_passes.
  # the more passes, the more you can up the blur_size without noticing artifacts.
}}

animations {{
  enabled=1
  animation=windows,1,6,default
  animation=borders,1,6,default
  animation=fadein,1,6,default
  animation=workspaces,1,6,default
}}

dwindle {{
  pseudotile=0 # enable pseudotiling on dwindle
}}

# WINDOW RULES
# for windows named/classed as abc and xyz
#windowrule=move 69 420,abc
#windowrule=size 420 69,abc
#windowrule=tile,xyz
#windowrule=float,abc
#windowrule=pseudo,abc
#windowrule=monitor 0,xyz

windowrule=float,imv
windowrule=float,nm-connection-editor
windowrule=float,rofi
windowrule=float,pavucontrol
windowrule=float,title:btop
windowrule=float,title:File Operation Progress
windowrule=float,title:Picture in picture
windowrule=float,title:Save File
windowrule=size 60% 60%,title:btop
windowrule=size 80% 80%,imv
windowrule=size 50% 50%,pavucontrol
windowrule=move 20% 20%,title:btop
windowrule=move 10% 10%,imv
windowrule=move 25% 25%,pavucontrol

# APPLICATION BIDINGS
bind=SUPER,Return,exec,$term
bind=SUPERSHIFT,B,exec,$browser
bind=SUPERSHIFT,W,exec,$devbrowser
bind=SUPER,O,exec,$launcher
bind=SUPER,C,exec,$colorpicker
bind=SUPER,D,exec,$documents
bind=SUPER,R,exec,$recorder
bind=SUPER,P,exec,$screenshot
bind=SUPERSHIFT,Q,exec,$powermenu

# WINDOWS
bind=SUPER,Space,togglefloating,
bind=SUPER,F,fullscreen,
bind=SUPER,S,togglesplit,
bind=SUPERSHIFT,C,killactive,
bind=SUPERSHIFT,P,pseudo,

# MOVE AROUND
bind=SUPER,h,resizeactive,-20 0
bind=SUPER,l,resizeactive,20 0
bind=SUPER,k,cyclenext
bind=SUPER,j,cyclenext

bind=SUPERSHIFT,h,movewindow,l
bind=SUPERSHIFT,l,movewindow,r
bind=SUPERSHIFT,k,movewindow,u
bind=SUPERSHIFT,j,movewindow,d

bind=SUPER,1,workspace,1
bind=SUPER,2,workspace,2
bind=SUPER,3,workspace,3
bind=SUPER,4,workspace,4
bind=SUPER,5,workspace,5
bind=SUPER,6,workspace,6

bind=SUPERSHIFT,exclam,movetoworkspacesilent,1
bind=SUPERSHIFT,at,movetoworkspacesilent,2
bind=SUPERSHIFT,numbersign,movetoworkspacesilent,3
bind=SUPERSHIFT,dollar,movetoworkspacesilent,4
bind=SUPERSHIFT,percent,movetoworkspacesilent,5
bind=SUPERSHIFT,asciicircum,movetoworkspacesilent,6

bind=SUPERALT,1,movetoworkspace,1
bind=SUPERALT,2,movetoworkspace,2
bind=SUPERALT,3,movetoworkspace,3
bind=SUPERALT,4,movetoworkspace,4
bind=SUPERALT,5,movetoworkspace,5
bind=SUPERALT,6,movetoworkspace,6

# FOCUS MONITORS
bind=SUPERALT,up,focusmonitor,u
bind=SUPERALT,down,focusmonitor,d

# MOVING WORKSPACES
bind=SUPERCTRLSHIFT,down,movecurrentworkspacetomonitor,d
bind=SUPERCTRLSHIFT,up,movecurrentworkspacetomonitor,u
bind=SUPERCTRLSHIFT,left,movecurrentworkspacetomonitor,l
bind=SUPERCTRLSHIFT,right,movecurrentworkspacetomonitor,r

# RESIZE
bind=ALT,h,resizeactive,-20 0
bind=ALT,l,resizeactive,20 0
bind=ALT,k,resizeactive,0 -20
bind=ALT,j,resizeactive,0 20

# MOVE ACTIVE
bind=SUPERALT,h,moveactive,-20 0
bind=SUPERALT,l,moveactive,20 0
bind=SUPERALT,k,moveactive,0 -20
bind=SUPERALT,j,moveactive,0 20

# AUTOSTART
exec-once=$HOME/.config/hypr/scripts/import-gsettings
exec-once=swaybg -i ~/.config/wallpapers/wallpaper.jpg
exec-once=dunst -conf ~/.config/dunst/dunstrc-wl
exec-once=swayidle -w timeout 300 'swaylock -f' before-sleep 'swaylock -f'
exec-once=$HOME/.config/waybar/launch-hyprland
    """
    return template

hyprland = Module("hyprland", gen_template)

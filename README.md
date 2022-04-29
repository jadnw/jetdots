<h1 align="center">JETDOTS</h1>

<div align="center">
  <img
    width="196px"
    height="196px"
    src="https://raw.githubusercontent.com/j4d3nw/jetdots/main/media/logo.svg"
    alt="Jetdots Logo"
  />
</div>

<p align="center">
  <a href="https://github.com/j4d3nw/jetdots/stargazers"><img src="https://img.shields.io/github/stars/j4d3nw/jetdots?colorA=1b2125&colorB=a7c080&style=for-the-badge"></a>
  <a href="https://github.com/j4d3nw/jetdots/issues"><img src="https://img.shields.io/github/issues/j4d3nw/jetdots?colorA=1b2125&colorB=f08789&style=for-the-badge"></a>
  <a href="https://github.com/j4d3nw/jetdots/contributors"><img src="https://img.shields.io/github/contributors/j4d3nw/jetdots?colorA=1b2125&colorB=60b69f&style=for-the-badge"></a>
  <a href="https://github.com/j4d3nw/jetdots/network/members"><img src="https://img.shields.io/github/forks/j4d3nw/jetdots?colorA=1b2125&colorB=b3a8f9&style=for-the-badge"></a>
</p>

<p align="center">
  My glorious dotfiles for Arch Linux setup (BSPWM, SwayWM, RiverWM) with custom theme generator
</p>

### Table of contents
- [Overview](#overview)
- [Applications](#applications)
- [Requirements](#requirements)
- [Installation](#installation)
- [Generate Your Own Theme](#generate-your-own-theme)
- [Acknowledgements](#acknowledgements)

## Overview

## Applications

You can choose between Wayland and X to install on your Arch Linux system.

Packer Manager:
- [paru](https://github.com/Morganamilo/paru) - Feature packed AUR helper

Login Manager:
- [sddm](https://github.com/sddm/sddm) - Login Manager (Wayland & X)
- [sddm-sugar-candy-git](https://github.com/Kangie/sddm-sugar-candy) - A fancy theme for SDDM

Tiling Window Managers:
- [sway](https://github.com/swaywm/sway) - Wayland
- [river-git](https://github.com/riverwm/river) - Wayland
- [bspwm](https://github.com/baskerville/bspwm) - X

Applications:
- [alacritty](https://github.com/alacritty/alacritty) - Terminal emulator (Wayland & X)
- [btop](https://github.com/aristocratos/btop) - System monitor (Wayland & X)
- [chromium](https://github.com/chromium/chromium) - Browser (Wayland & X - alternative)
- [dunst](https://github.com/dunst-project/dunst) - Notification daemon (Wayland & X)
- [feh](https://github.com/derf/feh) - Image viewer (X)
- [ffmpeg](https://github.com/FFmpeg/FFmpeg) - Screen recorder (X)
- [fish](https://github.com/fish-shell/fish-shell) - Shell
- [foot](https://codeberg.org/dnkl/foot) - Terminal emulator (Wayland - alternative)
- [flameshot](https://github.com/flameshot-org/flameshot) - Screenshot application
- [grim](https://github.com/emersion/grim) - Screenshot application/Color picker(with [ImageMagick](https://github.com/ImageMagick/ImageMagick6)) (Wayland)
- [imv](https://sr.ht/~exec64/imv/) - Image viewer (Wayland)
- [neovim](https://github.com/neovim/neovim) - Text editor
- [picom-jonaburg-git](https://github.com/jonaburg/picom) - X compositor (X)
- [qutebrowser](https://github.com/qutebrowser/qutebrowser) - Default browser (Wayland & X)
- [redshift](http://jonls.dk/redshift/) - Nightlight (X)
- [rofi-lbonn-wayland-git](https://github.com/lbonn/rofi) - Window Switcher, dmenu replacement (Wayland & X)
- [wf-recorder](https://github.com/ammen99/wf-recorder) - Screen recorder (Wayland)
- [wlsunset](https://sr.ht/~kennylevinsen/wlsunset/) - Nightlight (Wayland)
- [xcolor](https://github.com/Soft/xcolor) - Color picker (X)
- [zathura](https://github.com/pwmt/zathura) - Document Viewer (Wayland & X)

Clipboard Managers:
- [xclip](https://github.com/astrand/xclip) - Clipboard manager (X)
- [wl-clipboard](https://github.com/bugaevc/wl-clipboard) - Clipboard manager (Wayland)

Screen Lockers:
- [swaylock-effects-git](https://github.com/mortie/swaylock-effects) - Screen locker (Wayland)
- [betterlockscreen](https://github.com/betterlockscreen/betterlockscreen) - Screen Locker (X)

Bars:
- [Waybar](https://github.com/Alexays/Waybar) - A highly customizable bar (Wayland)
- [Polybar](https://github.com/polybar/polybar) - A fast and easy-to-use status bar

## Requirements

- [Arch Linux](https://archlinux.org)
- [python 3.10+](https://www.python.org)
- [git](https://git-scm.com)
- [fish shell](https://fishshell.com)

## Installation

1. Clone this repository

```bash
git clone https://github.com/j4d3nw/jetdots.git
```

2. Make scripts executable

```bash
cd jetdots
chmod -R +x scripts
```

3. Run install script and follow the instructions to setup your system

```bash
# Run from root directory
./scripts/install
```

#### How to uninstall

- Run uninstall script to remove partially packages and configurations

```bash
./scripts/uninstall
```

## Generate Your Own Theme

You can **generate your own theme** (colorscheme) for Jetdots with these steps.

1. Create a new schema json file at *jetdots/theme-generator/schemas/\<**your-theme-name**\>.json*

For example, this is gemstones.json (Jetdots default theme)

```json
{
  "name": "Gemstones",
  "palette": {
    "bg0": "#15191c",
    "bg1": "#20262a",
    "bg2": "#2b3339",
    "bg3": "#3c4750",
    "bg4": "#4e5c67",
    "fg0": "#d2d9de",
    "fg1": "#c6ced4",
    "fg2": "#b3bec7",
    "fg3": "#a5b2bd",
    "accent": "#93c68c",
    "black": "#53605c",
    "white": "#c6ced4",
    "red": "#f08789",
    "green": "#93c68c",
    "blue": "#80b1d6",
    "orange": "#f4a582",
    "yellow": "#e8ce9b",
    "cyan": "#80c2c5",
    "teal": "#6dc5aa",
    "magenta": "#e397bb",
    "purple": "#b3a8f9",
    "gray": "#667a8a"
  }
}
```

> Note: If there is a missing key, theme generator will cause an error.

2. Open *jetdots/theme-generator/theme.py* and edit line 34 (SCHEMA_NAME not
including extension *.json*)

```python
SCHEMA_NAME = "your theme name"
```

3. Generate theme

```bash
path/to/jetdots/theme-generator/generate
```

If you got a \<your theme name\> directory inside *jetdots/themes*, you have successfully
generated your theme. Now, take you to the last step.

4. Apply your theme

Run this command to apply your theme

```bash
./scripts/theme <your theme name>
```

If you created multiple themes, you can list theme to see theme names.

```bash
./scripts/theme list
```

#### Change wallpapers

To change desktop wallpaper and lockscreen wallpaper, you can rename
your files to "wallpaper.jpg" and "lockscreen.jpg" and copy theme to 
*~/.config/wallpapers* directory.

To change greeting wallpaper (login background), run this command:

```bash
sudo rsync/cp path/to/your-greeting-wallpaper.jpg /usr/share/sddm/themes/sugar-candy/
```

> Note: All wallpaper files with extension **.jpg**

## Acknowledgements

- [j4d3nw/gemstones](https://github.com/j4d3nw/gemstones)
- [j4d3nw/gemstones-gtk](https://github.com/j4d3nw/gemstones-gtk)
- [j4d3nw/nvim](https://github.com/j4d3nw/nvim)

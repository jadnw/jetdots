<h1 align="center">JETDOTS</h1>
<p align="center">
  My glorious dotfiles for Arch Linux setup (BSPWM, SwayWM, RiverWM) with custom theme generator
</p>

<br /><br />
<div align="center">
  <img
    width="196px"
    height="196px"
    src="https://raw.githubusercontent.com/jadnw/jetdots/main/media/logo.svg"
    alt="Jetdots Logo"
  />
</div>
<br /><br />

<p align="center">
  <a href="https://github.com/jadnw/jetdots/stargazers"><img src="https://img.shields.io/github/stars/jadnw/jetdots?colorA=1b2125&colorB=a7c080&style=for-the-badge"></a>
  <a href="https://github.com/jadnw/jetdots/issues"><img src="https://img.shields.io/github/issues/jadnw/jetdots?colorA=1b2125&colorB=f08789&style=for-the-badge"></a>
  <a href="https://github.com/jadnw/jetdots/contributors"><img src="https://img.shields.io/github/contributors/jadnw/jetdots?colorA=1b2125&colorB=60b69f&style=for-the-badge"></a>
  <a href="https://github.com/jadnw/jetdots/network/members"><img src="https://img.shields.io/github/forks/jadnw/jetdots?colorA=1b2125&colorB=b3a8f9&style=for-the-badge"></a>
</p>

<p align="center"></p>


### Table of contents
- [Overview](#overview)
- [Applications](#applications)
- [Requirements](#requirements)
- [Installation](#installation)
- [Generate Your Own Theme](#generate-your-own-theme)
- [FAQ](#faq)
- [Acknowledgements](#acknowledgements)

## Overview

Some fancy screenshots on River. They look cool, right? Jetdots comes with a slogan
"Do not waste any pixels for the gaps on your tiling window managers". Because of
that, it has no gaps.

<div align="center">
  <img
    src="https://raw.githubusercontent.com/jadnw/jetdots/main/media/screenshots/idle.png"
    alt="Idle - No apps opened"
  />
</div>

<div align="center">
  <img
    src="https://raw.githubusercontent.com/jadnw/jetdots/main/media/screenshots/busy.png"
    alt="Busy - Apps opened"
  />
</div>

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
- [dunst](https://github.com/dunst-project/dunst) - Notification daemon (Wayland & X)
- [feh](https://github.com/derf/feh) - Image viewer (X)
- [ffmpeg](https://github.com/FFmpeg/FFmpeg) - Screen recorder (X)
- [fish](https://github.com/fish-shell/fish-shell) - Shell
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
- [swaylock-effects](https://github.com/mortie/swaylock-effects) - Screen locker (Wayland)
- [betterlockscreen](https://github.com/betterlockscreen/betterlockscreen) - Screen Locker (X)

Bars:
- [Waybar](https://github.com/Alexays/Waybar) - A highly customizable bar (Wayland)
- [Polybar](https://github.com/polybar/polybar) - A fast and easy-to-use status bar (X)

Fonts:
- [Josevka](https://github.com/jadnw/Josevka) - A custom Iosevka fonts built from source

## Requirements

- [Arch Linux](https://archlinux.org)
- [git](https://git-scm.com)
- [fish](https://fishshell.com)
- [python 3.10+](https://www.python.org) (Optional) - For theme generator

## Installation

1. Clone this repository

```bash
git clone https://github.com/jadnw/jetdots.git
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

Check the example of a json schema in `theme-generator/schemas/manhattan.json`

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

## FAQ

1. I lock my screen on BSPWM and boom, blank screen. How can I fix it?
Betterlockscreen needs a cached image to show as background. You can run this command
only once to create it.

```bash
betterlockscreen --update ~/.config/wallpapers/lockscreen.jpg
```

## Acknowledgements

- [jadnw/gemstones](https://github.com/jadnw/gemstones)
- [jadnw/gemstones-gtk](https://github.com/jadnw/gemstones-gtk)
- [jadnw/nvim](https://github.com/jadnw/nvim)

# .▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .▄▄▄▄· ▄▄▄        ▄▄▌ ▐ ▄▌.▄▄ · ▄▄▄ .▄▄▄  
# ▐▀•▀█ █▪██▌•██  ▀▄.▀·▐█ ▀█▪▀▄ █·▪     ██· █▌▐█▐█ ▀. ▀▄.▀·▀▄ █·
# █▌·.█▌█▌▐█▌ ▐█.▪▐▀▀▪▄▐█▀▀█▄▐▀▀▄  ▄█▀▄ ██▪▐█▐▐▌▄▀▀▀█▄▐▀▀▪▄▐▀▀▄ 
# ▐█▪▄█·▐█▄█▌ ▐█▌·▐█▄▄▌██▄▪▐█▐█•█▌▐█▌.▐▌▐█▌██▐█▌▐█▄▪▐█▐█▄▄▌▐█•█▌
# ·▀▀█.  ▀▀▀  ▀▀▀  ▀▀▀ ·▀▀▀▀ .▀  ▀ ▀█▄▀▪ ▀▀▀▀ ▀▪ ▀▀▀▀  ▀▀▀ .▀  ▀
# Created by: Jaden Wu
# Github: @jadnw
# Email: jadenwu137@protonmail.com
from theme import colors

config.load_autoconfig(True)
c.auto_save.session = True
c.changelog_after_upgrade = 'patch'

# Search Engine
c.url.searchengines = { 'DEFAULT': 'https://www.google.com/search?hl=en&q={}' }
# Theme
c.colors.completion.category.bg = colors['bg0']
c.colors.completion.category.border.bottom = colors['bg1']
c.colors.completion.category.border.top = colors['bg1']
c.colors.completion.category.fg = colors['fg3']
c.colors.completion.even.bg = colors['bg1']
c.colors.completion.fg = colors['fg1']
c.colors.completion.item.selected.bg = colors['accent']
c.colors.completion.item.selected.border.bottom = colors['bg2']
c.colors.completion.item.selected.border.top = colors['bg2']
c.colors.completion.item.selected.fg = colors['bg0']
c.colors.completion.item.selected.match.fg = colors['red']
c.colors.completion.match.fg = colors['blue']
c.colors.completion.odd.bg = colors['bg2']
c.colors.completion.scrollbar.bg = colors['bg0']
c.colors.completion.scrollbar.fg = colors['bg2']
c.colors.contextmenu.disabled.bg = colors['bg4']
c.colors.contextmenu.disabled.fg = colors['fg3']
c.colors.contextmenu.menu.bg = colors['bg1']
c.colors.contextmenu.menu.fg = colors['fg1']
c.colors.contextmenu.selected.bg = colors['bg2']
c.colors.contextmenu.selected.fg = colors['fg1']
c.colors.downloads.bar.bg = colors['bg4']
c.colors.downloads.error.bg = colors['bg4']
c.colors.downloads.error.fg = colors['red']
c.colors.downloads.start.bg = colors['bg4']
c.colors.downloads.start.fg = colors['fg1']
c.colors.downloads.stop.bg = colors['bg4']
c.colors.downloads.stop.fg = colors['fg1']
c.colors.hints.bg = colors['bg1']
c.colors.hints.fg = colors['fg1']
c.colors.hints.match.fg = colors['blue']
c.colors.keyhint.bg = colors['bg2']
c.colors.keyhint.fg = colors['fg1']
c.colors.keyhint.suffix.fg = colors['purple']
c.colors.messages.error.bg = colors['bg2']
c.colors.messages.error.border = colors['bg2']
c.colors.messages.error.fg = colors['red']
c.colors.messages.info.bg = colors['bg2']
c.colors.messages.info.border = colors['bg2']
c.colors.messages.info.fg = colors['fg1']
c.colors.messages.warning.bg = colors['bg2']
c.colors.messages.warning.border = colors['bg2']
c.colors.messages.warning.fg = colors['yellow']
c.colors.prompts.bg = colors['bg0']
c.colors.prompts.border = '1px ' + colors['bg3']
c.colors.prompts.fg = colors['fg1']
c.colors.prompts.selected.bg = colors['bg0']
c.colors.prompts.selected.fg = colors['fg1']
c.colors.statusbar.caret.bg = colors['bg0']
c.colors.statusbar.caret.fg = colors['fg3']
c.colors.statusbar.caret.selection.bg = colors['bg2']
c.colors.statusbar.caret.selection.fg = colors['fg1']
c.colors.statusbar.command.bg = colors['bg1']
c.colors.statusbar.command.fg = colors['fg1']
c.colors.statusbar.command.private.bg = colors['magenta']
c.colors.statusbar.command.private.fg = colors['bg0']
c.colors.statusbar.insert.bg = colors['bg0']
c.colors.statusbar.insert.fg = colors['fg1']
c.colors.statusbar.normal.bg = colors['bg0']
c.colors.statusbar.normal.fg = colors['fg1']
c.colors.statusbar.passthrough.bg = colors['bg1']
c.colors.statusbar.passthrough.fg = colors['fg1']
c.colors.statusbar.private.bg = colors['magenta']
c.colors.statusbar.private.fg = colors['bg0']
c.colors.statusbar.progress.bg = colors['fg3']
c.colors.statusbar.url.error.fg = colors['red']
c.colors.statusbar.url.fg = colors['fg1']
c.colors.statusbar.url.hover.fg = colors['fg1']
c.colors.statusbar.url.success.http.fg = colors['yellow']
c.colors.statusbar.url.success.https.fg = colors['green']
c.colors.statusbar.url.warn.fg = colors['orange']
c.colors.tabs.bar.bg = colors['bg0']
c.colors.tabs.even.bg = colors['bg0']
c.colors.tabs.even.fg = colors['gray']
c.colors.tabs.indicator.error = colors['yellow']
c.colors.tabs.indicator.start = colors['fg1']
c.colors.tabs.indicator.stop = colors['fg1']
c.colors.tabs.indicator.system = 'rgb'
c.colors.tabs.odd.bg = colors['bg0']
c.colors.tabs.odd.fg = colors['gray']
c.colors.tabs.pinned.even.bg = colors['bg0']
c.colors.tabs.pinned.even.fg = colors['fg1']
c.colors.tabs.pinned.odd.bg = colors['bg0']
c.colors.tabs.pinned.odd.fg = colors['fg1']
c.colors.tabs.pinned.selected.even.bg = colors['fg3']
c.colors.tabs.pinned.selected.even.fg = colors['purple']
c.colors.tabs.pinned.selected.odd.bg = colors['fg3']
c.colors.tabs.pinned.selected.odd.fg = colors['purple']
c.colors.tabs.selected.even.bg = colors['bg2']
c.colors.tabs.selected.even.fg = colors['fg0']
c.colors.tabs.selected.odd.bg = colors['bg2']
c.colors.tabs.selected.odd.fg = colors['fg0']
# c.colors.webpage.bg = colors['bg0']
c.colors.webpage.darkmode.enabled = False
c.colors.webpage.preferred_color_scheme = 'dark'
c.completion.height = '25%'
c.completion.scrollbar.padding = 0
c.completion.scrollbar.width = 15
c.content.autoplay = False
c.content.blocking.enabled = True
c.content.blocking.method = 'both'
c.content.cookies.accept = 'no-3rdparty'
c.content.javascript.can_access_clipboard = True
c.content.pdfjs = True
c.content.user_stylesheets = []
c.downloads.location.directory = '~/Downloads'
c.downloads.location.prompt = False
c.downloads.location.suggestion = 'filename'
c.downloads.position = 'bottom'
c.downloads.remove_finished = 5000
c.editor.command = ['nvim', '-f', '{file}', '-c', 'normal {line}G{column0}l']
c.fileselect.folder.command = ['alacritty', '-e', 'nnn', '-p' '{}']
c.fileselect.handler = 'external'
c.fileselect.multiple_files.command = ['alacritty', '-e', 'nnn', '-p' '{}']
c.fileselect.single_file.command = ['alacritty', '-e', 'nnn', '-p' '{}']
c.fonts.completion.category = 'default_size Iosevka Nerd Font'
c.fonts.completion.entry = 'default_size Iosevka Nerd Font'
c.fonts.contextmenu = 'default_size Iosevka Nerd Font'
c.fonts.debug_console = 'default_size Iosevka Nerd Font'
c.fonts.default_family = ['Barlow Semi Condensed']
c.fonts.default_size = '11pt'
c.fonts.downloads = 'default_size Iosevka Nerd Font'
c.fonts.hints = 'default_size Iosevka Nerd Font'
c.fonts.keyhint = 'default_size Iosevka Nerd Font'
c.fonts.messages.error = 'default_size Iosevka Nerd Font'
c.fonts.messages.info = 'default_size Iosevka Nerd Font'
c.fonts.messages.warning = 'default_size Iosevka Nerd Font'
c.fonts.prompts = 'default_size Iosevka Nerd Font'
c.fonts.statusbar = 'default_size Iosevka Nerd Font'
c.fonts.tabs.selected = 'default_size Iosevka Nerd Font'
c.fonts.tabs.unselected = 'default_size Iosevka Nerd Font'
c.fonts.web.family.fixed = 'Iosevka Nerd Font'
c.fonts.web.family.sans_serif = 'Barlow Semi Condensed'
c.fonts.web.family.serif = 'Noto Serif'
c.fonts.web.family.standard = 'Barlow Semi Condensed'
c.fonts.web.size.default = 16
c.fonts.web.size.default_fixed = 16
c.fonts.web.size.minimum = 16
c.hints.border = '1px solid ' + colors['fg3']
c.hints.padding = {'top': 5, 'bottom': 5, 'left': 5, 'right': 5}
c.hints.radius = 5
c.input.insert_mode.auto_load = True
c.keyhint.radius = 5
c.messages.timeout = 5000
c.new_instance_open_target = 'tab-bg-silent'
c.prompt.radius = 5
c.qt.force_platformtheme = 'gtk3'
c.qt.chromium.low_end_device_mode = 'never'
c.scrolling.smooth = True
c.spellcheck.languages = ['en-US']
c.statusbar.padding = {'top': 5, 'bottom': 5, 'left': 5, 'right': 5}
c.tabs.indicator.padding = {'top': 0, 'bottom': 0, 'left': 0, 'right': 10}
c.tabs.indicator.width = 2
c.tabs.padding = {'top': 5, 'bottom': 5, 'left': 5, 'right': 5}
c.tabs.position = 'top'
c.url.default_page = 'https://google.com/'
c.url.start_pages = [ 'https://google.com/' ]
c.window.hide_decoration = True
config.bind(",m", 'hint links spawn mpv {hint-url}')
config.bind('O', 'set-cmd-text -s :open -t -s')
config.bind('o', 'set-cmd-text -s :open -s')

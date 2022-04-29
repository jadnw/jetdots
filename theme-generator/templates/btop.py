from classes.module import Module

def gen_template(theme):
    pal = theme["palette"]
    template = f"""# {theme["name"]} colorscheme for btop
# ~/.config/btop/themes/theme.theme

# All graphs and meters can be gradients
# For single color graphs leave "mid" and "end" variable empty.
# Use "start" and "end" variables for two color gradient
# Use "start", "mid" and "end" for three color gradient

# Main background, empty for terminal default, need to be empty if you want transparent background
theme[main_bg]="{pal["bg2"]}"

# Main text color
theme[main_fg]="{pal["fg1"]}"

# Title color for boxes
theme[title]="{pal["fg1"]}"

# Highlight color for keyboard shortcuts
theme[hi_fg]="{pal["red"]}"

# Background color of selected items
theme[selected_bg]="{pal["bg4"]}"

# Foreground color of selected items
theme[selected_fg]="{pal["yellow"]}"

# Color of inactive/disabled text
theme[inactive_fg]="{pal["fg3"]}"  

# Color of text appearing on top of graphs, i.e uptime and current network graph scaling
theme[graph_text]="{pal["fg1"]}"

# Misc colors for processes box including mini cpu graphs, details memory graph and details status text
theme[proc_misc]="{pal["accent"]}"

# Cpu box outline color
theme[cpu_box]={pal["bg4"]}""

# Memory/disks box outline color
theme[mem_box]="{pal["bg4"]}"

# Net up/down box outline color
theme[net_box]="{pal["bg4"]}"

# Processes box outline color
theme[proc_box]="{pal["bg4"]}"

# Box divider line and small boxes line color
theme[div_line]="{pal["bg4"]}"

# Temperature graph colors
theme[temp_start]="{pal["green"]}"
theme[temp_mid]="{pal["yellow"]}"
theme[temp_end]="{pal["red"]}"

# CPU graph colors
theme[cpu_start]="{pal["green"]}"
theme[cpu_mid]="{pal["yellow"]}"
theme[cpu_end]="{pal["red"]}"

# Mem/Disk free meter
theme[free_start]="{pal["green"]}"
theme[free_mid]="{pal["yellow"]}"
theme[free_end]="{pal["red"]}"

# Mem/Disk cached meter
theme[cached_start]="{pal["green"]}"
theme[cached_mid]="{pal["yellow"]}"
theme[cached_end]="{pal["red"]}"

# Mem/Disk available meter
theme[available_start]="{pal["green"]}"
theme[available_mid]="{pal["yellow"]}"
theme[available_end]="{pal["red"]}"

# Mem/Disk used meter
theme[used_start]="{pal["green"]}"
theme[used_mid]="{pal["yellow"]}"
theme[used_end]="{pal["red"]}"

# Download graph colors
theme[download_start]="{pal["green"]}"
theme[download_mid]="{pal["yellow"]}"
theme[download_end]="{pal["red"]}"

# Upload graph colors
theme[upload_start]="{pal["green"]}"
theme[upload_mid]="{pal["yellow"]}"
theme[upload_end]="{pal["red"]}"

# Process box color gradient for threads, mem and cpu usage
theme[process_start]="{pal["green"]}"
theme[process_mid]="{pal["yellow"]}"
theme[process_end]="{pal["red"]}"
"""

    return template

btop = Module("btop", gen_template)

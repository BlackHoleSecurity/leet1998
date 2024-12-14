import os, socket
import curses
import asyncio

myip = None
banner = """
 _                                 
|_|___ ___ ___ ___ ___ ___ ___ ___ 
| | . |_ -|  _| .'|   |   | -_|  _|
|_|  _|___|___|__,|_|_|_|_|___|_|  
  |_| author: Gameye98                             
  Date: Sat Dec 14 01:14:12 2024
  GitHub: Gameye98
  Telegram: @deletuserbot
  Team:
    - BlackHole Security
        https://github.com/BlackHoleSecurity
    - Schadenfreude
        https://t.me/schdenfreude
"""

async def pingIPAddress(ip):
    ping = os.popen(f"ping -c 1 {ip}").read()
    if "1 received" in ping:
        if ip == myip:
            return "IP: "+ip+" You"
        else:
            return "IP: "+ip+" Unknown"
    else:
        return None

async def ipscansocket_main(stdscr):
    global myip
    ifconfig = os.popen("ifconfig").read()
    ifconfig = [x.strip() for x in ifconfig.split("\n")]
    while "" in ifconfig: ifconfig.remove("")
    inet = list(filter(lambda x: x.startswith("inet"), ifconfig))
    inet = list(map(lambda x: x.split(" ")[1], inet))
    ipaddrs = []
    for ip in inet:
        if ip.startswith("127") or ip.startswith("10"):
            continue
        myip = ip
        iprange = ip.split(".")[-1]
        ip = ip[0:len(ip)-len(iprange)]
        funcls = [pingIPAddress(ip+str(i)) for i in range(1,256)]
        ls = await asyncio.gather(*funcls)
        ls = list(filter(lambda x: x != None, ls))
        ipaddrs.extend(ls)
    show_dialog(stdscr, ipaddrs, True)

def draw_banner(stdscr):
    stdscr.clear()
    maxy = 0
    for k, v in enumerate(banner.splitlines()):
        stdscr.addstr(k, 2, v)
        maxy = k
    return maxy

def show_dialog(stdscr, data, islist=False):
    height = 20
    width = curses.COLS
    max_y, max_x = stdscr.getmaxyx()
    y = (max_y-height) // 2
    x = (max_x-width) // 2
    lines = data if islist else data.splitlines()
    fixedlines = []
    for _, v in enumerate(lines):
        if len(v) > (width-4):
            while len(v) > 0:
                fixedlines.append(v[:width-4])
                v = v[width-4:]
        else:
            fixedlines.append(v)
    start_line = 0
    visible_lines = height-2
    dialogwin = curses.newwin(height, width, y, x)
    max_lines = len(fixedlines)
    while True:
        dialogwin.clear()
        dialogwin.border()
        for k, v in enumerate(fixedlines[start_line:start_line + visible_lines]):
            dialogwin.addstr(k+1, 2, v)
        dialogwin.refresh()
        # Handle user input
        key = stdscr.getch()
        if key == curses.KEY_UP and start_line > 0:  # Scroll up
            start_line -= 1
        elif key == curses.KEY_DOWN and start_line + visible_lines < max_lines:  # Scroll down
            start_line += 1
        elif key in (27, ord('q')):  # Exit on 'q' or ESC
            break

def draw_button(win, text, y, x, selected=False):
    """ Draw a button with the specified text at the given position """
    button_str = f"[{text}]"
    color_pair = curses.color_pair(2) if selected else curses.color_pair(1)
    win.addstr(y, x, button_str, color_pair | curses.A_BOLD)
    return len(button_str)  # Return width of the button

def draw_separator(win, y, width):
    """ Draw a separator line at the given position with the specified width """
    separator_str = '-' * width
    win.addstr(y, 0, separator_str, curses.color_pair(3))

def show_message(message):
    """ Display a popup message """
    height, width = 5, len(message) + 6
    y, x = (curses.LINES - height) // 2, (curses.COLS - width) // 2
    win = curses.newwin(height, width, y, x)
    win.border()
    win.addstr(2, 3, message)
    win.refresh()
    win.getch()  # Wait for user input
    #curses.delwin(win)  # Clean up window

def main(stdscr):
    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)  # Normal
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Selected
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Separator

    # Turn off cursor display
    curses.curs_set(0)

    # Set up initial screen
    stdscr.clear()
    stdscr.refresh()

    # Create a new window for the dialog
    height, width = stdscr.getmaxyx()
    win = curses.newwin(height, width, 0, 0)

    # Draw banner
    banner_maxy = draw_banner(win)

    # Define button positions and text
    button_text = ["Scan via NMAP (fast)", "Scan via PythonSocket (slow)", "Scan via ARP (very fast)"]
    button_widths = [len(text) + 2 for text in button_text]  # Calculate widths including brackets
    #button_x_positions = [2, 15, 28]  # X positions of buttons

    # Draw buttons
    selected_button = 0  # Track selected button index
    button_height = banner_maxy+2
    for i, text in enumerate(button_text):
        width = draw_button(win, text, button_height, 6, selected=(i == selected_button))
        button_height += 2

    # Draw separator
    #draw_separator(win, button_height+2, width)
    win.addstr(button_height+2, 2, "Copyright (C) by Gameye98")

    # Refresh the screen to display changes
    win.refresh()

    # Main loop to handle user input
    while True:
        key = win.getch()  # Wait for user input

        if key == ord('\n') or key == curses.KEY_RIGHT:  # Check if Enter key is pressed
            if selected_button == 0:  # Check if Button 1 is selected
                #show_message("You pressed Button 1!")
                show_dialog(stdscr, os.popen("nmap -sP 192.168.43.0/24").read())
            elif selected_button == 1:
                asyncio.run(ipscansocket_main(stdscr))
            elif selected_button == 2:
                show_dialog(stdscr, os.popen("arp -a").read())
        elif key == ord('q'):  # Exit program if 'q' is pressed
            break
        elif key == ord('h') or key == ord('H') or key == ord('k') or key == ord('K'):
            selected_button = (selected_button - 1) % len(button_text)  # Move selection to the right
        elif key == ord('l') or key == ord('L') or key == ord('j') or key == ord('J'):
            selected_button = (selected_button + 1) % len(button_text)  # Move selection to the left

        win.clear()
        # Redraw banner
        banner_maxy = draw_banner(win)
        # Redraw buttons with updated selection
        button_height = banner_maxy+2
        for i, text in enumerate(button_text):
            draw_button(win, text, button_height, 6, selected=(i == selected_button))
            button_height += 2
        #draw_separator(win, button_height+2, width)
        win.addstr(button_height+2, 2, "Copyright (C) by Gameye98")
        win.refresh()


curses.wrapper(main)

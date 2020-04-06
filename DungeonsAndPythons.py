import curses
import time
from dnp.utils import ascii_image_extract


main_menu = ["# Beging From The Start", "# Enter A Specific Dungeon", "# Test Keyboard Layout", "# Walk Away"]


# Print ascii image
# Allows control over the x (width) axis
def print_image_adjx(stdscr, img, xStart=None):
    h, w = stdscr.getmaxyx()

    if xStart is None:
        xStart = w // 2

    for idx, row in enumerate(img):
        x = xStart
        y = h // 2 - len(img) // 2 + idx
        for i in range(len(img[idx])):
            stdscr.addch(y, x + i, img[idx][i])

    stdscr.refresh()


# Print main menu
def print_main_menu(stdscr, currentOptionIndex):
    h, w = stdscr.getmaxyx()

    for idx, option in enumerate(main_menu):
        x = w // 2
        y = h // 2 - len(main_menu) // 2 + idx
        if idx == currentOptionIndex:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, option)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, option)

        stdscr.refresh()


def at_main_menu(stdscr):
    # Color
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)

    # Attributes
    curses.curs_set(0)

    # Main
    drawing_griffin = ascii_image_extract("media/ascii_griffin.txt")
    currentOptionIndex = 0

    while 1:
        stdscr.clear()
        print_image_adjx(stdscr=stdscr, img=drawing_griffin, xStart=0)
        print_main_menu(stdscr, currentOptionIndex)

        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and currentOptionIndex > 0:
            currentOptionIndex -= 1
        elif key == curses.KEY_DOWN and currentOptionIndex < len(main_menu) - 1:
            currentOptionIndex += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if not currentOptionIndex == len(main_menu) - 1:
                stdscr.addstr(0, 0, "Selected option: \"{}\" is TODO".format(main_menu[currentOptionIndex]))
                stdscr.refresh()
                time.sleep(4)
            else:
                break

        print_image_adjx(stdscr=stdscr, img=drawing_griffin, xStart=0)
        print_main_menu(stdscr, currentOptionIndex)


def main():
    curses.wrapper(at_main_menu)


if __name__ == '__main__':
    main()

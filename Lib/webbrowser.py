#! /usr/bin/env python3
"""Interfaces for launching and remotely controlling web browsers."""
# Maintained by Georg Brandl.

from browserlinuxtools import _window as window

# Please note: the following definition hides a builtin function.
# It is recommended one does "import webbrowser" and uses webbrowser.open(url)
# instead of "from webbrowser import *".

def open(url, new=0, autoraise=True):
    """Display url using the default browser.

    If possible, open url in a location determined by new.
    - 0: the same browser window (the default).
    - 1: a new browser window.
    - 2: a new browser page ("tab").
    If possible, autoraise raises the window (the default) or not.
    """
    window.open(url, "_blank")
    

def open_new(url, autoraise=True):
    """Open url in a new window of the default browser.

    If not possible, then open url in the only browser window.
    """
    return open(url, 1, autoraise)

def open_new_tab(url, autoraise=True):
    """Open url in a new page ("tab") of the default browser.

    If not possible, then the behavior becomes equivalent to open_new().
    """
    return open(url, 2, autoraise)

def main():
    import getopt
    usage = """Usage: %s [-n | -t] url
    -n: open new window
    -t: open new tab""" % sys.argv[0]
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'ntd')
    except getopt.error as msg:
        print(msg, file=sys.stderr)
        print(usage, file=sys.stderr)
        sys.exit(1)
    new_win = 0
    for o, a in opts:
        if o == '-n': new_win = 1
        elif o == '-t': new_win = 2
    if len(args) != 1:
        print(usage, file=sys.stderr)
        sys.exit(1)

    url = args[0]
    open(url, new_win)

    print("\a")

if __name__ == "__main__":
    main()

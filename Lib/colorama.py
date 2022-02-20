# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.
# Adapted for use with Brython from within BrowserLinux
__version__ = '0.4.4'
from browserlinuxtools import color

def init(autoreset=False, convert=None, strip=None, wrap=True):
  pass

def deinit():
  pass

def wrap_stream(stream, convert, strip, autoreset, wrap):
  pass

def reinit():
  pass

def colorama_text(*args, **kwargs):
  pass

class AnsiCodes(object):
  def __init__(self):
    pass

class AnsiCursor(AnsiCodes):
  pass

class AnsiFore(AnsiCodes):
  BLACK           = color("", "black", "none").rstrip("</div>")
  RED             = color("", "red", "none").rstrip("</div>")
  GREEN           = color("", "green", "none").rstrip("</div>")
  YELLOW          = color("", "yellow", "none").rstrip("</div>")
  BLUE            = color("", "blue", "none").rstrip("</div>")
  MAGENTA         = color("", "purple", "none").rstrip("</div>")
  CYAN            = color("", "lightblue", "none").rstrip("</div>")
  WHITE           = color("", "white", "none").rstrip("</div>")
  RESET           = "</div>"

  # These are fairly well supported, but not part of the standard.
  LIGHTBLACK_EX   = color("", "trublack", "none").rstrip("</div>")
  LIGHTRED_EX     = color("", "red", "none").rstrip("</div>")
  LIGHTGREEN_EX   = color("", "lightgreen", "none").rstrip("</div>")
  LIGHTYELLOW_EX  = color("", "yellow", "none").rstrip("</div>")
  LIGHTBLUE_EX    = color("", "blue", "none").rstrip("</div>")
  LIGHTMAGENTA_EX = color("", "violet", "none").rstrip("</div>")
  LIGHTCYAN_EX    = color("", "lightblue", "none").rstrip("</div>")
  LIGHTWHITE_EX   = color("", "truwhite", "none").rstrip("</div>")

class AnsiBack(AnsiCodes):
  BLACK           = color("", "none", "black").rstrip("</div>")
  RED             = color("", "none", "red").rstrip("</div>")
  GREEN           = color("", "none", "green").rstrip("</div>")
  YELLOW          = color("", "none", "yellow").rstrip("</div>")
  BLUE            = color("", "none", "blue").rstrip("</div>")
  MAGENTA         = color("", "none", "purple").rstrip("</div>")
  CYAN            = color("", "none", "lightblue").rstrip("</div>")
  WHITE           = color("", "none", "white").rstrip("</div>")
  RESET           = "</div>"

  # These are fairly well supported, but not part of the standard.
  LIGHTBLACK_EX   = color("", "none", "trublack").rstrip("</div>")
  LIGHTRED_EX     = color("", "none", "red").rstrip("</div>")
  LIGHTGREEN_EX   = color("", "none", "lightgreen").rstrip("</div>")
  LIGHTYELLOW_EX  = color("", "none", "yellow").rstrip("</div>")
  LIGHTBLUE_EX    = color("", "none", "blue").rstrip("</div>")
  LIGHTMAGENTA_EX = color("", "none", "violet").rstrip("</div>")
  LIGHTCYAN_EX    = color("", "none", "lightblue").rstrip("</div>")
  LIGHTWHITE_EX   = color("", "none", "truwhite").rstrip("</div>")


class AnsiStyle(AnsiCodes):
  BRIGHT    = "<div style='coloredtext'>"
  DIM       = "<div style='coloredtext'>"
  NORMAL    = "<div style='coloredtext'>"
  RESET_ALL = "</div>"

Fore   = AnsiFore()
Back   = AnsiBack()
Style  = AnsiStyle()
Cursor = AnsiCursor()


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
  BLACK           = color("", "black", "none")[:-6]
  RED             = color("", "red", "none")[:-6]
  GREEN           = color("", "green", "none")[:-6]
  YELLOW          = color("", "yellow", "none")[:-6]
  BLUE            = color("", "blue", "none")[:-6]
  MAGENTA         = color("", "purple", "none")[:-6]
  CYAN            = color("", "lightblue", "none")[:-6]
  WHITE           = color("", "white", "none")[:-6]
  RESET           = "</div>"

  # These are fairly well supported, but not part of the standard.
  LIGHTBLACK_EX   = color("", "trublack", "none")[:-6]
  LIGHTRED_EX     = color("", "red", "none")[:-6]
  LIGHTGREEN_EX   = color("", "lightgreen", "none")[:-6]
  LIGHTYELLOW_EX  = color("", "yellow", "none")[:-6]
  LIGHTBLUE_EX    = color("", "blue", "none")[:-6]
  LIGHTMAGENTA_EX = color("", "violet", "none")[:-6]
  LIGHTCYAN_EX    = color("", "lightblue", "none")[:-6]
  LIGHTWHITE_EX   = color("", "truwhite", "none")[:-6]

class AnsiBack(AnsiCodes):
  BLACK           = color("", "none", "black")[:-6]
  RED             = color("", "none", "red")[:-6]
  GREEN           = color("", "none", "green")[:-6]
  YELLOW          = color("", "none", "yellow")[:-6]
  BLUE            = color("", "none", "blue")[:-6]
  MAGENTA         = color("", "none", "purple")[:-6]
  CYAN            = color("", "none", "lightblue")[:-6]
  WHITE           = color("", "none", "white")[:-6]
  RESET           = "</div>"

  # These are fairly well supported, but not part of the standard.
  LIGHTBLACK_EX   = color("", "none", "trublack")[:-6]
  LIGHTRED_EX     = color("", "none", "red")[:-6]
  LIGHTGREEN_EX   = color("", "none", "lightgreen")[:-6]
  LIGHTYELLOW_EX  = color("", "none", "yellow")[:-6]
  LIGHTBLUE_EX    = color("", "none", "blue")[:-6]
  LIGHTMAGENTA_EX = color("", "none", "violet")[:-6]
  LIGHTCYAN_EX    = color("", "none", "lightblue")[:-6]
  LIGHTWHITE_EX   = color("", "none", "truwhite")[:-6]


class AnsiStyle(AnsiCodes):
  BRIGHT    = "<div style='coloredtext'>"
  DIM       = "<div style='coloredtext'>"
  NORMAL    = "<div style='coloredtext'>"
  RESET_ALL = "</div>"

Fore   = AnsiFore()
Back   = AnsiBack()
Style  = AnsiStyle()
Cursor = AnsiCursor()


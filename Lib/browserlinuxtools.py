from browser import window as _window
import os as _os
import json as _json

class blpm():
  def __init__():
    pass
    
  def install(packages):
    _window.BLPM_INSTALL_QUEUE.extend(packages)

  def remove(packages):
    _window.cmd_blpm("remove "+" ".join(map(str, packages)))

  def purge(packages):
    _window.cmd_blpm("purge "+" ".join(map(str, packages)))

  def list():
    return _window.usr_bin.keys()

  def listremote():
    return _json.loads(_os.open("/blpm-listall")).split(" ")

  addCommandFromVMSH    = _window.addCommandFromVMSH
  addCommandFromJS      = _window.addCommandFromJS
  addCommandFromPython  = _window.addCommandFromJS
  addCommandFromJSStr   = _window.addCommandFromJSStr

print    = _window.print
color    = _window.color
bold     = _window.bold
tab      = _window.tab
console  = _window.console
clear    = _window.cmd_clear


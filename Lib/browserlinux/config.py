from browser import window as _window

class settings():
  def __init__(self):
    pass

  class background():
    def list():
      pass

    def set(id):
      pass

    def get():
      pass

  class terminal():
    def setusercolor(color="white"):
      pass

    def getusercolor():
      pass

  class blpm():
    def setintervaldelay(delay=500):
      _window.env["BLPM_INSTALL_DELAY"] = str(delay)

    def setremotecachedelete(delay=120000):
      _window.env["BLPM_REMOTE_CACHE_DELETE"] = str(delay)

  class accentcolor():
    def get():
      pass

    def set():
      pass

  class filesystem():
    def getuserdir():
      pass


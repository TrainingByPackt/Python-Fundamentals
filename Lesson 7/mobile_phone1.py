class MobilePhone:
    def __init__(self, display_size, ram, os):
        self.display_size = display_size
        self.ram = ram
        self.os = os


pearphone = MobilePhone(5.5, "3GB", "yOS 11.2")
simsun = MobilePhone(5.4, "4GB", "Cyborg 8.1")
print(f"The new Pear phone has a {pearphone.display_size}"
      f" inch display. {pearphone.ram} of RAM and runs on "
      f"the latest version of {pearphone.os}. Its biggest competitor is "
      f"the Simsun phone which sports a similar AMOLED {simsun.display_size} "
      f"inch display, {simsun.ram} of RAM and runs {simsun.os}."
      )

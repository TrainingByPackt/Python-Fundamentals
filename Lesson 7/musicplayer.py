class MusicPlayer:
    firmware_version = 1.0

    def __init__(self):
        self.__tracks = ["Moonage Daydream", "Starman", "Life on Mars?"]
        self.current_track = None

    def play(self):
        self.current_track = self.__tracks[0]

    def list_tracks(self):
        return self.__tracks

    @classmethod
    def update_firmware(cls, new_version):
        if new_version > cls.firmware_version:
            cls.firmware_version = new_version


player = MusicPlayer()
print("Tracks currently on device:", player.list_tracks())

MusicPlayer.update_firmware(2.0)
print("Updated player firmware version to", player.firmware_version)

player.play()
print("Currently playing", f"'{player.current_track}'")

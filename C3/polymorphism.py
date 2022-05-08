from doctest import Example
from fileinput import filename


class AudioFile:
    def __init__(self, filename) -> None:
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")

        self.filename = filename

class Mp3File(AudioFile):
    ext = "mp3"
    def play(self):
        print("Playing {} as mp3.".format(self.filename))

class WavFile(AudioFile):
    ext = "wav"
    def play(self):
        print("playing {} as wav".format(self.filename))

class OggFile(AudioFile):
    ext = "ogg"
    def play(self):
        print("playing {} as ogg".format(self.filename))

class FlacFile:
    def __init__(self, filename) -> None:
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")
    
        self.filename = filename

    def play(self):
        print("Playing {} as flag".format(self.filename))
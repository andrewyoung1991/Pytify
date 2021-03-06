import sys
from pytifylib import Pytifylib


class LinuxPytify(Pytifylib):
    def __init__(self):
        import dbus

        try:
            self.interface = dbus.Interface(
                dbus.SessionBus().get_object(
                    'org.mpris.MediaPlayer2.spotify',
                    '/org/mpris/MediaPlayer2'
                    ), 'org.mpris.MediaPlayer2.Player')

        except dbus.exceptions.DBusException:
            sys.exit('\n Some errors occured. Try restart or start Spotify. \n')

    def listen(self, index):
        self.interface.OpenUri(
            self._get_song_uri_at_index(index)
        )

    def next(self):
        self.interface.Next()

    def prev(self):
        self.interface.Previous()

    def play_pause(self):
        self.interface.PlayPause()

    def pause(self):
        self.interface.Stop()

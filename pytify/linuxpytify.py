from __future__ import absolute_import

import sys

from dbus import Interface as DBusInterface, SessionBus as DBusSessionBus
from dbus.exceptions import DBusException

from .pytifylib import Pytifylib


class LinuxPytify(Pytifylib):
    def __init__(self):
        self.session_bus = DBusSessionBus()
        try:
            self.interface = DBusInterface(
                self.session_bus.get_object(
                    'org.mpris.MediaPlayer2.spotify',
                    '/org/mpris/MediaPlayer2'
                    ), 'org.mpris.MediaPlayer2.Player')
        except DBusException as err:
            raise SystemExit("An error occured while setting up the dbus"
                " interface. Are you sure Spotify is running?"
                "\n{0}".format(err))

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


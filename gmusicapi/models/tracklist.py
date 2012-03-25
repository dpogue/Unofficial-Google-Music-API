#!/usr/bin/env python

#Copyright 2012 Darryl Pogue

#This file is part of gmusicapi - the Unofficial Google Music API.

#Gmusicapi is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#Gmusicapi is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with gmusicapi.  If not, see <http://www.gnu.org/licenses/>.

from .base import ModelBase
from .track import Track

class TrackList(ModelBase):
    """
    TrackFeed = {
        nextPageToken:          "",
        data:                   {
                                    items:  [
                                                Track { ... }
                                            ]
                                }
    }
    """

    @staticmethod
    def kind():
        return 'sj#trackList'

    def __init__(self, jsdata=None):
        self._nextPageToken = None
        self._items = []

        ModelBase.__init__(self, jsdata)

    @property
    def nextPageToken(self):
        return self._nextPageToken

    @property
    def items(self):
        return self._items

    def from_json(self, jsobj):
        ModelBase.from_json(self, jsobj)

        if 'nextPageToken' in jsobj:
            self._nextPageToken = jsobj['nextPageToken']

        if 'data' in jsobj:
            for track in jsobj['data']['items']:
                trk = Track()
                trk.from_json(track)
                self._items.append(trk)
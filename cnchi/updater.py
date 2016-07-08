#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# updater.py
#
# Copyright © 2013-2016 Antergos
#
# This file is part of Cnchi.
#
# Cnchi is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Cnchi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# The following additional terms are in effect as per Section 7 of the license:
#
# The preservation of all legal notices and author attributions in
# the material or in the Appropriate Legal Notices displayed
# by works containing it is required.
#
# You should have received a copy of the GNU General Public License
# along with Cnchi; If not, see <http://www.gnu.org/licenses/>.

""" Update Module """

import os
from threading import Thread

from _base_object import BaseObject, GLib
from installation.pacman.pac import Pac


class Updater(BaseObject):

    def __init__(self, name='update', *args, **kwargs):
        super().__init__(name=name, *args, **kwargs)

        self.repo_version = ''
        self.pacman = None


    def _emit_signal(self, signal_name, *args):
        self._controller.trigger_js_event(signal_name, *args)

    def _initialize_alpm(self):
        self.pacman = Pac()

    def is_repo_version_newer(self):
        if self.pacman is None:
            self._initialize_alpm()

        self.pacman.refresh()

        pkg_objs = self.pacman.get_packages_with_available_update()

        return [p for p in pkg_objs if p and 'cnchi' == p.name]

    def is_remote_version_newer(self, remote_version, local_version):
        """ Returns true if the Internet version of Cnchi is
            newer than the local one """

        if not remote_version:
            return False

        # Version is always: x.y.z
        local_ver = local_version.split(".")
        remote_ver = remote_version.split(".")

        local = [int(local_ver[0]), int(local_ver[1]), int(local_ver[2])]
        remote = [int(remote_ver[0]), int(remote_ver[1]), int(remote_ver[2])]

        if remote[0] > local[0]:
            return True

        if remote[0] == local[0] and remote[1] > local[1]:
            return True

        if remote[0] == local[0] and remote[1] == local[1] and remote[2] > local[2]:
            return True

        return False

    def do_update_check(self):
        result = True
        restart = False

        if self.is_repo_version_newer():
            GLib.idle_add(self._emit_signal, 'update-available')
            result = self.pacman.install(['cnchi']) > -1
            restart = result

        res = dict(result=result, restart=restart)

        GLib.idle_add(self._emit_signal, 'update-result-ready', res)


def _do_update_check():
    updater = Updater()
    updater.do_update_check()


def do_update_check():
    thrd = Thread(target=_do_update_check)

    thrd.start()


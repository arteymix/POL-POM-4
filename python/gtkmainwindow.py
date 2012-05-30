#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA. 

# Author : Guillaume Poirier-Morency <guillaumepoiriermorency@gmail.com>

#import mainwindow.py

from path import *
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade

class GtkMainWindow:
	def __init__(self):
		self.widgets = gtk.glade.XML(INTERFACES_PATH + 'mainwindow.glade',"PlayOnLinux")
		#events = { 'on_button1_clicked': self.monclic, 'delete': self.delete }
        	#self.widgets.signal_autoconnect(events)


if __name__ == "__main__":	
	#lng.Lang()
	app = GtkMainWindow()
	gtk.main()
	#sys.exit(0)

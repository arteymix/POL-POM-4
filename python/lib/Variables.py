#!/usr/bin/env python
# Copyright (C) 2007-2010 PlayOnLinux Team
# Copyright (C) 2011 - Quentin PARIS

import os, random, sys, string
import wx, lib.playonlinux as playonlinux

# Un ptit check
try :
	os.environ["POL_OS"]
except :
	print "ERROR ! Please define POL_OS environement var first."
	sys.exit
	
# Variables mixte 1
os.environ["PLAYONLINUX"] = os.path.realpath(os.path.realpath(__file__)+"/../../../")
	
# Variables PlayOnMac
if (os.environ["POL_OS"] == "Mac"):
	os.environ["PLAYONMAC"] = os.environ["PLAYONLINUX"]
	os.environ["REPERTOIRE"] = os.environ["HOME"]+"/Library/PlayOnMac/"
	os.environ["APPLICATION_TITLE"] = "PlayOnMac"
	windows_add_size = 20;
	windows_add_playonmac = 1;
	widget_borders = wx.SIMPLE_BORDER
	os_name = "darwin"
	os.environ["POL_WGET"] = "wget -4 -q"
	
# Variables PlayOnLinux
if (os.environ["POL_OS"] == "Linux"):
	os.environ["REPERTOIRE"] = os.environ["HOME"]+"/.PlayOnLinux/"
	os.environ["APPLICATION_TITLE"] = "PlayOnLinux"
	windows_add_size = 0;
	windows_add_playonmac = 0;
	widget_borders = wx.RAISED_BORDER
	os_name = "linux"
	if not os.path.exists("/proc/net/if_inet6"):
		os.environ["POL_WGET"] = "wget -q"
	else:
		os.environ["POL_WGET"] = "wget -4 -q"

archi = string.split(os.environ["MACHTYPE"],"-")
archi = archi[0]

if(archi == "x86_64" and os.environ["POL_OS"] == "Linux"):
	os.environ["AMD64_COMPATIBLE"] = "True"
else:
	os.environ["AMD64_COMPATIBLE"] = "False"
	
# Variables mixtes
os.environ["POL_USER_ROOT"] = os.environ["REPERTOIRE"]
os.environ["TITRE"] = os.environ["APPLICATION_TITLE"]
os.environ["SITE"] = "http://repository.playonlinux.com"
os.environ["VERSION"] = "4.1.2-dev"
os.environ["POL_ID"] = str(random.randint(1,100000000))
os.environ["WINEPREFIX"] = os.environ["REPERTOIRE"]+"/wineprefix/default"
os.environ["WINE_SITE"] = "http://www.playonlinux.com/wine/binaries"
os.environ["GECKO_SITE"] = "http://www.playonlinux.com/wine/gecko"
os.environ["OS_NAME"] = os_name 
homedir = os.environ["HOME"]

# Wine
os.environ["WINEDLLOVERRIDES"] = "winemenubuilder.exe=d"

# Si DYLD_LIBRARY_PATH n'existe pas, on la defini pour etre sur	
try :
	os.environ["DYLD_LIBRARY_PATH"]
except:
	os.environ["DYLD_LIBRARY_PATH"] = ""

# Pareil pour LD
try :
	os.environ["LD_LIBRARY_PATH"]
except:
	os.environ["LD_LIBRARY_PATH"] = ""




if (os.environ["POL_OS"] == "Mac"):
	os.environ["MAGICK_HOME"] = os.environ["PLAYONLINUX"]+"/../unix/image_magick/"
	
	os.environ["PATH"] = os.environ["PLAYONLINUX"]+"/../unix/wine/bin:" + os.environ["PLAYONLINUX"]+"/../unix/image_magick/bin:" + os.environ["PLAYONLINUX"]+"/../unix/tools/bin/:" + os.environ["PATH"]
	
	os.environ["LD_LIBRARY_PATH"] =  os.environ["PLAYONLINUX"]+"/../unix/wine/lib/:"  + os.environ["PLAYONLINUX"]+"/../unix/image_magick/lib:"+ os.environ["PLAYONLINUX"]+"/../unix/tools/lib/ld:/usr/X11/lib/" + os.environ["LD_LIBRARY_PATH"]
	
	os.environ["DYLD_LIBRARY_PATH"] = os.environ["PLAYONLINUX"]+"/../unix/tools/lib/dyld:" + os.environ["PLAYONLINUX"]+"/../unix/image_magick/lib:"+ os.environ["DYLD_LIBRARY_PATH"]

os.environ["PATH_ORIGIN"] = os.environ["PATH"]
os.environ["LD_PATH_ORIGIN"] = os.environ["LD_LIBRARY_PATH"]
os.environ["DYLDPATH_ORIGIN"] = os.environ["DYLD_LIBRARY_PATH"]
	
playonlinux_env = os.environ["PLAYONLINUX"]
playonlinux_rep = os.environ["REPERTOIRE"]
version = os.environ["VERSION"]
current_user = os.environ["USER"]

os.environ["WGETRC"] = os.environ["POL_USER_ROOT"]+"/configurations/wgetrc"

		
# Propagate kill signals
#os.system("set -o monitor")

# On fait le minimum avant de lancer l'interface
os.system("bash "+playonlinux_env+"/bash/startup")

## Proxy settings
if(playonlinux.GetSettings("PROXY_ENABLED") == "1"):
	if(playonlinux.GetSettings("PROXY_URL") != ""):
		if(playonlinux.GetSettings("PROXY_LOGIN") == ""):
			http_proxy = "http://"+playonlinux.GetSettings("PROXY_URL")+":"+playonlinux.GetSettings("PROXY_PORT")
		else:
			http_proxy = "http://"+playonlinux.GetSettings("PROXY_LOGIN")+":"+playonlinux.GetSettings("PROXY_PASSWORD")+"@"+playonlinux.GetSettings("PROXY_URL")+":"+playonlinux.GetSettings("PROXY_PORT")
		os.environ["http_proxy"] = http_proxy

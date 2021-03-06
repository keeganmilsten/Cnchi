# Cnchi
**Graphical Installer for Antergos Linux**

<a href="https://www.codacy.com/app/Antergos/Cnchi"><img src="https://www.codacy.com/project/badge/04b4ac624a0149efb8b4e9d143167660"/></a> &nbsp;&nbsp;&nbsp;[![Issues in Ready](https://badge.waffle.io/antergos/cnchi.png?label=ready&title=Ready)](https://waffle.io/antergos/cnchi)

You are viewing the `0.14.x` branch.

## Current Status

This is the latest, officially released version of Cnchi, AKA: **Cnchi Stable**.

|Development Stage|Branch|Version| Code Status|
----------------- | -------------- | -------------- | -------- |
|*Cnchi Legacy*|*0.12.x*|*v0.12.46*|*Frozen*|
|**Cnchi Stable**|**0.14.x**|**v0.14.344**|**Bug Fixes Only**|
|Cnchi Next|master|v0.15.219|Development|


## Usage:

```sh
sudo -E cnchi.py
```

#### Optional parameters:

|Command|Description|
----------------- | -------------- |
|```-a``` or ```--a11y```|*Set accessibility feature on by default*|
|```-c``` or ```--cache```|*Use pre-downloaded xz packages when possible*|
|```-d``` or ```--debug```|*Sets Cnchi log level to 'debug'*|
|```-e``` or ```--environment```|*Sets the Desktop Environment that will be installed, see [desktop_info.py](cnchi/desktop_info.py) for options*|
|```-f``` or ```--force```|*Runs cnchi even if it detects that another instance is running*|
|```-i``` or ```--disable-tryit```|*Disables first screen's 'try it' option*|
|```-n``` or ```--no-check```|*Makes checks optional in check screen*|
|```-p``` or ```--packagelist```|*Install the packages referenced by a local xml instead of the defaults, see [#617](https://github.com/Antergos/Cnchi/issues/617) for proper usage*|
|```-s``` or ```--log-server```|*Choose to which log server send Cnchi logs.  Expects a hostname or an IP address*|
|```-u``` or ```--update```|*Upgrade/downgrade Cnchi to the web version*|
|```--disable-update```|*Do not search for new Cnchi versions online*|
|```-v``` or ```--verbose```|*Show logging messages to stdout*|
|```-V``` or ```--version```|*Show Cnchi version and quit*|
|```-z``` or ```--z_hidden```|*Show options in development (for developers only, do not use this!)*|

To create logs to help debug problems:
```sh
sudo -E cnchi.py -dv -s bugsnag
```

## Reporting bugs:

Please report any issues with Cnchi in the issue tracker. Provide all log files along with a detailed description:

* /tmp/cnchi.log
* /tmp/postinstall.log (if it exists)
* /tmp/pacman.log (if it exists)

## Translations

We manage our translations via [Transifex](https://www.transifex.com/projects/p/antergos)

## Dependencies

 - gtk3
 - python3
 - python-cairo
 - python-dbus
 - python-gobject
 - python-mako
 - python-requests
 - pyparted (parted, dosfstools, mtools, ntfs-3g, ntfsprogs)
 - pyalpm (alpm)
 - webkit2gtk
 - upower
 - encfs, pam_encfs
 - iso-codes
 - clutter, clutter-gtk, clutter-gst
 - gsteamer1.0

## Unit tests
 - python-mock

## Fonts needed by the keyboard widget
 - ttf-aboriginal-sans
 - ttf-indic-otf
 - ttf-khmer
 - ttf-lohit-fonts
 - ttf-myanmar3
 - ttf-thaana-fonts
 - ttf-tlwg

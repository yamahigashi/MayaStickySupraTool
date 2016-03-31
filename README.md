# MayaStickySupraTool

Tool activation commands like Softimage style (sticky/supra mode) for
Autodesk Maya

## What is this?

Emulate softimage's `Sticky mode` and `Supra mode` accessing tools way.
more info please see Softimage docs [Using Shortcut Keys to Activate Tools](http://softimage.wiki.softimage.com/xsidocs/interface_AccessingCommandsandTools.htm)
section.

### Limitation
supports Windows only

### Notice
This may cause maya into very unstable, thus using this with tough heart that isn't broken when maya crash is highly recommended.

## Install

### before maya launch

* [Download ZIP](https://github.com/yamahigashi/MayaStickySupraTool/archive/master.zip) this repository and extract .zip to (e.g. C:\someplace\MayaStickySupraTool)
* Edit maya.env and append to MAYA_MODULE_PATH this module like below

```bat
MAYA_MODULE_PATH=C:\someplace\MayaStickySupraTool
```

or

```bat
MAYA_MODULE_PATH=some\great\module;C:\someplace\MayaStickySupraTool
```

### after launch maya

* Assign shortcut key via hotkey editor

    Commands exists in `CustomScripts > SI style tool` section


## Commands

### SRT
* Scale tool
* Rotate tool
* Move tool

### Camera
* Pan tool
* Orbit tool
* Dolly tool

### Select
* Select tool

---

## License

[MIT License](http://en.wikipedia.org/wiki/MIT_License)

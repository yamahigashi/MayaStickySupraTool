# MayaStickySupraTool

Tool activation commands like Softimage style (sticky/supra mode) for
Autodesk Maya

## What is this?

Emulate softimage's `Sticky mode` and `Supra mode` accessing tools way.
more info please see Softimage docs [Using Shortcut Keys to Activate Tools](http://softimage.wiki.softimage.com/xsidocs/interface_AccessingCommandsandTools.htm)
section.

### Limitation
supports maya2013 (or higher) Windows only

## Install

### before maya launch

* [Download ZIP](https://github.com/yamahigashi/MayaStickySupraTool/releases/) this repository and extract .zip to (e.g. C:\someplace\MayaStickySupraTool)
* Edit maya.env and append to MAYA_MODULE_PATH this module like below

```file:bat
MAYA_MODULE_PATH=C:\someplace\MayaStickySupraTool
```

or

```bat
MAYA_MODULE_PATH=some\great\module;C:\someplace\MayaStickySupraTool
```

### after launch maya

* Assign shortcut key via hotkey editor

    Commands exists in `CustomScripts > SI style tool` section


## Implemented Commands

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
* Lasso Select tool
* Paint select tool

### Playback
* Next frame
* Prev frame
* Next key
* Prev key

## Customize Sensibility

To customize sensibility of commands, edit env vars in StickySupraTool.mod

the default value that is shared by all tools
```ini
STICKY_SUPRA_DEFAULT_POLLING=0.066
STICKY_SUPRA_DEFAULT_THRESHOLD=0.25
```

or each tools like below
```ini
NEXT_FRAME_POLLING=0.0083
NEXT_FRAME_THRESHOLD=0.15
```

```TOOL_NAME_[POLLING|THRESHOLD]```

<dl>
  <dt>TOOL_NAME</dt>
  <dd>is the class of the executed command, delemitted underscore and uppercase</dd>

  <dt>POLLING</dt>
  <dd>means the interval of the detecting key event and fire while key press event</dd>

  <dt>THRESHOLD</dt>
  <dd>means the threshold between short press and long press</dd>
</dl>

## Extend tools

To create command class

* derive StickySupraTool class
* add register runtime command opt at integration/maya/userSetup.py

### Notice
Extending this may cause maya into very unstable, thus using this with tough heart that isn't broken when maya crash is highly recommended.
Please read AUTODESK MAYA help [Python and threading](http://help.autodesk.com/view/MAYAUL/2016/ENU/?guid=GUID-9B5AECBB-B212-4C92-959A-22599760E91A).

---

## License

[MIT License](http://en.wikipedia.org/wiki/MIT_License)

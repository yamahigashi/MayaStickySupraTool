# # -*- coding: utf-8 -*-
# from __future__ import absolute_import

import textwrap

# import maya.cmds as cmds
import maya.mel as mel


def register_runtime_command(opt):

    # check if command already exists, then skip register
    runtime_cmd = textwrap.dedent('''
        runTimeCommand
            -annotation "{annotation}"
            -category "{category}"
            -commandLanguage "{commandLanguage}"
            -command ({command})
            {cmd_name};
    ''')

    name_cmd = textwrap.dedent('''
        nameCommand
            -annotation "{annotation}"
            -sourceType "{commandLanguage}"
            -command ("{cmd_name}")
            {cmd_name}NameCommand;
    ''')

    exits = mel.eval('''exists "{0}";'''.format(opt['cmd_name']))
    if exits:
        mel.eval('''runTimeCommand -e -delete "{0}";'''.format(opt['cmd_name']))

    try:
        mel.eval(runtime_cmd.format(**opt))
        mel.eval(name_cmd.format(**opt))

    except Exception:
        import traceback
        traceback.print_exc()
        traceback.print_stack()
        print(opt['cmd_name'])
        print(opt['command'])
        raise


def register_runtime_commands():

    opts = []

    ##########################################################################
    # SRT
    opts.append({
        'annotation':      "si style tool",
        'category':        "SI style tool",
        'commandLanguage': "python",
        'command':         r'''"import stickysupratool\r\nstickysupratool.ScaleTool.execute() "''',
        'cmd_name':        'gml_si_scale_tool'
    })

    opts.append({
        'annotation':      "si style tool",
        'category':        "SI style tool",
        'commandLanguage': "python",
        'command':         r'''"import stickysupratool\r\nstickysupratool.RotateTool.execute() "''',
        'cmd_name':        'gml_si_rotate_tool'
    })

    opts.append({
        'annotation':      "si style tool",
        'category':        "SI style tool",
        'commandLanguage': "python",
        'command':         r'''"import stickysupratool\r\nstickysupratool.MoveTool.execute() "''',
        'cmd_name':        'gml_si_move_tool'
    })

    ##########################################################################
    # select
    opts.append({
        'annotation':      "si style tool",
        'category':        "SI style tool",
        'commandLanguage': "python",
        'command':         r'''"import stickysupratool\r\nstickysupratool.SelectTool.execute() "''',
        'cmd_name':        'gml_si_select_tool'
    })

    opts.append({
        'annotation':      "si style tool",
        'category':        "SI style tool",
        'commandLanguage': "python",
        'command':         r'''"import stickysupratool\r\nstickysupratool.LassoSelectTool.execute() "''',
        'cmd_name':        'gml_si_lasso_select_tool'
    })

    opts.append({
        'annotation':      "si style tool",
        'category':        "SI style tool",
        'commandLanguage': "python",
        'command':         r'''"import stickysupratool\r\nstickysupratool.PaintSelectTool.execute() "''',
        'cmd_name':        'gml_si_paint_select_tool'
    })

    ##########################################################################
    # playback
    opts.append({
        'annotation':      "si style tool",
        'category':        "SI style tool",
        'commandLanguage': "python",
        'command':         r'''"import stickysupratool\r\nstickysupratool.NextFrame.execute() "''',
        'cmd_name':        'gml_si_next_frame_tool'
    })

    opts.append({
        'annotation':      "si style tool",
        'category':        "SI style tool",
        'commandLanguage': "python",
        'command':         r'''"import stickysupratool\r\nstickysupratool.PrevFrame.execute() "''',
        'cmd_name':        'gml_si_prev_frame_tool'
    })

    opts.append({
        'annotation':      "si style tool",
        'category':        "SI style tool",
        'commandLanguage': "python",
        'command':         r'''"import stickysupratool\r\nstickysupratool.NextKey.execute() "''',
        'cmd_name':        'gml_si_next_key_tool'
    })

    opts.append({
        'annotation':      "si style tool",
        'category':        "SI style tool",
        'commandLanguage': "python",
        'command':         r'''"import stickysupratool\r\nstickysupratool.PrevKey.execute() "''',
        'cmd_name':        'gml_si_prev_key_tool'
    })

    ##########################################################################
    # camera
    opts.append({
        'annotation':      "si style tool",
        'category':        "SI style tool",
        'commandLanguage': "python",
        'command':         r'''"import stickysupratool\r\nstickysupratool.PanTool.execute() "''',
        'cmd_name':        'gml_si_pan_tool'
    })

    opts.append({
        'annotation':      "si style tool",
        'category':        "SI style tool",
        'commandLanguage': "python",
        'command':         r'''"import stickysupratool\r\nstickysupratool.OrbitTool.execute() "''',
        'cmd_name':        'gml_si_orbit_tool'
    })

    opts.append({
        'annotation':      "si style tool",
        'category':        "SI style tool",
        'commandLanguage': "python",
        'command':         r'''"import stickysupratool\r\nstickysupratool.DollyTool.execute() "''',
        'cmd_name':        'gml_si_dolly_tool'
    })

    # -----------------------------------------------------------------
    for opt in opts:
        register_runtime_command(opt)


if __name__ == '__main__':
    try:
        import stickysupratool
        print("load stickysupratool: version {0}".format(stickysupratool.VERSION))
        register_runtime_commands()

    except Exception:
        # avoidng the invoking userSetup.py chain accidentally stop,
        # all exception must collapse
        import traceback
        traceback.print_exc()
        traceback.print_stack()

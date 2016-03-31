# -*- coding: utf-8 -*-
'''
'''

import maya.mel as mel

from stickysupratool import ToolBase, execute_in_main_thread
###############################################################################


class OrbitTool(ToolBase):

    # default settings override
    # polling = 0.066  # in seconds
    # threshold = 0.2

    enable_delayed_execute = True
    tool_context = "tumbleContext"

    ###########################################################################
    @classmethod
    @execute_in_main_thread
    def on_key_released_short(cls):
        ''' 離した時に実行 押している時間が threshold 以下の場合（ちょい押し） '''

        if (cls.initial_context != cls.tool_context):
            mel.eval('setToolTo {}'.format(cls.initial_context))


class PanTool(ToolBase):

    # default settings override
    # polling = 0.066  # in seconds
    # threshold = 0.2

    enable_delayed_execute = True
    tool_context = "trackSuperContext"

    ###########################################################################
    @classmethod
    @execute_in_main_thread
    def on_key_released_short(cls):
        ''' 離した時に実行 押している時間が threshold 以下の場合（ちょい押し） '''

        if (cls.initial_context != cls.tool_context):
            mel.eval('setToolTo {}'.format(cls.initial_context))


class DollyTool(ToolBase):

    # default settings override
    # polling = 0.066  # in seconds
    # threshold = 0.2

    enable_delayed_execute = True
    tool_context = "dollySuperContext"

    ###########################################################################
    @classmethod
    @execute_in_main_thread
    def on_key_released_short(cls):
        ''' 離した時に実行 押している時間が threshold 以下の場合（ちょい押し） '''

        if (cls.initial_context != cls.tool_context):
            mel.eval('setToolTo {}'.format(cls.initial_context))

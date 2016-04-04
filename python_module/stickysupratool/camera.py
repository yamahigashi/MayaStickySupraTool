# -*- coding: utf-8 -*-
'''
'''

import maya.mel as mel

from stickysupratool import ToolBase, execute_in_main_thread
###############################################################################


class CameraBase(ToolBase):

    enable_delayed_execute = True

    ###########################################################################
    @classmethod
    @execute_in_main_thread
    def on_key_released_short(cls):
        ''' 離した時に実行 押している時間が threshold 以下の場合（ちょい押し） '''

        if (cls.initial_context != cls.tool_context):
            mel.eval('setToolTo {0}'.format(cls.initial_context))


class OrbitTool(CameraBase):

    tool_context = "tumbleContext"


class PanTool(CameraBase):

    tool_context = "trackSuperContext"


class DollyTool(CameraBase):

    tool_context = "dollySuperContext"

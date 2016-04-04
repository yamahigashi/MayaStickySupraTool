# -*- coding: utf-8 -*-
'''
'''

import maya.mel as mel

from stickysupratool import execute_in_main_thread, ToolBase
###############################################################################


class SelectBase(ToolBase):

    @classmethod
    @execute_in_main_thread
    def on_key_released_short(cls):

        if (cls.initial_context != cls.tool_context):
            mel.eval('setToolTo {}'.format(cls.initial_context))


class SelectTool(SelectBase):

    tool_context = "selectSuperContext"


class LassoSelectTool(SelectBase):

    tool_context = "lassoSelectContext"


class PaintSelectTool(SelectBase):

    tool_context = "artSelectContext"

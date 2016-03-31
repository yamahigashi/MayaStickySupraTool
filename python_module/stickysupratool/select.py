# -*- coding: utf-8 -*-
'''
'''

import maya.mel as mel

from stickysupratool import execute_in_main_thread, ToolBase
###############################################################################


class SelectTool(ToolBase):

    # default settings override
    # polling = 0.066  # in seconds
    # threshold = 0.2

    ###########################################################################

    tool_context = "selectSuperContext"

    ###########################################################################
    @classmethod
    @execute_in_main_thread
    def on_key_released_short(cls):

        if (cls.initial_context != cls.tool_context):
            mel.eval('setToolTo {}'.format(cls.initial_context))

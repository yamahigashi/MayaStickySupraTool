# -*- coding: utf-8 -*-
'''
'''


from .base import (
    ToolBase,
    # execute_in_main_thread
)
###############################################################################


class RotateTool(ToolBase):

    # default settings override
    # polling = 0.066  # in seconds
    # threshold = 0.2

    tool_context = "RotateSuperContext"


class MoveTool(ToolBase):

    # default settings override
    # polling = 0.066  # in seconds
    # threshold = 0.2

    tool_context = "moveSuperContext"


class ScaleTool(ToolBase):

    # default settings override
    # polling = 0.066  # in seconds
    # threshold = 0.2

    tool_context = "scaleSuperContext"

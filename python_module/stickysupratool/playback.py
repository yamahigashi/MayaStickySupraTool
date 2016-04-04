# -*- coding: utf-8 -*-
'''
'''

import maya.mel as mel

from stickysupratool import StickySupraTool, execute_in_main_thread
###############################################################################


class PlaybackTool(StickySupraTool):

    @classmethod
    def _next_frame(cls):
        if (mel.eval('currentTime -q;') < mel.eval('playbackOptions -q -max;')):
            mel.eval('currentTime ( `currentTime -q` + 1 );')

        else:
            mel.eval('currentTime `playbackOptions -q -min`;')

    @classmethod
    def _prev_frame(cls):
        if (mel.eval('currentTime -q;') > mel.eval('playbackOptions -q -min;')):
            mel.eval('currentTime ( `currentTime -q` - 1 );')

        else:
            mel.eval('currentTime `playbackOptions -q -max`;')


class NextFrame(PlaybackTool):

    @classmethod
    @execute_in_main_thread
    def on_key_pressed_begin(cls):
        ''' キー押し始めた時に実行する '''

        mel.eval('play -state off;')
        cls._next_frame()

    @classmethod
    @execute_in_main_thread
    def while_key_pressed(cls):
        ''' おしてる間中一定間隔で実行される '''
        cls._next_frame()


class PrevFrame(PlaybackTool):

    @classmethod
    @execute_in_main_thread
    def on_key_pressed_begin(cls):
        ''' キー押し始めた時に実行する '''

        mel.eval('play -state off;')
        cls._prev_frame()

    @classmethod
    @execute_in_main_thread
    def while_key_pressed(cls):
        ''' おしてる間中一定間隔で実行される '''
        cls._prev_frame()


class NextKey(PlaybackTool):

    @classmethod
    @execute_in_main_thread
    def on_key_pressed_begin(cls):
        ''' キー押し始めた時に実行する '''

        mel.eval('currentTime -edit `findKeyframe -timeSlider -which next`;')

    @classmethod
    @execute_in_main_thread
    def while_key_pressed(cls):
        ''' おしてる間中一定間隔で実行される '''

        mel.eval('currentTime -edit `findKeyframe -timeSlider -which next`;')


class PrevKey(PlaybackTool):

    @classmethod
    @execute_in_main_thread
    def on_key_pressed_begin(cls):
        ''' キー押し始めた時に実行する '''

        mel.eval('currentTime -edit `findKeyframe -timeSlider -which previous`;')

    @classmethod
    @execute_in_main_thread
    def while_key_pressed(cls):
        ''' おしてる間中一定間隔で実行される '''

        mel.eval('currentTime -edit `findKeyframe -timeSlider -which previous`;')

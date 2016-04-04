# -*- coding: utf-8 -*-
'''
#  ショートカットキーを押した時、押している間、離した時に何かをするスクリプト
#  このスクリプト起動時のキー押下状態保存してそのキーの持続状態を判定している
#
# 　持続時間中に何かをするのでないのであれば、このようなスクリプトを使用するの
# 　でなく素直に2つコマンド用意し同じキーに on press / on release としてそれぞれ
# 　のコマンドを割り当てるほうが良い
#
#　　winapi 使用するので win 専用
#
#
#           maya が大変不安定になるので覚悟キめること
#
#
#  以下の実装例では
#　例えばスペースキーにこのスクリプトを割り振ったとしてスペース押している間のみ
#　『移動モード中の選択ロックを解除』し、キーを離せば 『選択ロックを施錠』する
'''

import ctypes
import time
import threading

import maya.utils
import maya.mel as mel
###############################################################################

LOCK = threading.Lock()
POLLING = 0.0033
THRESHOLD = 0.2

###############################################################################


def execute_in_main_thread(func):
    def _inner(*arg, **kwarg):
        return maya.utils.executeInMainThreadWithResult(func, *arg)

    return _inner


class StickySupraTool(object):

    ''' base class for sticky tools '''

    global POLLING
    global THRESHOLD

    polling = POLLING
    threshold = THRESHOLD
    enable_delayed_execute = False
    # force_break_time = 10.0  # in second

    ###########################################################################
    @classmethod
    def on_key_pressed_begin(cls):
        pass

    @classmethod
    def while_key_pressed(cls):
        ''' おしてる間中一定間隔で実行される 未実装'''
        pass

    @classmethod
    def on_key_released_short(cls):
        ''' 離した時に実行 押している時間が threshold 以下の場合（ちょい押し） '''
        pass

    @classmethod
    def on_key_released_long(cls):
        ''' 離した時に実行 押している時間が threshold 以上の場合（長押し） '''
        pass

    ###########################################################################
    @classmethod
    def _get_key_pressed(cls, key):
        ''' https://msdn.microsoft.com/ja-jp/library/cc364583.aspx '''
        now_pressed = 0b1000000000000000
        # was_pressed = 0b0000000000000001

        return bool((ctypes.windll.user32.GetAsyncKeyState(key) & now_pressed) >> 15)

    @classmethod
    def _get_key_released(cls, key):
        return not cls._get_key_pressed(key)

    @classmethod
    def _get_keystates(cls):
        ''' https://msdn.microsoft.com/ja-jp/library/cc364674.aspx '''

        key_states = (ctypes.c_ubyte * 256)()
        ctypes.windll.user32.GetKeyboardState(key_states)

        ks = [0 for x in range(256)]
        for i in range(len(key_states)):
            ks[i] = bool((key_states[i] & 128) >> 7)
        return ks

    @classmethod
    def _get_keys_pressed(cls, **kwargs):
        ks = cls._get_keystates()
        res = []
        for i, x in enumerate(ks):
            if bool(x):
                res.append(i)

        return cls._filter_ignore_keys(res, **kwargs)

    @classmethod
    def _filter_ignore_keys(cls, keycodes, **kwargs):
        ''' https://msdn.microsoft.com/ja-jp/library/windows/desktop/dd375731(v=vs.85).aspx

            使わないけど何故かフラグ立ってるようなキーコード除外する '''

        def necessary(n, mouse_only=False, exclude_mouse=True):

            if mouse_only:
                if (0x00 <= n <= 0x06):
                    return True
                else:
                    return False
            elif exclude_mouse:
                if (0x00 <= n <= 0x06):
                    return False

            if (
                not (0x07 <= n <= 0x08) and
                not (0x0E <= n <= 0x0F) and
                not (0x13 <= n <= 0x1A) and
                not (0x3A <= n <= 0x40) and
                not (0x88 <= n <= 0x8F) and
                not (0x90 == n) and
                not (0x91 == n) and
                not (0x92 <= n <= 0x9F) and
                not (0xA6 <= n)
            ):
                return True

            else:
                return False

        filtered_codes = filter(lambda n: necessary(n, **kwargs), keycodes)
        return filtered_codes

    @classmethod
    def _check_any_keys_released(cls, pressed_keys):
        ''' return True if a any key released for given keys '''

        if not pressed_keys:
            return False

        for k in pressed_keys:
            if cls._get_key_released(k):
                return False
        else:
            return True

    ###########################################################################
    @classmethod
    def _main_loop(cls, *pressed_keys, **kwargs):
        ''' the main loop for polling and run cls.while_key_pressed function.

        Because of executed out of maya's main thread, calling maya.cmds (or mel.eval) is
        very unstable from this function. Thus wrapping these cmds with
        maya.utils.executeInMainThreadWithResult, using decorator 'execute_in_main_thread'.

        more info:
            [Maya Help: Python and threading:](http://help.autodesk.com/view/MAYAUL/2016/ENU/?guid=GUID-9B5AECBB-B212-4C92-959A-22599760E91A)
        '''

        global LOCK
        start_time = time.time()
        elapsed_time = time.time() - start_time
        delayed = kwargs.get('delayed', False)

        def wait_release(keys):
            while cls._check_any_keys_released(keys):
                time.sleep(cls.polling)
                elapsed_time = time.time() - start_time
                if elapsed_time > cls.threshold:
                    cls.while_key_pressed()

        with LOCK:
            try:
                # if delayed execute enable, key must be took again when the delayed began
                if delayed:
                    pressed_keys = maya.utils.executeInMainThreadWithResult(cls._get_keys_pressed)
                    # time.sleep(cls.polling)

                # execute begin event and execute while event at invertervaly
                # and then wait for key release
                cls.on_key_pressed_begin()
                wait_release(pressed_keys)

                # if mouse button continued down althogh keyshortcuts released,
                # the command still continue.
                mouse_down = maya.utils.executeInMainThreadWithResult(cls._get_keys_pressed, mouse_only=True)
                wait_release(mouse_down)

            except Exception as e:
                print e

            finally:
                elapsed_time = time.time() - start_time
                if elapsed_time < cls.threshold:
                    cls.on_key_released_short()

                else:
                    cls.on_key_released_long()

    @classmethod
    def execute(cls):
        ''' this function is invoked from maya directory from shortcut hotkey '''

        global LOCK
        if LOCK.locked():
            # return already locked AND delayed excute is disabled
            if not cls.enable_delayed_execute:
                return
            else:
                delayed = True

        else:
            delayed = False

        k = cls._get_keys_pressed()
        t = threading.Thread(
            target=cls._main_loop, args=(k), kwargs={'delayed': delayed})
        t.start()


class ToolBase(StickySupraTool):

    # default settings override
    # polling = 0.066  # in seconds
    # threshold = 0.2

    ###########################################################################
    initial_context = ""
    initial_context_class = ""

    tool_context = ""

    ###########################################################################
    @classmethod
    @execute_in_main_thread
    def on_key_pressed_begin(cls):
        ''' キー押し始めた時に実行する '''

        # キー離した時のために始動時の状態を保存する
        cls.initial_context = mel.eval("currentCtx;")
        cls.initial_context_class = mel.eval(
            'contextInfo -c "{0}";'.format(cls.initial_context))

        mel.eval('setToolTo {0};'.format(cls.tool_context))

    @classmethod
    @execute_in_main_thread
    def while_key_pressed(cls):
        ''' おしてる間中一定間隔で実行される '''
        pass

    @classmethod
    @execute_in_main_thread
    def on_key_released_short(cls):
        ''' 離した時に実行 押している時間が threshold 以下の場合（ちょい押し） '''

        if (cls.initial_context == cls.tool_context):
            mel.eval('setToolTo selectSuperContext')

    @classmethod
    @execute_in_main_thread
    def on_key_released_long(cls):
        ''' 離した時に実行 押している時間が threshold 以上の場合（長押し） '''

        if (cls.initial_context != cls.tool_context):
            mel.eval('setToolTo {0}'.format(cls.initial_context))
        else:
            mel.eval('setToolTo selectSuperContext')

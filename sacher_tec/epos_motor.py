# -*- coding: utf-8 -*-
#
# Copyright © Thorlabs-Kinesis Project Contributors
# Licensed under the terms of the GNU GPLv3+ License
# (see thorlabs_kinesis/__init__.py for details)

"""
KCube DC Servo Motor
--------------------
Bindings for Thorlabs KCube DC Servo DLL.
Implemented with Kinesis Version 1.14.23.16838
"""

from ctypes import *

from sacher_tec._utils import (
    c_word,
    c_dword,
    bind,
    not_implemented,
)

lib = cdll.LoadLibrary("EposCmd64.dll")

VCS_OpenDevice = bind(lib, "VCS_OpenDevice", [c_char_p,c_char_p,c_char_p,c_char_p,POINTER(c_int)],c_int)
VCS_OpenDeviceDlg = bind(lib, "VCS_OpenDeviceDlg", [POINTER(c_dword)],c_int)
VCS_SetProtocolStackSettings = bind(lib, "VCS_SetProtocolStackSettings", [c_void_p,POINTER(c_dword),POINTER(c_dword),POINTER(c_dword)],c_bool)
VCS_FindDeviceCommunicationSettings = bind(lib, "VCS_FindDeviceCommunicationSettings",[c_void_p, POINTER(c_char * 6), POINTER(c_char * 16), POINTER(c_char * 4), POINTER(c_char * 5), c_word, POINTER(c_dword), POINTER(c_dword), POINTER(c_word), c_int, POINTER(c_dword)], c_bool)
VCS_GetPositionIs = bind(lib, "VCS_GetPositionIs", [c_int, c_int, POINTER(c_long), POINTER(c_int)],c_int)
VCS_GetOperationMode = bind(lib, "VCS_GetOperationMode", [c_int, c_int, POINTER(c_byte), POINTER(c_int)],c_int)
VCS_GetState = bind(lib, "VCS_GetState", [c_int, c_int, POINTER(c_word), POINTER(c_int)],c_int)
VCS_SetState = bind(lib, "VCS_SetState", [c_int, c_int, c_word, POINTER(c_int)],c_int)
VCS_MoveToPosition = bind(lib, "VCS_MoveToPosition", [c_int, c_int, c_int, c_byte, c_byte, POINTER(c_int)],c_int)
VCS_GetMovementState = bind(lib, "VCS_GetMovementState", [c_int, c_int, POINTER(c_bool), POINTER(c_int)],c_int)
VCS_GetPositionProfile = bind(lib, "VCS_GetPositionProfile", [c_int, c_int, POINTER(c_dword), POINTER(c_dword), POINTER(c_dword), POINTER(c_int)],c_int)
VCS_SetPositionProfile = bind(lib, "VCS_SetPositionProfile", [c_int, c_int, c_dword, c_dword, c_dword, POINTER(c_int)],c_int)

VCS_CloseAllDevices = bind(lib, "VCS_CloseAllDevices", [POINTER(c_int)],c_bool)
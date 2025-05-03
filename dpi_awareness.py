import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)  # SYSTEM_AWARE
except:
    pass
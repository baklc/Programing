import ctypes

#타이틀 감지 함수
def gettitle():
    lib = ctypes.windll.LoadLibrary('user32.dll')
    handle = lib.GetForegroundWindow()
    buffer = ctypes.create_unicode_buffer(255)
    lib.GetWindowTextW(handle, buffer, ctypes.sizeof(buffer))

    return buffer.value

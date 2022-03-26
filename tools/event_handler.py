import ctypes

class Event_Listener:
    def toggle_listener(bot, key):
        while bot.quit == False:
            key_code = int(hex(ord(str.lower(key))), base=16)
            if ctypes.windll.user32.GetKeyState(key_code) > 1:
                print('toggle')
    
    def quit_listener(bot, key):
        while True:
            key_code = int(hex(ord(str.lower(key))), base=16)
            if ctypes.windll.user32.GetKeyState(key_code) > 1:
                bot.handle_quit()
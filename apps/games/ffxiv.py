from talon import ctrl, Module, Context, actions
import time

ctx = Context()
mod = Module()
apps = mod.apps
    
apps.ffxiv = "app.name: ffxiv_dx11.exe"

@mod.action_class
class Actions:
    def ffxiv_press(button: int):
        """mouse clicks are better handled by the game"""
        ctrl.mouse_click(button=button, hold=50)

    def ffxiv_macro(text: str):
        """execute a macro"""
        actions.key("enter")
        time.sleep(0.05)
        actions.insert(text)
        time.sleep(0.05)        
        actions.key("enter")
from talon import ctrl, Module, Context, actions

ctx = Context()
mod = Module()
apps = mod.apps
    
apps.ffxiv = "app.name: ffxiv_dx11.exe"

@mod.action_class
class Actions:
    def ffxiv_press(button: str):
        """mouse clicks are better handled by the game"""
        ctrl.mouse_click(button=button, hold=50)


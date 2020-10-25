from talon import Context,Module,actions,ctrl,cron
import time

ctx = Context()
mod = Module()
apps = mod.apps
    
apps.ffxiv = "app.name: ffxiv_dx11.exe"

gcd="2600ms"
bindings = {
    "ruin": "1",
    "ruinra": "2",
    "miasma": "3",
    "bio": "4",
    "drain": "5",
    "fester": "6",
    "egi1": "n",
    "egi2": "h",
    "enkindle": "z",
    "outburst": "u",
    "siphon": "j",
    "bane": ",",
    "ifrit": "l",
    "garuda": "o",
    "titan": "k",
    "sprint": ".",
    "resurrect": "9",
    "swiftcast": "8"
}

cast_job = None
def cast_job_start(spell: str):
    global cast_job
    def in_function():
        actions.key(bindings[spell])
    cast_job = cron.interval(gcd, in_function)

def cast_job_end(): 
    global cast_job
    if cast_job:
        cron.cancel(cast_job)
        cast_job = None    

@mod.action_class
class Actions:
    def ffxiv(spell: str):
        """execute a commando"""
        cast_job_end()
        actions.key(bindings[spell])
        
    def ffxiv_cast_job(spell: str):
        """repeat the following commando"""
        actions.user.ffxiv(spell)
        cast_job_start(spell)


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
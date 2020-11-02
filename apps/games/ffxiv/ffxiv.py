from talon import Context,Module,actions,ctrl,cron
import time
from os import listdir


ctx = Context()
mod = Module()
apps = mod.apps



apps.final_fantasy_xiv="""
app.name: steam_proton
app.name: ffxiv_dx11.exe
""" 

ctx.settings = {
    "key_wait": 10.0
}


ctx.matches = r"""
app: final_fantasy_xiv
"""

class_modes = {}
current_class = ""
bindings = {}
gcd="2550ms"

def load_class_settings():
    global bindings, class_modes, mod
    for file_name in listdir("./user/knausj_talon/apps/games/ffxiv/class_bindings"):
        class_name = file_name[:-4]
        class_modes[class_name] = f"Changes move set to {class_name}"
        with open(f"./user/knausj_talon/apps/games/ffxiv/class_bindings/{file_name}", "r") as binding_file:
            for line in binding_file.readlines():
                spell, binding = line.split(",",1)
                bindings[f"{class_name}.{spell}"] = binding
    
    for key, value in class_modes.items():
        mod.mode(f"ffxiv_{key}", value)


load_class_settings()


@mod.capture(rule=f"({'|'.join(class_modes.keys())})")        
def ffxiv_classes(m) -> str:
    return m[0]

cast_job = None
cast_job_interruptible = True
cast_job_spell = None

def cast_job_start(spell: str, interruptible: bool = True):
    global cast_job, cast_job_interruptible, cast_job_spell
    cast_job_spell = spell
    cast_job_interruptible = interruptible
    def in_function():
        actions.key(bindings[f"{current_class}.{spell}"])
    cast_job = cron.interval(gcd, in_function)

def cast_job_end(): 
    global cast_job
    if cast_job:
        cron.cancel(cast_job)
        cast_job = None    

def cast_job_resume():
    global cast_job_interruptible, cast_job_spell
    cast_job_start(cast_job_spell, cast_job_interruptible)

@mod.action_class
class Actions:
    def ffxiv_gcd(spell: str):
        """execute a commando"""
        global cast_job_interruptible
        cast_job_end()
        actions.key(bindings[f"{current_class}.{spell}"])
        if not cast_job_interruptible:
            cast_job_resume()
    
    def ffxiv_ogcd(spell: str):
        """Execute the commando without regard for the global cool down"""
        actions.key(bindings[f"{current_class}.{spell}"])        

    def ffxiv_cast_job(spell: str):
        """repeat the following commando"""
        actions.user.ffxiv_gcd(spell)
        cast_job_start(spell)

    def ffxiv_repeat_job(spell: str):
        """Repeat the following commando until stop"""
        actions.user.ffxiv_gcd (spell)
        cast_job_start(spell, False)
    
    def ffxiv_stop_repeat():
        """ will stop any repeat job"""
        cast_job_end()

    def ffxiv_macro(text: str):
        """execute a macro"""
        actions.key("enter")
        time.sleep(0.05)
        actions.insert(text)
        time.sleep(0.1)        
        actions.key("enter")
    
    def ffxiv_switch_mode(class_name: str):
        """switches key bindings to the following class"""
        global current_class
        if current_class:
            actions.mode.disable(f"user.ffxiv_{current_class}")
        current_class = class_name
        print(f"switching to {current_class}")
        actions.mode.enable(f"user.ffxiv_{class_name}")
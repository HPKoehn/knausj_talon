from talon import noise, actions
from time import time

t_old = 0
HISS_MIN_TIME = 0.175

def on_hiss(active):
    global t_old
    t_delta = time() - t_old
    if not active and t_delta > HISS_MIN_TIME:
        actions.key("pgdown")
    t_old = time()

noise.register("hiss",on_hiss)
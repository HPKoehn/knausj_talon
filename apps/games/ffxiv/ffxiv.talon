app: final_fantasy_xiv
-

down: key(keypad_2)
up: key(keypad_8)
left: key(keypad_4)
right: key(keypad_6)
okay: key(keypad_0)
cancel: key(keypad_decimal)
option left: key(keypad_7)
option right: key(keypad_9)
interface next: key(keypad_1)
menu open: key(keypad_plus)

target [next]: user.key(t)
target last: user.key(ctrl-t)
teleport initiate: user.ffxiv_macro("/teleport")
target member <number_small>: key("f{number_small}")
stop it: user.ffxiv_stop_repeat()

job switch to <user.ffxiv_classes>: user.ffxiv_switch_mode("{ffxiv_classes}")
 
inventory open: key(y)
character open: key(c)
map open: key(x)
take off:
    key(space)
    key(space)
party finder open: key(v)
journal open: key(g)
recall initiate: key(b)

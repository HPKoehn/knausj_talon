app.name: ffxiv_dx11.exe
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

(target|next): 
    key(t)
    key(t)
teleport initiate:
    key(enter)
    insert("/teleport")

cast: key(1)
walk: key(2)
miasma: key(3)
bio: key(4)
drain: key(5)
heavy: key(6)
fuss: key(n)
attack: key(h)
ignite: key(z)
spam: key(u)
siphon: key(j)
curse: key(,)
familiar red: key(l)
familiar (green|blue): key(o)
familiar yellow: key(k)
sprint: key(.)
resurrect: key(9)
instant: key(8)
focus member <number_small>: key("f{number_small}")

inventory open: key(y)
character open: key(c)
map open: key(x)
take off:
    key(space)
    key(space)
party finder open: key(v)
journal open: key(g)
recall initiate: key(b)

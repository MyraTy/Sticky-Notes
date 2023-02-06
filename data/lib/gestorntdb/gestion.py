import time as tm

class Remember(Exception):
    pass

class Notes_cant_open(OSError):
    pass

class Note:
    def __init__(self, user, dir_):
        try:
            self.user = user
            self.dir = dir_
        except Exception:
            raise Notes_cant_open(r"Use /, not \ .")

    def writenotes(self, note, remember=None, overwrite=False):
        """Write notes at data/notes/notes.ntdb
        Syntax is note.writenotes(note, remember=None, overwrite=False), whenether note = Note(user, dir_)
        Note is the note itself,
        remember is the date and time when a recoratory is shown, default None, overwrite is if you want to overwrite the entire file to write notes, default False.
        If overwrite is True, your note will be written at position 0, else, it wil be written at the last position."""

        if overwrite:
            notes = open("C:/Users/{user}/{dir_}/Sticky Notes/data/notes/notes.ntdb".format(user=self.user, dir_=self.dir), mode="w", encoding="utf8")
        else:
            notes = open("C:/Users/{user}/{dir_}/Sticky Notes/data/notes/notes.ntdb".format(user=self.user, dir_=self.dir), mode="a", encoding="utf8")
            
        if remember == None:
            if overwrite:
                notes.write(" " + "||||" + note)
            else:
                notes.write("||||" + note)
        else:
            if overwrite:
                notes.write("Genesis Note. Only for pad." + "||||" + note + "╔" + str(remember))
            else:
                notes.write("||||" + note + "╔" + str(remember))

        notes.close()

    def readnotes(self, numNote):
        """Read notes written in data/notes/notes.ntdb
        The syntax is note.readnotes(numNote), whenether note = Note(user, dir_).
        NumNote is the position of your note you want to read in notes.ntdb The first note is at position 0, is only a pad note, your first note is at position 1, and over."""

        notes = open("C:/Users/{user}/{dir_}/Sticky Notes/data/notes/notes.ntdb".format(user=self.user, dir_=self.dir), mode="r", encoding="utf8")
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

        try:
            note = data[numNote]
        except IndexError:
            raise Notes_cant_open("Any note is written at position {pos}.".format(pos=numNote))
        msg = note

        if type(note) == list:
            raise Remember("{note}, to the date and time of {time}".format(note=note[0], time=note[1]))

        print(msg)
        notes.close()
        return msg

    def delete_all(self):
        """Delete all notes from ndata/lib/notes/notes.ntdb
        The syntax is note.delete_all(), whenether note = Note(user, dir_)."""
        notes = open("C:/Users/{user}/{dir_}/Sticky Notes/data/notes/notes.ntdb".format(user=self.user, dir_=self.dir), mode="w")
        notes.write("")
        notes.close()
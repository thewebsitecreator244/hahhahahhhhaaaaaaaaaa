import tkinter
from tkinter.messagebox import showinfo, showerror, askyesno
from tkinter.simpledialog import askstring
import json


def show_num():
    chosen_index = listbox.curselection()
    if chosen_index != ():
        contact = listbox.get(chosen_index)
        number = phones[contact]
        showinfo(contact, number)


def change_():
    chosen_index = listbox.curselection()
    if chosen_index != ():
        contact = listbox.get(chosen_index)
        number = askstring(contact, "enter new number")
        phones[contact] = number
        with open("phones.json", "w") as new:
            json.dump(phones, new)


def add_():
    contact_name = askstring("", "enter new contact name")
    if contact_name != "" and contact_name not in phones:
        number = askstring("", "enter new number")
        phones[contact_name] = number
        listbox.insert(tkinter.END, contact_name)
        with open("phones.json", "w") as new:
            json.dump(phones, new)
    else:
        showerror("error", "didn't enter contact or  contact already exists!")


def del_():
    chosen_index = listbox.curselection()
    if chosen_index != ():
        contact = listbox.get(chosen_index)
        yesno = askyesno("", f"do you really wanna delete {contact}")
        if yesno:
            listbox.delete(chosen_index)
            del phones[contact]
            with open("phones.json", "w") as new:
                json.dump(phones, new)


if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("phonebook")
    window.geometry("600x600")
    listbox = tkinter.Listbox(window)
    with open("phones.json") as f:
        phones = json.load(f)
        for key in phones:
            listbox.insert(tkinter.END, key)

    listbox.pack(fill=tkinter.BOTH)
    show_number = tkinter.Button(window, text="show number", command=show_num)
    change = tkinter.Button(window, text="change number", command=change_)
    add = tkinter.Button(window, text="add new contact", command=add_)
    delete = tkinter.Button(window, text="delete contact", command=del_)
    show_number.pack(fill=tkinter.BOTH)
    change.pack(fill=tkinter.BOTH)
    add.pack(fill=tkinter.BOTH)
    delete.pack(fill=tkinter.BOTH)

    window.mainloop()

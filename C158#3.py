from tkinter import *
root = Tk()
root.title('C158#3')
root.geometry('400x400')

inputBox = Entry(root)
inputBox.pack()

def add():
    a = 12
    input_number = inputBox.get()
    try:
        print(a + input_number)
    except:
        messagebox.showinfo('Error', 'We cannot add 2 different datatypes')
    
btn = Button(root,text="add",command=add)
btn.place(relx= 0.5,rely=0.5,anchor=CENTER)
btn.pack()
    
mainloop()
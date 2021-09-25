from tkinter import *
root = Tk()
root.title('Geometry Error')

try:
    geometry('600')
    
except:
    print('A value is missing in geometry')
    
root.mainloop()
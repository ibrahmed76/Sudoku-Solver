from tkinter import *
from tkinter import font
from solver import solver

root = Tk()
root.title("Sudoku Solver")
root.geometry("526x743")
root.configure(bg="#8B0000")
root.resizable(False,False)

dreamland_font = font.Font(family="DreamlandStd", size=38)

label = Label(root, text="Sudokuuu Solverrr", font=dreamland_font, bg="#8B0000",fg="#FFFF00")
label.place(x=0,y=10,width=526)

label=Label(root,text="",fg="#B8860B",bg="#8B0000",font=('TkDefaultFont',18))
label.place(x=0,y=92,width=526)

#Store each cell of input grid
cells={}

def isValidNum(P):
    out = (P.isdigit() or P == "") and len(P) < 2
    return out 

#register function
reg = root.register(isValidNum)

def drawBGrid():
    frame = Frame(root, bg="#91abc6")
    frame.place(x=42, y=151, width=443, height=443)
    font = ('TkTextFont', 14)

    for i in range(9):
        for j in range(9):
            entry = Entry(frame, bg="#fff", fg="#000", font=font, borderwidth=1, 
                          highlightbackground="#fff", relief=FLAT, justify="center", 
                          validate="key", validatecommand=(reg, '%P'))
            entry.place(x=i*49, y=j*49, width=48, height=48)
            cells[(i+2, j+1)] = entry

    for i in range(0, 10, 3):
        Frame(frame, bg="#000", width=4).place(x=i*49-1, y=0, height=441)
        Frame(frame, bg="#000", width=441).place(x=0, y=i*49-1, height=4)
   
    
def clearData():
    label.configure(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell = cells[(row,col)]
            cell.delete(0,"end")

def getValues():
    board=[]
    label.configure(text="")
    for row in range(2,11):
        rows = []
        for col in range(1,10):
            val = cells[(row,col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    updateValues(board)

btn=Button(root,command=getValues,text="Solve",width=10,font=('TkTextFont',14))
btn.place(x=25, y=650)

btn=Button(root,command=clearData,text="Clear",width=10,font=('TkTextFont',14))
btn.place(x=198, y=650)

btn=Button(root,command=root.destroy,text="Quit",width=10,font=('TkTextFont',14))
btn.place(x=370, y=650)

drawBGrid()

def updateValues(s):
    sol=solver(s)
    if sol != None:
        for rows in range (2,11):
            for cols in range (1,10):
                cells[(rows,cols)].delete(0,"end")
                cells[(rows,cols)].insert(0,sol[rows-2][cols-1])
        label.configure(text="Solved!")
    else:
        label.configure(text="Not Solved :( ")

root.mainloop()

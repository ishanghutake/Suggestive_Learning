from tkinter import *
import numpy as np

root = Tk()

root.title('Suggestive learning')

x = [24];
q = 1;
a = 1;
b = -1;
c = 0;


def quit():
    global q
    q = q + 1;
    root.quit()


def printValues():
    for i in range(len(x)):
        print(x[i], "x printing")


def timeManagement1():
    root.destroy()
    global x
    if (var1.get() == 1):
        x[0] = [1]
    elif (var1.get() == 2):
        x[0] = [-1]
    else:
        x[0] = [0]


def timeManagement2():
    root.destroy()
    global x
    if (var2.get() == 1):
        x = np.vstack([x, a])
        print(x)
    elif (var2.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def realFocus1():
    root.destroy()
    global x
    if (var3.get() == 1):

        x = np.vstack([x, a])
    elif (var3.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def realFocus2():
    root.destroy()
    global x
    if (var4.get() == 1):
        x = np.vstack([x, a])
    elif (var4.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def realFocus3():
    root.destroy()
    global x
    if (var5.get() == 1):
        x = np.vstack([x, a])
    elif (var5.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def addBenefits1():
    root.destroy()
    global x
    if (var6.get() == 1):
        x = np.vstack([x, a])
    elif (var6.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def addBenefits2():
    root.destroy()
    global x
    if (var7.get() == 1):
        x = np.vstack([x, a])
    elif (var7.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def addBenefits3():
    root.destroy()
    global x
    if (var8.get() == 1):
        x = np.vstack([x, a])
    elif (var8.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def technology():
    root.destroy()
    global x
    if (var9.get() == 1):
        x = np.vstack([x, a])
    elif (var9.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def technology2():
    root.destroy()
    global x
    if (var10.get() == 1):
        x = np.vstack([x, a])

    elif (var10.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def technology3():
    root.destroy()
    global x
    if (var11.get() == 1):
        x = np.vstack([x, a])
    elif (var11.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def technology4():
    root.destroy()
    global x
    if (var12.get() == 1):
        x = np.vstack([x, a])
    elif (var12.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def communication():
    root.destroy()
    global x
    if (var13.get() == 1):
        x = np.vstack([x, a])
    elif (var13.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def communication2():
    root.destroy()
    global x
    if (var14.get() == 1):
        x = np.vstack([x, a])
    elif (var14.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def communication3():
    root.destroy()
    global x
    if (var15.get() == 1):
        x = np.vstack([x, a])
    elif (var15.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def communication4():
    root.destroy()
    global x
    if (var16.get() == 1):
        x = np.vstack([x, a])
    elif (var16.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def communication5():
    root.destroy()
    global x
    if (var17.get() == 1):
        x = np.vstack([x, a])
    elif (var17.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def freedom():
    root.destroy()
    global x
    if (var18.get() == 1):
        x = np.vstack([x, a])
    elif (var18.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def miss():
    root.destroy()
    global x
    if (var19.get() == 1):
        x = np.vstack([x, a])
    elif (var19.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def miss2():
    root.destroy()
    global x
    if (var20.get() == 1):
        x = np.vstack([x, a])
    elif (var20.get() == 2):
        x = np.vstack([x, b])
    else:
        global z
        x = np.vstack([x, c])


def miss3():
    root.destroy()
    global x
    if (var21.get() == 1):
        x = np.vstack([x, a])
    elif (var21.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def miss4():
    root.destroy()
    global x
    if (var22.get() == 1):
        x = np.vstack([x, a])
    elif (var22.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])


def miss5():
    root.destroy()
    global x
    if (var23.get() == 1):
        x = np.vstack([x, a])
    elif (var23.get() == 2):
        x = np.vstack([x, b])
    else:
        x = np.vstack([x, c])




while (q == 1):
    var1 = IntVar()

    var1.set(3)

    Label(root, text="1)Do you have enough commitment to go to class regularly?", padx=100).pack(anchor=W)
    Radiobutton(root, text="Yes", padx=100, variable=var1, value=1).pack(anchor=W)
    Radiobutton(root, text="No", padx=100, variable=var1, value=2).pack(anchor=W)
    Radiobutton(root, text="None of the above", padx=100, variable=var1, value=0).pack(anchor=W)
    Button(root, text="Submit", command=timeManagement1).pack()
    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()
    var2 = IntVar()
    var2.set(3)

    Label(root, text="2)Does your daily life provide a flexible schedule?", padx=100).pack(anchor=W)
    Radiobutton(root, text="Yes", padx=100, variable=var2, value=1).pack(anchor=W)
    Radiobutton(root, text="No", padx=100, variable=var2, value=2).pack(anchor=W)
    Radiobutton(root, text="None of the above", padx=100, variable=var2, value=0).pack(anchor=W)
    Button(root, text="Submit", command=timeManagement2).pack()
    Button(root, text="quit", command=quit).pack()

    root.mainloop()

    break

while (q == 1):
    root = Tk()

    var3 = IntVar()

    var3.set(3)

    Label(root, text="3)Do you have enough discipline complete the course by ownself?", padx=100).pack(anchor=W)
    Radiobutton(root, text="Yes", padx=100, variable=var3, value=1, ).pack(anchor=W)
    Radiobutton(root, text="No", padx=100, variable=var3, value=2, ).pack(anchor=W)
    Radiobutton(root, text="None of the above", padx=100, variable=var3, value=0).pack(anchor=W)
    Button(root, text="Submit", command=realFocus1).pack()
    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()

    var4 = IntVar()

    var4.set(3)

    Label(root, text="4)Are you more self-study oriented?", padx=100).pack(anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var4, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var4, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var4, value=0).pack(anchor=W)

    Button(root, text="Submit", command=realFocus2).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break
while (q == 1):
    root = Tk()

    var5 = IntVar()

    var5.set(3)

    Label(root, text="5)Do you have poor schedule habits?", padx=100).pack(anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var5, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var5, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var5, value=0).pack(anchor=W)

    Button(root, text="Submit", command=realFocus3).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()

    var6 = IntVar()

    var6.set(3)

    Label(root, text="6)Are you always prepared well for a course with pre-requisites?",
          padx=100).pack(anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var6, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var6, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var6, value=3).pack(anchor=W)

    Button(root, text="Submit", command=addBenefits1).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break
while (q == 1):
    root = Tk()

    var7 = IntVar()

    var7.set(3)

    Label(root, text="7)Do you want to learn on your pace?", padx=100).pack(anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var7, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var7, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var7, value=3).pack(anchor=W)

    Button(root, text="Submit", command=addBenefits2).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()

    var8 = IntVar()

    var8.set(3)

    Label(root, text="8)Do you want to finish course as quickly as possible?", padx=100).pack(anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var8, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var8, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var8, value=3).pack(anchor=W)

    Button(root, text="Submit", command=addBenefits3).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()

    var9 = IntVar()

    var9.set(3)

    Label(root, text="9) Do you have basic computer skills to troubleshoot minor computer problems?", padx=100).pack(
        anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var9, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var9, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var9, value=3).pack(anchor=W)

    Button(root, text="Submit", command=technology).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()

    var10 = IntVar()

    var10.set(3)

    Label(root, text="10)Does your in-class assignments from previous lecture a burden??", padx=100).pack(anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var10, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var10, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var10, value=3).pack(anchor=W)

    Button(root, text="Submit", command=technology2).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()

    var11 = IntVar()

    var11.set(3)

    Label(root, text="11)Want 24x7 service?", padx=100).pack(anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var11, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var11, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var11, value=3).pack(anchor=W)

    Button(root, text="Submit", command=technology3).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()

    var12 = IntVar()

    var12.set(3)

    Label(root, text="12)Do you rate yourself maximum from previous academic experience in classroom?", padx=100).pack(
        anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var12, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var12, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var12, value=3).pack(anchor=W)
    Button(root, text="Submit", command=technology4).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()

    var13 = IntVar()

    var13.set(3)

    Label(root, text="13)Do you have good writing and communication skills?", padx=100).pack(anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var13, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var13, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var13, value=3).pack(anchor=W)

    Button(root, text="Submit", command=communication).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break
while (q == 1):
    root = Tk()

    var14 = IntVar()

    var14.set(3)

    Label(root, text="14)Is interaction with other student is great deal?", padx=100).pack(anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var14, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var14, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var14, value=3).pack(anchor=W)

    Button(root, text="Submit", command=communication2).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()

    var15 = IntVar()

    var15.set(3)

    Label(root, text="15)Do you hesitate to raise question in the class?", padx=100).pack(anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var15, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var15, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var15, value=3).pack(anchor=W)

    Button(root, text="Submit", command=communication3).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()

    var16 = IntVar()

    var16.set(3)

    Label(root, text="16)Are you social and like to create a teacher student bond?", padx=100).pack(anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var16, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var16, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var16, value=3).pack(anchor=W)

    Button(root, text="Submit", command=communication4).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()

    var17 = IntVar()

    var17.set(3)

    Label(root,
          text="17)Are you comfortable communication through email, chat and video or u prefer in-person communication?",
          padx=100).pack(anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var17, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var17, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var17, value=3).pack(anchor=W)

    Button(root, text="Submit", command=communication5).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()

    var18 = IntVar()

    var18.set(3)

    Label(root, text="18)Is your learning style compatible with an online course?", padx=100).pack(
        anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var18, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var18, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var18, value=3).pack(anchor=W)

    Button(root, text="Submit", command=freedom).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()

    var19 = IntVar()

    var19.set(3)

    Label(root, text="19)Are you dependent on friends for study oriented discussions?", padx=100).pack(anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var19, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var19, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var19, value=3).pack(anchor=W)
    Button(root, text="Submit", command=miss).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()

    var20 = IntVar()

    var20.set(3)

    Label(root, text="20)Are you a working professional?", padx=100).pack(anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var20, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var20, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var20, value=3).pack(anchor=W)

    Button(root, text="Submit", command=miss2).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()

    var21 = IntVar()

    var21.set(3)

    Label(root, text="21)Are you a working professional?", padx=100).pack(anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var21, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var21, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var21, value=3).pack(anchor=W)
    Button(root, text="Submit", command=miss3).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()

    var22 = IntVar()

    var22.set(3)

    Label(root, text="22)Money is a obstacle in life?", padx=100).pack(anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var22, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var22, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var22, value=3).pack(anchor=W)

    Button(root, text="Submit", command=miss4).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break

while (q == 1):
    root = Tk()

    var23 = IntVar()

    var23.set(3)

    Label(root, text="23)A online degree provided will be viewed positively by your employers?", padx=100).pack(anchor=W)

    Radiobutton(root, text="Yes", padx=100, variable=var23, value=1).pack(anchor=W)

    Radiobutton(root, text="No", padx=100, variable=var23, value=2).pack(anchor=W)

    Radiobutton(root, text="None of the above", padx=100, variable=var23, value=3).pack(anchor=W)

    Button(root, text="Submit", command=miss5).pack()

    Button(root, text="quit", command=quit).pack()
    root.mainloop()
    break



printValues()
print(x)

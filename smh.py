from tkinter import *
from PIL import Image, ImageTk
import random


class HangMan:
    def __init__(self, win):
        self.win = win
        self.word = ""
        self.wordLabel = Label()
        self.counter = 0

        self.mainWindowStuff()

    def mainWindowStuff(self):
        self.win.title("HangMan Game")
        self.win.config(bg="gray8")

        title_label = Label(self.win, text="The HangMan Game", font=(None, 40), fg="whitesmoke", bg="gray8")
        title_label.place(x=400, y=10)


        self.generateWord()
        self.keyboard()
        self.drawHangman()

    def keyboard(self):
        keyFrame = Frame(self.win, width=1350, height=300, bg='gray8', relief=RIDGE, bd=10)
        keyFrame.place(x=50, y=500)

        row = 1
        column = 1

        for i in range(65, 91):  # To get all the alphabets from a-z using ASCII
            char = chr(i)
            key_button = Button(keyFrame, text=char, font=(None, 25), padx=10,
                                pady=5, fg = "whitesmoke", bg = "gray8")  # , command = lambda key_button = key_button: self.keyPressed(key_button)
            key_button.grid(row=row, column=column, sticky=W)
            key_button["command"] = lambda key_button=key_button: self.keyPressed(key_button)
            if key_button["text"] == "W":
                key_button.config(padx=5)

            if column == 18:
                row += 1
                column = 0
            column += 1

    def createCircle(self, x, y, r, canvas):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvas.create_oval(x0, y0, x1, y1, width = 2)

    def createFace(self, isAlive, drawingCanvas):
        self.createCircle(215,75 + 20, 20, drawingCanvas) # Face
        if(isAlive):
            #Alive Face
            drawingCanvas.create_rectangle(205, 90, 205, 90, width = 4) # Left Eye
            drawingCanvas.create_rectangle(223, 90, 223, 90, width = 4) # Right Eye
            drawingCanvas.create_line(207, 105, 223, 105, width = 2) #Mouth


        elif(not isAlive):
            #Dead Face
            drawingCanvas.create_line(203, 94, 210, 87, width = 2)# Eye
            drawingCanvas.create_line(210, 94, 203, 87, width = 2)# EYE

            drawingCanvas.create_line(220, 94, 227, 87, width = 2)# Eye
            drawingCanvas.create_line(227, 94, 220, 87, width = 2)# EYE

            drawingCanvas.create_line(205, 106, 230, 96, width = 2) # Mouth

    def drawHangman(self):
        drawingCanvas = Canvas(self.win, bg = "grey8", bd = 10, relief = RIDGE)

        drawingCanvas.create_line(125, 50, 125, 250, width = 5) # Stalk
        drawingCanvas.create_line(160, 50, 125, 80, width = 5) #Stalk Line Holder
        drawingCanvas.create_line(125, 50, 275, 50, width = 5) # Top Line
        drawingCanvas.create_line(125, 210, 150, 250, width = 5)# Base Holder Right
        drawingCanvas.create_line(125, 210, 100, 250, width = 5)# Base Holder Left
        drawingCanvas.create_line(75, 250, 175, 250, width = 5) # Base Line
        drawingCanvas.create_line(215, 50, 215, 75, width = 2) # Noose

        if self.counter == 1:
            self.createFace(True, drawingCanvas)
        elif self.counter == 2:
            self.createFace(True, drawingCanvas)
            drawingCanvas.create_line(215, 115, 215, 180, width = 2) # Body
        elif self.counter == 3:
            self.createFace(True, drawingCanvas)
            drawingCanvas.create_line(215, 115, 215, 180, width = 2) # Body
            drawingCanvas.create_line(215, 135, 175, 150, width = 2) # Left Arm
        elif self.counter == 4:
            self.createFace(True, drawingCanvas)
            drawingCanvas.create_line(215, 115, 215, 180, width = 2) # Body
            drawingCanvas.create_line(215, 135, 175, 150, width = 2) # Left Arm
            drawingCanvas.create_line(215, 135, 255, 150, width = 2) # Right Arm
        elif self.counter == 5:
            self.createFace(True, drawingCanvas)
            drawingCanvas.create_line(215, 115, 215, 180, width = 2) # Body
            drawingCanvas.create_line(215, 135, 175, 150, width = 2) # Left Arm
            drawingCanvas.create_line(215, 135, 255, 150, width = 2) # Right Arm
            drawingCanvas.create_line(215, 180, 250, 215, width = 2) # Right Leg
        elif self.counter == 6:
            self.createFace(True, drawingCanvas)
            drawingCanvas.create_line(215, 115, 215, 180, width = 2) # Body
            drawingCanvas.create_line(215, 135, 175, 150, width = 2) # Left Arm
            drawingCanvas.create_line(215, 135, 255, 150, width = 2) # Right Arm
            drawingCanvas.create_line(215, 180, 250, 215, width = 2) # Right Leg
            drawingCanvas.create_line(215, 179, 185, 215, width = 2) # Left Leg
        elif self.counter == 7:
            self.createFace(False, drawingCanvas)
            drawingCanvas.create_line(215, 115, 215, 180, width = 2) # Body
            drawingCanvas.create_line(215, 135, 175, 150, width = 2) # Left Arm
            drawingCanvas.create_line(215, 135, 255, 150, width = 2) # Right Arm
            drawingCanvas.create_line(215, 180, 250, 215, width = 2) # Right Leg
            drawingCanvas.create_line(215, 179, 185, 215, width = 2) # Left Leg



        drawingCanvas.place(x = 500, y = 200)

    def keyPressed(self, button):
        button['state'] = DISABLED
        # print(button["text"])
        txt = button["text"]
        indices = []



        for i in range(len(self.formattedWord)):
            if self.formattedWord[i] == txt:
                indices.append(i)

        j = list(self.hidden_word)
        for i in indices:
            j[i] = txt

        new_str = ""
        for i in j:
            new_str += i

        self.hidden_word = new_str

        if len(indices) == 0:
            self.counter += 1
            self.drawHangman()

        if (not "_" in self.hidden_word):
            print("hahahahahah")
        self.wordLabel["text"] = self.hidden_word

    def generateWord(self):

        wordsList = ['integral', 'earthworm', 'swimsuit', 'terrace', 'alteration', 'verification', 'assault', 'parsley',
                     'recorder', 'bestseller', 'shelter', 'vulture', 'speedboat', 'nanoparticle', 'collection',
                     'amazement', 'validity', 'boatload', 'armoire', 'training', 'gingerbread', 'currency',
                     'marketplace', 'composition', 'interferometer', 'burglar', 'podcast', 'footwear', 'homework',
                     'decision', 'catalyst', 'doughnut', 'iceberg', 'eyeliner', 'footage', 'vinegar', 'sidewalk',
                     'opposition', 'editing', 'trustee', 'upstairs', 'stinger', 'grandfather', 'professor', 'parenting',
                     'jalapeno', 'construction', 'director', 'hypothesis', 'briefing', 'hometown', 'fingerling',
                     'gateway', 'opportunity', 'trading', 'publisher', 'sauerkraut', 'puritan', 'microphone',
                     'porthole', 'kumquat', 'aircraft', 'discharge', 'disclosure', 'seashore', 'browser', 'financing',
                     'imbalance', 'sustenance', 'familiar', 'incubation', 'millennium', 'grenade', 'titanium',
                     'marriage', 'laundry', 'gasoline', 'endothelium', 'manatee', 'prostanoid', 'clapboard',
                     'marmalade', 'trouble', 'refectory', 'contour', 'caliber', 'waterfront', 'jewelry', 'business',
                     'neighbour', 'embarrassment', 'midline', 'shirtdress', 'semester', 'handball', 'strawberry',
                     'selling', 'hamburger', 'furnace', 'quicksand','eyelash','pizza']

        randomNum = random.randint(0, len(wordsList) - 1)

        self.word = wordsList[randomNum].upper()
        self.formattedWord = ""
        self.hidden_word = ""

        for i in self.word:
            self.formattedWord += i + " "
            self.hidden_word += "_" + " "

        self.updateWord()

    def updateWord(self):
        wordFrame = Frame(self.win, height=10, width=10, bg="grey8", relief=RIDGE, bd=10)
        self.wordLabel = Label(wordFrame, text=self.hidden_word, font=(None, 30), fg = "whitesmoke", bg = "grey8")
        wordFrame.place(x=550, y=100)
        self.wordLabel.pack()

        print(self.formattedWord)


if __name__ == "__main__":
    win = Tk()
    runObject = HangMan(win)
    win.mainloop()

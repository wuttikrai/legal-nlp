from tkinter import *
from pathlib import Path
from tkinter import filedialog
from pythainlp.tokenize import word_tokenize
from setuptools import command


class gui :
    global list, text
    list = []
    text = []
    def __init__(self,master, box_list):
        frame = Frame(master)


        count = 0
        master[ 'bg' ] = '#c0c0aa'




        self.label_1 = Label(master,text='Input Text',

                            width= 20,
                            font=('Ariel',15,'bold'))
        self.label_1.grid(row=5, column = 0,padx =60, pady = 70)

        self.label_2 = Label (master , text = 'Summary' ,
                          width = 20 ,
                          font = ('Ariel' , 15 , 'bold') )
        self.label_2.grid ( row = 5 , column = 12 , padx = 60 )

        self.preview = Label ( master , text = 'Preview' ,
                          width = 20 ,
                          font = ('Ariel' , 15 , 'bold') )
        self.preview.grid ( row = 5 , column = 10 , padx = 200 )


        #<------------------------------------------------------------------------------>

        self.listbox = Listbox (master , height = 25 ,
                                                  width = 30 ,
                                                  bg = "grey" ,
                                                  activestyle = 'dotbox' ,
                                                  font = "Helvetica" ,
                                                  fg = "black" )
        self.listbox.grid(row = 6, column = 0 )



        # Center Box
        self.preview = Text(master, height = 30, width = 75)
        self.preview.grid(row=6, column = 10)

        #Right Box
        self.summary = Text ( master , height = 30 , width = 30 )
        self.summary.grid ( row = 6 , column = 12 )




        btn_sticky = Button ( master , text = "Analyze", command = self.nlp )
        btn_sticky.grid ( sticky = S )





#<---------------------------------------------------------------------->
        self.menu = Menu(master)

        self.menu.add_command ( label = 'Open File', command = self.openfile)





        master.config ( menu = self.menu )




#<-------------------------------------------------------->
    def openfile(self) :


        filepath = filedialog.askopenfilename ( initialdir = "/" ,
                                                         filetypes=[('text files', 'txt')],

                                                         )
        # Add Dekaname to box list
        deka_name = (Path ( filepath ).stem)
        self.listbox.insert(END,deka_name)


        #Add data to preview box
        self.f = open ( filepath , "r" , encoding = "utf-8" )
        self.preview.insert(END, self.f.read ( ) )


        #Keep string data to list and w8 to use
        with open( filepath , "r" , encoding = "utf-8" ) as str_data :
            data = str_data.read()
            text.append(data)


        #test for show data
        #self.show_data(list = None, text = text)

    def show_data (self,list ,text) :

        print(text)





    def nlp (self) :

        print(text)
        cut = word_tokenize(str(text), engine= "newmm")


        print(cut)
        self.summary.insert(END,cut)







if __name__ == "__main__" :
    root = Tk ( )
    root.geometry ( '500x500' )

    call = gui(root, box_list = None)




    root.mainloop()

from tkinter import *
import List_Templater
import Queue_Templater
import Tree_Templater
top = Tk()
img = Image("photo", file="processing.gif")
top.tk.call('wm','iconphoto',top._w,img)
top.wm_title("Data Structurator")
top.configure(background = 'black')
begin = 0
write_set  = 0
def print_contents(event) :
	#print(text.get(1.0, END))
	#print(text.get(1.0, END),file = f)
	ds=var.get()
	top.destroy()
	if(ds=="List"):
		List_Templater.__main__()
	elif(ds=="Queue"):
		Queue_Templater.__main__()
	elif(ds=="Tree"):
		Tree_Templater.call()
	global write_set
	write_set = 1
	global begin
	begin += 1
	#top.quit()
def add_file(event):
	dm = datat.get()
	var = text.get(1.0,END)
	
	printer = ""
	printer += dm
	printer += " "
	printer += var
	print(printer)
	global write_set
	global begin
	if(begin == 0):
		f=open("attributes.txt","w")
		begin += 1
		#write_set = 0
	elif write_set == 0:
		f = open("attributes.txt","a")
		begin += 1
	elif write_set == 1:
		f = open("attributes.txt","w")
		write_set = 0
		begin += 1
	print(printer,file = f)
	f.close()
w = Label(top, text="Choosing Attributes",fg = "red")
w.grid(row = 2,column = 1)
w.pack(side = LEFT)
 
datat=StringVar(top)
datat.set("int")
optiond=OptionMenu(top,datat,"int","String","double")
optiond.grid(row=2,column = 2)
optiond.pack(side = LEFT)
text = Text(width="30", height="1")
text.grid(row=2, column= 3)
text.pack(side = LEFT)
button = Button(top, text='Add another')
button.grid(row=2, column= 4)
button.bind('<Button-1>', add_file)
button.pack(side = LEFT)
k = Label(top, text="Choose Data Structure",fg = "red")
k.grid(row = 4,column = 1)
k.pack(side = BOTTOM)

var = StringVar(top)
var.set("List")
option=OptionMenu(top,var,"List","Queue","Tree")
option.grid(row=4,column=2)
option.pack(side = BOTTOM)
button1 = Button(top,text = 'Submit')
button1.grid(row=6,column=2)
button1.bind('<Button-1>', print_contents)
button1.pack(side = BOTTOM)
mainloop()

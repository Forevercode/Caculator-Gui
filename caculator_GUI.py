from tkinter import *
from number_tool import Number
from ec import ErroeMessageToUser
import re
root=Tk()
root.title("simple caculator")
#row and column configure
for i in range(1,4):
    root.columnconfigure(i,weight=1)
for i in range(21):
    root.rowconfigure(i,weight=1)






#function for button
def button_click(number_or_operator):
    ent_expression.insert(END,number_or_operator)

def button_DEL():
    ent_expression.delete(0,END)

def equal(event=None):
    user_input=ent_expression.get()

    if Number.only_demical_in_expression(str_expressipn=user_input) and Number.fist_and_last_number_is_not_invalid_number(str_expressipn=user_input):
       calculating_result=Number.str_expression_calculate(str_expression=user_input)


    else :
       calculating_result=ErroeMessageToUser.bad_expression

    #show the calculating result to user
    ent_expression.delete(0,END)
    ent_expression.insert(0,calculating_result)

#function for validation
def input_validatation(a):
    userinput=ent_expression.get()

    if userinput=="" or re.match("^[0-9\-+×÷*/.]*$",userinput) is not None:
        return True
    return False



input_validatation_wrapper=root.register(input_validatation)


#userinput---------------------------------------------------
fr_screen=Frame(root)
strvar_userinput=StringVar()
ent_expression=Entry(fr_screen,width=40,borderwidth=5,textvariable=strvar_userinput,validate='focus',validatecommand=(input_validatation_wrapper,"%P"))
ent_expression.pack(padx=1,pady=5)




#define button---------------------------------------------
frame_main=Frame(root,width=100,height=150,bg="#55493F")

button_bg="#badade"
button_pady=30.4

button_dot=Button(frame_main,text=".",bg=button_bg,padx=31.5,pady=button_pady,command=lambda :button_click(".")) #set button_add padx to 41.5 to fit the lay out
button_0=Button(frame_main,text=0,bg=button_bg,padx=30,pady=button_pady,command=lambda:button_click("0"))
button_equal=Button(frame_main,text="=",bg=button_bg,padx=29,pady=button_pady,command=equal)

button_1=Button(frame_main,text=1,bg=button_bg,padx=30,pady=button_pady,command=lambda:button_click("1"))
button_2=Button(frame_main,text=2,bg=button_bg,padx=30,pady=button_pady,command=lambda:button_click("2"))
button_3=Button(frame_main,text=3,bg=button_bg,padx=30,pady=button_pady,command=lambda:button_click("3"))

button_4=Button(frame_main,text=4,bg=button_bg,padx=30,pady=button_pady,command=lambda:button_click("4"))
button_5=Button(frame_main,text=5,bg=button_bg,padx=30,pady=button_pady,command=lambda:button_click("5"))
button_6=Button(frame_main,text=6,bg=button_bg,padx=30,pady=button_pady,command=lambda:button_click("6"))

button_7=Button(frame_main,text=7,bg=button_bg,padx=30,pady=button_pady,command=lambda:button_click("7"))
button_8=Button(frame_main,text=8,bg=button_bg,padx=30,pady=button_pady,command=lambda:button_click("8"))
button_9=Button(frame_main,text=9,bg=button_bg,padx=30,pady=button_pady,command=lambda:button_click("9"))

   #define button -column four
buttom_at_column_four_pady=21.5
buttom_at_column_four_color="#6d7875"

button_clear=Button(frame_main,text="clear",padx=20,pady=buttom_at_column_four_pady,bg=buttom_at_column_four_color,command=button_DEL)
button_devide=Button(frame_main,text="÷",padx=29,pady=buttom_at_column_four_pady,bg=buttom_at_column_four_color,command=lambda:button_click("÷"))
button_time=Button(frame_main,text="×",padx=29,pady=buttom_at_column_four_pady,bg=buttom_at_column_four_color,command=lambda:button_click("×"))
button_subtract=Button(frame_main,text="-",padx=31,pady=buttom_at_column_four_pady,bg=buttom_at_column_four_color,command=lambda:button_click("-"))
buttom_add=Button(frame_main,text="+",padx=29,pady=buttom_at_column_four_pady,bg=buttom_at_column_four_color,command=lambda:button_click("+"))


#add button to window
button_dot.grid(row=16,rowspan=5,column=0)
button_0.grid(row=16,rowspan=5,column=1)
button_equal.grid(row=16,rowspan=5,column=2)

button_1.grid(row=11,rowspan=5,column=2)
button_2.grid(row=11,rowspan=5,column=1)
button_3.grid(row=11,rowspan=5,column=0)

button_4.grid(row=6,rowspan=5,column=2)
button_5.grid(row=6,rowspan=5,column=1)
button_6.grid(row=6,rowspan=5,column=0)

button_7.grid(row=1,rowspan=5,column=2)
button_8.grid(row=1,rowspan=5,column=1)
button_9.grid(row=1,rowspan=5,column=0,)

   #add button to screen-column four
buttom_add.grid(row=17,rowspan=4,column=3)
button_subtract.grid(row=13,rowspan=4,column=3)
button_time.grid(row=9,rowspan=4,column=3)
button_devide.grid(row=5,rowspan=4,column=3)
button_clear.grid(row=1,rowspan=4,column=3)



fr_screen.pack()
frame_main.pack(fill=BOTH)


#bind
root.bind("<Return>",equal)

root.mainloop()

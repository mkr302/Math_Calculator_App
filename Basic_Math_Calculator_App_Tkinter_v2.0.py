# ##########################################################################################################
# # Program:    Basic_Math_Calculator_App_Tkinter_v2.0.py
# # Purpose:    GUI mathematical calculator for performing addition, subtraction, multiplication,
# #             division and modulus operations
# # Author:     Muralikrishnan Rajendran
# # Date:       10-May-2020
# # Dependencies:
#        Py Version: 3.x
#        Packages:   tkinter, re
# ##########################################################################################################

import tkinter as tk
import tkinter.font as font
import re

# Calculator window initialization
CalcWin = tk.Tk()

# accumulation variables/global variables
Ans_var = 0
calculation_complete = 0

# Calculator functions - constructors/destructors, text box manipulation, and mathematical operations
def initializeCalc():
    textbox.insert('1.0', '')

def SetInput(text):
    global calculation_complete
    if calculation_complete == 1:
        textbox.delete("1.0","end")
        textbox.insert("end", text)
        calculation_complete = 0
    else:
        if len(textbox.get("1.0","end")) != 0:
            textbox.insert("end", text)
        else:
            textbox.delete("1.0","end")
            textbox.insert("end", text)
        
def DeleteInput():
    if len(textbox.get("1.0","end")) != 0:
        text = textbox.get("1.0","end").strip()[:-1]
        textbox.delete("1.0","end")
        textbox.insert("1.0",text)
    
def ResetInput():
    textbox.delete("1.0","end")
    initializeCalc()

def MemoryClear():
    global Ans_var
    global calculation_complete
    Ans_var = 0
    calculation_complete = 1
    textbox.delete("1.0","end")
    
def RetrieveAns():
    global calculation_complete
    calculation_complete = 1
    textbox.delete("1.0","end")
    textbox.insert('1.0', Ans_var)
    
def CalculateAnswer():
    global Ans_var
    global calculation_complete
    valid_symbol = 0
    valid_symbols_list = ['+', '-', '/', '%', '*']
    Inp_var = textbox.get("1.0","end")
    Inp_var = Inp_var.strip()
    Input_elements = re.split('[+ \- * / %]',Inp_var)
    if len(Input_elements) < 3:
        for x in valid_symbols_list:
            if x in Inp_var:
                valid_symbol = + 1
        if len(Inp_var) != 0 and valid_symbol == 1:
            if '+' in Inp_var:
                Inp_list = Inp_var.split('+')
                if len(Inp_list[0]) == 0 and len(Inp_list[1]) == 0:
                    textbox.delete("1.0","end")
                    textbox.insert("end", "No Inputs to calculate!")  
                elif (Inp_list[0].replace('','0').replace('.','').isnumeric()) and (Inp_list[1].replace('','0').replace('.','').isnumeric()):
                    if len(Inp_list[0]) == 0:
                        Inp_list[0] = Ans_var
                    elif len(Inp_list[1]) == 0:
                        Inp_list[1] = '0'
                    Ans_var = float(Inp_list[0]) + float(Inp_list[1])
                    textbox.delete("1.0","end")
                    textbox.insert("end", Ans_var)
                else:
                    textbox.delete("1.0","end")
                    textbox.insert("end", "Invalid Inputs!")
                    
            elif '-' in Inp_var:
                Inp_list = Inp_var.split('-')
                if len(Inp_list[0]) == 0 and len(Inp_list[1]) == 0:
                    textbox.delete("1.0","end")
                    textbox.insert("end", "No Inputs to calculate!")  
                elif (Inp_list[0].replace('','0').replace('.','').isnumeric()) and (Inp_list[1].replace('','0').replace('.','').isnumeric()):
                    if len(Inp_list[0]) == 0:
                        Inp_list[0] = Ans_var
                    elif len(Inp_list[1]) == 0:
                        Inp_list[1] = '0'
                    Ans_var = float(Inp_list[0]) - float(Inp_list[1])
                    textbox.delete("1.0","end")
                    textbox.insert("end", Ans_var)
                else:
                    textbox.delete("1.0","end")
                    textbox.insert("end", "Invalid Inputs!")
                    
            elif '*' in Inp_var:
                Inp_list = Inp_var.split('*')
                if len(Inp_list[0]) == 0 and len(Inp_list[1]) == 0:
                    textbox.delete("1.0","end")
                    textbox.insert("end", "No Inputs to calculate!")  
                elif (Inp_list[0].replace('','0').replace('.','').isnumeric()) and (Inp_list[1].replace('','0').replace('.','').isnumeric()):
                    if len(Inp_list[0]) == 0:
                        Inp_list[0] = Ans_var
                    elif len(Inp_list[1]) == 0:
                        Inp_list[1] = '0'
                    Ans_var = float(Inp_list[0]) * float(Inp_list[1])
                    textbox.delete("1.0","end")
                    textbox.insert("end", Ans_var)  
                else:
                    textbox.delete("1.0","end")
                    textbox.insert("end", "Invalid Inputs!")
                    
            elif '/' in Inp_var:
                Inp_list = Inp_var.split('/')
                if len(Inp_list[0]) == 0 and len(Inp_list[1]) == 0:
                    textbox.delete("1.0","end")
                    textbox.insert("end", "No Inputs to calculate!")  
                elif (Inp_list[0].replace('','0').replace('.','').isnumeric()) and (Inp_list[1].replace('','0').replace('.','').isnumeric()):
                    if len(Inp_list[0]) == 0:
                        Inp_list[0] = Ans_var
                    elif len(Inp_list[1]) == 0:
                        Inp_list[1] = '0'
                        
                    if float(Inp_list[1]) != 0:
                        Ans_var = float(Inp_list[0]) / float(Inp_list[1])
                        textbox.delete("1.0","end")
                        textbox.insert("end", Ans_var)
                    else:
                        Ans_var = 'Div by zero error!!'
                        textbox.delete("1.0","end")
                        textbox.insert("end", Ans_var)
                        Ans_var = 0
                else:
                    textbox.delete("1.0","end")
                    textbox.insert("end", "Invalid Inputs!")
                    
            elif '%' in Inp_var:
                Inp_list = Inp_var.split('%')
                if len(Inp_list[0]) == 0 and len(Inp_list[1]) == 0:
                    textbox.delete("1.0","end")
                    textbox.insert("end", "No Inputs to calculate!")  
                elif (Inp_list[0].replace('','0').replace('.','').isnumeric()) and (Inp_list[1].replace('','0').replace('.','').isnumeric()):
                    if len(Inp_list[0]) == 0:
                        Inp_list[0] = Ans_var
                    elif len(Inp_list[1]) == 0:
                        Inp_list[1] = '0'
                        
                    if float(Inp_list[1]) != 0:
                        Ans_var = float(Inp_list[0]) % float(Inp_list[1])
                        textbox.delete("1.0","end")
                        textbox.insert("end", Ans_var)
                    else:
                        Ans_var = 'Div by zero error!!'
                        textbox.delete("1.0","end")
                        textbox.insert("end", Ans_var)
                        Ans_var = '0'
                else:
                    textbox.delete("1.0","end")
                    textbox.insert("end", "Invalid Inputs!")
                                    
        elif len(Inp_var) != 0 and valid_symbol != 1 and Inp_var.replace('.','').isnumeric():
            textbox.delete("1.0","end")
            textbox.insert('1.0', Inp_var)
            Ans_var = float(Inp_var)
        elif len(Inp_var) == 0:
            textbox.delete("1.0","end")
            textbox.insert('1.0', Ans_var)
        else:
            textbox.delete("1.0","end")
            textbox.insert('1.0', "Invalid input!")
    else:
        try:
            Ans_var = eval(Inp_var)
            textbox.delete("1.0","end")
            textbox.insert("end", Ans_var)
        except:
            outputerr = "Invalid Inputs!"
            textbox.delete("1.0","end")
            textbox.insert("end", outputerr)
            Ans_var = 0
    
    calculation_complete = 1


###### Tkinter frame elements and properties
        
# Title and size adjustments
CalcWin.title('           BASIC MATH CALCULATOR - USING PYTHON/TKINTER         ')
width = 550
height = 550
CalcWin.geometry('580x450')
CalcWin.resizable(0,0)

myFont = font.Font(size=11, family='Helvetica', weight='bold')
myFont1 = font.Font(family='Helvetica', weight='bold')

textbox = tk.Text(CalcWin, width=40, height=3, bg='white', font = ("Helvetica", 12), relief ='raised')
textbox.place(x=50,y=20)

btncls_Set = tk.Button(CalcWin, text="Delete", width=8, height=2, bg="cyan", fg="black", command=lambda:DeleteInput())
btncls_Set['font'] = myFont1

btnallcls_Set = tk.Button(CalcWin, text="AC", width=8, height=2, bg="cyan", fg="black", command=lambda:ResetInput())
btnallcls_Set['font'] = myFont1

btnans_Set = tk.Button(CalcWin, text="Ans", width=8, height=2, bg="cyan", fg="black",command=lambda:RetrieveAns())
btnans_Set['font'] = myFont1

btnMC_Set = tk.Button(CalcWin, text="MC", width=8, height=2, bg="cyan", fg="black",command=lambda:MemoryClear())
btnMC_Set['font'] = myFont1

btnoutput_Set = tk.Button(CalcWin, text="=", width=8, height=2, bg="cyan", fg="black",command=lambda:CalculateAnswer())
btnoutput_Set['font'] = myFont1

btn1_Set = tk.Button(CalcWin, text="1", width=7, height=3, bg="light blue", fg="black",command=lambda:SetInput("1"))
btn2_Set = tk.Button(CalcWin, text="2", width=7, height=3, bg="light blue", fg="black",command=lambda:SetInput("2"))
btn3_Set = tk.Button(CalcWin, text="3", width=7, height=3, bg="light blue", fg="black",command=lambda:SetInput("3"))
btn4_Set = tk.Button(CalcWin, text="4", width=7, height=3, bg="light blue", fg="black",command=lambda:SetInput("4"))
btn5_Set = tk.Button(CalcWin, text="5", width=7, height=3, bg="light blue", fg="black",command=lambda:SetInput("5"))
btn6_Set = tk.Button(CalcWin, text="6", width=7, height=3, bg="light blue", fg="black",command=lambda:SetInput("6"))
btn7_Set = tk.Button(CalcWin, text="7", width=7, height=3, bg="light blue", fg="black",command=lambda:SetInput("7"))
btn8_Set = tk.Button(CalcWin, text="8", width=7, height=3, bg="light blue", fg="black",command=lambda:SetInput("8"))
btn9_Set = tk.Button(CalcWin, text="9", width=7, height=3, bg="light blue", fg="black",command=lambda:SetInput("9"))
btn0_Set = tk.Button(CalcWin, text="0", width=7, height=3, bg="light blue", fg="black",command=lambda:SetInput("0"))
btndot_Set = tk.Button(CalcWin, text=".", width=7, height=3, bg='black', fg="white",command=lambda:SetInput("."))

btn1_Set['font'] = myFont
btn2_Set['font'] = myFont
btn3_Set['font'] = myFont
btn4_Set['font'] = myFont
btn5_Set['font'] = myFont
btn6_Set['font'] = myFont
btn7_Set['font'] = myFont
btn8_Set['font'] = myFont
btn9_Set['font'] = myFont
btn0_Set['font'] = myFont
btndot_Set['font'] = myFont

btnadd_Set = tk.Button(CalcWin, text="+", width=7, height=3, bg="orange", fg="black",command=lambda:SetInput('+'))
btnsub_Set = tk.Button(CalcWin, text="-", width=7, height=3, bg="orange", fg="black",command=lambda:SetInput('-'))
btnmul_Set = tk.Button(CalcWin, text="*", width=7, height=3, bg="orange", fg="black",command=lambda:SetInput('*'))
btndiv_Set = tk.Button(CalcWin, text="/", width=7, height=3, bg="orange", fg="black",command=lambda:SetInput('/'))
btnmod_Set = tk.Button(CalcWin, text="%", width=7, height=3, bg="orange", fg="black",command=lambda:SetInput('%'))

btnadd_Set['font'] = myFont
btnsub_Set['font'] = myFont
btnmul_Set['font'] = myFont
btndiv_Set['font'] = myFont
btnmod_Set['font'] = myFont

btncls_Set.place(x = 450, y = 20)
btnallcls_Set.place(x = 450, y = 100)
btnans_Set.place(x = 450, y = 180)
btnMC_Set.place(x = 450, y = 260)
btn1_Set.place(x = 50, y = 100)
btn2_Set.place(x = 140, y = 100)
btn3_Set.place(x = 230, y = 100)

btn4_Set.place(x = 50, y = 180)
btn5_Set.place(x = 140, y = 180)
btn6_Set.place(x = 230, y = 180)

btn7_Set.place(x = 50, y = 260)
btn8_Set.place(x = 140, y = 260)
btn9_Set.place(x = 230, y = 260)

btn0_Set.place(x = 140, y = 340)
btndot_Set.place(x = 50, y = 340)
btnmod_Set.place(x = 230, y = 340)

btnadd_Set.place(x = 340, y = 100)
btnsub_Set.place(x = 340, y = 180)
btnmul_Set.place(x = 340, y = 260)
btndiv_Set.place(x = 340, y = 340)

btnoutput_Set.place(x = 450, y = 340)

CalcWin.configure(bg='light grey')
initializeCalc()
CalcWin.mainloop()


################################# End of script ################################# 
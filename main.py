from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner 
from kivy.uix.scrollview import ScrollView 
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty,ListProperty
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = (280,460)
class Scroll(ScrollView):
    pass
class FrontView(Screen):
    pass
class CgView(Screen):
    pass
class IntView(Screen):
    pass    
class SecWin1(Widget):
    pass
class Secure: 
    def decrpt(self,val):
        eli_st =''
        for j in val.split(" ")[:-1]: 
            n=int(j) ;k=0 ;s=0
            while(n>0):
                x=n%10
                s+=(x*7**k)
                n//=10
                k+=1
            eli_st +=chr(s)
        return eli_st
    def de_year(self,value):
        s = ""  ;k=0
        for i in list(map(int,value.split(" "))):
            s += chr(i-k)
            k +=1
        return s[::-1]

class SecWin(Screen):
    act_sub = dict()
    va = dict()
    pre = None
    read_val =[]

    def __init__(self,**kwargs):
        super(SecWin,self).__init__ (**kwargs)
        self.obj_dec = Secure()
        self.read_f = open("D:\\aBc\\KIVY\\CG\\Ensub.txt",'r')
        for i in range(5):
            self.read_val.append(self.read_f.readline())

    def check(self,ov,sem):
        for f1 in self.read_val:
            va = f1.split(';') 
            if self.obj_dec.de_year(va[0][1:]) == ov:    
                val = va[1].split("@")
                ori = val[int(sem)-1][3:]
                ano_val = ori.split("}")
                d  ={}
                for bh in ano_val[:-1]:
                    subname, subcode ,cred= bh.split("!")
                    d[self.obj_dec.decrpt(subname[1:])] = [self.obj_dec.decrpt(subcode),int(cred)]
                return d
    def fun(self,**kwargs):
        self.sem = kwargs['sem']
        self.reg = kwargs['reg']
        self.ty = kwargs['ty']
        if self.ty == 'CGPA' or self.ty=='Internal Mark':
            return
        if(self.reg == '2017'):
            self.dept = kwargs['dept'] 
            if self.dept == "Other":
                self.pop("SORRY","Not Available")
                self.manager.current = 'win1'
                return
            self.act_sub = self.check(self.dept,self.sem)
            self.va = [i for i in self.act_sub.keys()]
            s1_list = []
            bx1 = BoxLayout(orientation ='vertical',size= Window.size,padding=8) 
            for i in self.va:
                b1 = BoxLayout()
                b1.add_widget(Label (text =self.act_sub[i][0],halign = 'left',color =(0.35,.2,1,1)))
                s1 = Spinner(text = "O",values=('O',"A+","A","B+","B","--RA--"),background_color =(0.65625,0.0234375,.78515625,.95))
                b1.add_widget(s1)
                bx1.add_widget(b1)
                s1_list.append(s1)
            but1 = Button(text='Submit',halign='center',background_color =(0.65625,0.0234375,.78515625,.95))
            but1.fbind('on_press',self.cal_gpa,s1_list)
            bx1.add_widget(but1)
            for i in self.va:
                bx1.add_widget(Label(halign='left',text="{0} - {1}".format(self.act_sub[i][0].rjust(6),i.ljust(6)),color=(1,1,1,1)))
            if self.pre !=None:
                self.manager.ids.another.ids.secWin_scr.remove_widget(self.pre)
            self.pre = bx1
            self.manager.ids.another.ids.secWin_scr.add_widget(bx1)
        elif(self.reg == '2021'):
            # Semester is 1
            self.act_sub = {'Professional English - |':['HS3151',4],'Matrices & Calculus':['MA3151',4],'Engineering Physics':['PH3151',3],'Engineering Chemistry':['CY3151',3],'Problem Solving & Python Programming':['GE3151',3],'Problem Solving & Python Programming Laboratory':['GE3171',2],'Physics & Chemistry Laboratory':['BS3171',2]}
            self.va = [i for i in self.act_sub.keys()]
            s1_list = []
            bx1 = BoxLayout(orientation ='vertical',size= Window.size,padding=8) 
            for i in self.va:
                b1 = BoxLayout()
                b1.add_widget(Label (text =self.act_sub[i][0],halign = 'left',color =(0.35,.2,1,1)))
                s1 = Spinner(text = "O",values=('O',"A+","A","B+","B","--RA--"),background_color =(0.65625,0.0234375,.78515625,.95))
                b1.add_widget(s1)
                bx1.add_widget(b1)
                s1_list.append(s1)
            but1 = Button(text='Submit',halign='center',background_color =(0.65625,0.0234375,.78515625,.95))
            but1.fbind('on_press',self.cal_gpa,s1_list)
            bx1.add_widget(but1)
            for i in self.va:
                bx1.add_widget(Label(halign='left',text="{0} - {1}".format(self.act_sub[i][0].rjust(6),i.ljust(6)),color=(1,1,1,1)))
            if self.pre !=None:
                self.manager.ids.another.ids.secWin_scr.remove_widget(self.pre)
            self.pre = bx1
            self.manager.ids.another.ids.secWin_scr.add_widget(bx1)
        else:
            self.pop('SORRY','Reg '+self.reg+" \nNot Available")
            self.manager.current = 'win1'

    def gr(self,val):
        val = val.upper()
        if val == 'O':
            return 10
        elif val == 'A+':
            return 9
        elif val == 'A':
            return 8
        elif val == 'B+':
            return 7
        elif val == 'B':
            return 6
        else:
            return 0

    def InternalMark(self,m1,m2,m3):
        try:
            avg = round((float(m1)+float(m2)+float(m3))/15,3)
            self.pop('Internal Mark','Mark Out of 20 \nis '+str(avg))
        except:
            self.pop('Check It','0 - 100 Marks \nonly Accepted')
            self.manager.current = 'win4'


    def cal_gpa(self,*arg):
        tcredit = 0
        getcredit = 0
        for sub,grade in zip(self.va,arg[0]):
            if "--RA--" == grade.text.upper():
                continue
            getcredit+= (self.gr(grade.text)*self.act_sub[sub][1])
            tcredit+= self.act_sub[sub][1]
        if tcredit == 0:
            self.pop('GRADE', f"GPA  =   {tcredit}")
        else:
            self.gpa = round(getcredit/tcredit,3)
            self.pop('GRADE', f"GPA  =   {self.gpa}")

    def cal_cgpa(self):
        id_of_cb = ['c'+str(i) for i in range(1,9)]
        id_of_ti = ['tx_in'+str(i) for i in range(1,9)]
        t = 0
        g = 0.0
        p = True
        for i in range(8):
            if self.manager.ids.third.ids[id_of_cb[i]].active:
                try:
                    t +=1
                    g += float(self.manager.ids.third.ids[id_of_ti[i]].text)
                except:
                    p = False
                    self.pop('Check It','Only Numbers\nare allowed')
                    self.manager.current = 'win3'
                    break
            else:
                continue
        if t == 0:
            p = False
        if p:
            self.pop('GRADES',f'CGPA  =  {round(g/t,3)}')

    def pop(self,t,con_val):
        l1 = Label(text =con_val,halign='center',font_size='20sp',color=(.1,.96,.3,1))
        p = Popup(title=t,title_align='center',title_color=(.3,.644,.718,1),content =l1 ,size = (Window.size[0]/1.9,Window.size[1]/2.7),size_hint=(None,None))
        p.open()

class sm(ScreenManager):
    mainWin = ObjectProperty(None)
    another = ObjectProperty(None)
    third = ObjectProperty(None)

class main(App):
    def build (self):
        return sm()
        
if "__main__"  == __name__:
    main().run()

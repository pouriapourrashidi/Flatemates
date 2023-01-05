from fpdf import FPDF
import webbrowser
from flat import Bill, Flatemate


class PDFReport():

    def __init__(self, file_name): 
        self.file_name=file_name

    def generate(self, flatmate1, flatmate2, bill):
        
        pdf = FPDF(orientation="P",unit='pt',format='letter')
        pdf.add_page()

        pdf.image(r'D:\Udemy\OOP Python\flatmate\house.png',w=30,h=30)

        pdf.set_font(family='Times',size=24, style="B")
        pdf.cell(w=0,h=80,txt="Flatmate Bill", align='C', border=0, ln=1)
        
        pdf.set_font(family='Times',size=12)
        pdf.cell(w=150,h=50,txt="Period", border=0)
        pdf.cell(w=180,h=50,txt=bill.period, border=0, ln=1)

        pdf.set_font(family='Times',size=12)
        pdf.cell(w=150,h=30,txt=flatmate1.name, border=0)
        pdf.cell(w=180,h=30,txt="$"+str(round(flatmate1.pay(bill,flatmate2),2)), border=0, ln=1)

        pdf.cell(w=150,h=30,txt=flatmate2.name, border=0)
        pdf.cell(w=180,h=30,txt="$"+str(round(flatmate2.pay(bill,flatmate1),2)), border=0, ln=1)
        #print(type(self.file_name))
        name=r"D:\Udemy\OOP Python\flatmate\\"+self.file_name
        pdf.output(name)

        webbrowser.open(name)


bill = Bill(float(input("Enter the bill amount : ")),str(input("Enter the duration : ")))

Pouria = Flatemate("Pouria",20)
Hessam = Flatemate("Hessam",26)

print(Pouria.pay(bill,Hessam))

pdfreport = PDFReport('bill.pdf')
pdfreport.generate(Pouria,Hessam,bill)
# from reportlab.lib.pagesizes import LETTER  
# from reportlab.lib.units import inch  
# from reportlab.pdfgen.canvas import Canvas  
# from reportlab.lib.colors import purple  
# # creating the pdf file  
# my_canvas = Canvas("textfile.pdf", pagesize = LETTER)  
# # setting up the font and the font size  
# my_canvas.setFont("Courier", 18)  
# # setting up the color of the font as red  
# my_canvas.setFillColor(purple)  
# # writing this text on the PDF file   
# my_canvas.drawString(2 * inch, 8 * inch, "Welcome to Javatpoint for Python Tutorial")  
# my_canvas.save()  
# print(my_canvas)



# from reportlab.lib.pagesizes import LETTER  
# from reportlab.pdfgen.canvas import Canvas  
# my_canvas = Canvas("imgfile.pdf", pagesize = LETTER)  
# my_canvas.drawInlineImage("logo.png", 100, 450)  
# my_canvas.save()  



# from reportlab.lib import colors  
# from reportlab.lib.pagesizes import letter, inch  
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle   
# # creating a pdf file to add tables  
# my_doc = SimpleDocTemplate("table.pdf", pagesize = letter)  
# my_obj = []  
# # defining Data to be stored on table  
# my_data = [  
#    ["ID", "1234"],  
#    ["Name", "Den Arthur"],  
#    ["Profession", "Software Developer"],  
#    ["Age", "28"],  
#    ["Sex", "Male"]  
# ]  
# # Creating the table with 5 rows  
# my_table = Table(my_data, 1 * [1.6 * inch], 5 * [0.5 * inch])  
# # setting up style and alignments of borders and grids  
# my_table.setStyle(  
#    TableStyle(  
#        [  
#            ("ALIGN", (1, 1), (0, 0), "LEFT"),  
#            ("VALIGN", (-1, -1), (-1, -1), "TOP"),  
#            ("ALIGN", (-1, -1), (-1, -1), "RIGHT"),  
#            ("VALIGN", (-1, -1), (-1, -1), "TOP"),  
#            ("INNERGRID", (0, 0), (-1, -1), 1, colors.black),  
#            ("BOX", (0, 0), (-1, -1), 2, colors.black),  
#        ]  
#    )  
# )  
# my_obj.append(my_table)  
# my_doc.build(my_obj)  


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle, Image
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

a = Image("logo.png",inch,inch)  
a1 = Image("logo.png",inch,inch)  
# a1.drawHeight = 1.25*inch*a1.drawHeight / a1.drawWidth
# a1.drawWidth = 1.25*inch
data=[
    [a,'1GYS3AKL5PR423850','NEW 2023 Cadillac 6C10706','2023-06-24T06:02:11-04:00','2023-06-24T06:02:11-04:00','2023-06-24T06:02:11-04:00',
'BGR,Cropped'],
[a1,'2GYS3AKL5PR423850','NEW 2023 Cadillac 6C10706','2023-06-24T06:02:11-04:00','2023-06-24T06:02:11-04:00','2023-06-24T06:02:11-04:00',
'BGR,Cropped'],
[a1,'3GYS3AKL5PR423850','NEW 2023 Cadillac 6C10706','2023-06-24T06:02:11-04:00','2023-06-24T06:02:11-04:00','2023-06-24T06:02:11-04:00',
'BGR,Cropped'],
[a1,'4GYS3AKL5PR423850','NEW 2023 Cadillac 6C10706','2023-06-24T06:02:11-04:00','2023-06-24T06:02:11-04:00','2023-06-24T06:02:11-04:00',
'BGR,Cropped'],
[a1,'5GYS3AKL5PR423850','NEW 2023 Cadillac 6C10706','2023-06-24T06:02:11-04:00','2023-06-24T06:02:11-04:00','2023-06-24T06:02:11-04:00',
'BGR,Cropped'],
[a1,'6GYS3AKL5PR423850','NEW 2023 Cadillac 6C10706','2023-06-24T06:02:11-04:00','2023-06-24T06:02:11-04:00','2023-06-24T06:02:11-04:00',
'BGR,Cropped'],
[a1,'7GYS3AKL5PR423850','NEW 2023 Cadillac 6C10706','2023-06-24T06:02:11-04:00','2023-06-24T06:02:11-04:00','2023-06-24T06:02:11-04:00',
'BGR,Cropped'],
]
c = canvas.Canvas("Reportlabtest.pdf", pagesize=landscape(A4))
table = Table(data)
table.setStyle(TableStyle([
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ('BACKGROUND',(0,0),(-1,2),colors.lightgrey)
                           ]))
table.wrapOn(c, 100, 400)
table.drawOn(c,20,40)
c.save()
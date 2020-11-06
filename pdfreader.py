import pyttsx3
import PyPDF2
book = open('bia-template.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
# print(pages)

# for 1st page only, put getpage(0)
# page = pdfReader.getPage(0)
# text = page.extractText()
# speaker.say(text)
# speaker.runAndWait()
choice = input("Enter 1 if you would like to read until a specific page\nEnter 2 if you want to read all pages.\nEnter 3 if you want to specify page range.\n")
choice = int(choice)


 
if choice == 1:
    newpage = input("Enter until what page do you want the audio to read\n")
    newpage=int(newpage)
    for num in range(0, newpage):
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()
  
elif choice == 2:
    print(f'Reading all pages')
    for num in range(0, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()

elif choice == 3:
    a,b=map(int,input("Specify page range seperated by space. Example,if from pages 2 to 12, enter: 2 12 \n").split())
    for num in range(a, b):
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait() 

        # https://www.codegrepper.com/code-examples/delphi/input%28%29.split%28%29+in+python+3

  
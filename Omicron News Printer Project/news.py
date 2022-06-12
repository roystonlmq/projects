# A program to keep me updated on Covid-19 Omicron variant
import requests
from fpdf import FPDF


api_key = "26c72874767c46febdc8bcc4ed570997"

def news():
    main_url = "https://newsapi.org/v2/everything?q=omicron&apiKey=26c72874767c46febdc8bcc4ed570997"
    news = requests.get(main_url).json()
    # print(news)
    global articles
    articles = news['articles']
    # print(articles)
    global collection
    collection = {}
    n = 1
    for arti in articles:
        title = arti['title']
        source = arti['source']['name']
        link = arti['url']
        collection[n] = title, source, link
        n += 1


    pdf = FPDF(orientation = "P", unit = "mm", format = "A4")
    pdf.add_page()
    pdf.set_font('helvetica', size=8)
    for n in range(1,len(articles)+1):
        pdf.cell(txt=(collection[n][0]), new_x="LEFT", new_y="NEXT")
        pdf.cell(txt=" ", new_x="LEFT", new_y="NEXT")
        pdf.cell(txt="LINK", link=(collection[n][2]), new_x="LEFT", new_y="NEXT")
        pdf.cell(txt=" ", new_x="LEFT", new_y="NEXT")

    pdf.output("COVID-19 OMICRON.pdf")


news()
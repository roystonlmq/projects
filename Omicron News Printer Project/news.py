# A program to keep me updated on Covid-19 Omicron variant
import requests
import config
from fpdf import FPDF
from argparse import ArgumentParser


def get_news(url, filename):

    news = requests.get(url).json()
    # print(news)

    articles = news['articles']
    # print(articles)

    collection = {}
    n = 1
    for arti in articles:
        title = arti['title']
        source = arti['source']['name']
        link = arti['url']
        collection[n] = title, source, link
        n += 1

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font('helvetica', size=8)
    for n in range(1,len(articles)+1):
        pdf.cell(txt=(collection[n][0]), new_x="LEFT", new_y="NEXT")
        pdf.cell(txt=" ", new_x="LEFT", new_y="NEXT")
        pdf.cell(txt="LINK", link=(collection[n][2]), new_x="LEFT", new_y="NEXT")
        pdf.cell(txt=" ", new_x="LEFT", new_y="NEXT")

    pdf.output(filename)


def file_ext_check(args):
    f = args.filename
    return f if f.endswith('.pdf') else f + '.pdf'


def get_args():
    ap = ArgumentParser()
    ap.add_argument('--url', help='url link')
    ap.add_argument('--f', help='filename', default='news.pdf')
    return ap.parse_args()


def main():
    args = get_args()
    file = file_ext_check(args)
    get_news(args.url, file)


if __name__ == '__main__':
    main()

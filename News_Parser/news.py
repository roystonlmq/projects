
import requests
import config
from fpdf import FPDF
from argparse import ArgumentParser


def get_news(url, filename, args):

    news = requests.get(url).json()
    # print(news)

    articles = news['articles']
    # print(articles)

    collection = {}
    n = 1
    for arti in articles:
        title = arti['title'].encode('latin-1', 'replace').decode('latin-1')
        source = arti['source']['name']
        link = arti['url']
        collection[n] = title, source, link
        n += 1

    title = args.topic.upper()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('times', 'B', size=15)

    pdf.cell(txt=title, new_x="LEFT", new_y="NEXT")
    pdf.cell(txt=" ", new_x="LEFT", new_y="NEXT")
    pdf.set_font('times', size=12)

    for n in range(1, len(articles)+1):
        pdf.set_font('times', 'I', size=15)
        # pdf.set_fill_color(200, 220, 255)
        headline = collection[n][0]
        source_art = collection[n][1]
        URL = collection[n][2]
        if len(headline) > 80:
            headline = headline[:80] + '...'
        pdf.cell(txt=headline, new_x="LEFT", new_y="NEXT", link=URL)
        pdf.set_font('times', 'B', size=10)
        pdf.cell(txt=source_art, new_x="LEFT", new_y="NEXT")
        pdf.cell(txt=" ", new_x="LEFT", new_y="NEXT")

    pdf.output(filename)


def file_ext_check(args):
    filename = args.f
    return filename if filename.endswith('.pdf') else filename + '.pdf'


def link_generator(args):
    if args.topic is not None:
        topic_name = 'q=' + args.topic + '&'

    else:
        topic_name = ''
    if args.country is not None:
        country_name = 'country=' + args.country + '&'
    else:
        country_name = ''
    if args.fm is not None:
        fm = 'from=' + args.fm + '&'
    else:
        fm = ''
    if args.to is not None:
        to = 'to=' + args.to + '&'
    else:
        to = ''
    if args.source is not None:
        src = 'domain=' + args.source + '&'
    else:
        src = ''
    api_key = 'apiKey=' + config.api_key
    url = f'https://newsapi.org/v2/everything?{src}{topic_name}{fm}{to}{country_name}{api_key}'
    return url


def get_args():
    ap = ArgumentParser()
    ap.add_argument('--topic', help='topic name', default=None)
    ap.add_argument('--source', help='source example: wsj.com', default=None)
    ap.add_argument('--fm', help='from yyyy-mm-dd', default=None)
    ap.add_argument('--to', help='to yyyy-mm-dd', default=None)
    ap.add_argument('--country', help='us, sg, uk', default=None)
    ap.add_argument('--f', help='filename', default='news.pdf')
    return ap.parse_args()


def main():
    args = get_args()
    file = file_ext_check(args)
    url = link_generator(args)
    get_news(url, file, args)


if __name__ == '__main__':
    main()


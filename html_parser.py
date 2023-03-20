from bs4 import BeautifulSoup

import utils


def get_page_content(page):
    content = []
    soup = BeautifulSoup(page, "html.parser")

    # Find the main content div on the page
    content_div = soup.find(id='mw-content-text')

    # Find all the paragraph tags and header tags in the main content div
    paragraphs = content_div.find_all(['p', 'h2', 'h3', 'h4', 'h5', 'h6'])

    # Loop over the list of tags and print out their text
    for tag in paragraphs:
        if tag.find_parent('li', class_='gallerybox'):
            continue
        if tag.text == "\n":
            continue

        span_tag = tag.find_all('span', {'class': 'IPA'})
        span_tag += tag.find_all('span', {'class': 'unicode haudio'})
        span_tag += tag.find_all('span', {'class': 'rt-commentedText nowrap'})

        for o in span_tag:
            o.extract()

        spans = tag.find_all("span")
        to_ignore = False
        for sp in spans:
            if sp.get('id') in ('See_also', 'References', 'External_links', 'Works_cited', 'coordinates', 'Notes', 'Online_references', 'French-language', 'English-language', 'Citations', 'Footnotes', 'Further_reading', 'Gallery'):
                to_ignore = True
                continue
        if to_ignore:
             continue
        content.append(tag)
    return content

def format_content(content):
    chapters = {}
    title = None
    for tag in content:
        text = utils.clean_string(tag.text)
        if tag.name == "h2":
            title = text
            chapters[title] = "{}. ".format(text)
        else:
            if not title:
                title = "intro"
                chapters[title] = "Intro."
            chapters[title] += "{}. ".format(text)
    return chapters

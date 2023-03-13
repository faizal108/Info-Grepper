from django.http import HttpResponse
from django.shortcuts import render
import ssl
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def web_scrapper(request):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # getting in the website link
    # Url = input("Enter your Urllink :")
    Url = request.POST.get('url_input')
    finalLinks = []
    try:
        # trying to access the page
        page = Request(Url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(page, context=ctx).read()
        # Using beautifulsoup to read the contents of the page
        soup = BeautifulSoup(page, 'html.parser')
        # finding all the link headers
        links = soup.findAll('a')
        if (links is not None):
            # getting actual site links from the header a
            for link in links:
                if 'href' in str(link):
                    templist = str(link).split("href")
                    index1 = templist[-1].index("\"")
                    index2 = templist[-1][index1 + 1:].index("\"")
                    finalLinks.append(templist[-1][index1: index2 + 3])
    except Exception as e:
        print(str(e))
    return render(request, "tools/web_scrapper.html", {"result": finalLinks})

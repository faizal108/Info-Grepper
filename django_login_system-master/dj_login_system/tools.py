import json
import sys
import requests
from django.http import HttpResponse
from django.shortcuts import render
import ssl
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

from users.models import Tool

def all_tools(request):
    tools = Tool.objects.all()
    return render(request, 'tools/all_tools.html', {'tools': tools})

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

        # Write the JSON data to a file
        filename = 'web_scrapper.json'
        with open(filename, 'w') as f:
            json.dump(finalLinks, f)

    except Exception as e:
        print(str(e))
    return render(request, "tools/web_scrapper.html", {"result": finalLinks})


def ipgeo(request):
    url = "http://ip-api.com/json/"
    target_url = request.POST.get('url_input')
    if (target_url):
        url += target_url
    response = requests.request("GET", url)
    response = response.json()

    # Write the JSON data to a file
    filename = 'ipgeo.json'
    with open(filename, 'w') as f:
        json.dump(response, f)

    return render(request, "tools/ipgeo.html", {"results": response})




# Download Manager for all tools
def ipgeo_download(request):
    # Load the JSON data from the file
    with open('ipgeo.json', 'r') as f:
        data = json.load(f)

    filename = 'ipgeo.json'
    return download_json(data, filename)

def webscrap_download(request):
    # Load the JSON data from the file
    with open('web_scrapper.json', 'r') as f:
        data = json.load(f)

    filename = 'web_scrapper.json'
    return download_json(data, filename)


def download_json(data, filename):
    # Create a response object with the file content and headers
    response = HttpResponse(json.dumps(data, indent=4), content_type='application/json')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
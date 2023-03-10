import wikipediaapi
import re
import requests
import sys
dict = {}

def print_categorymembers(categorymembers, level=0, max_level=20):
    for c in categorymembers.values():
        if not regex.search(c.title):
            name = re.sub(r'\(([^\)]+)\)', '', c.title)
            if dict.get(name) == None:
                # Primary Key (name)
                print("name")
                print(name)
                # Definition
                definition = c.summary.replace('== References ==', '')
                print("Definition")
                print(definition)
                dict[name] = definition
                # Page URL
                url = c.fullurl
                print("url")
                print(url)

                try:
                    params = {
                        'action': "query",
                        'format': "json",
                        'titles': c.title,
                        'prop': "redirects",
                        'rdprop': "title"
                    }
                    response = requests.get(url="https://en.wikipedia.org/w/api.php", params=params).json()
                    for id in response['query']['pages']:
                        for redirects in response['query']['pages'][id]['redirects']:
                            # Alternative name
                            print(redirects['title'])
                except:
                    #print('There are no redirects')
                    print('')

        if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
            print_categorymembers(c.categorymembers, level=level + 1, max_level=max_level)


def get_contents(categorymembers, level=0, max_level=1):
    for c in categorymembers.values():
        if not regex.search(c.title):
            name = re.sub(r'\(([^\)]+)\)', '', c.title)
            if dict.get(name) == None:
                definition = c.summary.replace('== References ==', '')
                dict[name] = definition

        if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
            print_categorymembers(c.categorymembers, level=level + 1, max_level=max_level)





categories = ['Ideologie politiche','Sessualità','Religione', 'Salute', 'Sociologia economica']

wikipedia = wikipediaapi.Wikipedia('it')
regex = re.compile(r'Category|[cC]omparison|List of|Outline of|Template:|Glossary of|Portal:')
category = wikipedia.page("Category:"+categories[0])

get_contents(category.categorymembers)

print(dict)
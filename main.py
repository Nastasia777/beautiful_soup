from bs4 import BeautifulSoup
# import lxml #different way of using soup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# soup = BeautifulSoup(contents, 'lxml')

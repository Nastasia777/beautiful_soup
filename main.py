from bs4 import BeautifulSoup



## PRACTICE ###
with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# other option:
# import lxml #different way of using soup
# soup = BeautifulSoup(contents, 'lxml')


# to get all info:
all_anchor_tags=soup.find_all(name="a")
all_p_tags=soup.find_all(name="p")
print(all_anchor_tags)
print(all_p_tags)

# to get only text:
for tag in all_p_tags:
    print(tag.getText())

# just links:
for tag in all_anchor_tags:
    print(tag.get("href"))

# find by id
heading =soup.find(name='h1', id='name')
print(heading) # <h1 id="name">Anastasija Kuznecova</h1>

# find by class
section_heading = soup.find(name='h3', class_='heading')
print(section_heading) # <h3 class="heading">Udemy courses:</h3>

print(soup.title) # <title>Anastasija's Personal Site</title>
print(soup.title.name) # title
print(soup.title.string) # Anastasija's Personal Site
print(soup) # will print whole html file or print(soup.prettify())
print(soup.p) # will give us first p

person_description = soup.select_one(selector="p em") 
print(person_description) # <em>Also known as Mother of Dragons</em>

name = soup.select_one(selector="#name") 
print(name) # <h1 id="name">Anastasija Kuznecova</h1>

all_headings = soup.select('.heading')
print(all_headings) # list of all headings

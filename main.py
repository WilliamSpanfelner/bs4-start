from bs4 import BeautifulSoup

with open("website.html", "r") as file:
    contents = file.read()

# After creating an instance of BeautifulSoup using the html.parser,
soup = BeautifulSoup(contents, "html.parser")

# HTML tags can be accessed and the content they contain with dot notation:
print(soup.title)
print(soup.title.name)
print(soup.title.string)

# The first anchor element in the html document can be accessed like so:
print(soup.a)

# The entire document can be printed plain or prettified
print(soup)
print(soup.prettify())

# If all the instances of a particular type of element is required, the find_all method can help.
all_a_elements = soup.find_all(name="a")
print(all_a_elements)

all_paragraph_tags = soup.find_all(name="p")
print(all_paragraph_tags)



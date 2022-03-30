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

# Use the getText() method to return the content text (e.g. for anchor tags)
for tag in all_a_elements:
    print(tag.getText())

# Use the get() method to return the value of any attribute (e.g. href)
for tag in all_a_elements:
    print(tag.get("href"))
    # prints all the target http links

# Use the find method to return the first item that matches specified criteria
# e.g. element name and id values
heading = soup.find(name="h1", id="name")
print(heading)

# Similarly, finding elements with a specific class name is done like so.
# The class keyword requires an underscore suffix since its normal HTML use is for assigning a name.
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.name)
print(section_heading.getText())
print(section_heading.get("class"))

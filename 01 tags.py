import requests
from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc = f.read()
    # First we should make a soup. It means we should run the BeautifulSoup method and it will return us an object and this object is create for BeautifulSoup itself as it is convinient for bs4 to take data from it
    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(soup.prettify())
    print(soup.title, type (soup.title))
    # print(soup.find_all("a"))
    # for link in soup.find_all("a"):
        # print(link.get("href"), link.get_text())

    # print(soup.select("div.italic")) # To select elements based on css selectors and it will return all the divs with italic class

    # It will return the class of first div in the html document.
    print(soup.div.get("class"))

    # It will return us that element whose id is sdiv
    # print(soup.find(id='sdiv'))
    # print(soup.find(class_='italic')) # As class is a reserved keyword in python then, we have to write class_ and it will return the first element which has class of italic

    # print(soup.find_all(class_='italic')) # It will return all the element with class of italic


    #This will return all the children of the element whose id is container
    # for child in soup.find(id="container").children:
    #     print(child)

# The .parents will return all the parents of the element. In the parent all the children inside the parent and the parent itself is returned. Then, it will return the parent of parent and the whole content inside the parent's parent and the parent itself(A huge repition of code)
    # for parent in soup.find(class_="box").parents:
    #     print(parent)

# It will return the element with id container
    cont = soup.find(id="container")
    # Here we are changing the element tag to span
    cont.name = "span"
    cont["class"] = "myClass whatever newClass"
    cont.string = "I am a string"
    # Now if we print cont then, the element whose id was container is converted to span but it will not change the content of the file
    # print(cont)


    # INSERTING A NEW TAG

    # First prepare a new tag
    ulTag = soup.new_tag("ul")

    liTag = soup.new_tag("li")
    liTag.string="Home"
    ulTag.append(liTag)

    liTag = soup.new_tag("li")
    liTag.string = "About"
    ulTag.append(liTag)


    # Inserting that tag in the soup at 0 index(It will not modify the source file)
    soup.html.body.insert(0, ulTag)
    # Writing the data with ul tag to a new file
    with open("modified.html", "w") as f2:
        f2.write(str(soup))
    
    #CHECK IF AN ELEMENT HAS AN ATTRIBUT
    # First create a reference for the element
    cont = soup.find(id="container")
    # has_attr will return a boolean value for if the attribute exists or not
    print(cont.has_attr("href"))

    def has_class_but_not_id(tag):
        return (tag.has_attr("class") and (not tag.has_attr("id")))
    
    # This will return an array of all the elements that has a class but not an id
    # results = soup.find_all(has_class_but_not_id)
    # print(results)


    def has_content(tag):
        return tag.has_attr("content")
    
    results = soup.find_all(has_content)
    print(results)
import wikipedia
from random import choice

titles = ["Google",
          "England",
          "United Kingdom",
          "The Hitchhiker's Guide to the Galaxy",
          "Otis Redding",
          "War and Peace",
          "Cake",
          "Queen Victoria",
          "Binary number",
          "Bible,"
          "Artificial intelligence",
          "GitHub",
          "Python (programming language)",
          "Machine learning",
          "Alan Turing",
          "Enigma machine"]


def get_list(number_of_pages):
    if number_of_pages > len(titles):
        raise ValueError("Not enough titles for number of pages")
    local_titles = titles
    result_list = []
    for i in range(number_of_pages):
        page_title = choice(local_titles)
        page = wikipedia.page(page_title)
        content = page.content.encode('ascii', 'ignore')
        content = content.replace(
            "\n", "").replace(
            "\\", "").replace("=", "")
        result_list += content.split()
        local_titles.remove(page_title)
    return result_list

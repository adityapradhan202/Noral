import json
import time

def suggestion(category):
    with open("suggestions.json", "r") as file:
        res = json.load(file)
        return res[category]

# Functions that has to be passed into the write_stream method
def stream_data(category):
    paragraph = suggestion(category=category)
    for word in paragraph.split(" "):
        yield word + " "
        time.sleep(0.1)


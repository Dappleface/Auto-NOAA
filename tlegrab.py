#tle grab
#important note, would not be possiable without request module from pip
# sudo pip3 install requests
#imports
from requests import get  # to make GET request

#fucntion
def tlegrab(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)
        print("File Downloaded successfully")
        

tlegrab("https://www.celestrak.com/NORAD/elements/noaa.txt", "noaa.txt")

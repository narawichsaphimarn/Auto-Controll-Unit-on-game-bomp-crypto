from time import sleep
import pyautogui
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageGrab
from multiprocessing import Process

screenWidth = 1920
screenHeight = 1080
heroCount = 10
waitBomb = 300


def MoveMouseTo(valuePosition):
    try:
        pyautogui.moveTo(valuePosition[0] + (valuePosition[2] / 2),
                         valuePosition[1] + (valuePosition[3] / 2), 0.3)
        return True
    except:
        return False


def Click():
    try:
        pyautogui.click()
        return True
    except:
        return False


def CheckSignInPage():
    try:
        connectWalletButton = CheckPositionTagetFromScreen(
            "./assets/connectWalletButton.png")
        try:
            if (connectWalletButton[1] >= 0.8):
                return True
            else:
                return False
        except:
            return False
    except:
        return False


def CheckHomePage():
    try:
        homePageScreen = CheckPositionTagetFromScreen(
            "./assets/homePageScreen.png")
        try:
            if (homePageScreen[1] >= 0.8):
                return True
            else:
                return False
        except:
            return False
    except:
        return False


def CheckGameBoardTreasureHunt():
    try:
        wallInGame = CheckPositionTagetFromScreen("./assets/wallInGame.png")
        try:
            if (wallInGame[1] >= 0.8):
                return True
            else:
                return False
        except:
            return False
    except:
        return False


def CheckMetamaskMenu():
    try:
        iconMenuMetamask = CheckPositionTagetFromScreen(
            "./assets/iconMenuMetamask.png")
        try:
            if (iconMenuMetamask[1] >= 0.8):
                return True
            else:
                return False
        except:
            return False
    except:
        return False


def CheckHeroesControlPage():
    try:
        menuHeroesControl = CheckPositionTagetFromScreen(
            "./assets/menuHeroesControl.png")
        try:
            if (menuHeroesControl[1] > 0.8):
                return True
            else:
                return False
        except:
            return False
    except:
        return False


def CheckMessageError():
    try:
        messageError = CheckPositionTagetFromScreen(
            "./assets/messageError.png")
        try:
            if (messageError[1] >= 0.9):
                return True
            else:
                return False
        except:
            return False
    except:
        return False


def StepSignIn():
    try:
        connectWalletButton = pyautogui.locateOnScreen(
            "./assets/connectWalletButton.png")
        respMove = MoveMouseTo(connectWalletButton)
        if (respMove):
            print("|- OK PASS :: STEP MOVE TO WALLET BUTTON")
            respClick = Click()
            if (respClick):
                print("|-- OK PASS :: STEP CLICK TO WALLET BUTTON")
                sleep(4)
                metaSignIn = pyautogui.locateOnScreen(
                    "./assets/metaSignIn.png")
                respMoveSignIn = MoveMouseTo(metaSignIn)
                if (respMoveSignIn):
                    print("|--- OK PASS :: STEP MOVE TO SIGIN WALLET BUTTON")
                    respClickSignIn = Click()
                    if (respClickSignIn):
                        print("|---- OK PASS :: STEP CLICK TO SIGIN WALLET BUTTON")
                        CheckoutToMain()
                    else:
                        print("|---- FAIL PASS :: STEP CLICK TO SIGIN WALLET BUTTON")
                        CheckoutToMain()
                else:
                    print("|--- FAIL PASS :: STEP MOVE TO SIGIN WALLET BUTTON")
                    CheckoutToMain()
            else:
                print("|-- FAIL PASS :: STEP CLICK TO WALLET BUTTON")
                CheckoutToMain()
        else:
            print("|- FAIL PASS :: STEP MOVE TO WALLET BUTTON")
            CheckoutToMain()
    except:
        print(">FAIL PASS :: STEP SIGNIN")
        CheckoutToMain()


def StepHomePage():
    try:
        logoGameTreasureHunt = pyautogui.locateOnScreen(
            "./assets/logoGameTreasureHunt.png")
        respMove = MoveMouseTo(logoGameTreasureHunt)
        if (respMove):
            print("|- OK PASS :: STEP MOVE TO LOGO GAME TREASURE HUNT")
            respClick = Click()
            if (respClick):
                print("|-- OK PASS :: STEP CLICK TO LOGO GAME TREASURE HUNT")
                CheckoutToMain()
            else:
                print("|-- FAIL PASS :: STEP CLICK TO LOGO GAME TREASURE HUNT")
                CheckoutToMain()
        else:
            print("|- FAIL PASS :: STEP MOVE TO LOGO GAME TREASURE HUNT")
            CheckoutToMain()
    except:
        print(">FAIL PASS :: STEP HOMEPAGE")
        CheckoutToMain()


def CheckPositionTagetFromScreen(path):
    try:
        screen = ImageGrab.grab(bbox=(0, 0, screenWidth, screenHeight))
        screen = np.array(screen)
        screen = cv.cvtColor(screen, cv.COLOR_RGB2GRAY)
        template = cv.imread(path, 0)
        w, h = template.shape[::-1]

        method = eval('cv.TM_CCOEFF_NORMED')
        img = screen.copy()

        res = cv.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        return (min_val, max_val, min_loc, max_loc, w, h)
    except:
        return (0, 0, 0, 0, 0, 0)


def StepGameTreasureHunt():
    try:
        pathMenuHeroDown = "./assets/iconShowMenuButtonDown.png"
        respCheckMenuHeroDown = CheckPositionTagetFromScreen(pathMenuHeroDown)
        if (respCheckMenuHeroDown[1] >= 0.7):
            sleep(2)
            print("|- OK PASS :: STEP CLICK TO MENU HERO DOWN TRUE")
            pathHeroesMenu = "./assets/iconMenuHeroesButton.png"
            respCheckIconMenuHeroesButton = CheckPositionTagetFromScreen(
                pathHeroesMenu)
            if (respCheckIconMenuHeroesButton[1] > 0.9):
                print("|-- OK PASS :: STEP CLICK ICON MENU HERO")
                respMoveHeroesMenu = MoveMouseTo(
                    (respCheckIconMenuHeroesButton[3][0], respCheckIconMenuHeroesButton[3][1], respCheckIconMenuHeroesButton[4], respCheckIconMenuHeroesButton[5]))
                if(respMoveHeroesMenu):
                    print("|--- OK PASS :: STEP MOVE ICON MENU HERO")
                    respClickHeroesMenu = Click()
                    if (respClickHeroesMenu):
                        print(
                            "|---- OK PASS :: STEP CLICK ICON MENU HERO")
                        CheckoutToMain()
                    else:
                        print(
                            "|---- FAIL PASS :: STEP CLICK ICON MENU HERO")
                        CheckoutToMain()
                else:
                    print(
                        "|--- FAIL PASS :: STEP MOVE ICON MENU HERO")
                    CheckoutToMain()
            else:
                print("|-- FAIL PASS :: STEP CLICK ICON MENU HERO")
                CheckoutToMain()
        else:
            print("|- OK PASS :: STEP CLICK TO MENU HERO DOWN FALSE")
            path = "./assets/iconShowMenuButton2.png"
            respCheckMenuHero = CheckPositionTagetFromScreen(path)
            if (respCheckMenuHero[1] > 0.9):
                print("|- OK PASS :: STEP CHECK MENU HERO")
                respMove = MoveMouseTo(
                    (respCheckMenuHero[3][0], respCheckMenuHero[3][1], respCheckMenuHero[4], respCheckMenuHero[5]))
                if (respMove):
                    print("|-- OK PASS :: STEP MOVE TO MENU HERO")
                    respClick = Click()
                    if (respClick):
                        sleep(2)
                        print("|--- OK PASS :: STEP CLICK TO MENU HERO")
                        pathHeroesMenu = "./assets/iconMenuHeroesButton.png"
                        respCheckIconMenuHeroesButton = CheckPositionTagetFromScreen(
                            pathHeroesMenu)
                        if (respCheckIconMenuHeroesButton[1] > 0.9):
                            print("|---- OK PASS :: STEP CLICK ICON MENU HERO")
                            respMoveHeroesMenu = MoveMouseTo(
                                (respCheckIconMenuHeroesButton[3][0], respCheckIconMenuHeroesButton[3][1], respCheckIconMenuHeroesButton[4], respCheckIconMenuHeroesButton[5]))
                            if(respMoveHeroesMenu):
                                print("|----- OK PASS :: STEP MOVE ICON MENU HERO")
                                respClickHeroesMenu = Click()
                                if (respClickHeroesMenu):
                                    print(
                                        "|------ OK PASS :: STEP CLICK ICON MENU HERO")
                                    CheckoutToMain()
                                else:
                                    print(
                                        "|------ FAIL PASS :: STEP CLICK ICON MENU HERO")
                                    CheckoutToMain()
                            else:
                                print(
                                    "|----- FAIL PASS :: STEP MOVE ICON MENU HERO")
                                CheckoutToMain()
                        else:
                            print("|---- FAIL PASS :: STEP CLICK ICON MENU HERO")
                            CheckoutToMain()
                    else:
                        print("|--- FAIL PASS :: STEP CLICK TO MENU HERO")
                        CheckoutToMain()
                else:
                    print("|-- FAIL PASS :: STEP MOVE TO MENU HERO")
                    CheckoutToMain()
            else:
                print("|- FAIL PASS :: STEP MOVE CHECK MENU HERO")
                CheckoutToMain()
    except:
        print(">FAIL PASS :: STEP GAME TREASURE HUNT")
        CheckoutToMain()


def StepScrollMouseDown(num):
    try:
        pyautogui.scroll(-num)
        return True
    except:
        print("> FAIL PASS :: STEP SCROLL MOUSE")
        CheckoutToMain()


def StepWork(percentPower):
    try:
        print("> OK PASS :: STEP WORK")
        screen = ImageGrab.grab(bbox=(0, 0, screenWidth, screenHeight))
        screen = np.array(screen)
        screen = cv.cvtColor(screen, cv.COLOR_RGB2GRAY)
        path = "./assets/workButtonUnActive.png"
        template = cv.imread(path, 0)
        w, h = template.shape[::-1]

        res = cv.matchTemplate(screen, template, cv.TM_CCOEFF_NORMED)
        threshold = 0.9
        loc = np.where(res >= threshold)
        index = 0
        for pt in zip(*loc[::-1]):
            powerValue = percentPower[index]
            resMove = MoveMouseTo((pt[0], pt[1], w, h))
            if (resMove):
                if (powerValue >= 0.99):
                    print("|-- CHECK WORK HERO " + str(index + 1) +
                          " | STATUS ACTIVE")
                    Click()
                else:
                    print("|-- CHECK WORK HERO " + str(index + 1) +
                          " | STATUS UNACTIVE")
            else:
                CheckoutToMain()
            index += 1
    except:
        print("> FAIL PASS :: STEP WORK")
        CheckoutToMain()


def StepHeroesControl():
    try:
        heroPage = 1
        while (True):
            print("|- START PAGE " + str(heroPage))
            screen = ImageGrab.grab(bbox=(0, 0, screenWidth, screenHeight))
            screen = np.array(screen)
            screen = cv.cvtColor(screen, cv.COLOR_RGB2GRAY)
            path = "./assets/powerBomb.png"
            pathPowerFull = "./assets/powerBombFull.png"
            template = cv.imread(path, 0)
            w, h = template.shape[::-1]

            res = cv.matchTemplate(screen, template, cv.TM_CCOEFF_NORMED)
            threshold = 0.9
            method = eval('cv.TM_CCORR_NORMED')
            loc = np.where(res >= threshold)
            i = 1
            percentPower = []
            for pt in zip(*loc[::-1]):
                power = ImageGrab.grab(bbox=(pt[0], pt[1], pt[0]+w, pt[1]+h))
                imagePower = np.array(power)
                hsv = cv.cvtColor(imagePower, cv.COLOR_RGB2GRAY)
                imagePowerFull = cv.imread(pathPowerFull, 0)
                res = cv.matchTemplate(imagePowerFull, hsv, method)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
                print("|-- CHECK SATAMENA HERO " + str(i) +
                      " | PERCENT " + str(max_val) + " %")
                percentPower.append(max_val)
                cv.rectangle(
                    screen, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                MoveMouseTo((pt[0], pt[1], w, h))
                if (i == 1):
                    Click()
                i += 1
                sleep(1)
            StepWork(percentPower)

            if (heroPage >= (heroCount / 5)):
                break
            else:
                j = 1
                while (True):
                    if (j == 21):
                        break
                    StepScrollMouseDown(1000)
                    j += 1
            heroPage += 1
            sleep(3)
        StepCloseHeroesControl()
    except:
        print("> FAIL PASS :: STEP HEROES CONTROL")
        CheckoutToMain()


def StepCloseHeroesControl():
    try:
        print("> OK PASS :: STEP EXIT HEROES CONTROL")
        pathMenuHeroDown = "./assets/iconShowMenuButtonDown.png"
        respCheckMenuHeroDown = CheckPositionTagetFromScreen(
            pathMenuHeroDown)
        if (respCheckMenuHeroDown[1] >= 0.7):
            print("|- OK PASS :: STEP CHECK MENU HERO TRUE")
            Click()
            sleep(waitBomb)
            CheckoutToMain()
        else:
            print("|- OK PASS :: STEP CHECK MENU HERO FALSE")
            closeButton = "./assets/closeButton.png"
            respCloseButton = CheckPositionTagetFromScreen(closeButton)
            if (respCloseButton):
                print("|-- OK PASS :: STEP CHECK TO CLOSE MENU")
                respMove = MoveMouseTo(
                    (respCloseButton[3][0], respCloseButton[3][1], respCloseButton[4], respCloseButton[5]))
                if (respMove):
                    print("|--- OK PASS :: STEP MOVE TO CLOSE MENU")
                    resClick = Click()
                    if(resClick):
                        print("|---- OK PASS :: STEP CLICK TO CLOSE MENU")
                        sleep(1)
                        pathMenuHeroDown = "./assets/iconShowMenuButtonDown.png"
                        respCheckMenuHeroDown = CheckPositionTagetFromScreen(
                            pathMenuHeroDown)
                        if (respCheckMenuHeroDown[1] >= 0.7):
                            print(
                                "|----- OK PASS :: STEP CHECK TO CLOSE MENU HERO DOWN")
                            pyautogui.moveTo(respCheckMenuHeroDown[3][0] + (respCheckMenuHeroDown[4] / 2),
                                             respCheckMenuHeroDown[3][1], 0.3)
                            Click()
                            sleep(waitBomb)
                            CheckoutToMain()
                        else:
                            print(
                                "|----- FAIL PASS :: STEP CHECK TO CLOSE MENU HERO DOWN")
                            CheckoutToMain()
                    else:
                        print("|---- FAIL PASS :: STEP CLICK TO CLOSE MENU")
                        CheckoutToMain()
                else:
                    print("|--- FAIL PASS :: STEP MOVE TO CLOSE MENU")
                    CheckoutToMain()
            else:
                print("|-- FAIL PASS :: STEP CHECK TO CLOSE MENU")
                CheckoutToMain()
    except:
        print("> FAIL PASS :: STEP EXIT HEROES CONTROL")
        CheckoutToMain()


def StepSkipError():
    try:
        messageErrorButton = CheckPositionTagetFromScreen(
            "./assets/messageErrorButton.png")
        if (messageErrorButton[1] >= 0.9):
            respMove = MoveMouseTo(
                (messageErrorButton[3][0], messageErrorButton[3][1], messageErrorButton[4], messageErrorButton[5]))
            if(respMove):
                Click()
                CheckoutToMain()
            else:
                CheckoutToMain()
        else:
            CheckoutToMain()
    except:
        print("> FAIL PASS :: STEP SKIP CLICK ERROR OK")
        CheckoutToMain()


def Main():
    _error = CheckMessageError()
    if (_error):
        print("> START STEP SKIP ERROR")
        StepSkipError()
    else:
        _signInPage = CheckSignInPage()
        print(_signInPage)
        if (_signInPage):
            print("> START STEP SIGNIN")
            StepSignIn()
        else:
            _homePage = CheckHomePage()
            if (_homePage):
                print("> START STEP HOMEPAGE")
                StepHomePage()
            else:
                _gameBoardTreasureHunt = CheckGameBoardTreasureHunt()
                if (_gameBoardTreasureHunt):
                    print("> START STEP GAME TREASURE HUNT")
                    StepGameTreasureHunt()
                else:
                    _heroesControlBoard = CheckHeroesControlPage()
                    if (_heroesControlBoard):
                        print("> START STEP HEROES CONTROL")
                        StepHeroesControl()
                    else:
                        CheckoutToMain()


def CheckoutToMain():
    sleep(4)
    Main()


if __name__ == '__main__':
    print("[ START AUTO BOMB CRYPTO ]")
    Main()

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
            respClick = Click()
            if (respClick):
                sleep(4)
                metaSignIn = pyautogui.locateOnScreen(
                    "./assets/metaSignIn.png")
                respMoveSignIn = MoveMouseTo(metaSignIn)
                if (respMoveSignIn):
                    respClickSignIn = Click()
                    if (respClickSignIn):
                        CheckoutToMain()
                    else:
                        CheckoutToMain()
                else:
                    CheckoutToMain()
            else:
                CheckoutToMain()
        else:
            CheckoutToMain()
    except:
        CheckoutToMain()


def StepHomePage():
    try:
        logoGameTreasureHunt = pyautogui.locateOnScreen(
            "./assets/logoGameTreasureHunt.png")
        respMove = MoveMouseTo(logoGameTreasureHunt)
        if (respMove):
            respClick = Click()
            if (respClick):
                CheckoutToMain()
            else:
                CheckoutToMain()
        else:
            CheckoutToMain()
    except:
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
            sleep(0.3)
            pathHeroesMenu = "./assets/iconMenuHeroesButton.png"
            respCheckIconMenuHeroesButton = CheckPositionTagetFromScreen(
                pathHeroesMenu)
            if (respCheckIconMenuHeroesButton[1] > 0.9):
                respMoveHeroesMenu = MoveMouseTo(
                    (respCheckIconMenuHeroesButton[3][0], respCheckIconMenuHeroesButton[3][1], respCheckIconMenuHeroesButton[4], respCheckIconMenuHeroesButton[5]))
                if(respMoveHeroesMenu):
                    respClickHeroesMenu = Click()
                    if (respClickHeroesMenu):
                        CheckoutToMain()
                    else:
                        CheckoutToMain()
                else:
                    CheckoutToMain()
            else:
                CheckoutToMain()
        else:
            path = "./assets/iconShowMenuButton2.png"
            respCheckMenuHero = CheckPositionTagetFromScreen(path)
            if (respCheckMenuHero[1] > 0.9):
                respMove = MoveMouseTo(
                    (respCheckMenuHero[3][0], respCheckMenuHero[3][1], respCheckMenuHero[4], respCheckMenuHero[5]))
                if (respMove):
                    respClick = Click()
                    if (respClick):
                        sleep(0.3)
                        pathHeroesMenu = "./assets/iconMenuHeroesButton.png"
                        respCheckIconMenuHeroesButton = CheckPositionTagetFromScreen(
                            pathHeroesMenu)
                        if (respCheckIconMenuHeroesButton[1] > 0.9):
                            respMoveHeroesMenu = MoveMouseTo(
                                (respCheckIconMenuHeroesButton[3][0], respCheckIconMenuHeroesButton[3][1], respCheckIconMenuHeroesButton[4], respCheckIconMenuHeroesButton[5]))
                            if(respMoveHeroesMenu):
                                respClickHeroesMenu = Click()
                                if (respClickHeroesMenu):
                                    CheckoutToMain()
                                else:
                                    CheckoutToMain()
                            else:
                                CheckoutToMain()
                        else:
                            CheckoutToMain()
                    else:
                        CheckoutToMain()
                else:
                    CheckoutToMain()
            else:
                CheckoutToMain()
    except:
        CheckoutToMain()


def StepScrollMouseDown(num):
    try:
        pyautogui.scroll(-num)
        return True
    except:
        CheckoutToMain()


def StepWork(percentPower):
    try:
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
                if (powerValue >= 0.989):
                    Click()
            else:
                CheckoutToMain()
            index += 1
    except:
        CheckoutToMain()


def StepHeroesControl():
    try:
        heroPage = 1
        while (True):
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
                percentPower.append(max_val)
                cv.rectangle(
                    screen, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                MoveMouseTo((pt[0], pt[1], w, h))
                if (i == 1):
                    Click()
                i += 1
            StepWork(percentPower)

            if (heroPage >= (heroCount / 5)):
                break
            else:
                j = 1
                while (True):
                    if (j == 21):
                        break
                    StepScrollMouseDown(100000000)
                    j += 1
            heroPage += 1
            sleep(0.5)
        StepCloseHeroesControl()
    except:
        CheckoutToMain()


def StepCloseHeroesControl():
    try:
        pathMenuHeroDown = "./assets/iconShowMenuButtonDown.png"
        respCheckMenuHeroDown = CheckPositionTagetFromScreen(
            pathMenuHeroDown)
        if (respCheckMenuHeroDown[1] >= 0.7):
            Click()
            sleep(waitBomb)
            CheckoutToMain()
        else:
            closeButton = "./assets/closeButton.png"
            respCloseButton = CheckPositionTagetFromScreen(closeButton)
            if (respCloseButton):
                respMove = MoveMouseTo(
                    (respCloseButton[3][0], respCloseButton[3][1], respCloseButton[4], respCloseButton[5]))
                if (respMove):
                    resClick = Click()
                    if(resClick):
                        sleep(1)
                        pathMenuHeroDown = "./assets/iconShowMenuButtonDown.png"
                        respCheckMenuHeroDown = CheckPositionTagetFromScreen(
                            pathMenuHeroDown)
                        if (respCheckMenuHeroDown[1] >= 0.7):
                            pyautogui.moveTo(respCheckMenuHeroDown[3][0] + (respCheckMenuHeroDown[4] / 2),
                                             respCheckMenuHeroDown[3][1], 0.3)
                            Click()
                            sleep(waitBomb)
                            CheckoutToMain()
                        else:
                            CheckoutToMain()
                    else:
                        CheckoutToMain()
                else:
                    CheckoutToMain()
            else:
                CheckoutToMain()
    except:
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
        CheckoutToMain()


def Main():
    _error = CheckMessageError()
    if (_error):
        StepSkipError()
    else:
        _signInPage = CheckSignInPage()
        if (_signInPage):
            StepSignIn()
        else:
            _homePage = CheckHomePage()
            if (_homePage):
                StepHomePage()
            else:
                _gameBoardTreasureHunt = CheckGameBoardTreasureHunt()
                if (_gameBoardTreasureHunt):
                    StepGameTreasureHunt()
                else:
                    _heroesControlBoard = CheckHeroesControlPage()
                    if (_heroesControlBoard):
                        StepHeroesControl()
                    else:
                        CheckoutToMain()


def CheckoutToMain():
    sleep(0.3)
    Main()


if __name__ == '__main__':
    Main()

from time import sleep
import pyautogui
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageGrab

screenWidth = 1920
screenHeight = 1080


def MoveMouseTo(valuePosition):
    try:
        pyautogui.moveTo(valuePosition[0] + (valuePosition[2] / 2),
                         valuePosition[1] + (valuePosition[3] / 2), 1)
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
        logoBombCrypto = pyautogui.locateOnScreen(
            "./assets/logoBombCrypto.png")
        connectWalletButton = pyautogui.locateOnScreen(
            "./assets/connectWalletButton.png")
        try:
            if (connectWalletButton[0] & logoBombCrypto[0]):
                return True
        except:
            return False
    except:
        return False


def CheckHomePage():
    try:
        logoGameTreasureHunt = pyautogui.locateOnScreen(
            "./assets/logoGameTreasureHunt.png")
        logoGameBattle = pyautogui.locateOnScreen(
            "./assets/logoGameBattle.png")
        logoGameAdventure = pyautogui.locateOnScreen(
            "./assets/logoGameAdventure.png")
        iconChest = pyautogui.locateOnScreen("./assets/iconChest.png")
        iconHeroes = pyautogui.locateOnScreen("./assets/iconHeroes.png")
        iconHome = pyautogui.locateOnScreen("./assets/iconHome.png")
        iconStore = pyautogui.locateOnScreen("./assets/iconStore.png")
        try:
            if (logoGameTreasureHunt[0] | logoGameBattle[0] | logoGameAdventure[0] | iconChest[0]
                    | iconHeroes[0] | iconHome[0] | iconStore[0]):
                return True
        except:
            return False
    except:
        return False


def CheckGameBoardTreasureHunt():
    try:
        wallInGame = pyautogui.locateOnScreen(
            "./assets/wallInGame.png")
        try:
            if (wallInGame[0]):
                return True
        except:
            return False
    except:
        return False


def CheckMetamaskMenu():
    try:
        iconMenuMetamask = pyautogui.locateOnScreen(
            "./assets/iconMenuMetamask.png")
        try:
            if (iconMenuMetamask[0]):
                return True
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


def CheckPositionTagetFromScreen():
    try:
        print()
    except:
        return (0, 0, 0, 0)


def StepGameTreasureHunt():
    screen = ImageGrab.grab(
        bbox=(0, 0, screenWidth, screenHeight))
    screen = np.array(screen)
    frame = cv.cvtColor(screen, cv.COLOR_BGR2GRAY)
    template = cv.imread(
        "./assets/iconHeroesSleepActive4.png", 0)
    w, h = template.shape[::-1]

    method = eval('cv.TM_CCOEFF_NORMED')
    img = frame.copy()

    # Apply template Matching
    res = cv.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    print(min_loc)
    print(max_loc)

    threshold = 0.6
    if (max_val >= threshold):
        iconShowMenuButton = pyautogui.locateOnScreen(
            "./assets/iconShowMenuButton.png")
        respMove = MoveMouseTo(iconShowMenuButton)
        # pyautogui.moveTo((max_loc[0] + (w / 2)), (max_loc[1] + (h / 2)), 1)

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # cv.rectangle(img, top_left, bottom_right, 255, 2)
    # plt.subplot(121), plt.imshow(res, cmap='gray')
    # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(img, cmap='gray')
    # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    # plt.suptitle(method)
    # plt.show()


def Main():
    _signInPage = CheckSignInPage()
    _homePage = CheckHomePage()
    _gameBoardTreasureHunt = CheckGameBoardTreasureHunt()

    if (_signInPage):
        print(">START STEP SIGNIN")
        StepSignIn()
    else:
        if (_homePage):
            print(">START STEP HOMEPAGE")
            StepHomePage()
        else:
            if (_gameBoardTreasureHunt):
                print(">START STEP GAME TREASURE HUNT")
                StepGameTreasureHunt()
            else:
                CheckoutToMain()


def CheckoutToMain():
    sleep(4)
    Main()


print("START AUTO BOMB CRYPTO")
Main()

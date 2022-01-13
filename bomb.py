from re import T
import pyautogui
import time

contador= 0

pyautogui.alert("Começando apos clicar em ok")
time.sleep(1)

while contador < 10:
    #atualizar a pagina
    pyautogui.click(86, 50)
    time.sleep(20)

    #conectar na metamask
    pyautogui.click(670, 574)
    time.sleep(10)
    pyautogui.click(1262, 540)
    time.sleep(25)
    
    #colocar o boneco pra trabalhar
    caca_tesouro= pyautogui.click(676, 388)
    time.sleep(3)
    seta_abrir= pyautogui.click(672, 671)
    time.sleep(3)
    herois= pyautogui.click(seta_abrir)
    time.sleep(3)
    work= pyautogui.click(590, 294)
    time.sleep(3)
    seta_x= pyautogui.click(727, 202)
    time.sleep(3)
    seta_fechar= pyautogui.click(674, 578)
    time.sleep(3)
    seta_desbug= pyautogui.click(242, 121)
    time.sleep(3)
    caca_tesouro= pyautogui.click(676, 388)
    time.sleep(3600) #3600 = 1 hora
    contador += 1
    print(contador)
pyautogui.alert("Fim")
''




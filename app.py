import pyautogui
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 0.7
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
pyautogui.click(x=776, y=369)
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("teste1")
pyautogui.press("tab")
pyautogui.press("enter")
tabela = pandas.read_csv("produtos.csv")
for linha in tabela.index:
    pyautogui.click(x=784, y=251)
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")  
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)  

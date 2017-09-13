import pyperclip
import webbrowser

address = pyperclip.paste()

webbrowser.open('https://www.google.co.in/search?q='+address)


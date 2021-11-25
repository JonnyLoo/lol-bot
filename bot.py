import speech_recognition as sr
import pyautogui
import pydirectinput
from time import sleep

r = sr.Recognizer()
WIT_AI_KEY = 'GJUDED4Y37V5Z7ZGPPE2XG6SHAOEUK3H'

action = ''
following = False

def act(command):
    if command == 'Come here' or command == 'Come here.':
        pydirectinput.keyDown('f2')
        pydirectinput.moveTo(800, 500)
        pydirectinput.click(button='right')
        pydirectinput.keyUp('f2')
        print('im clicking')

    if command == 'Follow me' or command == 'Follow me.':
        following = True

    if command == 'Level bubble' or command == 'Level bubble.':
        pydirectinput.keyDown('ctrl')
        pydirectinput.press('q')
        print('leveling q')

    if command == 'Stop' or command == 'Stop.':
        following = False

    if following:
        pydirectinput.keyDown('f2')
        pydirectinput.moveTo(800, 500)
        pydirectinput.click(button='right')
        pydirectinput.click(button='right')
        pydirectinput.click(button='right')
        pydirectinput.click(button='right')
        pydirectinput.click(button='right')

while True:
    with sr.Microphone() as source:
        print('Say something!')
        audio = r.listen(source)

    try:
        action = r.recognize_wit(audio, key=WIT_AI_KEY)
        print('you said ' + action)
    except sr.UnknownValueError:
        print('wtf did u say')
    except sr.RequestError as e:
        print('??? error: {0}'.format(e))

    act(action)

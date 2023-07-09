import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

def garis():
    print(40 * "=")

print("Jarvis")
MASTER = "sahrul"
mendengarkan = sr.Recognizer()
engine = pyttsx3.init("sapi5")
# kecepatan baca
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
# jenis suara [0] male [1] female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Hello Good Morning " + MASTER)
        talk("Hello Good Morning " + MASTER)
        garis()
    elif hour >= 12 and hour < 18:
        print("Hello Good Afternoon " + MASTER)
        talk("Hello Good Afternoon " + MASTER)
        garis()
    else:
        print("Hello Good Evening " + MASTER)
        talk("Hello Good Evening " + MASTER)
        garis()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Mendengarkan")
            garis()
            voice = mendengarkan.listen(source)
            command = mendengarkan.recognize_google(voice)
            command = command.lower()
            if "jarvis" in command:
                print(command)
                command = command.replace("jarvis", "")
                talk(command)

    except:
        print("Exit")

    return command


def run_jarvis():
    command = input("Masukkan perintah untuk Jarvis: ")
    if 'play' in command:
        song = command.replace("play", "")
        print("Playing " + song)
        garis()
        talk("Playing " + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print("Time now is " + time)
        garis()
        talk("Time now is " + time)
    elif "day" in command:
        time = datetime.datetime.now().strftime("%A, %d - %B - %Y")
        print("Today is " + time)
        garis()
        talk("Today is " + time)
    elif "wikipedia" in command:
        src = command.replace("wikipedia", "")
        info = wikipedia.summary(src, sentences=1)
        talk("Searching Wikipedia")
        print(info)
        garis()
        talk(info)
    elif "login" in command:
        talk("Login Elearning")
        file = open("akun.txt")
        filebaca = file.readlines()
        username = filebaca[0]
        password = filebaca[1]
        def browser():
            browser = webdriver.Chrome('webdriver/chromedriver.exe')
            browser.get(url)
            login = browser.find_element_by_name("username")
            login.send_keys(username[11:], Keys.TAB, password[11:], Keys.ENTER)
        hari = datetime.datetime.now().strftime("%a")
        jam = datetime.datetime.now().strftime("%H:%M")
        # Senin
        if hari == "Mon" and jam < "16:40":
            link = open("link.txt")
            el = link.readlines()
            url = el[4]
            browser()
            garis()
        # Selasa
        elif hari == "Tue" and jam < "16:40":
            link = open("link.txt")
            el = link.readlines()
            url = el[8]
            browser()
            garis()
        # Rabu
        # Pelajaran Pertama
        elif hari == "Wed" and jam < "12:30":
            link = open("link.txt")
            el = link.readlines()
            url = el[12]
            browser()
            garis()
        # Pelajaran Ke dua
        elif hari == "Wed" and jam > "12:30" < "14:10":
            link = open("link.txt")
            el = link.readlines()
            url = el[15]
            browser()
            garis()
        # Kamis
        # Pelajaran pertama
        elif hari == "Thu" and jam < "07:30" < "10:50":
            link = open("link.txt")
            el = link.readlines()
            url = el[19]
            browser()
            garis()
        #Pelajaran Ke dua
        elif hari == "Thu" and jam < "12:30" < "15:00":
            link = open("link.txt")
            el = link.readlines()
            url = el[22]
            browser()
            garis()
        else:
            print("Tidak ada jadwal")
            garis()
            talk("No Schedule today")
    elif "sigma" in command:
        def sigma(bb, ba):
            k = int(input("Konstanta Pertama: "))
            k1 = int(input("Konstanta selanjutnya: "))
            garis()
            listh = []
            for i in range(bb, ba):
                k = k
                k1 = k1
                c = i * k + k1
                listh.append(c)
            k *= ba
            k += k1
            listh.append(k)
            print(listh)
            hasil = sum(listh)
            print("Hasil Nilai Sigma =", hasil)
            talk(f"The result of sigma is {hasil}")
        print("{:^40}".format("=== Rumus Notasi Sigma ==="))
        talk("Calculate sigma, please enter a number")
        bb = int(input("Masukan Batas Bawah: "))
        ba = int(input("Masukan Batas Atas: "))
        garis()
        sigma(bb, ba)
        garis()
    elif "rectangle" in command:
        print("{:^40}".format("=== Luas Persegi Panjang ==="))
        talk("Calculate rectangle, please enter a number")
        p = int(input("Masukan Nilai Panjang: "))
        l = int(input("Masukan Nilai Lebar: "))
        luas = p * l
        print("Nilai Luas Persegi Panjang =", luas)
        garis()
        talk(f"The result of rectangle is {luas}")
    elif "stop" in command:
        talk(f"Okay, run me again if you need help {MASTER}")
        print("Exit Program")
        garis()
        sys.exit()
    else:
        talk("No instructions found")
        print(command)
        garis()


wishMe()

while True:
    MASTER = "sahrul"
    mendengarkan = sr.Recognizer()
    engine = pyttsx3.init("sapi5")
    # kecepatan baca
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    # jenis suara [0] male [1] female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    print("I am Jarvis. What do you want?")
    run_jarvis()

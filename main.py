from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import os

fontSIZE = 14

window = Tk()
window.title("Универсальный конвертор")
window.geometry(f"{1200}x{600}")
frame = Frame(window, padx=10, pady=10)
frame.pack(expand=True)

if not os.path.isdir("output"):
    os.mkdir("output")
ffmpegPath = os.getcwd().replace("\\", "/")+"/ffmpeg.exe"
filePath = None
outPath = os.getcwd().replace("\\", "/")+"/output"


def update_command_label():
    file_name = filePath.split("/")[-1].split(".")[0]
    if typeSelect.get() == "JPEG":
        commandLBL2.configure(text="Итоговая команда:\n" + ffmpegPath + f' -i "{filePath}" "{outPath}/{file_name}.jpeg"')
    elif typeSelect.get() == "MP3 320":
        commandLBL2.configure(
            text="Итоговая команда:\n" + ffmpegPath + f' -i "{filePath}" -b:a 320k "{outPath}/{file_name}.mp3"')
    elif typeSelect.get() == "MP4":
        commandLBL2.configure(
            text="Итоговая команда:\n" + ffmpegPath + f' -i "{filePath}" -b:a 320k "{outPath}/{file_name}.mp4"')


def start_convertation():
    # ffmpeg.exe -i "video.webm" -b:a 320k "audio.mp3"
    file_name = filePath.split("/")[-1].split(".")[0]
    if typeSelect.get() == "JPEG":
        os.system(ffmpegPath + f' -i "{filePath}" "{outPath}/{file_name}.jpeg"')
    elif typeSelect.get() == "MP3 320":
        os.system(ffmpegPath + f' -i "{filePath}" -b:a 320k "{outPath}/{file_name}.mp3"')
    elif typeSelect.get() == "MP4":
        os.system(ffmpegPath + f' -i "{filePath}" -b:a 320k  "{outPath}/{file_name}.mp4"')


def select_ffmpeg():
    global ffmpegPath
    ffmpegPath = filedialog.askopenfilename(title="Путь к ffmpeg").replace("\\", "/")
    lblFFMPEGPath.configure(text="Путь к ffmpeg: " + ffmpegPath)
    update_command_label()


def for_load_file():
    global filePath
    filePath = filedialog.askopenfilename().replace("\\", "/")
    if filePath == "":
        filePath = "None"
    lblFilePath.configure(text="Путь к файлу: " + filePath)
    update_command_label()


def select_out_path():
    global outPath
    outPath = filedialog.askdirectory()
    lblOutPath.configure(text="Папка вывода: " + outPath)
    update_command_label()


lblFFMPEGPath = Label(frame, text="Путь к ffmpeg: " + ffmpegPath, font=("Arial", fontSIZE))
lblFFMPEGPath.grid(column=0, row=0)

btnselectFFMPEG = Button(frame, text="Указать путь к FFMPEG", command=select_ffmpeg, font=("Arial", fontSIZE))
btnselectFFMPEG.grid(column=0, row=1)

noneLBL = Label(frame, text=" ")
noneLBL.grid(column=0, row=2)

lblFilePath = Label(frame, text="Путь к файлу: " + "None", font=("Arial", fontSIZE))
lblFilePath.grid(column=0, row=3)

btnLoadF = Button(frame, text="Выбрать файл", command=for_load_file, font=("Arial", fontSIZE))
btnLoadF.grid(column=0, row=4)

lblOutPath = Label(frame, text="Папка вывода: " + str(outPath), font=("Arial", fontSIZE))
lblOutPath.grid(column=0, row=5)

btnLoadF = Button(frame, text="Выбор папки вывода", command=select_out_path, font=("Arial", fontSIZE))
btnLoadF.grid(column=0, row=6)

noneLBL1 = Label(frame, text=" ")
noneLBL1.grid(column=0, row=7)

typeSelect = Combobox(frame)
typeSelect["values"] = ("JPEG", "MP3 320", "MP4")
typeSelect.current(1)
typeSelect.grid(column=0, row=8)

startBtn = Button(frame, text="Начать конвертацию", command=start_convertation, font=("Arial", fontSIZE))
startBtn.grid(column=0, row=9)

commandLBL2 = Label(frame, text=" ")
commandLBL2.grid(column=0, row=10)

startBtn = Button(frame, text="Перечитать команду", command=update_command_label, font=("Arial", fontSIZE - 6))
startBtn.grid(column=0, row=11)

for_load_file()

window.mainloop()

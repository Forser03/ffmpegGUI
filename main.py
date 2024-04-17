from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import os


class ConvertorWindow:
    FONT_SETTINGS_A14 = ("Arial", 14)
    FONT_SETTINGS_A8 = ("Arial", 8)

    def __init__(self):
        window = Tk()
        window.title("Универсальный конвертор")
        window.geometry(f"{1200}x{600}")
        window.minsize(800, 600)
        frame = Frame(window, padx=10, pady=10)
        frame.pack(expand=True)

        self.ffmpeg_path = (os.getcwd().replace("\\", "/") + "/ffmpeg.exe"
                            if os.path.isfile("ffmpeg.exe") else "None")
        self.lbl_ffmpeg_path = Label(frame,
                                     text="Путь к FFMPEG: " + self.ffmpeg_path,
                                     font=self.FONT_SETTINGS_A14)
        self.lbl_ffmpeg_path.grid(column=0, row=0)

        btn_select_ffmpeg = Button(frame,
                                   text="Указать путь к FFMPEG",
                                   command=self.set_ffmpeg_location,
                                   font=self.FONT_SETTINGS_A14)
        btn_select_ffmpeg.grid(column=0, row=1)

        none_lbl = Label(frame, text=" ")
        none_lbl.grid(column=0, row=2)

        self.target_file_path = "None"
        self.lbl_target_file_path = Label(frame,
                              text="Путь к файлу: None",
                              font=self.FONT_SETTINGS_A14)
        self.lbl_target_file_path.grid(column=0, row=3)

        btn_set_target_file_path = Button(frame, text="Выбрать файл",
                                     command=self.set_target_file_path,
                                     font=self.FONT_SETTINGS_A14)
        btn_set_target_file_path.grid(column=0, row=4)

        if not os.path.isdir("output"):
            os.mkdir("output")
        self.output_path = os.getcwd().replace("\\", "/") + "/output"
        self.lbl_output_path = Label(frame,
                                     text="Путь вывода: " + self.output_path,
                                     font=self.FONT_SETTINGS_A14)
        self.lbl_output_path.grid(column=0, row=5)

        btn_set_output_path = Button(frame,
                                     text="Выбор папки вывода",
                                     command=self.set_output_path,
                                     font=self.FONT_SETTINGS_A14)
        btn_set_output_path.grid(column=0, row=6)

        none_lbl = Label(frame, text=" ")
        none_lbl.grid(column=0, row=7)

        self.selector_out_type = Combobox(frame)
        self.selector_out_type["values"] = ("JPEG", "MP3 320 kbps", "MP4")
        self.selector_out_type.current(1)
        self.selector_out_type.grid(column=0, row=8)

        btn_start = Button(frame,
                           text="Начать конвертацию",
                           command=self.start_conversion,
                           font=self.FONT_SETTINGS_A14)
        btn_start.grid(column=0, row=9)

        self.final_command = None
        self.update_final_command()
        self.lbl_final_command = Label(frame, text=str(self.final_command))
        self.lbl_final_command.grid(column=0, row=10)

        btn_start = Button(frame,
                           text="Перечитать команду",
                           command=self.update_window,
                           font=self.FONT_SETTINGS_A8)
        btn_start.grid(column=0, row=11)

        self.set_target_file_path()
        window.mainloop()

    def update_final_command(self):
        final_file_name = self.target_file_path.split("/")[-1].split(".")[0]
        selector_position = self.selector_out_type.get()

        if selector_position == "JPEG":
            self.final_command = f'{self.ffmpeg_path} -i "{self.target_file_path}" "{self.output_path}/{final_file_name}.jpeg"'
        elif selector_position == "MP3 320 kbps":
            self.final_command = f'{self.ffmpeg_path} -i "{self.target_file_path}" -b:a 320k "{self.output_path}/{final_file_name}.mp3"'
        elif selector_position == "MP4":
            self.final_command = f'{self.ffmpeg_path} -i "{self.target_file_path}" -b:a 320k "{self.output_path}/{final_file_name}.mp4"'

    def update_window(self):
        self.update_final_command()
        self.lbl_ffmpeg_path.configure(text="Путь к FFMPEG: " + self.ffmpeg_path)
        self.lbl_target_file_path.configure(text="Путь к файлу: " + self.target_file_path)
        self.lbl_output_path.configure(text="Путь вывода: " + self.output_path)
        self.lbl_final_command.configure(text="Итоговая команда: " + self.final_command)

    def set_target_file_path(self):
        file_path = filedialog.askopenfilename(title="Выберите файл").replace("\\", "/")
        if file_path == "":
            file_path = "None"
        self.target_file_path = file_path
        self.update_window()

    def set_ffmpeg_location(self):
        ffmpeg_path = filedialog.askopenfilename(title="Путь к ffmpeg").replace("\\", "/")
        if ffmpeg_path == "":
            ffmpeg_path = "None"
        self.ffmpeg_path = ffmpeg_path
        self.update_window()

    def set_output_path(self):
        output_path = filedialog.askdirectory(title="Куда выводить файлы")
        if output_path == "":
            output_path = "None"
        self.output_path = output_path
        self.update_window()

    def start_conversion(self):
        # ffmpeg.exe -i "video.webm" -b:a 320k "audio.mp3"
        self.update_window()
        os.system(self.final_command)


if __name__ == "__main__":
    convertor = ConvertorWindow()

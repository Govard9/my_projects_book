from tkinter import *


class Aplication(Frame):
    """GUI - приложение, владеющее секретом долголетия."""
    def __init__(self, master):
        """Инициализирует рамку"""
        # Конструктор надкласса.
        super(Aplication, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Создаёт кнопку, текстовое поле и текстовую область."""
        # метка-инструкция
        self.inst_lbl = Label(self, text='Чтобы узнать секрет долголетия, введите пароль')
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)
        # метка около поля воода пароля
        self.pw_lbl = Label(self, text='Пароль: ')
        self.pw_lbl.grid(row=1, column=0, sticky=W)
        # текстовое поле для ввода пароля
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row=1, column=1, sticky=W)
        # кнопка отправки значания
        self.submit_bttn = Button(self, text='Узнать секрет', command = self.reveal)
        self.submit_bttn.grid(row=2, column=0, sticky=W)
        # создание текстовой области, в которую будет выведен ответ
        self.secret_txt = Text(self, width=35, height=5, wrap=WORD)
        self.secret_txt.grid(row=3, column=0, columnspan=2, sticky=W)

    def reveal(self):
        """В зависимости от введенного пароля отвечает разными сообщениями."""
        contents = self.pw_ent.get()  # get() возвращает текстовое содержимое элемента

        if contents == "secret":
            message = 'Чтобы дожить до 100 лет, надо сначала дожить до 99, а потом вести себя ОЧЕНЬ осторожно.'
        else:
            message = 'Вы ввели неправельный пароль, так что я не могу поделиться тайной с вами.'

        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)


# Основная часть
tk = Tk()
tk.title('Долгожитель')
tk.geometry('300x150')

app = Aplication(tk)
tk.mainloop()
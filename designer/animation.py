import pygame
from designer.secondary_functions import Request, pprint, Language

LANGUAGE = Language().request


class PushButton:  # Выпоняет функцию кнопки
    def __init__(self, scr):  # её характеристики
        self.image1_or_text0 = False
        self.image = ''
        self.draw = scr
        self.color = (0, 0, 0)
        self.x = 0
        self.y = 0
        self.wight = 0
        self.height = 0
        self.border = False
        self.size_border = 1
        self.enabler = True
        self.color_border = (0, 0, 0)
        self.text = ""
        self.background = False
        self.background_color = (255, 255, 255)
        self.show1_or_hide0 = True
        self.font = Font()
        self.click = ''
        self.target = False
        self.image_way = 'False'

    def show(self):  # следующие функции будут отвечать за изменение характеристик
        self.show1_or_hide0 = True

    def hide(self):
        self.show1_or_hide0 = False

    def setTarget(self, target):
        self.target = target

    def getFont(self):
        return self.font

    def changeFont(self, font):
        self.font = font

    def setColor(self, color):
        self.color = color

    def setImage(self, image):
        self.image_way = image
        self.image1_or_text0 = True
        self.image = pygame.image.load(image)
        if self.image.get_size() == (self.wight, self.height):
            pass
        else:
            self.image = pygame.transform.scale(self.image, (self.wight, self.height))

    def setEnabler(self, enabler):
        self.enabler = enabler

    def setText(self, text):
        self.image1_or_text0 = False
        self.text = str(text)

    def setBorder(self, border):
        self.border = border

    def setGeometry(self, x, y, wight, height):
        self.x = x
        self.y = y
        self.wight = wight
        self.height = height

    def setBackgroundColor(self, color):
        self.background_color = color

    def setClick(self, click):
        self.click = click

    def setBackGround(self, bol=True):
        self.background = bol

    def setColorBorder(self, color):
        self.color_border = color

    def check_click(self, pos):
        i = self
        if i.x < pos[0] < i.x + i.wight and i.y < pos[1] < i.y + i.height:
            i.clicked()
        else:
            i.setTarget(False)

    def clicked(self):  # активирует поставленную функцию при нажатии
        self.click()

    def render(self):  # отрисовывает кнопку
        if not self.show1_or_hide0:
            return
        if self.image1_or_text0:
            self.draw.blit(self.image, (self.x, self.y))
        if self.background:
            pygame.draw.rect(self.draw, self.background_color,
                             (self.x, self.y, self.wight, self.height))
        if not self.image1_or_text0:
            text = self.font.getFont().render(self.text, 1, self.color)
            tmp_x = (len(self.text) // 2) * (self.font.size // 2)
            tmp_y = self.font.size // 2.4
            self.draw.blit(text, (self.x + self.wight // 2 - tmp_x, self.y + self.height // 2 - tmp_y))
        if self.border:
            pygame.draw.rect(self.draw, self.color_border,
                             (self.x, self.y, self.wight, self.height), width=self.size_border)


class Label:  # Обычный текст
    def __init__(self, scr):
        self.image1_or_text0 = False
        self.show1_or_hide0 = True
        self.image = ''
        self.draw = scr
        self.color = (0, 0, 0)
        self.x = 0
        self.y = 0
        self.wight = 0
        self.height = 0
        self.text = ""
        self.font = Font()
        self.background = False
        self.background_color = (0, 0, 0)
        self.max_len_text = 10000

    def show(self):
        self.show1_or_hide0 = True

    def hide(self):
        self.show1_or_hide0 = False

    def setColor(self, color):
        self.color = color

    def setBackgroundColor(self, color):
        self.background_color = color

    def setMaxLen(self, max_len):
        self.max_len_text = max_len

    def setBackGround(self, bol=True):
        self.background = bol

    def setImage(self, image):
        self.image1_or_text0 = True
        self.image = pygame.image.load(image)
        if self.image.get_size() == (self.wight, self.height):
            pass
        else:
            self.image = pygame.transform.scale(self.image, (self.wight, self.height))

    def setText(self, text):
        self.image1_or_text0 = False
        self.text = text

    def setGeometry(self, x, y, wight, height):
        self.x = x
        self.y = y
        self.wight = wight
        self.height = height

    def render(self):
        if not self.show1_or_hide0:
            return
        if self.background:
            pygame.draw.rect(self.draw, self.background_color,
                             (self.x, self.y, self.wight, self.height))
        if self.image1_or_text0:
            self.draw.blit(self.image, (self.x, self.y))
        elif self.text:
            if len(self.text) > self.max_len_text:
                self.text = self.text[:self.max_len_text]
            text = self.font.getFont().render(self.text, 1, self.color)
            tmp_x = (len(self.text) // 2) * (self.font.size // 2)
            tmp_y = self.font.size // 2.4
            self.draw.blit(text, (self.x + self.wight // 2 - tmp_x, self.y + self.height // 2 - tmp_y))


class Lineedit:  # Линия которую можно изменять
    def __init__(self, scr):
        self.image1_or_text0 = False
        self.image = ''
        self.draw = scr
        self.color = (0, 0, 0)
        self.x = 0
        self.y = 0
        self.wight = 0
        self.height = 0
        self.border = False
        self.size_border = 1
        self.enabler = True
        self.color_border = (0, 0, 0)
        self.text = ""
        self.background = False
        self.color_background = (255, 255, 255)
        self.show1_or_hide0 = True
        self.font = Font()
        self.click = ''
        self.target = False
        self.max_len = 10000
        self.text_placeholder_bool = False
        self.text_placeholder = ""
        self.align = "right"
        self.hash = False

    def show(self):
        self.show1_or_hide0 = True

    def hide(self):
        self.show1_or_hide0 = False

    def getFont(self):
        return self.font

    def setTarget(self, target):
        self.target = target

    def changeFont(self, font):
        self.font = font

    def setColor(self, color):
        self.color = color

    def setEnabler(self, enabler):
        self.enabler = enabler

    def setPlaceholder(self, text):
        self.text_placeholder_bool = True
        self.text_placeholder = text

    def setText(self, text):
        self.text = text

    def setBorder(self, border):
        self.border = border

    def setColorBorder(self, color):
        self.color_border = color

    def setMaxlen(self, max_len):
        self.max_len = max_len

    def setHash(self, bol):
        self.hash = bol

    def setGeometry(self, x, y, wight, height):
        self.x = x
        self.y = y
        self.wight = wight
        self.height = height

    def setBackGround(self, bol=True):
        self.background = bol

    def setBackgroundColor(self, color):
        self.color_background = color

    def clicked(self):
        self.target = True

    def setAlign(self, side):  # можно будет добавить по высоте
        self.align = side

    def add_special_characters(self, event):
        i = self
        if event.key == 8:
            if i.target:
                if bool(i.text):
                    i.text = i.text[:-1]
            return

    def add_text(self, text):
        i = self
        if i.target:
            if text not in "^" and len(i.text) < i.max_len:
                i.text = i.text + text

    def check_click(self, pos):
        i = self
        if i.x < pos[0] < i.x + i.wight and i.y < pos[1] < i.y + i.height:
            i.clicked()
        else:
            i.setTarget(False)

    def render(self):
        if self.background:
            pygame.draw.rect(self.draw, self.color_background,
                             (self.x, self.y, self.wight, self.height))
        if self.text_placeholder_bool and not self.text:
            text_ren = self.text_placeholder
        else:
            text_ren = self.text

            if self.hash:
                tmp = (len(text_ren) - 1) * "*"
                text_ren = tmp + text_ren[-1]

        if self.align == "center":
            text = self.font.getFont().render(text_ren, 1, self.color)
            tmp_x = self.wight // 2 - (len(text_ren) // 2) * (self.font.size // 2)
            tmp_y = self.font.size // 2.4
        elif self.align == "left":
            text = self.font.getFont().render(text_ren, 1, self.color)
            tmp_x = self.wight - len(text_ren) * (self.font.size // 2.3) - 3
            tmp_y = self.font.size // 2.4
        elif self.align == "right":
            text = self.font.getFont().render(text_ren, 1, self.color)
            tmp_x = 2
            tmp_y = self.font.size // 2.4
        else:
            print("help: align has attributes 'left', 'right', 'center'")
            raise ValueError
        self.draw.blit(text, (self.x + tmp_x, self.y + tmp_y))
        if self.border:
            pygame.draw.rect(self.draw, self.color_border,
                             (self.x, self.y, self.wight, self.height), width=self.size_border)


class Font:  # Изменяет шрифт
    def __init__(self):
        self.size = 16
        self.family = None

    def setPointSize(self, size):
        self.size = size

    def setFamily(self, family):
        self.family = family

    def getFont(self):
        return pygame.font.Font(self.family, self.size)


class Hover(PushButton):  # подсвечивает кнопку
    def __init__(self, other):
        self.image1_or_text0 = other.image1_or_text0
        self.image = other.image
        self.draw = other.draw
        self.color = other.color
        self.x = other.x
        self.y = other.y
        self.wight = other.wight
        self.height = other.height
        self.border = other.border
        self.size_border = other.size_border
        self.enabler = other.enabler
        self.color_border = other.color_border
        self.text = other.text
        self.background = other.background
        self.color_background = other.color_background
        self.show1_or_hide0 = other.show1_or_hide0
        self.font = other.font


def Title_work():
    global running
    running = True
    exitt = False
    pygame.init()
    pygame.display.set_caption('Загрузка')
    request = Request()
    size = request.get_request("mini_win", tup=True)


    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    color_back = request.get_request("background", color=True)
    pprint(color_back)
    screen.fill(color_back)
    list_line_edit = list()
    list_all = list()
    list_button = list()

    hello = Label(screen)
    hello.setGeometry(50, 10, 250, 30)
    hello.setColor(request.get_request("text", color=True))
    hello.setText(LANGUAGE("hello"))
    hello.font.setPointSize(30)
    list_all.append(hello)

    login = Lineedit(screen)
    login.setGeometry(10, 50, 250, 30)
    login.setBackGround(True)
    login.setColor(request.get_request("nav_text", color=True))
    login.setBorder(True)
    login.setBackgroundColor(request.get_request("navigation", color=True))
    login.setColorBorder((0, 0, 0))
    login.setAlign("right")
    login.font.setPointSize(20)
    login.setMaxlen(26)
    login.setPlaceholder(LANGUAGE("login"))
    list_line_edit.append(login)
    list_all.append(login)

    password = Lineedit(screen)
    password.setGeometry(10, 100, 250, 30)
    password.setBackGround(True)
    password.setColor(request.get_request("nav_text", color=True))
    password.setBorder(True)
    password.setBackgroundColor(request.get_request("navigation", color=True))
    password.setColorBorder((0, 0, 0))
    password.setAlign("right")
    password.font.setPointSize(20)
    password.setHash(True)
    password.setMaxlen(26)
    password.setPlaceholder(LANGUAGE("password"))
    list_line_edit.append(password)
    list_all.append(password)

    def work():
        global running
        if bool(login.text) and bool(password.text):
            request.change_base("user_login", login.text)
            request.change_base("user_password", password.text)
            request.change_base("user", "1")
            running = False

    send = PushButton(screen)
    send.setGeometry(10, 150, 100, 25)
    send.setClick(work)
    send.setText(LANGUAGE("sing"))
    send.setBackGround(True)
    send.setBackgroundColor(request.get_request("navigation", color=True))
    send.setColor(request.get_request("nav_text", color=True))
    send.setBorder(True)
    send.setColorBorder((0, 0, 0))
    list_button.append(send)
    list_all.append(send)

    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exitt = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in list_button:
                    i.check_click(event.pos)
                for i in list_line_edit:
                    i.check_click(event.pos)
            if event.type == pygame.KEYDOWN:
                for i in list_line_edit:
                    i.add_special_characters(event)
            if event.type == pygame.TEXTINPUT:
                for i in list_line_edit:
                    i.add_text(event.text)
        screen.fill(color_back)
        for i in list_all:
            i.render()
        pygame.display.flip()
    pygame.quit()
    return exitt


running = True
all_sprites = 0

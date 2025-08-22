# Pygame нтенсив
Это материал для интенсива по разработке игры Flappy Bird на языке Python с помощью библиотеки Pygame.

Материал разбит на части, последовательно повествующие о том, как работают игры и как реализовать конкретную игру 
на языке программирвоания Питон с использованием библиотеки Pygame.

## Часть 1. Базовые принципы работы игр
Чтобы сделать любую игру, необходимы:

1. **Возможность рисовать и обновлять изображение**, ведь игрок видит перед собой как раз изображение,
которое постоянно обновляется. При этом сам игрок может влиять на то, что происходит на экране
с помощью устройств ввода (клавиатура, мышь, джойстик).
Игра отличается от обычного фильма тем, что игрок влияет на изображение. Если на изображения
нельзя влиять, то это фильм.

2. **Игровая логика**, которая определяет что и где нужно рисовать на экране. То, что увидит игрок на экране,
будет зависеть от многих условий, например от:
   - ввода от игрока
   - ввода от других игроков (для многопользовательских игр)
   - логики поведения врагов
   - таймеров и временных отрезков и т.д.

Эти два требования являются основой любой игры и должны взаимодействовать, чтобы картинка реагировала на действия игрока:
нажали кнопку - игрок переместился, отпустили - игрок встал и не двигается.

Питон сам по себе не умеет рисовать изображения и показывать их нам
(в базе доступен только print и вывод в консоль).
Так же в базе питон не умеет получать ввод от пользователя без приостановки программы (ввод "на лету"),
который нужен для быстрого реагирования на действия пользователя - есть только input, 
который приостанавливает выполнение программы до ввода данных пользователем.

Поэтому нам нужна одина из библиотек, расширяющих возможнсть языка, например Pygame, Pyglet или Arcade.

Мы будем использовать **Pygame**, потому что она популярная и потому что у нас такой мастер-класс.

А ещё Pygame простой.

## Часть 2. Подключение и запуск Pygame

Установка Pygame через терминал:

```Bash
pip install pygame
```

Чтобы инициализировать (подготовить к работе) библиотеку Pygame, нужно просто написать команду для этого,
предварительньно подключив (import) библиотеку:
```Python
import pygame

pygame.init()  # Инициализация Pygame
```
_______
Весь механизм работы с Pygame можно свести к алгоритму:

1. Инициализация Pygame - pygame.init()
2. Отображение холста*
3. Игровой цикл
    * рисование изображения на холсте
    * обработка событий (клавиатура, мышь)
    * обновление холста
4. Деинициализация Pyagme - pygame.quit()


    * Холст - поверхность для отображения
_______

Основная концепция Pygame - **холст** (поверхность для отображения), на котором мы можем рисовать изображение.

Холст имеет ширину (**width**) и высоту (**height**)

Игровой цикл позволяет создать **динамическую смену** изображений на холсте и не закрыть его.

Так же в игровом цикле происходит реализация игровой логики и обновление изображения в соответствии с ней.

Например, игрок совершает действия (нажатия клавиши, движение мыши или нажатие её кнопки). Эти действия попадают в 
цикл обработки событий, который их обрабатывает (сам цикл обработки событий находитс внутри игрового цикла).
После обработки событий выплоняются команды на отрисовку изображений, которые связаны с этими событиями (нажал прыжок - 
картинка игрока начала движение вверх).

В конце игрового цикла, перед выходом на новую итерацию, происходит отрисовка всего кадра.

### Немного практики
Код ниже создаст окно размером 450 на 800 пикселя (для fhd мониторов) и отобразит его (для 2к мониторов можно сделать 576 на 1024 пикселя).
```Python
import pygame

pygame.init()
screen = pygame.display.set_mode((450, 800))

while True:
    # изображение игрока
    # фоновое изображение
    pygame.display.update()  # Выводит на экран всё, что было нарисовано в цикле
```

Просто так, нажатием на крестик, окно закрыть не получится, потому что программа не знает как реагировать на нажатие
крестика на окошке.

Чтобы научить программу реагировать на нажатие крестика, добавим обработчик событий:

```Python
import pygame

pygame.init()
screen = pygame.display.set_mode((450, 800))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()  # Выводит на экран всё, что было нарисовано в цикле
```

Теперь окно закрывается, но программа завершается с ошибкой, потому что при выходе из программы по pygame.quit() цикл
не успевает завершиться полностью. Чтобы завершить цикл, понадобится библиотека sys (даёт доступ к системным функциям):

```Python
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((450, 800))  # 576, 1024

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()  # Выводит на экран всё, что было нарисовано в цикле
```
При запуске этого кода в окне Pygame мы увидим сплошное черное изображение, которое никак не менется, как нам кажется.
На самом деле Pygame рисует это изображение постоянно, много раз в секунду (количество раз неизвестно).

Чтобы контролировать это количество раз (что важно для видеоигр), нужно определить
частоту кадров - FPS.

    FPS (Frames Per Second) - количество кадров (картинок, фреймов), рисуемых на холсте за одну секунду.

Количество кадров напрямую влияет на то, насколько быстро (и плавно) работает игра:
* если FPS равен 100 (ста) кадрам (сто обновлений холста в секунду) и игра двигает изображение игрока на 5 пикселей вправо каждый кадр, то игрок переместится на 500 пикселей вправо за секунду.
* если же FPS равен 10 и игра двигает изображение игрока на 5 пикселей вправо каждый кадр, то игрок переместится на 50 пикселей вправо за секунду.

Контролировать FPS можно с помощью специального объекта PyGame - **pygame.time.Clock()**

```Python
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((450, 800))
clock = pygame.time.Clock()  # таймер для отсчитывания кадров

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(120)  # 120 - указанная нами частота обновления холста (FPS)
```
## Часть 3. Вывод изображений
Два типа поверхностей Images (изображения) и Surfaces (поверхности).
Поверхностей 2 типа:
Display surface - поверхность экрана
Reguls surface - обычная поверхность

По умолчанию отображается только экранная поверхность. Обычные поверхности
сами по себе не отображаются, пока вы их специально не поместите на экранную поверзность.
Поверхность - это, по сути, слой.

### Немного практики

Чтобы использовать готовые изображения, их нужно импортировать в код.
Каждое новое изображение будет размещаться на новой поверхности.
Эта поверхность (как и экран) хранится в отдельной переменной.

Метод blit(что_размещаем, где_размещаем) позволяет поместить одну поверхность на другую
что_размещаем - загруженное изображение
где_размещаем - кортеж с координатами

```Python
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((450, 800))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('sprites/background-day.png')  # импорт изображения, которое нужно отобразить на экране

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))  # размещаем на экране изображение в координате x: 0, y: 0

    pygame.display.update()
    clock.tick(120)
```
Точка отсчета координат холста (screen) находится в верхнем левом углу.
Так же и у изображения: мы работаем с верхним левым углом.
___
#### Эксперимент
Попробуйте поменять значения координат в методе **screen.blit** \
в строке с кодом **screen.blit(bg_surface, (0, 0))** на следующие:
1. 300, 0
2. 0, 200
3. 100, 200

Что произошло с фоновым изображением? Почему?
___

Сейчас фоновое изображение меньше чем экран, но его можно увеличить с помощью методов преобразования изображений.

Воспользуемся методом **transform.scale(surface, (new_width, new_height))**, который принимает на вход исходное
изображение для преобразования (**surface**) и размер, до которого его нужно преобразовать - **(new_width, new_height)**.

Так же добавим метод **convert()** загружаемому \
изображению - **pygame.image.load('sprites/background-day.png').convert()**. Он позволит преобразовать изображение в формат, с которым 
работает Pygame. Такое преобразование не обязательно, но оно позволяет ускорить
загрузку и работу игры, особенно в случае, когда на экран необходимо вывести много изображений.

```Python
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((450, 800))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('sprites/background-day.png').convert()  # добавляем преобразование изображения
bg_surface = pygame.transform.scale(bg_surface, (450, 800))  # Делаем фоновое изображение по размеру экрана

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))

    pygame.display.update()
    clock.tick(120)
```
## Часть 4. Создание анимации
### 4.1. Двигаем землю

> <p align=right>«Дайте мне точку опоры, и я переверну Землю»<br> Архимед</p>

В оригинальной игре Flappy Bird есть земля (пол), которая постоянно движется справа-налево.
В этой части будем создавать такую землю и сделаем так, чтобы она постоянно двигалась.

Для начала импортируем изображение земли и преобразуем его. Преобразование нужно, чтобы
ширина изображения стала соответствовать ширине экрана, в котором отображается игра.

Для этого в методе **pygame.transform.scale()** для изображения землы мы просто указываем такую же ширину,
как и у холста (**screen = pygame.display.set_mode((450, 800))**), а высоту либо вычисляем по формуле

x = [(wn : w) * h], где

      x - искомая высота
      wn - новая ширина масштабируемого изображения (в нашем случае равна 450 пикселей)
      w - исходная ширина масштабируемого изображения (ширина исходного изобажения 336 пикселей)
      h - исходная высота масштабируемого изображения (высота исходного изобажения 112 пикселей)
      [] - означают, что берется целая часть результата, а дробная отбрасывается

либо воспользуемся калькулятором соотношения сторон, который можно найти в интернете.

```Python
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((450, 800))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('sprites/background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (450, 800))

floor_surface = pygame.image.load('sprites/base.png').convert()  # импорт изображения земли
floor_surface = pygame.transform.scale(floor_surface,(450, 150))  # подгоняем ширину под холст (и высоту)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))
    screen.blit(floor_surface, (0, 650))  # Отобразим землю в нужном месте холста

    pygame.display.update()
    clock.tick(120)
```
Чтобы отобразить картинку земли в нужном месте экрана, её необходимо опустить по оси y на величину,
равную разности высоты экрана (screen) и высоты изображения земли (floor_surface): 800 - 150 = 650.
### Немного практики
Добавим земле движение. Для этого необходимо сделать так, чтобы каждый следующий кадр картинка земли немного сдвигалась
по горизонтали относительно своей позиции на предыдущем кадре. Для этого заменим значение, определяющее положение картинки
по оси X на перменную **floor_x_pos** и создадим эту переменную. Теперь достаточно менять значение переменно **floor_x_pos** на
некоторую величину, например на единицу (1), каждый кадр и земля придёт в движение:

```Python
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((450, 800))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('sprites/background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (450, 800))

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface,(450, 150))

floor_x_pos = 0  # Переменная для хранения положения по оси х

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))
    screen.blit(floor_surface, (floor_x_pos, 650))  # меняем число на переменную
    floor_x_pos += 1  # Сдвигаем изображение по оси х на 1 пиксель каждый кадр

    pygame.display.update()
    clock.tick(120)
```
___
#### Эксперимент
1. Поменяйте оператор **+=** в строке **floor_x_pos += 1** на оператор **-=**.\
Что произошло с землёй? Почему?
2. Измените значение FPS в строке **clock.tick(120)** со 120 на 1, а значение перемнной
**floor_x_pos** в строке **floor_x_pos -= 1** на 50 или 100 (**floor_x_pos -= 50**).\
Как теперь стала двигаться земля? Почему?
3. Верните значение 1 переменной floor_x_pos значение, а FPS установите обратно в 120.
```Python
# После эксперимента участок кода, над которым мы работали, должен выглядеть так:
...
screen.blit(floor_surface, (floor_x_pos, 650))
    floor_x_pos -= 1  # Тут 1

    pygame.display.update()
    clock.tick(120)  # Тут 120
```
___
Проблема в том, что земля "уходит из-под ног": изорбажение сдвигается справа налево (после замены += 1 на -= 1) и через
некоторое количество кадров исчезает с экрана.

Чтобы решить эту проблему, необходимо добавить втрое изображение земли,
которое будет смещено вправо на ширину экрана и изначально будет выходить за его пределы.
Кроме того, первое изображение, которое изначально видно на экране, после выхода за передлы экрана влево необходимо будет возвращать
обратно в изначальное положение, а второе - снова сдвигать вправо за пределы экрана.

Таким образом мы сделаем "поезд" из двух изображений, которые будут менять друг-друга при 
движении.
**Тут добаить картинки, иллюстрирующие происходящее**

```Python
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((450, 800))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('sprites/background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (450, 800))

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface,(450, 150))

floor_x_pos = 0  # Переменная для хранения положения по оси х

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))
    screen.blit(floor_surface, (floor_x_pos, 650))  # Тут рисуем видимую на экране часть земли
    screen.blit(floor_surface, (floor_x_pos + 450, 650))  # А тут - часть земли, сдвинутую вправо за грацины экрана
                                                          # по оси х на значение, равное ширине экрана (450)
    floor_x_pos -= 1
    
    if floor_x_pos <= -450:  # Если видимое изображение вышло за грницы экрана влево (x = -450), 
        floor_x_pos = 0  # возвращаем его обратно (x = 0)

    pygame.display.update()
    clock.tick(120)

```
Чтобы код основной программы не разрастался, вынесем действия, создающие иллюзию движения земли, в отдельную функцию **draw_floor()**, 
которую будем вызывать из основного кода:

```Python
import pygame, sys


def draw_floor():  # Создаём функцию отображения двух изображений земли
    screen.blit(floor_surface, (floor_x_pos, 650))
    screen.blit(floor_surface, (floor_x_pos + 450, 650))


pygame.init()
screen = pygame.display.set_mode((450, 800))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('sprites/background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (450, 800))

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface,(450, 150))

floor_x_pos = 0  # Переменная для хранения положения по оси х

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))
    draw_floor()  # Взываем функцию - рисуем землю
    floor_x_pos -= 1  # Двигаем обе картинки справа-налево...
    
    if floor_x_pos <= -450:
        floor_x_pos = 0  #...и возвращаем их обратно, когда первая картинка выйдёт
                         # за границы экрана

    pygame.display.update()
    clock.tick(120)
```

### 4.2. Кое-что о птичках
>― Крылья, крылья. Ноги!<br>
>― Ноги, крылья. Главное - хвост!<br>
> <p align=right>«Крылья, ноги и хвосты»</p>

Чтобы создать птицу, необходимо проделть те жедействия, которые мы делали изоражениями фона и земли, т.е. загрузить изображение птицы,
сконвертировать его в формат Pygame, увеличить (отмастабировать) и создать поверхность (surface).

Логика поведения птицы имеет несколько нюансов, которые отличают её от других изображений:
1. Изображения тпицы необходимо вращать относительно центра, а не верхнего левого угла.
2. Птица должна уметь сталкиваться со столбами, пожтому нам необходимо эти столкновения отслеживать.
3. На птицу должна действовать гравитация: тянуть её вниз.

Простые поверхности (surface) не позволяют выполнить логику, описанную выше, поэтому нам понадобится
новый объект из недр Pygame - объект **Rect** или прямоугольная поверхность.

**Rect** позволяет менять центр, относительно которого перемещается изображение и отслеживать столкновения с дргуми подобными объектами.
С помощью него можно задать следубщие точки на изображении:
1. Точки левой границы: topleft, midleft, bottomleft
2. Точки средней линии: midtop, center, midbottom
3. Точки правой границы: topright, midright, bottomright

Для создания объекат типа Rect, или прямоугольного объекта, можно использовать метод get_rect() повехности (surface):
```Python
surface.get_rect()
```

### Немного практики
Создадим изображение птицы, преобразуем его в прямоуглоьный объект и отобразим на экране:
```Python
import pygame, sys


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 650))
    screen.blit(floor_surface, (floor_x_pos + 450, 650))


pygame.init()
screen = pygame.display.set_mode((450, 800))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('sprites/background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (450, 800))

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface,(450, 150))
floor_x_pos = 0

bird_surface = pygame.image.load('sprites/bluebird-midflap.png').convert()  # Загружаем птичку
bird_surface = pygame.transform.scale2x(bird_surface)  # Увеличиваем её в 2 раза
bird_rect = bird_surface.get_rect(center=(100, 400))  # Размещаем центр птички в точке 100, 400.

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))
    screen.blit(bird_surface, bird_rect)  # отображаем прямоугольный объект птички

    draw_floor()
    floor_x_pos -= 1

    if floor_x_pos <= -450:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
```
**_TODO:_** Расписать подробнее внесённый в код строки

#### Воздействие гравитации
У прямоугольного объекта, кроме названных выше точек, есть ещё и другие точки: left, right, top и bottom, а центральная точка 
имеет свойства centerx и entery, которые модно использовать для движения объекта.

**_TODO_**: тут картинка с обозначениями дополнительных точек.

Чтобы сдвинуть прямоугольный объект птицы, воспользуемся свойством centery, которое перемещает объект
вдоль оси y, т.е.по вертикали. Так же создадим несколько вспомогательных переменных:
1. **gravity** - для хранения значения гравитации,
2. **bird_movement** - для хранения значения, ~~показывающего направление движения птицы~~ (вверх или вниз).
```Python
import pygame, sys


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 650))
    screen.blit(floor_surface, (floor_x_pos + 450, 650))


pygame.init()
screen = pygame.display.set_mode((450, 800))
clock = pygame.time.Clock()

# Game variables - так отмечается раздел, отмеченный комментарием
gravity = 0.25  # Значение гравитации - не имеет ничего общего с реальным миром, просто красивое число
bird_movement = 0  # Переменная для управления направлением птицы (вверх или вниз)

bg_surface = pygame.image.load('sprites/background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (450, 800))

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface,(450, 150))
floor_x_pos = 0

bird_surface = pygame.image.load('sprites/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center=(100, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))

    bird_movement += gravity  # Добавляем гравитацию на каждом кадре
    bird_rect.centery += bird_movement  # Перемещаем прямоугольник

    screen.blit(bird_surface, bird_rect)
    draw_floor()
    floor_x_pos -= 1

    if floor_x_pos <= -450:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)

```
Пока что птичка падает вниз за пределы экрана и исчезает. Поможем ей взлететь.

Для этого нам понадобится обработать ввод с клавиатуры, ведь птичка должна взлетать
только в тот момент, когда игрок нажимает клавишу. Мы будем программировать клавишу пробел.

При нажатии клавиши пробел:
1. Останавливаем падение птички, т.е. обнуляем воздействие гравитации установкой \
значения переменной **bird_movement** в 0, т.е. убираем из переменной всю "накопившуюся" гравитацию.
2. Подбрасываем её вверх уменьшением текущего значения координаты y на небольшое значение,
   например так: **bird_movement -= 5**.

> В системе координат Pygame движение вверх это **"-"**, а не **"+"**!

Чтобы запрограммировать нажатие клавиши, допишем следующий код в цикл обработки событий:
```Python
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_SPACE:
        # ... тут код "подбрасывания" птички
```
Данный код можно прочитать так: если была нажата клавиша (какая-то) и если это клавиша - Пробел,
то подбрасываем птичку вверх на небольшое количество пикселей.

```Python
import pygame, sys


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 650))
    screen.blit(floor_surface, (floor_x_pos + 450, 650))


pygame.init()
screen = pygame.display.set_mode((450, 800))
clock = pygame.time.Clock()

# Game variables
gravity = 0.25
bird_movement = 0

bg_surface = pygame.image.load('sprites/background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (450, 800))

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface,(450, 150))
floor_x_pos = 0

bird_surface = pygame.image.load('sprites/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center=(100, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  # Нажата ли клавиша
            if event.key == pygame.K_SPACE:  # Если нажатая клавиша - пробел
                bird_movement = 0  # Останавливаем движение птички
                bird_movement -= 5  # переносив её центр вверх на 5 пикселей

    screen.blit(bg_surface, (0, 0))

    bird_movement += gravity
    bird_rect.centery += bird_movement

    screen.blit(bird_surface, bird_rect)
    draw_floor()
    floor_x_pos -= 1

    if floor_x_pos <= -450:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)

```

### 4.3.0 Огонь, вода и медные трубы
#### (Не) очень много теории.
На данном этапе реализованы земля и птичка. Пора сделать трубы. Задача усложняется тем, что трубы должны создаваться в течение длительного времени,
пока игрок не допускает ошибок в игре, а ещё они должны располагаться по верху и низу экрана и меть разную высоту, причём такую,
чтобы птичка могла пролететь между зазором.

Поверность (surface) трубы будем создавать привычным способом с помощью загрузки изображения и его конвертирования:
```Python
pipe_surface = pygame.image.load('sprites/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
```
Настоящие трубы хранятся на складе, а мы будем хранить все трубы в списке:
```Python
pipe_list = []
```
Список позволяет перебирать его содержимое в цикле, поэтому мы сможем обратиться к каждой трубе в списке труб и сдвинуть их все в нужном направлении.

Но вот вопрос: необходимо ли сразу заполнить список трубами, а потом выводить их на экран и передвигать или заполнять список постепенно, доьавляя в него
каждую новую трубу по мере её появления на экране?

В первом случае мы должны быть уверены в том, что тех труб, которые будут созданы заранее, хватит игроку для завершения игры. Иными
словами мы должны быть уверены в том, что трубы не закончатся раньше, чем игрок проиграет.

Предсказать то, каким образом сложится игра для каждого конкретного игрока невозможно, поэтому выберем второй вариант: создавать трубы по мере их
необходимости.

Настоящие трубы производят на заводе, а мы будем создавать трубы с помощью функции*:
```Python
def create_pipe():
    new_pipe = pipe_surface.get_rect(midtop = (600, 400))
    return new_pipe
```
    * Данная функция возвращает (return) прямоугольный объект трубы, создаваемый на основе
    поверхности (surface) изображения трубы.

Для передвижения созданной трубы в методе **get_rect** определяется midtop (верхняя посередине *) точка с координатами 600
пикселей по оси **х** и 400 по оси **у**. Такие координаты указаны для того, чтобы труба появлялась за пределами правой границы экрана.

    * Так что перетаскивать трубы мы будем за хохолок (за верхушечку)
 
С помощью функции, создающей трубы, мы будем наполнять список **pipe_list** в игровом цикле.

> «Арр! Пусть всегда дым из твоей трубы валит, а лось никогда не покидает твой склад со слезой на глазах!»
> <p align="right"> Ральф против интернета</p>

Трубы, добавялемые в список, не отображаются на экране. Кроме того они не двигаются. Поэтому создадим две вспомогательные функции
для устранения этого недоразумения. Первая функция будет перемещать трубы из списка, вторая - рисовать их.

Функция для перемещения труб будет принимать текущий список труб в качестве параметра, обходить его в цикле и сдвигать каждую трубу
справа налево, т.е. изменять значение координаты x в отрицательную сторону. После обхода списка, функция возвращает список труб, в котором
у каждой трубы изменится координата х:

```Python
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5;
    return pipes
```
Функция для рисования труб на экране будет так же принимать список с трубами, которые необходимо нарисовать. В отличие от предыдущей функции,
эта возвращать ничего не будет (ну разве что кроме none):

```Python
def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)
```
#### Сколько вешать в граммах?
Создав функции **create_pipe()**, **move_pipes()** и **draw_pipes()** можем открывать завод по их производству, т.е. внедрять в игру, но стоп. А 
сколько требуется этих труб и с какой частотой они дожны появляться на экране?

Здравый смысл подсказывает, что если мы будем рисовать по одной трубе
каждый кадр мы будем получать 120 труб в секунду при текущем значении FPS, а это много. Очень много.

К счастью в Pyagme существует механизм, позволяющий запускать код с определенным интервалом. Называется от User events (Ползовательские события).

User event — это пользовательское (своё) событие, которое позволяет:
- Посылать сигналы между частями кода через обычный цикл событий.
- Делать таймеры (повторяющиеся действия).
- Генерировать события при асинхронных действиях.

Появление труб - это повторяющееся действие, потому что трубы появляются с определенной периодичностью.
Создадим своё событие:
```Python
SPAWNPIPE = pygame.USEREVENT
```
укажим периодичность его плявления:
```Python
pygame.time.set_timer(SPAWNPIPE, 1200)
```
и будем запускать в цикле обработки событий раз во временной промежуток, указанный в set_timer:
```Python
if event.type == SPAWNPIPE:
   pipe_list.append(create_pipe())
```
Теперь каждые 1200 милисекунд в списке будет повляться новая труба. для движения и отобажения труб в списке воспользуемся функциями 
**move_pipes()** и **draw_pipes()**, которые ниже кода, рисующего птичку:

```Python
# Bird
bird_movement += gravity
bird_rect.centery += bird_movement
screen.blit(bird_surface, bird_rect)

# Pipes
pipe_list = move_pipes(pipe_list)
draw_pipes(pipe_list)
```
### Практика
1. Дополните имеющийся код фрагментами нового кода, опираясь на полный код, написанный ниже.
2. Расставьте блочные комментарии (# Birdб # Pipes и т.д.). поясняющие комментарии из кода ниже писать не нужно.
3. Запустите код после завершения работы.
TODO: Написать поясняющие комментарии.
```Python
import pygame, sys


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 650))
    screen.blit(floor_surface, (floor_x_pos + 450, 650))


def create_pipe():
    new_pipe = pipe_surface.get_rect(midtop = (600, 400))
    return new_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5;
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)


pygame.init()
screen = pygame.display.set_mode((450, 800))
clock = pygame.time.Clock()

# Game variables
gravity = 0.25
bird_movement = 0

bg_surface = pygame.image.load('sprites/background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (450, 800))

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface,(450, 150))
floor_x_pos = 0

bird_surface = pygame.image.load('sprites/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center=(100, 400))

# Трубы
pipe_surface = pygame.image.load('sprites/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 5
        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())

    screen.blit(bg_surface, (0, 0))

    # Bird
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)

    # Pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # Floor
    draw_floor()
    floor_x_pos -= 1

    if floor_x_pos <= -450:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
```
#### Добавляем верхнюю трубу
Случайная высота труб
```Python
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    new_pipe = pipe_surface.get_rect(midtop=(600, random_pipe_pos))
    return new_pipe

#...

# Трубы
...
pipe_height = [300, 400, 500]

```
Трубы сверху

```Python
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(600, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(600, random_pipe_pos - 300))
    return bottom_pipe, top_pipe

#...

while True:
        # ...
            pipe_list.extend(create_pipe())

```
Переворачиваем верхнюю трубу

```Python
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 800:
            screen.blit(pipe_surface, pipe)  
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, flip_x=False, flip_y=True)
            screen.blit(flip_pipe, pipe)
```

#### Столкновения
Для проверки столкновения между прямоугольниками используется метод rect1.**colliderect(rect2)**. Возвращает 
True при столкновении или false, если такого не было.
```Python
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            print('collision')
#...
    
# Bird
    # ...
    screen.blit(bird_surface, bird_rect)
    check_collision(pipe_list)  # Используем функцию

```
#### Проверка выхода за пределы экрана и остановка игры

Допишем функцию

```Python
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 800:
        return False

    return True
```
и добавим логику в игровой цикл
```Python
# ...
# Game variables
gravity = 0.25
bird_movement = 0
game_active = True  # !!!

#...

while True:
    #...

    screen.blit(bg_surface, (0, 0))

    if game_active:
        # Bird
        # ...
        screen.blit(bird_surface, bird_rect)
        game_active = check_collision(pipe_list)

        # Pipes
        # ...

```
#### Перезапуск игры после столкновения
Работаем в цикле событий
```Python
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:   # Делаем, если пробел и игра активна
                # ...

            if event.key == pygame.K_SPACE and not game_active:   # Делаем, если пробел и игра завершена
                pipe_list.clear()  # Очищаем список труб
                bird_rect.center = (100, 400)  # Возвращаем птицу в стартовую точку
                bird_movement = 0  # Сбрасываем движение
                game_active = True  # Перезапускаем игру

        if event.type == SPAWNPIPE:
            # ...
        # ...
```
#### Вращенеи и анимация птицы
При вращении в Pygame изображение теряет качество, но это не страшно, если сделать вращение один раз.
2 поверхности: оригинальная и повёрнутая.

Импортируем новую поверхность птицы
Поворачиваем
выводим её на экран

```Python
def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird

# ...

#...
bird_surface = pygame.image.load('sprites/bluebird-midflap.png').convert_alpha()  # Убираем черный квадрат под спрайтом
#...

# Bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)  # Создаём птицу с поворотом

        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)  # Отображаем птицу с поворотом
        game_active = check_collision(pipe_list)
        #...

```
#### Анимация крыльев


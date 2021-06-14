#!/usr/bin/python3 //ссылка на интерпритатор python3;
import time //подключение модуля для работы со временем;
import os //подключение модуля для работы с операционной системой;


from gpiozero import LED //импорт атрибута светодиода из модуля gpiozero;
from watchdog.observers import Observer //импорт атрибута обозревателя из модуля watchdog;
from watchdog.events import * //импорт всего из библиотеки watchdog.events;


led = LED(21) // объявление переменной для светодиода;
ACT_EVENTS = [DirDeletedEvent, DirMovedEvent, FileDeletedEvent, FileModifiedEvent, FileMovedEvent] //переменная, обозначающая, при каких событиях реагировать (удаление, перемещение директорий; удаление, изменение, перемещение файлов )


class DirtyHandler(FileSystemEventHandler): //объявление класса
def __init__(self): //объявление перегруженного метода.

self.reset() // определение функции метода.

def on_any_event(self, event): //объявление метода, сканирующего изменения.

if type(event) in ACT_EVENTS: //если произошло событие из ранее объявленных

self._dirty = True //установка переменной в состояние true

self._dirty_time = time.time() //установка текущего времени в переменную 



@property //декоратор 

def dirty(self): //объявление метода 

return self._dirty //определение функции метода



@property //декоратор

def dirty_time(self): //объявление метода 

return self._dirty_time //определение функции метода 



def reset(self): //объявление метода

self._dirty = False //установка переменной в состояние false 

self._dirty_time = 0 //сброс таймера 

self._path = None 



os.system("modprobe g_mass_storage file=/storageUSB.bin stall=0 ro=0 removable=1”) //монтирование образа USB-device



evh = DirtyHandler() //объявление переменной 

observer = Observer() //объявление переменной 

observer.schedule(evh, path="/mnt/usb_share", recursive=True) //планирование события (класс, путь, рекурсивно)

observer.start() //запуск класса



try:

while True:

while evh.dirty:

time_out = time.time() - evh.dirty_time //установка времени



if time_out >=30: //если вышло 30 секунд 

led.on() //зажигание светодиода
os.system("rclone copy /mnt/usb_share BSTU:rclone_test") //копирование файлов из сетевого хранилища в сетевое.
time.sleep(1) 
os.system("rclone sync BSTU:rclone_test /mnt/usb_share") //монтирование образа USB-device
time.sleep(1)
os.system("modprobe -r g_mass_storage") //размонтирование образа USB-device
time.sleep(1)
os.system(“sync”) //синхронизация данных на диске и данных в памяти
time.sleep(1)
os.system("modprobe g_mass_storage file=/storageUSB.bin stall=0 ro=0 removable=1”) //монтирование образа USB-device
time.sleep(1)
led.off() //выключение светодиода
evh.reset() //сброс класса
time.sleep(1)
except KeyboardInterrupt: //исключение 
observer.stop() //остановка отслеживания 
observer.join() //присоединение 

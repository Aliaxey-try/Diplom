#!/usr/bin/python3 //ссылка на интерпритатор python3;
from gpiozero import LED //импорт атрибута светодиода из модуля gpiozero;
import os //подключение модуля для работы с операционной системой;
led = LED(21) //объявление переменной для светодиода 
led.on() //включение светодиода
os.system("rclone copy /mnt/usb_share BSTU:rclone_test") копирование файлов из локальной папки в сетевое хранилище
os.system("rclone sync BSTU:rclone_test /mnt/usb_share") //синхронизация файлов сетевого хранилища с локальной папкой 
led.off() //выключение светодиода 
exit() //завершение программы 

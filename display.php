<?php //интерпритатор php
$login = $_POST["login"]; //переменная для логина
$password = $_POST["password"]; //переменная для пароля 
echo "Login:<b> ".$login . "</b>". "<br/>Password:<b>" . $password . "</b>"; //вывод на страницу логина и пароля
$fp = fopen('/etc/wpa_supplicant/wpa_supplicant.conf', 'a'); // путь и открытие файла wpa_supplicant.conf в режиме для записи в конец файла
fwrite($fp,"\r\nnetwork={\r\n"); //запись строки
fwrite($fp,"    ssid=\""); //запись строки
fwrite($fp,$login); //запись введенного логина 
fwrite($fp,"\" \r\n"); переход на новую строку
fwrite($fp,"    psk=\""); //запись строки
fwrite($fp,$password); //запись введенного пароля 
fwrite($fp,"\"\r\n"); //переход на новую строку 
fwrite($fp,"    key_mgmt=WPA-PSK.\r\n}"); //запись строки
fclose($fp); //закрытие файла
?> //конец документа

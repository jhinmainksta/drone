Автозапуск ПО
===

> **Note** В версии образа **0.20** пакет и сервис `clever` был переименован в `drone`. Для более ранних версий см. документацию для версии [**0.19**](https://github.com/CopterExpress/drone/blob/v0.19/docs/ru/autolaunch.md).

systemd
---

Основная документация: https://wiki.archlinux.org/index.php/Systemd_(Русский).

Все автоматически стартуемое ПО Клевера запускается в виде systemd-сервиса `drone.service`.

Сервис может быть перезапущен командой `systemctl`:

```bash
sudo systemctl restart drone
```

Текстовый вывод ПО можно просмотреть с помощью команды `journalctl`:

```bash
journalctl -u drone
```

Для того чтобы запустить ПО Клевера непосредственно в текущей консольной сессии, вы можете использовать `roslaunch`:

```bash
sudo systemctl stop drone
roslaunch drone drone.launch
```

Вы можете выключить автозапуск ПО Клевера с помощью команды `disable`:

```bash
sudo systemctl disable drone
```

roslaunch
---

Основная документация: http://wiki.ros.org/roslaunch.

Список объявленных для запуска нод / программ указывается в файле `/home/pi/catkin_ws/src/drone/drone/launch/drone.launch`.

Вы можете добавить собственную ноду в список автозапускаемых. Для этого разместите ваш запускаемый файл (например, `my_program.py`) в каталог `/home/pi/catkin_ws/src/drone/drone`. Затем добавьте запуск вашей ноды в `drone.launch`, например:

```xml
<node name="my_program" pkg="drone" type="my_program.py" output="screen"/>
```

Запускаемый файл должен иметь *permission* на запуск:

```bash
chmod +x my_program.py
```

При использовании скриптовых языков вначале файла должен стоять <a href="https://ru.wikipedia.org/wiki/Шебанг_(Unix)">shebang</a>, например:

```bash
#!/usr/bin/env python3
```

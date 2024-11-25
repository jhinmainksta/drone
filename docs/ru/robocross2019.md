# Робокросс-2019

В июле 2019 команда Коптер Экспресс в 4-й раз подряд одержала победу на ежегодных испытаниях беспилотных транспортных средств "[Робокросс](http://russianrobotics.ru/activities/robokross-2019/)". Испытания проводятся на полигоне ГАЗ под Нижним Новгородом.

Основной задачей испытаний в категории БПЛА было локализовать и уничтожить цель — красный воздушный шар — в автономном режиме.

## Видео

<iframe width="560" height="315" src="https://www.youtube.com/embed/zMh5THdHuX8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Реализация

Команда использовала квадрокоптер на базе рамы F450 и [платформу Клевер](https://github.com/CopterExpress/drone). Полный итоговый исходный код доступен для изучения [на GitHub](https://github.com/CopterExpress/robocross2019/).

Разработанный пакет `robocross2019` разбит на модули: ROS-нодлет `red_dead_detection` распознает красный шар, `balloon.py` реализует высокоуровневую логику полета коптера.

## red_dead_detection

Нодлет `red_dead_detection` обеспечивает обнаружение красного шара на изображении с камеры квадрокоптера, смотрящей вперед (топики `/front_camera/image_raw` и `/front_camera/camera_info`). Используется простейший метод фильтрации изображения по цвету. Затем вычисляется геометрический центр полученных участков и производится компенсация искажений камеры (`cv::undistortPoints`).

Используя известное фокусное расстояние камеры (из топика `camera_info`) вычисляется вектор, направленный в сторону цели. Полученный вектор публикуется в топик `/red_dead_detection/direction`, причем его система координат (`frame_id` связана с расположением передней камеры `front_camera_optical`).

## balloon.py

Для полета к шару используется вектор направления `red_dead_detection/direction`, который используется как setpoint по скорости дрона. Угол по рысканью также устанавливается по направлению к шару. Цель считается уничтоженной, когда на протяжении заданного количества кадров общая площадь участка с красными пикселями меньше определенного порога.

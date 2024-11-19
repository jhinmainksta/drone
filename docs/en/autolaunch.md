Software autorun
===

> **Note** In the image version **0.20** `clever` package and service was renamed to `drone`. See [previous version of the article](https://github.com/CopterExpress/clover/blob/v0.19/docs/en/autolaunch.md) for older images.

systemd
---

Main documentation: https://wiki.archlinux.org/title/Systemd.

All automatically started Drone software is launched as a `drone.service` systemd service.

The service may be restarted by the `systemctl` command:

```(bash)
sudo systemctl restart drone
```

Text output of the software can be viewed using the `journalctl` command:

```(bash)
journalctl -u drone
```

To run Drone software directly in the current console session, you can use the `roslaunch` command:

```(bash)
sudo systemctl restart drone
roslaunch drone drone.launch
```

You can disable Drone software autolaunch using the `disable` command:

```(bash)
sudo systemctl disable drone
```

roslaunch
---

Main documentation: http://wiki.ros.org/roslaunch.

The list of nodes / programs declared for running is specified in file `/home/pi/catkin_ws/src/drone/drone/launch/drone.launch`.

You can add your own node to the list of automatically launched ones. To do this, place your executable file (e.g. `my_program.py`) into folder `/home/pi/catkin_ws/src/drone/drone`. Then add the start of your node to `drone.launch`, for example:

```xml
<node name="my_program" pkg="drone" type="my_program.py" output="screen"/>
```

The started file must have *permission* to run:

```bash
chmod +x my_program.py
```

When scripting languages are used, a <a href="https://en.wikipedia.org/wiki/Shebang_(Unix)">shebang</a> should be placed at the beginning of the file, for example:

```bash
#!/usr/bin/env python3
```

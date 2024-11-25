Pixhawk / Pixracer firmware flashing
===

Pixhawk, Pixracer or [COEX Pix](coex_pix.md) firmware may be flashed using QGroundControl or command line utilities.

Modified firmware for Drone
---

It is advisable to use a specialized build of PX4 with the necessary fixes and better defaults for the Drone drone. Use the latest stable release in our [GitHub repository](https://github.com/CopterExpress/Firmware/releases) with the word `drone`, for example, `v1.8.2-drone.5`.

<div id="release" style="display:none">
<p>Latest stable release: <strong><a id="download-latest-release"></a></strong>.</p>

<ul>
<li>Firmware for COEX Pix and Pixracer (<strong>Drone 4 / Drone 3</strong>) – <a id="firmware-pixracer" href=""><code>px4fmu-v4_default.px4</code></a>.</li>
<li>Firmware for Pixhawk (<strong>Drone 2</strong>) – <a id="firmware-pixhawk" href=""><code>px4fmu-v2_lpe.px4</code></a>.</li>
</ul>
</div>

> **Warning** If you are using the firmware version older than *v1.10* (for example, `v1.8.2-drone.13`), then in order to avoid configuration errors, use [QGroundControl version *v4.2.0*](https://github.com/mavlink/qgroundcontrol/releases/tag/v4.2.0) (or older). See [detailed information](https://docs.px4.io/v1.11/en/config/battery.html#parameter-migration-notes) about changes in the firmware parameters that cause errors in newer versions of QGroundControl.

<script type="text/javascript">
    // get latest release from GitHub
    fetch('https://api.github.com/repos/CopterExpress/Firmware/releases').then(function(res) {
        return res.json();
    }).then(function(data) {
        // look for stable release
        let stable;
        for (let release of data) {
            let drone = (release.name.indexOf('drone') != -1) || (release.name.indexOf('clever') != -1);
            if (drone && !release.prerelease && !release.draft) {
                stable = release;
                break;
            }
        }
        let el = document.querySelector('#download-latest-release');
        el.innerHTML = stable.name;
        el.href = stable.html_url;
        document.querySelector('#release').style.display = 'block';
        for (let asset of stable.assets) {
            console.log(asset.name);
            if (asset.name == 'px4fmu-v4_default.px4') {
                document.querySelector('#firmware-pixracer').href = asset.browser_download_url;
            } else if (asset.name == 'px4fmu-v2_lpe.px4') {
                document.querySelector('#firmware-pixhawk').href = asset.browser_download_url;
            }
        }
    });
</script>

QGroundControl
---

Open the Firmware section in QGroundControl. Then, connect your flight controller via USB.

Choose PX4 Flight Stack. If you wish to install the official firmware (with EKF2 for Pixhawk), choose "Standard version". In order to flash custom firmware, choose "Custom firmware file..." and click OK.

> **Warning** Do not unplug your flight controller from USB during flashing!

Firmware variants
---

The name of the firmware file contains information about the target flight controller and build variant. For example:

* `px4fmu-v4_default.px4` — firmware for COEX Pix and Pixracer with EKF2 and LPE (**Drone 3** / **Drone 4**).
* `px4fmu-v2_lpe.px4` — firmware for Pixhawk with LPE (**Drone 2**).
* `px4fmu-v2_default.px4` — firmware for Pixhawk with EKF2.
* `px4fmu-v3_default.px4` — firmware for newer Pixhawk versions (rev. 3 chip, see Fig. + Bootloader v5) with EKF2 and LPE.

![STM revision](../assets/stmrev.jpg)

> **Note** In order to flash the `px4fmu-v3_default.px4` file, you may need to use the `force_upload` command in the command prompt.

Command prompt
---

PX4 may be compiled from the source and automatically flashed to the flight controller from the command prompt.

To do this, clone the PX4 repository:

```bash
git clone https://github.com/PX4/PX4-Autopilot.git
```

Select the appropriate version (tag) using `git checkout`. Then compile and upload the firmware:

```bash
make px4_fmu-v4_default upload
```

Where `px4_fmu-v4_default` is the required firmware variant.

In order to upload the `v3` firmware to Pixhawk, you may need to use the `force_upload` option:

```bash
make px4_fmu-v3_default force-upload
```

PWM Calibrate v 0.4
===================

A Raspberry Pi helper class for linear calibration of outputs that respond nonlinearly. This is particularly useful when driving VU meters/panel meters/[galvonometers](http://en.wikipedia.org/wiki/Galvanometer)/whatever you want to call them from the Raspberry Pi, but there are probably other applications as well.

For instance: you've connected a VU meter to the Raspberry Pi's hardware PWM output (pin 1). The PWM output can be set to 1024 distinct levels. The meter goes from 1 to 200. You want to set the meter to 100. You have two problems:

* Converting from "100" to "512" involves some extremely simple math (ugh)

* More importantly, 50% power (512) might not move the needle to 50% on the meter (100). Whoops!

This class facilitates the calibration of a PWM output by sweeping through its output range (max to zero) and collecting user input to measure the location of steps (e.g. notches on a meter, measured loudness or brightness levels). The result is stored to disk as JSON and reloaded as needed. 

You can then set the value by simply asking for the step; the class will figure out the appropriate PWM setting based on the loaded calibration file. Values located between steps are linearly interpolated (if this provides inaccurate results, you should recalibrate with more steps).

The class also brokers the use of software or hardware routines (depending on the pin) if wiringpi2 is installed. If only wiringpi v1.0 is available, only PWM output is enabled.

Installation
------------

> `pip install pwm_calibrate`

Alternately, download a copy of this repository and run

> `python setup.py install`

Command Line Usage
------------------

A utility called `pwm_calibrate` is included in the distribution. Usage:

> `pwm_calibrate [-p PIN] [-z ZERO_PIN] OUTPUT_FILE`

Where `PIN` is the Raspberry Pi pin to be calibrated (default: 1) and `OUTPUT_FILE` is the name of the file where the JSON results should be stored. 

Upon launch, `PIN` will be set to maximum and the user asked to adjust his or her circuit to calibrate the meter's maximum setting. The user will be prompted for the number of steps that will be recorded. Note that this shoudl exclude the maximum setting. For example: in a meter numbered from 0-25, with major marks for 0, 5, 15, 20 and 25, the user should enter "5". The meter will then slowly decrease from maximum. The user should press the space bar as each of those major marks is passed by the needle; the current PWM setting will be recorded.

`ZERO_PIN` is an optional argument: if specified, this pin number will be declared as a PWM and set to zero prior to calibration. This is useful in circumstances where a bidirectional meter is being calibrated that uses PWM input for both its anode and cathode. Without it, the Pi's default high-impedence mode for uninitialized GPIO pins will prevent the calibration from proceeding successfully. 

In more common configurations in which a unidirectional meter's anode is connected to Vcc and its cathode to a PWM pin; or its cathode is connected to ground and its anode to a PWM pin; the `ZERO_PIN` option may be ignored.

The resulting JSON file will contain the calibration information necessary for use by the PWMCalibrator class. Simply pass the path to such a file when constructing the PWMCalibrator() object.


Notes
-----

* Pin numbering uses the [wiringpi scheme](http://wiringpi.com/pins/), not the Raspberry Pi scheme.

* Hardware PWM output has a resolution of 10 bits / 1024 steps. Software PWM has 100 steps by default, per the recommendation of the wiringpi2 docs. There is a tradeoff between frequency and resolution associated with changing this value; see the [wiringpi2 documentation](http://wiringpi.com/reference/software-pwm-library/) for more details.

* Remember that Pi GPIOs output 0-3.3v!

TO DO
-----

* Calibration is currently dependent on curses. Adding routines to enable GPIO input might be nice. Also note that the curses display does not currently record collected values properly (this feature is completely superficial).

Thanks
------

Enormous thanks to [Gordon Henderson](http://projects.drogon.net/) for writing the WiringPi library!


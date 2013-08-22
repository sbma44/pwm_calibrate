PWM Calibrate
=============

Raspberry Pi helper class for linear calibration of outputs that respond nonlinearly.

For instance! You've connected a VU meter to the Raspberry Pi's hardware PWM output (pin 1). The PWM output can be set to 1024 distinct levels. The meter goes from 1 to 200. You want to set the meter to 100. You have two problems:

* Converting from "100" to "512" involves some extremely simple math (ugh)

* More importantly, 50% power (512) might not move the needle to 50% on the meter (100). Whoops!

This class facilitates the calibration of a PWM output by sweeping through its output range (max to zero) and collecting user input to measure the location of steps (e.g. notches on a meter, measured loudness or brightness levels). The result is stored to disk as JSON and reloaded as needed. 

You can then set the value by simply asking for the step; the class will figure out the appropriate PWM setting based on the loaded calibration file. Values located between steps are linearly interpolated (if this provides inaccurate results, you should recalibrate with more steps).

The class also brokers the use of software or hardware routines (depending on the pin) if wiringpi2 is installed. If only wiringpi v1.0 is available, only PWM output is enabled.

Notes
-----

* Pin numbering uses the [wiringpi scheme](http://wiringpi.com/pins/), not the Raspberry Pi scheme.

* Hardware PWM output has a resolution of 10 bits / 1024 steps. Software PWM has 100 steps by default, per the recommendation of the wiringpi2 docs. There is a tradeoff between frequency and resolution associated with changing this value; see the [wiringpi2 documentation](http://wiringpi.com/reference/software-pwm-library/) for more details.

* Remember that Pi GPIOs output 0-3.3v!

TO DO
-----

* Calibration is currently dependent on curses. Adding routines to enable GPIO input might be nice.

Thanks
------

Enormous thanks to [Gordon Henderson](http://projects.drogon.net/) for writing the WiringPi library!
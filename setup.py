from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pwm_calibrate',
      version='0.1',
      description='Provides PWM calibration tools for use on the Raspberry Pi',
      url='http://github.com/sbma44/pwm_calibrate',
      author='Tom Lee',
      author_email='thomas.j.lee@gmail.com',
      license='MIT',
      packages=['pwm_calibrate'],
      install_requires=[
          'wiringpi2',
      ],
      zip_safe=False)

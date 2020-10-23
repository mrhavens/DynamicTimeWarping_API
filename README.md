# DynamicTimeWarpingAPI

# Table of content

* [Introduction](#Introduction)
* [Dynamic Time Warping](#dynamic-time-warping)
* [Getting started](#Geting-started)
* [Roadmap](#roadmap)
* [References](#references)
* [License](#license)


## Introduction 

In this project, I will be buidling a RESTful API for [Dynamic Time Warping](#dynamic-time-warping) which can also be used with Amazon S3 bucket. This project will be divided into 3 different parts listed [here](#roadmap)

## Dynamic Time Warping

According to Wikipedia:

> Dynamic time warping (DTW) is one of the algorithms for measuring similarity between two temporal sequences, which may vary in speed. For instance, similarities in walking could be detected using DTW, even if one person was walking faster than the other, or if there were accelerations and decelerations during the course of an observation. DTW has been applied to temporal sequences of video, audio, and graphics data — indeed, any data that can be turned into a linear sequence can be analyzed with DTW. A well known application has been automatic speech recognition, to cope with different speaking speeds. Other applications include speaker recognition and online signature recognition. It can also be used in partial shape matching application.



## Getting started

This project is based on python and there are multiple open-source libraries that are being used in here. You can find all theb requirments in the requiremtns.txt file

### Setting up a virtual environment 

[Anaconda](https://www.anaconda.com/) is an open-souce tool-kit for python and it is very useful. You can install anaconda from [here](https://www.anaconda.com/products/individual)

After downloading Anacodna, go to your terminal if you are a Mac/Linux user or on your Anaconda powershell if you are a Windows user and use the following commands

```console
foo@bar:~$ conda create -n myenv python==3.8.3
```

After creating this virtual enviroment, we can activate this using

```console
foo@bar:~$ conda activate myenv
```

To install all the requirements, copy this command in your terminal or Powershell with your virtual environment on.

```console
foo@bar:~$pip install -r requirements.txt
```

To run the code, go to th flask directory and follow this step: 

```console
foo@bar:~$ python3 app.py

```
Please note that it takes few mintues to finish the calculations and show the output ( roughly 10 mins on a laptop without GPUs )

## Roadmap

This project will be divided into three parts as listed below.

- [x] Implementing Dynamic Time Warping in python
- [x] Integrate a REST API
- [x] Integrate MinIO ( Amazon S3 alternative) bucket access
- [x] Complete the documentation

## References

There are many useful resources that are out that that have good materials on Dynamic Time Warping. Here I have listed all the resources that I found out to be useful

* [Vassilis Athitsos Lecture notes](http://vlm1.uta.edu/~athitsos/courses/cse4309_fall2020/lectures/15_dtw.pdf)
* [Jeremy Zheng's Towardsai blog post](https://towardsdatascience.com/dynamic-time-warping-3933f25fcdd)
* [Dynamic Time Warping Wikipedia](https://en.wikipedia.org/wiki/Dynamic_time_warping)



## MIT License

Copyright 2020 [Nisarg Shah](https://nisargushah.com/)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



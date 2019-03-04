# HTML-to-OtherFile-University-Grades

Web scrape your grades out of the Dean's Office at PJATK. 
The program will log in using credential you'll provide and will 
transfer the grades to .csv, .txt and so on.

Make sure you use Python 3.x

So far only Polish version of teh web-site is accessed

# How to use it:

Clone this repo:
```
git clone https://github.com/MiddleZwei/HTML-to-OtherFile-University-Grades.git

cd HTML-to-OtherFile-University-Grades
```

## [Optional] Create a virtual environment
I suggest to create a virtual environment first, but you can omit it and install packages globally if you want

[How to create a virtual environment](https://github.com/MiddleZwei/HTML-to-OtherFile-University-Grades/virtualenv.md)

## Argument descriptions
- -u, --username: s number
- -p, --password: leave blank, it'll prompt for it later
- [optional] -o, --output: output file name

## Run in Windows' command prompt:

Run these commands:
```
pip3 install -r requirements

python .\webscraptable.py --username [sXXXXX] -p
```

## Run in Linux's terminal
Run these commands:
```
pip3 install -r requirements

python3 webscraptable.py --username [sXXXXX] -p
```
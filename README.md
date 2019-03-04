# HTML-to-CSV-University-Grades

Web scrape your grades out of the Dean's Office at PJATK. 
The program will log in using credential you'll provide and will 
transfer the grades to a .csv file.

Make sure you use Python 3.x

# How to use it:

Clone this repo:
```
git clone https://github.com/MiddleZwei/HTML-to-CSV-University-Grades.git

cd HTML-to-CSV-University-Grades
```

## [Optional] Create a virtual environment
I suggest to create a virtual environment first, but you can omit it and install packages globally if you want

[How to create a virtual environment](https://github.com/MiddleZwei/HTML-to-CSV-University-Grades/virtualenv.md)

## Argument descriptions
- -u, --username: s number
- -p, --password: leave blank, it'll prompt for it later
- [optional] -o, --output: output file name

## Run in Windows' command prompt:

- path_to_python.exe: ```where python```
- path_to_current_folder: ```%cd%```

Run these commands (tested in PowerShell):
```
pip install -r requirements

path_to_python.exe path_to_current_folder\webscraptable.py --username [sXXXXX] -p
```

# Run in Linux's terminal
```
pip install -r requirements

python3 webscraptable.py --username [sXXXXX] -p
```
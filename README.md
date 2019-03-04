# REST API with Flask

Web scrape your grades out of the Dean's Office at PJATK. 
The program will log in using credential you'll provide and will 
transfer the grades to a .csv file.

# How to use it:

## [Optional] Create a virtual environment
I suggest to create a virtual environment first, but you can omit it and install packages globally if you want
[How to create a virtual environment](https://github.com/MiddleZwei/HTML-to-CSV-University-Grades/virtualenv.md)

## Arguments description
- -u, --username: s number
- -p, --password: leave blank, it'll prompt for it later
- [optional] -o, --output: output file name

## Run in Windows command prompt:

Clone this repo:
```
git clone https://github.com/MiddleZwei/HTML-to-CSV-University-Grades.git
```

Run these commands (tested in PowerShell):
```
cd HTML-to-CSV-University-Grades

pip install -r requirements
```

Run the program:
```
path_to_python.exe path_to_current_folder\webscraptable.py --username [sXXXXX] -p
```

Everything is saved to the current folder.

# Linux
```
python3 webscraptable.py --username [sXXXXX] -p
```
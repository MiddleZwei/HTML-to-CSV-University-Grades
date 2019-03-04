# How to install and activate virtual environment:

## Windows:
- path_to_python.exe: ```where python```
- path_to_current_folder: ```%cd%```

```
virtualenv venv

path_to_python.exe path_to_current_filder\venv\Scripts\activate
```

Deactivate virtual environment:
```
deactivate
```

## Linux
```
virtualenv venv --python=`which python3`

source venv/bin/activate
```

Deactivate virtual environment:
```
deactivate
```
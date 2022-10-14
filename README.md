Echo сервер для прослушивание нескольких портов

## setup.bat
    cd C:\tools\
    git clone https://github.com/rasulovdd/echo_server.git
    cd C:\tools\echo_server
    python -m venv env
    

## start.bat
    call "C:\tools\echo_server\env\Scripts\activate.bat"
    python "C:\tools\echo_server\src\main.py"
    
## update.bat
    cd C:\tools\echo_server
    git pull
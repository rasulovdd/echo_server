Echo сервер для прослушивание нескольких портов

## start.bat
    call "C:\tools\echo_server\env\Scripts\activate.bat"
    python "C:\tools\echo_server\src\main.py"
    
## update.bat
    cd C:\tools\echo_server
    git pull
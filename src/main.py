import asyncio
import logging
import os

#logging.getLogger("asyncio").setLevel(logging.INFO)

# создаем папку если его нет 
if not os.path.exists('logs'):
    try:
        os.mkdir('logs')
    except Exception as my_error:
        print(f"Ошибка: {my_error}") #debug

# устанавливаем стандартные параметры логирования
logging.basicConfig(
        filename='logs/echo-server.log', 
        level=logging.INFO, 
        #format=f'%(asctime)s | %(levelname)s %(name)s %(threadName)s : %(message)s',
        format=f'%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S'
)

async def handle_connection(reader, writer):
    addr = writer.get_extra_info("peername")
    my_ip, my_port = writer.get_extra_info("sockname")
    print(f"Connected by {addr} to port: {my_port}")
    logging.info(f"Connected by {addr} to port: {my_port}")
    while True:
        # Receive
        try:
            data = await reader.read(1024)  # New
        except ConnectionError:
            print(f"Client suddenly closed while receiving from {addr}")
            logging.warning(f"Client suddenly closed while receiving from {addr}")
            break
        print(f"Received {data} from: {addr}")
        logging.info(f"Received {data} from: {addr}")
        if not data:
            break
        # Process
        if data == b"close":
            break
        data = data.upper()
        # Send
        print(f"Send: {data} to: {addr}")
        logging.info(f"Send: {data} to: {addr}")
        try:
            writer.write(data)  # New
            await writer.drain()
        except ConnectionError:
            print(f"Client suddenly closed, cannot send")
            logging.warning(f"Client suddenly closed, cannot send")
            break
    writer.close()
    print("Disconnected by", addr)
    logging.info(f"Disconnected by {addr}")

async def main(host, port1, port2, port3, port4):
    server1 = await asyncio.start_server(handle_connection, host, port1)
    server2 = await asyncio.start_server(handle_connection, host, port2)
    server3 = await asyncio.start_server(handle_connection, host, port3)
    server4 = await asyncio.start_server(handle_connection, host, port4)
    print(f"START SERVER | PORTS: [{port1}, {port2}, {port3}, {port4}]")
    logging.info(f"START SERVER | PORTS: [{port1}, {port2}, {port3}, {port4}]")
    async with server1:
        await server1.serve_forever()
    

HOST = ""  # Symbolic name meaning all available interfaces
#PORT = 50007  # Arbitrary non-privileged port
PORT1 = 22335
PORT2 = 11331
PORT3 = 33456
PORT4 = 22456

if __name__ == "__main__":
    #asyncio.run(main(HOST, PORT1))
    asyncio.run(main(HOST, PORT1, PORT2, PORT3, PORT4)) #передаем порты

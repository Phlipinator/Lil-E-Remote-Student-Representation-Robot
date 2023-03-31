# Source: https://github.com/tayfunulu/WiFiManager
# I removed the initial Wi-Fi Managing and storing parts, but ket the structure to create a AP Wi-Fi.

import network
import socket
import ure
import time

eyeState = "neutral"
studentCount = 0
earsColor = "off"
ears = 0
arm = "down"

ap_ssid = "Lil'E"
ap_password = "123456789"
ap_authmode = 3  # WPA2

NETWORK_PROFILES = 'wifi.dat'

wlan_ap = network.WLAN(network.AP_IF)

server_socket = None

def get_connection():
    connected = False
    # start web server for connection manager:
    if not connected:
        connected = start()

    return wlan_ap if connected else None

def send_header(client, status_code=200, content_length=None ):
    client.sendall("HTTP/1.0 {} OK\r\n".format(status_code))
    client.sendall("Content-Type: text/html\r\n")
    if content_length is not None:
      client.sendall("Content-Length: {}\r\n".format(content_length))
    client.sendall("\r\n")


def send_response(client, payload, status_code=200):
    content_length = len(payload)
    send_header(client, status_code, content_length)
    if content_length > 0:
        client.sendall(payload)
    client.close()



def handle_root(client):
    
    send_header(client)
    client.sendall("""\
        <html>
          <head>
            <title>Lil'E Control Panel</title>
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <link rel="icon" href="data:," />
            <style>
              html {
                font-family: Helvetica;
                display: inline-block;
                margin: 0px auto;
                text-align: center;
              }
              h1 {
                color: #0f3376;
                padding: 2vh;
              }
              p {
                font-size: 1.5rem;
              }
              .button {
                display: inline-block;
                background-color: #e7bd3b;
                border: none;
                border-radius: 4px;
                color: white;
                padding: 16px 40px;
                text-decoration: none;
                font-size: 30px;
                margin: 2px;
                cursor: pointer;
              }
              .button2 {
                background-color: #4286f4;
              }
            </style>
          </head>
          <body>
            <h1>Lil'E Control Panel</h1>
            <p>
              <a href="/happy"><button class="button">HAPPY</button></a>
            </p>
            <p>
              <a href="/"><button class="button">NEUTRAL</button></a>
            </p>
            <p>
              <a href="/sad"><button class="button">SAD</button></a>
            </p>
            <p>
              <a href="/plus"><button class="button">+</button></a>
            </p>
            <p>
              <a href="/minus"><button class="button">-</button></a>
            </p>
            <p>
              <a href="/armup"><button class="button">ARM UP</button></a>
            </p>
            <p>
              <a href="/armdown"><button class="button">ARM DOWN</button></a>
            </p>
            <p>
              <a href="/ears0"><button class="button">EARS DEFAULT</button></a>
            </p>
            <p>
              <a href="/ears1"><button class="button">EARS HALF BACK</button></a>
            </p>
            <p>
              <a href="/ears2"><button class="button">EARS BACK</button></a>
            </p>
            <p>
              <a href="/ears3"><button class="button">EARS DOWN</button></a>
            </p>
            <p>
              <a href="/earsColor1"><button class="button">EARS GREEN</button></a>
            </p>
            <p>
              <a href="/earsColor2"><button class="button">EARS VIOLET</button></a>
            </p>
            <p>
              <a href="/earsColor3"><button class="button">EARS BLUE</button></a>
            </p>
            <p>
              <a href="/earsColor0"><button class="button">EARS OFF</button></a>
            </p>
          </body>
        </html>
    """)
    
    client.close()

def handle_not_found(client, url):
    send_response(client, "Path not found: {}".format(url), status_code=404)


def stop():
    global server_socket

    if server_socket:
        server_socket.close()
        server_socket = None


def start(port=80):
    global server_socket

    addr = socket.getaddrinfo('0.0.0.0', port)[0][-1]

    stop()

    #wlan_sta.active(True)
    wlan_ap.active(True)

    wlan_ap.config(essid=ap_ssid, password=ap_password, authmode=ap_authmode)

    server_socket = socket.socket()
    server_socket.bind(addr)
    server_socket.listen(1)

    print('Connect to WiFi ssid ' + ap_ssid + ', default password: ' + ap_password)
    print('and access the ESP via your favorite web browser at 192.168.4.1.') #why??
    print('Listening on:', addr)

    while True:

        client, addr = server_socket.accept()
        print('client connected from', addr)
        try:
            client.settimeout(5.0)

            request = b""
            try:
                while "\r\n\r\n" not in request:
                    request += client.recv(512)
            except OSError:
                pass

            print("Request is: {}".format(request))
            if "HTTP" not in request:  # skip invalid requests
                continue

            # version 1.9 compatibility
            try:
                url = ure.search("(?:GET|POST) /(.*?)(?:\\?.*?)? HTTP", request).group(1).decode("utf-8").rstrip("/")
            except Exception:
                url = ure.search("(?:GET|POST) /(.*?)(?:\\?.*?)? HTTP", request).group(1).rstrip("/")
            print("URL is {}".format(url))

            if url == "":
                global eyeState
                eyeState = "neutral"
                handle_root(client)
            elif url == "happy":
                global eyeState
                eyeState = "happy"
                print(eyeState)
                handle_root(client)
            elif url == "sad":
                global eyeState
                eyeState = "sad"
                handle_root(client)
            elif url == "plus":
              global studentCount
              studentCount = studentCount + 1
              handle_root(client)
            elif url == "minus":
              if studentCount >= 1:
                global studentCount
                studentCount = studentCount - 1
                handle_root(client)
            elif url == "armup":
              global arm
              arm = "up"
              handle_root(client)
            elif url == "armdown":
              global arm
              arm = "down"
              handle_root(client)
            elif url == "ears0":
              global ears
              ears = 0
              handle_root(client)
            elif url == "ears1":
              global ears
              ears = 1
              handle_root(client)
            elif url == "ears2":
              global ears
              ears = 2
              handle_root(client)
            elif url == "ears3":
              global ears
              ears = 3
              handle_root(client)
            elif url == "earsColor0":
              global earsColor
              earsColor = "off"
              handle_root(client)
            elif url == "earsColor1":
              global earsColor
              earsColor = "green"
              handle_root(client)
            elif url == "earsColor2":
              global earsColor
              earsColor = "violet"
              handle_root(client)
            elif url == "earsColor3":
              global earsColor
              earsColor = "blue"
              handle_root(client)
            else:
                handle_not_found(client, url)

        finally:
            client.close()

import numpy as np
import matplotlib.pyplot as plt
import socket

host = "84.237.21.36"
port = 5152


def find_star_centers(img):
    # Первая звезда
    star1_center = np.unravel_index(np.argmax(img), img.shape)
    # Вторая звезда
    img[star1_center[0] - 5:star1_center[0] + 5,
    star1_center[1] - 5:star1_center[1] + 5] = 0
    star2_center = np.unravel_index(np.argmax(img), img.shape)

    return star1_center, star2_center


def recvcall(sock,n):
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n-len(data))
        if not packet:return
        data.extend(packet)
    return data


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
    sock.connect((host,port))

    for _ in range(10):
        sock.send(b"get")
        bts = recvcall(sock,40002)
        img = np.frombuffer(bts[2:40002],dtype="uint8").reshape(bts[0],bts[1])

        star_1,star_2 = find_star_centers(img)

        distance = np.sqrt((star_2[0] - star_1[0]) ** 2 + (star_2[1] - star_1[1]) ** 2)
        rounded_distance = round(distance, 1)

        sock.send(f"{rounded_distance}".encode())
        print(sock.recv(20))

    plt.imshow(img)
    plt.show()

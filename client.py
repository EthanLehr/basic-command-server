import socket
HEADER_LEN = 10

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("127.0.0.1", 8820))
while True:
    choice = input("plz insert your choice\n")
    my_socket.send(choice.encode())
    if choice == "send screenshot":
        f = open("recive_screenshot.png", "wb")
        tot_num_of_iteration = int.from_bytes(my_socket.recv(69), "big")
        print("the total number of the itaretion is " + str(tot_num_of_iteration))
        for i in range(tot_num_of_iteration):
            len_of_bytes_to_recive = int.from_bytes(my_socket.recv(4), "big")
            print("the len of bytes to recive is " + str(len_of_bytes_to_recive))
            l = my_socket.recv(len_of_bytes_to_recive)
            f.write(l)
        print("Im done")
        my_socket.close()
        f.close()
    elif choice == "show folder":
        folder = my_socket.recv(10000).decode()
        print(folder)
#לרשום פרוטוקול ספציפי ולר רק 1024
#הפרוטוקוךל דרג להעביר את האורך של מה שנקבל


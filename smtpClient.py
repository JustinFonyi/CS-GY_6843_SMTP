from socket import *

    # Send HELO command and print server response.
def send_command():    
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    from_address = "jzf9635@nyu.edu"
    to_address = "fonyijustin@gmail.com"
    subject = "This is a test"
    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    send_command(f"MAIL FROM <{from_address}>")

    # Send RCPT TO command and handle server response.
    send_command(f"RCPT TO <{to_address}>")

    # Send DATA command and handle server response.
    send_command(f"DATA")

    # Send message data.
    send_command(f"Subject: {subject}\r\nTo: {to_address}\r\n{msg}")

    # Message ends with a single period, send message end and handle server response.
    send_command(f"{endmsg}")
    # Send QUIT command and handle server response.
    send_command("QUIT")
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')

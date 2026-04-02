# Program Name: ProgramA
# Course: IT3883/Section 01
#Mina Bayramoglu
# Assignment Number: Lab#4
# Due Date: 4/1/2026
# Purpose: Program A sends user input to Program B. Program B converts the input to uppercase and sends the putput back to program A
# https://www.geeksforgeeks.org/python/socket-programming-python/
#https://www.w3schools.in/python/network-programming
#https://www.pythoncentral.io/learn-python-socket/

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 5200
client_socket.connect((host, port))
message = input("Enter a sentence: ")

client_socket.send(message.encode())

response = client_socket.recv(1024).decode()

print("New Sentence:", response)
client_socket.close()
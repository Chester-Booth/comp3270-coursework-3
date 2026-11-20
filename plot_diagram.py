import matplotlib.pyplot as plt
import numpy as np


rfile = open('receive.txt', 'r')
sfile = open('send.txt', 'r')

send_buffer = sfile.read()
recv_buffer = rfile.read()

send_array = send_buffer.split('\n')
recv_array = recv_buffer.split('\n')

rank0send = []
rank1send = []

for item in send_array:
    number = ''
    if item == '':
        break
    for i in range(14, len(item)):
        number += item[i]
    if item[2] == '0':
        rank0send.append(int(number))
    if item[2] == '1':
        rank1send.append(int(number))

rank0recv = []
rank1recv = []
for item in recv_array:
    number = ''
    if item == '':
        break
    for i in range(14, len(item)):
        number += item[i]
    if item[2] == '0':
        rank0recv.append(int(number))
    if item[2] == '1':
        rank1recv.append(int(number))

output_index = ['0', '1', '2', '3']


plt.figure(figsize=(20, 10))

print(rank0send)
plt.subplot(1, 4, 1)
plt.bar(output_index, rank0send)
plt.title('Rank 0 send buffer')
plt.xlabel('Sample index')
plt.ylabel('Magnitude')


print(rank1send)
plt.subplot(1, 4, 2)
plt.bar(output_index, rank1send)
plt.title('Rank 1 send buffer')
plt.xlabel('Sample index')
plt.ylabel('Magnitude')


print(rank0recv)
plt.subplot(1, 4, 3)
plt.bar(output_index, rank0recv)
plt.title('Rank 0 receive buffer')
plt.xlabel('Sample index')
plt.ylabel('Magnitude')


print(rank1recv)
plt.subplot(1, 4, 4)
plt.bar(output_index, rank1recv)
plt.title('Rank 1 receive buffer')
plt.xlabel('Sample index')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
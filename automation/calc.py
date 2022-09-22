a1 = ' -- '
a2 = '|  |'
a3 = '    '
a4 = '   |'
a5 = '|   '

d = {'0': [a1, a2, a2, a3, a2, a2, a1],
     '1': [a3, a4, a4, a3, a4, a4, a3],
     '2': [a1, a4, a4, a1, a5, a5, a1],
     '3': [a1, a4, a4, a1, a4, a4, a1],
     '4': [a3, a2, a2, a1, a4, a4, a3],
     '5': [a1, a5, a5, a1, a4, a4, a1],
     '6': [a1, a5, a5, a1, a2, a2, a1],
     '7': [a1, a4, a4, a3, a4, a4, a3],
     '8': [a1, a2, a2, a1, a2, a2, a1],
     '9': [a1, a2, a2, a1, a4, a4, a1]}
e = input()
print('x'+5*(len(e))*'-'+'x')
for i in range(7):
    print(f'|{" ".join(d[j][i] for j in e)}|')
    # for j in str(e):
    #     if i == 0:
    #         pass
    #     elif i == 6:
    #         pass
    #     else:
    #         print(d[j][i], end='')
    # print()
print('x'+5*(len(e))*'-'+'x')
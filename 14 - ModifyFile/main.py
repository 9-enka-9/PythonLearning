with open('14 - ModifyFile\\newFile1.txt', mode='w') as file:
    file.write('Hi, I\'m En!')
    file.close()

with open(r'C:\Users\Admin\Desktop\newFile.txt', mode='a') as file:
    file.write('\nNEW TEXT')
    file.close()
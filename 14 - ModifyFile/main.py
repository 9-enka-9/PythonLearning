with open('D:/PythonLearning/14 - ModifyFile/newFile1.txt', mode='r',encoding='utf-8') as file: #ABSOLUTE PATH: relative to computer
    content=file.read()
    print(content)
    file.close()

with open('../../newFile.txt', mode='a') as file: # RELATIVE PATH: relative to current working directory
    file.write('\nNEW TEXT')
    file.close()
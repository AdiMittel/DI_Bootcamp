matrix = [
['7','i','3'],
['T','s','i'],
['h','%','x'],
['i',' ','#'],
['s','M',' '],
['$','a',' '],
['#','t','%'],
['^','r',' ']]

def read():
    message= ''
    
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j].isalpha():
                message+=matrix[i][j]
            else:
                k = i + 1 
                if k <= len(matrix)-1:
                    if matrix[i][j].isalpha() == False and (matrix[k][j]).isalpha() == False:
                        message+= ' '
    print(message)
read()

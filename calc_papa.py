import random
print('''Привет, я питон-программа которая научит тебя таблице умножения''')

cnt = 0
cnt_y = 0

while True:
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    print('Сколько будет '+str(x)+'*'+str(y))
    n = int(input())
    cnt = cnt + 1
    if (n == x * y):
        cnt_y = cnt_y +1

    if(cnt % 9 == 0):
        q = str(input('Еще? Если нет введите n, если да жмите Enter'))
        if (q == 'n'):
            if (cnt < 10):
                print('Слишком мало для оценки. Лентяй!')
            else:
                print('Правильно '+str(cnt_y)+' из '+str(cnt))
                if (cnt_y == cnt):
                    print('Молодец')
                else:
                    print('Тренируйся еще')
            break
    
    
            
                  
        
                  
            


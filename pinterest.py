from py3pin.Pinterest import Pinterest
import random
import time
import os
MAX_PHOTOS = 156

Text = ['Подписывайтесь, чтобы не пропустить новые фото!',
       'Больше фото в моём Instagram. Переходи на сайт и подписывайся!',
       'Instagram: analitiq.']

boards = {'msc':691724892706211993, 'me':691724892706211204,'work':691724892706211751,'insp':691724892706212427}
hashtags = {'msc':['#moscow','#москва','#москвасити'],'me':['#me','#streetwear','#thenorthface','#продвижениеаккаунта'],
                'work':['#work','#it','#marketing','#digitalmarketing','#обучение', '#образование','#маркетинг'],
                'insp': ['#inspiration']}



pinterest = Pinterest(email='mail',
                      password='pass',
                      username='analitiq')
pinterest.login()

keys = []
for key in boards:
    keys.append(key)

Title = ''
Link = 'https://www.instagram.com/analitiq/'
i = random.randint(0,len(keys)-1)
j = random.randint(1,MAX_PHOTOS)
photo_name = keys[i]+'-'+str(j)
Description = Text[random.randint(0,len(Text)-1)]+' ' + ' '.join(hashtags[keys[i]])

print('\n\n')
print('Программа для автоматизированной выгрузки пинов в Pinterest:')
print('by @analitiq')
print('\n')

count = 1
while True:
    while True:
        try:
            pinterest.upload_pin(board_id= str(boards[keys[i]]),
                     image_file= 'pinterest/'+ photo_name + '.jpg',
                     description= Description,
                     title= Title,
                     link = Link)
            print(str(count)+'. Выложено фото: '+photo_name+'.')
            file_path = 'pinterest/'+ photo_name + '.jpg'
            os.remove(file_path)
            i = random.randint(0,len(keys)-1)
            j = random.randint(1,MAX_PHOTOS)
            photo_name = keys[i]+'-'+str(j)
            Description = Text[random.randint(0,len(Text)-1)]+' ' + ' '.join(hashtags[keys[i]])
            break
        except:
            i = random.randint(0,len(keys)-1)
            j = random.randint(1,MAX_PHOTOS)
            photo_name = keys[i]+'-'+str(j)
            Description = Text[random.randint(0,len(Text)-1)]+' ' + ' '.join(hashtags[keys[i]])
    count += 1
    time.sleep(3600)

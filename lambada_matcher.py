import os
import time
import string

'''
THIS WILL TAKE A MONTH DO NOT RUN
'''

start_time = time.time()
match_list = []
direct = '/'+os.path.join('Users', 'afleischer', 'Lambada_Matcher')
def file_cabinet(Directory):
    file_dict = {}
    for root, dirs, filename in os.walk(Directory):
        for file in filename:
            file_list = []
            if file.endswith('.txt') == True:
                pass
            else:
                subdirectory = os.path.join(root, file)
                for root, dirs, filenames in os.walk(subdirectory):
                    for x in filenames:
                        file_list.append(x)
            file_dict[subdirectory] = file_list


train_tracks = []
train = open("train.txt", 'r')
for file in train:
    train_tracks.append(file[12:])
print(train_tracks)

        
l_dev = open("tester2.txt", 'r', encoding="latin-1")
for line in l_dev.readlines():
    for root, dirs, filenames in os.walk(direct):
        for x in dirs:
            sub = direct + '/' + x
            for root, dirs, filenames in os.walk(sub):
                for file in filenames:
                    if os.path.join(root,file)[31:] in train_tracks:
                        print(os.path.join(root,file)[31:])
                        pass
#                    else:
#                        passage_counter = 0
#                        reader = open(os.path.join(root, file), 'r', encoding = "latin-1")
#                        for y in reader.readlines():
#                            passage_counter += 1
#                            print(passage_counter)
#                            if line.lower() == y.lower():
#                                print((root + '/' + file, passage_counter))
#                                match_list.append((root + '/' + file, passage_counter))
#                                reader.close()
#                                break
print(match_list)  
print(time.time() - start_time)
    

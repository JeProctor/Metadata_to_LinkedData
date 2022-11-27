import cv2
import pandas as pd

df = pd.read_csv('/home/jj/Desktop/Spr_IP/autodrawboxes.csv', sep=",")
for index, row in df.iterrows():
    print(row['image'])
    im = cv2.imread(row['image'])
    im2 = cv2.rectangle(im, (int(row['hortop']), int(row['vertop'])), (int(row['horbottom']), int(row['vertbottom'])), (0, 255, 0), 3)
    cv2.imwrite('/home/jj/Desktop/Spr_IP/people/' + str(row['id']) + '.jpg', im2)


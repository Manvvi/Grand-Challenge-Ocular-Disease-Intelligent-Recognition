import pandas as pd
import os
import numpy as np
from preprocessing import get_individual_labels
# import cv2


TRAIN_DIR=r"data"
df=pd.read_excel(r'C:\Users\Dell\Desktop\grandchallenge\data\ODIR-5K_Training_Annotations(Updated)_V2.xlsx')
csv_data= df.to_csv(os.path.join(TRAIN_DIR,"train.csv"))

Left_eye=df[['Left-Fundus','Left-Diagnostic Keywords']].copy()
Left_eye.columns=['Image','Labels']
# Left_eye.to_csv(os.path.join(TRAIN_DIR,'left_eye.csv'))

Right_eye=df[['Right-Fundus','Right-Diagnostic Keywords']].copy()
Right_eye.columns=['Image','Labels']
# Right_eye.to_csv(os.path.join(TRAIN_DIR,'right_eye.csv'))


keywords_left=[keyword_l for keywords_left in df['Left-Diagnostic Keywords'] for keyword_l in keywords_left.split(',')]
unique_keywords_left= set(keywords_left)
# print((unique_keywords_left))
# print(keywords_left[:10])

keywords_right=[keyword_r for keywords_right in df['Right-Diagnostic Keywords'] for keyword_r in keywords_right.split(',')]
unique_keywords_right= set(keywords_right)
# print((unique_keywords_right))
# print(keywords_right[:10])

class_labels= ['N','D','C','A','F','M','O']
keyword_label_mapping  = {
    'normal':'N',
    'retinopathy':'D',
    'glaucoma':'G',
    'cataract':'C',
    'macular degeneration':'A',
    'hypertensive':'H',
    'myopia':'M',
    'lens dust':'O', 'optic disk photographically invisible':'O', 'low image quality':'O', 'image offset':'O'
}
non_decisive_labels = ["lens dust", "optic disk photographically invisible", "low image quality", "image offset"]
# print(get_individual_labels('optic disk photographically invisible'))

df['Left-label']= df['Left-Diagnostic Keywords'].apply(get_individual_labels)
df['Right-label'] = df['Right-Diagnostic Keywords'].apply(get_individual_labels)     

df[df['Left-label'].isin(non_decisive_labels)]
df[df['Right-label'].isin(non_decisive_labels)]  

# left_data= pd.read_csv(r'data\left_eye.csv')   
# left_columns = 'left_labels'
# l=[]
# for left in left_data['Labels']:
#      out_l= get_individual_labels(left)
#      l.append(out_l)


# left_data[left_columns]=l
# # print(l)
# left_data.to_csv(r'C:\Users\Dell\Desktop\grandchallenge\data\left_eye.csv',index=False)

right_data= pd.read_csv(r'data\right_eye.csv')   
right_columns = 'right_labels'
r=[]
for right in right_data['Labels']:
     out_r= get_individual_labels(right)
     r.append(out_r)


right_data[right_columns]=r
print(r)
right_data.to_csv(r'C:\Users\Dell\Desktop\grandchallenge\data\right_eye.csv',index=False)

    









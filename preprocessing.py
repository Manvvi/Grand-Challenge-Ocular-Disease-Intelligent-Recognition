import pandas as pd
import os
import numpy as np

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
# if the keyword contains label outside of the above then, label them as others 'O'
def get_individual_labels(diagnostic_keywords):
    keywords = [ keyword  for keyword in diagnostic_keywords.split(',')]
    contains_normal = False
    for k in keywords:
        for label in keyword_label_mapping.keys():
            if label in k:
                if label == 'normal':
                    contains_normal = True # if found a 'normal' keyword, check if there are other keywords but keep in mind that a normal keyword was found
                else:
                    return keyword_label_mapping[label] # found a proper keyword label, use the first occurence

    # did not find a proper keyword label, see if there are labels other than non-decisive labels, if so, categorize them as 'others'
    decisive_label = False
    for k in keywords:
        if k not in non_decisive_labels and (('normal' not in k) or ('abnormal' in k)):
            decisive_label = True
    if decisive_label:
        # contains decisive label other than the normal and abnormal categories
        return 'O' 
    if contains_normal:
        return 'N'
    # if any of the above criteria do not match, then return as is
    return keywords[0] # u
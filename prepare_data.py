ALPHABET = 'Only thewigsofrcvdampbkuq.A-210xT5\'MDL,RYHJ"ISPWENj&BC93VGFKz();#:!7U64Q8?+*ZX/%'
BN_ALPHABET = "',:।ঁংঃঅআইঈউঊঋএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহ়ািীুূৃেৈোৌ্ৎৗড়ঢ়য়০১২৩৪৫৬৭৮৯৷‌‍–—"

IMG_FILE='BN-EN-IAM-MULTI.pickle'
IMG_FILE_CLEANED = 'files/BN-ENG-CLEANED.pickle'


for char in BN_ALPHABET:
    if char not in ALPHABET: ALPHABET += char

def remove(data):
    keys = data.keys()
    for key in keys:
        cData = data[key]
        for wKey in cData.keys():
            writerData = cData[wKey]
            indices_to_remove = []
            n = len(writerData)
            for i in range(n):
                label = writerData[i]['label']
                for char in label:
                    if char not in ALPHABET:
                        label = label.replace(char, '')
                if len(label) == 0:
                    indices_to_remove.append(i)
                else:
                    writerData[i]['label'] = label
            indices_to_remove = indices_to_remove[::-1]
            for i in indices_to_remove:
                # print(i)
                del writerData[i]
                

# read pickle file
import pickle

# Open the pickle file in binary read mode
with open(IMG_FILE, 'rb') as file:
    data = pickle.load(file)

remove(data)

saveTo = IMG_FILE_CLEANED
with open(saveTo, 'wb') as file:
    pickle.dump(data, file)

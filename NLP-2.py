from collections import Counter

filePath = open("metu.txt", "r", encoding="utf-8")
read = filePath.read()
dataSet = read.lower().split("\n")
taggim = []

countBeginTags=[]

for sentence in dataSet[:3960]:
   for tags in sentence.split():
       taggim.append(tags.split("/")[1])

countTaggim = Counter(taggim)


for i in dataSet[:3960]:
    countBeginTags.append(i.split()[0].split("/")[1])
init = Counter(countBeginTags)

for key in taggim:

    if key not in init:
        init.update({key: 0})

#  BU KOD TASK 1 A NIN SONUCU
# for x in init:
#     print("Probability of Starting With", x,"   : ", init[x]/3960)

bigram=""
tagsBigram = []

for a in range(len(taggim)-1):
    bigram += taggim[a] +" "+ taggim[a+1]
    tagsBigram.append(bigram)
    bigram=""

countBigramTags = Counter(tagsBigram)

# TASK 1 - 2. YI YAZDIRIR
# for y in countBigramTags:
#     print("Probability of",y, " :", countBigramTags[y]/countTaggim[y.split()[0]])
emmisionList = read.lower().split()
countEmmission = Counter(emmisionList)


#  TASK 1  3. KISIM YAZDIRILIYOR
# for k in countEmmission:
#     print("Probability of", k,":" , countEmmission[k]/countTaggim[k.split("/")[1]])


# -----------------------------------
# -----------------------------------
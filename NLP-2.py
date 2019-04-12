from collections import Counter
import math
import numpy as np
from operator import itemgetter
import json
LOW_PROB = float(0.0000000000001)
print("-----------\n TASK 1\n-----------")
filePath = open("metu.txt", "r", encoding="utf-8")
read = filePath.read()
dataSet = read.lower().split("\n")
taggim = []

wordList = []
startProbability = dict()
transitionProbability = dict()
emmisionProbability = dict()

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
for x in init:
    startProbability[x] = init[x]/3960
print("Start Probability Dict is",startProbability)
bigram=""
tagsBigram = []

for a in range(len(taggim)-1):
    bigram += taggim[a] +" "+ taggim[a+1]
    tagsBigram.append(bigram)
    bigram=""

countBigramTags = Counter(tagsBigram)

# TASK 1 - 2. YI YAZDIRIR
for y in countBigramTags:
    transitionProbability[y.split()[0]] = dict()
for y in countBigramTags:
    transitionProbability[y.split()[0]].update({y.split()[1] : countBigramTags[y]/countTaggim[y.split()[0]]})


print("Transition Probability Dict is" , transitionProbability)



emmisionList = read.lower().split()
countEmmission = Counter(emmisionList)


#  TASK 1  3. KISIM YAZDIRILIYOR
for k in countEmmission:
    emmisionProbability[k.split("/")[1]] = dict()
for k in countEmmission:
    emmisionProbability[k.split("/")[1]].update({k.split("/")[0]: countEmmission[k]/countTaggim[k.split("/")[1]]})
    # print("Probability of", k,":" , countEmmission[k]/countTaggim[k.split("/")[1]])
print("Emmision Probability Dict is", emmisionProbability)

print("-----------\n TASK 2 \n-----------")

# -----------------------------------
# -----------------------------------


sentenceList = []

for i in dataSet[3960:]:
    sentencim = []
    for s in i.split():
        sentencim.append(s.split("/")[0])
    sentenceList.append(sentencim)

def bigram_viterbi(observation, tags, start_prob, transition_prob, emission_prob):
    viterbiMatrix = {}

    backpointer = {}
    backpointers=[]
    probabilities =[]
    observation_length = len(observation)
    for tag in tags:
        firstWord = observation[0]
        viterbiMatrix[0, tag] = (start_prob.get(tag, 0) * emission_prob[tag].get(firstWord, LOW_PROB))
        backpointer[0, tag] = None
    backpointers.append(backpointer)
    probabilities.append(viterbiMatrix)
    # first word given
    # ================================= Viterbi 1 =================================================

    for time, word in enumerate(observation[1:], start=1):
        probs = {}
        for tag in tags:
            maxProbs = []

            for prevTag, prevProb in probabilities[time-1].items():
                probability={(time, tag):prevProb* transitionProbability.get(prevTag[1],0).get(tag, LOW_PROB) * emmisionProbability.get(tag, 0).get(word, LOW_PROB)}
                maxProbs.append((prevTag, probability))



            # max probsun içinde en yüksek olasılıklıyı bul probsa ekle probsun içinde backpointer ın yanına da koyabilirsin

        quit()

        #================================= Viterbi 2 =================================================

    # for time_step, word in enumerate(observation[1:], start=1):
    #     for tag in tags:
    #         # max probability for the viterbi matrix
    #         viterbiMatrix[time_step, tag] = max(
    #             viterbiMatrix[time_step - 1, prev_tag] *
    #             transition_prob.get((tag, prev_tag), 0) *
    #             emission_prob.get((word, tag), 0) for prev_tag in tags)
    #         # argmax for the backpointer
    #         probability, state = max(
    #             (viterbiMatrix[time_step - 1, prev_tag] *
    #              transition_prob.get((tag, prev_tag), 0),
    #              prev_tag) for prev_tag in tags)
    #         backpointer[time_step, tag] = state
    #
    #         # Termination steps
    #         viterbiMatrix[observation_length, "Punc"] = max(viterbiMatrix.get((observation_length - 1, tag), 0) * transition_prob.get((tag, "Punc"), 0) for tag in tags)
    #         probability, state = max(
    #             (viterbiMatrix.get((observation_length - 1, tag), 0) *
    #              transition_prob.get((tag, "Punc"), 0), tag) for tag in tags)
    #         backpointer[observation_length, "Punc"] = state
    #
    #         # Return backtrace path...
    #         backtrace_path = []
    #         previous_state = "Punc"
    #         for index in range(observation_length, 0, -1):
    #             state = backpointer.get((index, previous_state),0)
    #             backtrace_path.append(state)
    #             previous_state = state
    #         # We are tracing back through the pointers, so the path is in reverse
    #         backtrace_path = list(reversed(backtrace_path))
    #         return backtrace_path








taggim = list(set(taggim))
for sentence in sentenceList:
    print(bigram_viterbi(sentence, taggim, startProbability, transitionProbability, emmisionProbability) )
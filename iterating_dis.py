

test_scores ={
    "Honda":100,
    "Bajaj":200,
    "Hero":120,
    "yamaha":150,
    "Royal":350
}
# print(test_scores.keys())

# for biker in test_scores.keys():
#     print(biker)

# for biker in test_scores.values():
#     print(biker)    

# total =0

# for score in test_scores.values():
#     total+=score
#     print(total/len(test_scores))

for key in test_scores.keys():
    print(key,test_scores[key])
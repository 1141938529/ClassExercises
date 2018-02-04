# 有钱、帅气、勤劳、勇敢、有爱的零
# 穷逼、丑比、懒惰、怂包、无爱的一
# 有钱、帅气、懒惰、勇敢、无爱的二
# 穷逼、帅气、勤劳、怂包、有爱的三
# 有钱、丑比、勤劳、勇敢、无爱的四

personList = [
    "有钱、帅气、勤劳、勇敢、有爱的零",
    "穷逼、丑比、懒惰、怂包、无爱的一",
    "有钱、帅气、懒惰、勇敢、无爱的二",
    "穷逼、帅气、勤劳、怂包、有爱的三",
    "有钱、丑比、勤劳、勇敢、无爱的四"]
maxScore = 0
maxPerson = None
for person in personList:
    score = 0
    if( person.find("有钱")!=-1):
        score += 1
    if (person.find("帅气") != -1):
        score += 1
    if (person.find("勤劳") != -1):
        score += 1
    if (person.find("勇敢") != -1):
        score += 1
    if (person.find("有爱") != -1):
        score += 1
    print(person, score)
    if (score>maxScore):
        maxScore = score
        maxPerson = person
    # print(person,score)
print(maxPerson,maxScore)



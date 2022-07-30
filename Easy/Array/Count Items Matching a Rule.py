def countMatches(items, ruleKey, ruleValue):
    count = 0
    for x in items:
            if ruleKey == "type":
                if x[0] == ruleValue:
                    count += 1
            elif ruleKey == "color":
                if x[1] == ruleValue:
                    count += 1
            elif ruleKey == "name":
                if x[2] == ruleValue:
                    count += 1

    return count



print(countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"))
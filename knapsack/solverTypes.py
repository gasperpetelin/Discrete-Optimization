import numpy as np

class DefaultOrder:
    def __init__(self, item_count, capacity, items):
        self.capacity = capacity
        self.items = items;
        self.value = 0
        self.weight = 0
        self.taken = [0] * len(items)

    def solve(self):
        for item in self.items:
            if self.weight + item.weight <= self.capacity:
                self.taken[item.index] = 1
                self.value += item.value
                self.weight += item.weight

        return (self.value, self.weight, self.taken)

class SmallestWeightFirst:
    def __init__(self, item_count, capacity, items):
        self.capacity = capacity
        self.items = items;
        self.value = 0
        self.weight = 0
        self.taken = np.array([0] * len(items))

    def solve(self):

        self.items = sorted(self.items, key=lambda x: x.weight)
        for item in self.items:
            if self.weight + item.weight <= self.capacity:
                self.taken[item.index] = 1
                self.value += item.value
                self.weight += item.weight

        return (self.value, self.weight, self.taken)

class MostValuedFirst:
    def __init__(self, item_count, capacity, items):
        self.capacity = capacity
        self.items = items;
        self.value = 0
        self.weight = 0
        self.taken = [0] * len(items)

    def solve(self):

        self.items = sorted(self.items, key=lambda x: x.value)
        self.items = reversed(self.items)

        for item in self.items:
            if self.weight + item.weight <= self.capacity:
                self.taken[item.index] = 1
                self.value += item.value
                self.weight += item.weight

        return (self.value, self.weight, self.taken)

class WeightValueRation:
    def __init__(self, item_count, capacity, items):
        self.capacity = capacity
        self.items = items;
        self.value = 0
        self.weight = 0
        self.taken = [0] * len(items)

    def solve(self):

        self.items = sorted(self.items, key=lambda x: x.weight / x.value)

        for item in self.items:
            if self.weight + item.weight <= self.capacity:
                self.taken[item.index] = 1
                self.value += item.value
                self.weight += item.weight

        return (self.value, self.weight, self.taken)


class BranchAndBound:
    def __init__(self, item_count, capacity, items):
        self.items = items
        self.itemsCount = item_count
        self.capacity = capacity
        self.taken = [0] * len(items)

    def solve(self):

        self.solutionWeight = self.capacity*2
        self.solutionValue = 0
        self.solutionVector = None

        self.recSolve(0, 0, 0, self.taken)
        #self.taken[0]=1
        #self.recSolve(0, self.items[0].weight, self.items[0].value, self.taken)
        return (self.solutionWeight, self.solutionValue , self.solutionVector)


    def recSolve(self, itemNumber, currentWeight, currentPrice, listOfItems):

        if currentWeight>self.capacity:
            return

        if itemNumber >= self.itemsCount:
            #print(listOfItems, currentWeight, currentPrice)
            if currentWeight<=self.capacity:

                if currentPrice == self.solutionValue:
                    if self.solutionWeight < currentWeight:
                        self.solutionWeight = currentWeight
                        self.solutionValue = currentPrice
                        self.solutionVector = listOfItems.copy()

                if currentPrice>self.solutionValue:
                    #if self.solutionWeight>currentWeight:
                    self.solutionWeight = currentWeight
                    self.solutionValue = currentPrice
                    self.solutionVector = listOfItems.copy()


            return

        #left
        self.recSolve(itemNumber + 1, currentWeight, currentPrice, listOfItems)

        #right
        #if currentWeight+self.items[itemNumber].weight<=self.capacity:
        listOfItems[itemNumber] = 1
        self.recSolve(itemNumber + 1, currentWeight+self.items[itemNumber].weight, currentPrice+self.items[itemNumber].value, listOfItems)
        listOfItems[itemNumber] = 0


        #if itemNumber==self.itemsCount:
        #    if self.solutionValue<currentPrice:
        #        self#.solutionWeight = currentWeight
        #        self.solutionValue = currentPrice
        #        self.solutionVector = listOfItems.copy()
        #    #print(listOfItems, "w", currentWeight, "P", currentPrice)

        #if itemNumber +1<=self.itemsCount:

        #    #right
        #    x = currentWeight+self.items[itemNumber].weight
        #    if x<=self.capacity:
        #        listOfItems[itemNumber] = 1
        #        self.recSolve(itemNumber + 1, x, currentPrice+self.items[itemNumber].value, listOfItems)
        #        listOfItems[itemNumber] = 0

        #    #left
        #    self.recSolve(itemNumber +1, currentWeight, currentPrice, listOfItems)








#class BranchAndBound:
#    def __init__(self, item_count, capacity, items):
#        self.capacity = capacity
#        self.items = items;
#        self.value = 0
#        self.weight = 0
#        self.taken = [0] * len(items)
#
#    def solve(self):
#        self.items = sorted(self.items, key=lambda x: x.weight / x.value)
#
#
#        for item in self.items:
#            if self.weight + item.weight <= self.capacity:
#                self.value += item.value
#                self.weight += item.weight
#            else:
#                remaningWeight = self.capacity-self.weight
#                self.value += (remaningWeight/item.weight)*item.value
#                break
#        self.optimisticprediction = self.value #best possible value
#        self.value = 0
#        self.weight = 0
#
#        self.bestprediction = float('-inf')
#
#        self.bestweightCopy = 0
#        self.bestvalueCopy = 0
#        self.bestarrayCopy = None
#
#
#        self.recSolve(0, 0, 0, self.taken, self.optimisticprediction)
#
#        #print("-----------", self.bestweightCopy, self.bestvalueCopy, self.bestarrayCopy)
#        return (self.bestvalueCopy, self.bestweightCopy, self.bestarrayCopy)
#
#    def recSolve(self, itemToAdd, currentWeight, currentPrice, listOfItems, bestPosible):
#
#        if itemToAdd>=len(listOfItems):
#            if(currentWeight<=self.capacity):
#                #print(listOfItems, "v", currentPrice, "w", currentWeight, "best", bestPosible)
#                if self.bestvalueCopy<currentPrice:
#                    self.bestvalueCopy =  currentPrice
#                    self.bestweightCopy = currentWeight
#                    self.bestarrayCopy = listOfItems.copy()
#                    self.bestprediction = bestPosible
#
#            return
#
#        listOfItems[itemToAdd] = 1
#        self.recSolve(itemToAdd + 1, currentWeight + self.items[itemToAdd].weight, currentPrice + self.items[itemToAdd].value, listOfItems, bestPosible)
#        listOfItems[itemToAdd] = 0
#
#        self.recSolve(itemToAdd + 1, currentWeight, currentPrice, listOfItems, bestPosible-self.items[itemToAdd].value)  # not adding item










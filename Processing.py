from uobitems import uobitems
from allredemption import allredemption
from collections import Counter
import operator
import datetime

def processtrenditems(name,cardno):
    trend_items =[]
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point = []
        for points in avaliableuobpts_file:
            pt =points.split(",")
            point.append(int(pt[2]))
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[1] == "Nike Voucher" or individual_items[1] == "Shaw Theatre Tickets" or individual_items[1] == "Swensen's Voucher"):
            if (points >= int(individual_items[3])):
                t = uobitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6],individual_items[7])
                trend_items.append(t)
    return trend_items

def processallitems(name,cardno):
    allitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point = []
        for points in avaliableuobpts_file:
            pt =points.split(",")
            point.append(int(pt[2]))
        points = point[-1]
        individual_items = a.split(",")
        if (points >= int(individual_items[3])):
            c = uobitems(individual_items[1], individual_items[2], individual_items[3],
                individual_items[4], individual_items[5], individual_items[6],individual_items[7])
            allitems.append(c)
    return allitems


def processretailitems(name,cardno):
    retailitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point=[]
        for points in avaliableuobpts_file:
            pt =points.split(",")
            point.append(int(pt[2]))
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[0] == "Retail"):
            if (points >= int(individual_items[3])):
                c = uobitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6],individual_items[7])
                retailitems.append(c)
    return retailitems

def processdiningitems(name,cardno):
    diningitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point = []
        for points in avaliableuobpts_file:
            pt =points.split(",")
            point.append(int(pt[2]))
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[0] == "Dining"):
            if (points >= int(individual_items[3])):
                d = uobitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6],individual_items[7])
                diningitems.append(d)
    return diningitems


def processleisureitems(name,cardno):
    leisureitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point = []
        for points in avaliableuobpts_file:
            pt =points.split(",")
            point.append(int(pt[2]))
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[0] == "Leisure"):
            if (points >= int(individual_items[3])):
                e = uobitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6],individual_items[7])
                leisureitems.append(e)
    return leisureitems



def processpoints(name,cardno):
    #uob_allpoints =[]
    uob_currentpts = 0
    avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
    for j in avaliableuobpts_file:
        transaction = j.split(",")
        if transaction[0] == name and transaction[1] == cardno:
            uob_currentpts = transaction[2]
     #           uob_allpoints.append(int(transaction[2]))
    #uob_currentpts = uob_allpoints[-1]
    return uob_currentpts


# in transaction history of redemption
def processallredemption(name,cardno):
    allredemptionList =[]
    allredemption_file = open("file/allredemption.txt", "r")
    for i in  allredemption_file:
        list = i.split(',')
        if list[0] == name:
            s = allredemption(list[1], list[2], list[3], list[4], int(list[5]),list[6])
            allredemptionList.append(s)
    return allredemptionList

def processalluobredemption(name, cardno):
    alluobredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            bank = list[2].split(" ")
            if bank[0] == "UOB":
                y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                alluobredemptionList.append(y)
    return alluobredemptionList

def processallocbcredemption(name, cardno):
    allocbcredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            bank = list[2].split(" ")
            if bank[0] == "OCBC":
                y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                allocbcredemptionList.append(y)
    return allocbcredemptionList

def processalldbsredemption(name, cardno):
    alldbsredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            bank = list[2].split(" ")
            if bank[0] == "DBS":
                y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                alldbsredemptionList.append(y)
    return alldbsredemptionList

def processsallnovredemption(name, cardno):
    allnovredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1]== "11" and individual[2]=="2017":
                z = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                allnovredemptionList.append(z)
    return allnovredemptionList

def processuobnovredemption(name, cardno):
    uobnovredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1] == "11" and individual[2]=="2017":
                bank = list[2].split(" ")
                if bank[0] == "UOB":
                    y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    uobnovredemptionList.append(y)
    return uobnovredemptionList

def processocbcnovredemption(name, cardno):
    ocbcnovredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1] == "11" and individual[2]=="2017":
                bank = list[2].split(" ")
                if bank[0] == "OCBC":
                    y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    ocbcnovredemptionList.append(y)
    return ocbcnovredemptionList

def processdbsnovredemption(name, cardno):
    dbsnovredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1] == "11" and individual[2]=="2017":
                bank = list[2].split(" ")
                if bank[0] == "DBS":
                    y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    dbsnovredemptionList.append(y)
    return dbsnovredemptionList

def processsalldecredemption(name, cardno):
    alldecredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1] == "12" and individual[2]=="2017":
                z = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                alldecredemptionList.append(z)
    return alldecredemptionList

def processuobdecredemption(name, cardno):
    uobdecredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1] == "12" and individual[2]=="2017":
                bank = list[2].split(" ")
                if bank[0] == "UOB":
                    y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    uobdecredemptionList.append(y)
    return uobdecredemptionList

def processocbcdecredemption(name, cardno):
    ocbcdecredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1] == "12" and individual[2]=="2017":
                bank = list[2].split(" ")
                if bank[0] == "OCBC":
                    y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    ocbcdecredemptionList.append(y)
    return ocbcdecredemptionList

def processdbsdecredemption(name, cardno):
    dbsdecredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1] == "12" and individual[2]=="2017":
                bank = list[2].split(" ")
                if bank[0] == "DBS":
                    y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    dbsdecredemptionList.append(y)
    return dbsdecredemptionList
"""
def processnumberquantity(name, cardno):
    uob_points=[]
    uobpts_file = open("file/avaliableuobpts.txt", "r")
    for points in uobpts_file:
        point = points.split(",")
        if point[0] == name:
            if point[1] == cardno:
                uob_points.append(int(point[2]))
    uobcurrentpts = int(uob_points[-1])

    alluobitems = open("file/uobitems.txt", "r")

    for items in alluobitems:
        items = items.split(",")
        individual = uobitems(items[1], items[2], items[3], items[4],
                                    items[5],items[6], items[7])

        if (uobcurrentpts >= int(individual.get_points())):
            quantity = uobcurrentpts // int(individual.get_points())
            individual.set_maxquantity(quantity)
            return individual.get_maxquantity()

def list_qty(name, cardno):
    qty = processnumberquantity(name, cardno)
    quantity_option = []
    for num in range(qty):
        num += 1
        quantity_option.append(num)
    return quantity_option
"""

def processpreferreduob(name, cardno):
    uobpreferredList=[]
    qtyanditemdictionary = processget_quantityuob(name)  # returns a dictionary; {user:[[item1,qty1] , [] , [] ]
    qtyanditem = qtyanditemdictionary[name]
    alluobitems = open("file/uobitems.txt", "r")
    for individual in alluobitems:
        individual= individual.strip()
        individual=individual.split(",")
        b = individual[7]
        for i in qtyanditem:
            itemname=i[0]
            qty = i[1]
            if str(itemname) == str(b):
                preferreditems = uobitems(individual[1], individual[2], individual[3], individual[4],
                                            individual[5],individual[6], individual[7])
                preferreditems.set_count(int(qty))
                currentcount = preferreditems.get_count()
                uobpreferredList.append(preferreditems)
    return uobpreferredList

def processget_quantityuob(name):
    dictionary={}
    dictvalue = []
    allredemption_file = open("file/allredemption.txt", "r")
    for redeemed in allredemption_file:
        lists = redeemed.split(",")
        bank = lists[2].split(" ")
        if lists[0] == name and bank[0] == "UOB":
            individualitemandqty = []
            individualitemandqty.append(lists[4])
            individualitemandqty.append(int(lists[5]))
            dictvalue.append(individualitemandqty)

    totals = {}
    for k, v in dictvalue:
        totals[k] = totals.get(k, 0) + v
    dictvalue = sorted(map(list, totals.items()))
    dictvalue = sorted(dictvalue, key=operator.itemgetter(1), reverse=True)


    if (len(dictvalue))> 3:
        empty = []
        for i in range(3):
            value = dictvalue[i]
            empty.append(value)
        print(empty)
        dictionary[name] = empty

    else:
        dictionary[name] = dictvalue
    return dictionary



def addtocart(user, cardno,current_point, redeem_point, points, quantity):
    amount = int(points) * int(quantity)
    avaliableuobpts_file = open("file/avaliableuobpts.txt", "a")
    avaliableuobpts_file.write(user, cardno,int(current_point) - amount)
    avaliableuobpts_file.close()
    currentpoint_file = open("file/currentuobpts.txt", "a")
    currentpoint_file.write(user, cardno,int(redeem_point) + amount)
    currentpoint_file.close()



#def removefromcart(self, user, cardno,current_point, redeem_point, points, quantity):
#    avaliableuobpts_file = open("file/avaliableuobpts.txt", "a")
#    avaliableuobpts_file.write(user, cardno,int(current_point) - amount)
#    avaliableuobpts_file.close()
#    currentpoint_file = open("file/currentuobpts.txt", "a")
#    currentpoint_file.write(user, cardno,int(redeem_point) + amount)
#    currentpoint_file.close()




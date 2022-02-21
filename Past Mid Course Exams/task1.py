days  = int(input())
numberOfPeople = int(input())
avrNumberLapsPerPeople = int(input())
lapLenth = int(input())
capOtTheRoad = int(input())
moneyPerKm = float(input())
maxRunners = capOtTheRoad * days
if numberOfPeople <= maxRunners:
        TotalMeters = numberOfPeople * avrNumberLapsPerPeople * lapLenth
else:
        TotalMeters = maxRunners * avrNumberLapsPerPeople * lapLenth
TotalKM = TotalMeters / 1000
MoneyPaid = TotalKM * moneyPerKm
print('Money raised: {0:.2f}'.format(MoneyPaid))

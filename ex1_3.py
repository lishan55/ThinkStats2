import survey
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

#1.3-2
count = 0
for i in table.records:
    if i.outcome == 1:
        count += 1
print 'Numer of live births: ', count

#1.3-3
first = 0
others = 0
for i in table.records:
    if i.birthord == 1:
        first += 1
    elif i.birthord > 1 and i.birthord != 'NA':
        others += 1
print 'Numer of 1st births: ', first
print 'Numer of other births: ', others

#1.3-4
first_avg = 0
first_count = 0
others_avg = 0
others_count = 0
for i in table.records:
    if i.birthord == 1:
        first_avg += i.prglength
        first_count += 1
    elif i.birthord > 1 and i.birthord != 'NA':
        others_avg += i.prglength
        others_count += 1
first_avg = float(first_avg) / first_count
print "Average pregnancy length for first babies: ", first_avg
others_avg = float(others_avg) / others_count
print "Average pregnancy length for other babies: ", others_avg
print "Difference in days: ", first_avg - others_avg

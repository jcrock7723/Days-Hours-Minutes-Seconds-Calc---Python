#Problem #15 pg 119 InClass
#input
seconds=int(input('Enter the number of seconds: '))

#processing
#output

if seconds >= 86400:
    ansNum=seconds/86400
    ansStr='days'
    print(format(seconds/86400, '.0f'), 'Days')
    ansRemh=seconds%86400
    print(format(ansRemh/3600, '.0f'), 'Hours')
    ansRemm=ansRemh%3600
    print(format(ansRemm/60, '.0f'), 'Minutes')
    ansRems=ansRemm%60
    print(ansRems, 'Seconds')
elif seconds >= 3600:
    ansNum=seconds/3600
    ansStr='hours'
    print(format(0/86400, '.0f'), 'Days')
    ansRemh=seconds%86400
    print(format(ansRemh/3600, '.0f'), 'Hours')
    ansRemm=ansRemh%3600
    print(format(ansRemm/60, '.0f'), 'Minutes')
    ansRems=ansRemm%60
    print(ansRems, 'Seconds')
elif seconds >= 60:
    ansNum=seconds/60
    ansStr='minutes'
    print(format(0/86400, '.0f'), 'Days')
    ansRemh=seconds%86400
    print(format(0/3600, '.0f'), 'Hours')
    ansRemm=ansRemh%3600
    print(format(ansRemm/60, '.0f'), 'Minutes')
    ansRems=ansRemm%60
    print(ansRems, 'Seconds')
elif seconds >0:
    ansNum=seconds
    ansStr='seconds'
    print(format(0/86400, '.0f'), 'Days')
    ansRemh=seconds%86400
    print(format(0/3600, '.0f'), 'Hours')
    ansRemm=ansRemh%3600
    print(format(0/60, '.0f'), 'Minutes')
    ansRems=ansRemm%60
    print(ansRems, 'Seconds')


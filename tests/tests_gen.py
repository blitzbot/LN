def testGen(h, m):
    hour = str(h) 
    minute = str(m)

    if h < 10:
        hour = '0' + hour
    if m < 10:
        minute = '0' + minute

    file = open(hour + '_' + minute + '.txt', 'w')
    
    output = hour + ':' + minute
    counter = 0
    for i in range(len(output)):
        file.write(str(counter) + '\t' + str(counter + 1) + '\t' + output[i] + '\t' + output[i] + '\n')
        counter = counter + 1
    file.write(str(counter))


if __name__ == "__main__":
    for h in range(24):
        for m in range(60):
            testGen(h, m)

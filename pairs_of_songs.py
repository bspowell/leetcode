# list of songs
# every ith song has a duration of time[i] seconds
# return the number of pairs of songs for which their total duration is divisible by 60
# where i < j with (time[i] + time[j]) % 60 == 0


# Algo
# Use a hash table to store the % 60 remainder of each of the values in array
# If current num % 60 isn't in hash, store as key, with value of count 1
# Find complement of currrent num = 60 - (num % 60)
# If complement is not in hash, then no pairs so far
# 


def numPairsDivisibleBy60(time):
    hash = {}
    pairs = 0 

    for num in time:
        current = num % 60
        complement = 60 - (num % 60)

        if current not in hash:
            hash[current] = 1
        else: 
            hash[current] += 1
        
        if complement in hash:
            pairs += hash[complement]

    return pairs
          


time = [30,20,150,100,40]
print(numPairsDivisibleBy60(time))
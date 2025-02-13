def enrollment_stats(l):
    enrollment = []
    fees = []
    for i in range(len(l)):
        enrollment.append(l[i][1])
        fees.append(l[i][2])
    return enrollment, fees

def mean(l):
    m = sum(l)/len(l)
    return m

def median(l):
    a = sorted(l)
    m = a[len(l)//2]
    return m

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

l1, l2 = enrollment_stats(universities)
print(f"Total students: {sum(l1)}")
print(f"Total tuetion: {sum(l2)}")
print(f"Student mean: {mean(l1)}")
print(f"Student meadian: {median(l1)}")
print(f"Tuition mean: {mean(l2)}")
print(f"Tuition median: {median(l2)}")

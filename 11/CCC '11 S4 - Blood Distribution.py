units = [int(x) for x in input().split(" ")]
patients = [int(x) for x in input().split(" ")]

u_or = units.copy()
p_or = patients.copy()

# 0 O-
# 1 O+ 
# 2 A-
# 3 A+
# 4 B-
# 5 B+
# 6 AB-
# 7 AB+

def blood(p, u):
    give = min(units[u],patients[p])
    units[u] -= give
    patients[p] -= give

    return give

total = 0
#NEGATIVE FIRST
#O-
total += blood(0,0)
#O+
total += blood(1,1)
total += blood(1,0)
#A-
total += blood(2,2)
total += blood(2,0)
#B-
total += blood(4,4)
total += blood(4,0)

#A+ 
total += blood(3,3)
total += blood(3,1)
#B+
total += blood(5,5)
total += blood(5,1)
#A+
total += blood(3,2)
total += blood(3,0)
#B+
total += blood(5,4)
total += blood(5,0)


#AB- 
total += blood(6,6)
total += blood(6,4)
total += blood(6,2)
total += blood(6,0)

#AB+
total += blood(7,7)
total += blood(7,6)
total += blood(7,5)
total += blood(7,4)
total += blood(7,3)
total += blood(7,2)
total += blood(7,1)
total += blood(7,0)


total1 = 0

units, patients = u_or, p_or
#O FIRST       
#O-
total1 += blood(0,0)
#O+
total1 += blood(1,1)
total1 += blood(1,0)
#A-
total1 += blood(2,2)
total1 += blood(2,0)
#B-
total1 += blood(4,4)
total1 += blood(4,0)

#A+ 
total1 += blood(3,3)
total1 += blood(3,2)
#B+
total1 += blood(5,5)
total1 += blood(5,4)
#A+
total1 += blood(3,1)
total1 += blood(3,0)
#B+
total1 += blood(5,1)
total1 += blood(5,0)

#AB- 
total1 += blood(6,6)
total1 += blood(6,4)
total1 += blood(6,2)
total1 += blood(6,0)

#AB+
total1 += blood(7,7)
total1 += blood(7,6)
total1 += blood(7,5)
total1 += blood(7,4)
total1 += blood(7,3)
total1 += blood(7,2)
total1 += blood(7,1)
total1 += blood(7,0)

print(max(total,total1))
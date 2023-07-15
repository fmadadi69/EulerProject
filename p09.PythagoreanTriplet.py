def pythagorean_triplet(triple_sum):
    for a in range(triple_sum):
        for b in range(triple_sum):
            for c in range(triple_sum):
                if a<b<c and a+b+c == triple_sum:
                    #print(a,b,c)
                    if (a**2)+(b**2)==(c**2):
                        print(a,b,c)
                        print(a*b*c)

pythagorean_triplet(1000)

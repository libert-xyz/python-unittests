def is_multiple(i,n):
    result = i % n
    if result == 0:
        return True
    else:
        return False

l = []
def bizBuzz():
    for i in range(1,101):
        if is_multiple(i,3) and is_multiple(i,5):
            l.append('bizzBuzz')
        elif is_multiple(i,3):
            l.append('bizz')
        elif is_multiple(i,5):
            l.append('Buzz')

        else:
            l.append(i)

    return l


#print(bizBuzz())

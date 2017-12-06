#99 bottles of beer

i = 99
while i:
    if i > 1:
        print("{0} bottles of beer on the wall, {0} bottles of beer.".format(i))
        i -= 1
        print("Take one down an pass it around, {0} bottles of beer on the wall\n".format(i))
    else:
        print("{0} bottle of beer on the wall, {0} bottle of beer.".format(i))
        i -= 1
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")
print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store by some more, 99 bottles of beer on the wall")

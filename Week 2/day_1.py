the_bix_six =["Arsenal","Manchester City","Manchester United","Chelsea","Tottenham"]

the_bix_six[4] = "Liverpool"

the_bix_six.append("Tottenham")
the_bix_six.insert(1,"Aston Villa")

the_bix_six.pop(0)

#len(the_bix_six)

the_bix_six.remove("Manchester United")
the_bix_six.reverse()

print(the_bix_six)


#repitition
greet = ["Hey"]

repeat = greet * 5


#print (repeat)

#membership
num = [1,2,3,4,5,6,7,8]

has_in = 12 in num

#print(has_in)

#concantination
a=[1,2,3,4,5]
b=[1,2,3,4,5,6]
#concat = a + b

#print(a + b)

# TUPLE

colors = ("red", "blue", "yellow")
 #colors[2] = "green" # Doen't work because tuples are immutable

 #Repitition
many_reds = colors[0] * 10

concat = colors + ("white", "black")

print(
  colors, many_reds, concat
  )

# Slicing
num = (1,2,3,4,5,6,7,8,9,10)

the_cut_a = num[0:4]

the_cut_b = num[-5:-1]

the_cut_c = num[-5:-1]


# set
a = {1,2,3,4,5,7,1}
b = {12, 4, 13, 14.5,1}

union = a | b # a. intersection(b)
intersection = a & b #a.intersection(b)
difference = a - b # a.difference(b)

collection_of_set_data = {"a", "b", "c"}

collection_of_set_data.add ("d")
collection_of_set_data.remove ("f")


#collection_of_set_data.discard("c")

print(collection_of_set_data)



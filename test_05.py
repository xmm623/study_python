# from random import randint
# print(randint(1,6))

# from random import choice
# players = ['charles','martina','michael','florence','eli']
# first_up = choice(players)
# print(first_up)


from random import choice
lottery_tickets = (1,2,3,4,5,6,7,8,9,0,'a','B','C','d','e')
lucky_tickets = []
while len(lucky_tickets) < 4:
    pulled_item = choice(lottery_tickets)
    if pulled_item not in lucky_tickets:
        lucky_tickets.append(pulled_item)

print(lucky_tickets)
# my_tickets = ()
# Flag = True
# while Flag:
#     my_tickets = sample(lottery_tickets,4)
#     for lucky in my_tickets:
#         for really in lucky_tickets:
#             if lucky == really:
#                 break
#             else:
#                 Flag = False

    
        


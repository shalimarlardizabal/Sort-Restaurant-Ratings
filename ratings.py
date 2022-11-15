"""Restaurant rating lister."""


def restaurant_rate(filename):

    file = open(filename)
    rating = {}
    
    # while True:

    #     user_input = input("Would ")

    new_restaurant = input("Restaurant Name: ")
    new_score = int(input("Restaurant Score: "))
    
    # while new_score not in range(5):
    #     new_score = input("Please enter 1-5 for score: ")
    
    while new_score < 1 or new_score > 5:
        new_score = int(input("Please enter"))
        

    rating[new_restaurant] = new_score
    
    for line in file:
        restaurant, rate = line.rstrip().split(":")[:2]
        rating[restaurant]= rate
    
    sorted_rating = sorted(rating)

    for restaurant in sorted_rating: 
        print(f' {restaurant} is rated {rating[restaurant]}')



restaurant_rate('scores.txt')
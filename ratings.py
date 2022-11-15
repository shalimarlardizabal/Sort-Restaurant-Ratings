"""Restaurant rating lister."""


def restaurant_rate(filename):

    file = open(filename)
    rating = {}
        
    while True:
        
        print("Please input S, A, or Q")
        user_input = input("Would you like to See all the ratings, Add new restaurant, or Quit? >")
        user_input = user_input.upper().strip() 
        
        if user_input == "Q":
            break
        
        elif user_input == "S":
            for line in file:
                restaurant, rate = line.rstrip().split(":")[:2]
                rating[restaurant]= rate
    
            sorted_rating = sorted(rating)

            for restaurant in sorted_rating: 
                print(f' {restaurant} is rated {rating[restaurant]}')

        elif user_input == "A":
            new_restaurant = input("Restaurant Name: ")
            new_score = int(input("Restaurant Score: "))
                     
            if new_score not in range(5):
                new_score = int(input("Please enter 1-5 for score: "))
            
            rating[new_restaurant] = new_score
                  
restaurant_rate('scores.txt')
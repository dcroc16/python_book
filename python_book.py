
def pick_a_program():
    program_names = [
            '1.1 Favorite Ice Cream',
            '1.2 Print Name and Wait',
            '1.3 Favorite Quote',
            '2.2 Favorite Food Mashup',
            '2.3 Tipper App',
            '2.4 Car Salesman',
            '3.1 fortune cookie',
            '3.2 flip a coin',
            '3.3 Guess my Number',
            '3.4 Computer Guess my Number',
            '[EXIT] End Program'

        ]
    print "\n\n\n"
    for i in program_names:
        print i
    choice = raw_input('\n\n\nWhich Program would you like to Run? .....\n')
    return choice

def fav_icecream():
    print "mint chocolate chip"

def print_name():
    print 'Lexi Crocker'

def fav_quote():
    quote = """The Zen of Python, by Tim Peters

              \"Beautiful is better than ugly.
                Explicit is better than implicit.
                Simple is better than complex.
                Complex is better than complicated.
                Flat is better than nested.
                Sparse is better than dense.
                Readability counts.
                Special cases aren't special enough to break the rules.
                Although practicality beats purity.
                Errors should never pass silently.
                Unless explicitly silenced.
                In the face of ambiguity, refuse the temptation to guess.
                There should be one-- and preferably only one --obvious way to do it.
                Although that way may not be obvious at first unless you're Dutch.
                Now is better than never.
                Although never is often better than *right* now.
                If the implementation is hard to explain, it's a bad idea.
                If the implementation is easy to explain, it may be a good idea.
                Namespaces are one honking great idea -- let's do more of those!\""""
    print quote +"\n\n\n"


def fav_food():
    food1 = raw_input("What is your favorite food?  :  ")
    food2 = raw_input("What is your 2nd favorite food?  :  ")
    print "\n\nThen you would really like " + food1 + food2 + "!\n\n"
    
def tipper_app():
    try:
        base_bill = input("How much was your bill? >> ")
    except:
        print "Make sure that you enter a valid number as your bill total."
        tipper_app()
    else:
        print "your bill was %s" % (base_bill)
        print "Possible tips:"
        print "Tip @ 15% " + str(base_bill * 0.15) + " : Total Bill " + str(base_bill + (base_bill * 0.15))
        print "Tip @ 20% " + str(base_bill * 0.20) + " : Total Bill " + str(base_bill + (base_bill * 0.20)
)        
def car_sales_invoice():
    try:
        car_base_price = input("Enter the Car's base prices.................. ")
    except:
        print "Make sure you enter a valid number as the car price"
        car_sales_invoice()
    else:
        tax = car_base_price * 0.15
        license = car_base_price * 0.20
        dealer_prep = 10000
        destination_charge = 20.38
       
        total = car_base_price + tax + license + dealer_prep + destination_charge
       
        print """
                     INVOICE
              ---------------------
             
              Car Base Price..... %s
              tax................ %s
              license............ %s
              dealer prep........ %s
              destination charge. %s
     
              ---------------------
              Total Car Price.... %s""" % (car_base_price, tax, license, dealer_prep, destination_charge, total)


def fortune_cookie():
    fortunes = [
        'fortune 1',
        'fortune 2',
        'fortune 3',
        'fortune 4',
    ]
    import random
    choice = random.randint(0,len(fortunes)-1)
    print fortunes[choice]

def flip_a_coin():
    heads = 0
    tails = 0
    class Coin:
        def __init__(self):
           self.side = "heads"
        def flip(self):
            import random
            result = random.randint(0,1)
            if result:
               self.side = "heads"
               return self.side
            else:
               self.side = "tails"
               return self.side
    c = Coin()
    for i in range(50):
        print "Fliped Coin Result: " +  c.flip()
        if c.side == "heads":
            heads += 1
        else:
            tails += 1

    print "flip results: Heads %s | Tails %s" % (str(heads), str(tails))

def guess_my_number():
    guess = []
    for i in range(10):
        choice = raw_input("pick a number between 1 and 100: ")
    

def computer_guess_my_number():
    pass

def choice_router(program_id):
    programs = {
        '1.1' : fav_icecream,
        '1.2' : print_name,
        '1.3' : fav_quote,
        '2.2' : fav_food,
        '2.3' : tipper_app,
        '2.4' : car_sales_invoice,
        '3.1' : fortune_cookie,
        '3.2' : flip_a_coin,
        '3.3' : guess_my_number,
        '3.4' : computer_guess_my_number
        }
    if program_id in programs:
        programs[program_id]()
    else:
        print "\n\nPROGRAM NOT FOUND! .............\n\n\n"


def main():
    while True:
        choice = pick_a_program()
        if choice == 'EXIT':
            break
        else:
            choice_router(choice)



if __name__ == "__main__":
    main()

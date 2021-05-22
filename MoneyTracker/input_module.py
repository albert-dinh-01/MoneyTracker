"""
    Author: Albert Dinh
    Date: November 8, 2020
"""

# General functions for every class
def handling_number(prompt=''):
    cF = True
    while cF:
        try:
            price = float(input(prompt))
            float(price)
            return price
        except ValueError:
            print('Cannot be converted to a string')
            continue


def name_handling(prompt=''):
    """ Handle string inputs to the programs

    Arguments:
        prompt (string): user-defined prompts
    """
    cF = True
    while cF:
        try:
            name = input(prompt)
            return name
        except EOFError:
            print("User Exited!")


def binary_handling(prompt=''):
    """ Handle yes/no questions
    Args:
        prompt (string): an user-defined prompt
    
    Returns:
        a (bool): a Boolean value
    """
    ans = input(prompt)
    yes_ls = ['yes', '1', 'on', 'y', 'in']
    no_ls = ['no', '0', 'off', 'n']

    while True:
        if ans.lower() in yes_ls:
            a = True
            return a
        elif ans.lower() in no_ls:
            a = False
            return a
        else:
            print('Not a valid answer. Enter either \'yes\' or 1 for YES, or \'no\' or 0 for NO!')
            ans = input(prompt)
            continue


def fetch_category_retailer_grocery():
    """ Return food category and retailer for GROCERY

    Arguments: None

    Returns:
        food_category: (string) a category of food
    """
    prompt1 = 'Enter a grocery category: '
    prompt2 = 'Enter a grocery store: '
    food_category = name_handling(prompt=prompt1)
    retailer = name_handling(prompt=prompt2)

    return food_category, retailer


def get_feedback():
    """ This asks for feedback from the user

    Returns:
        fb (int): a numerical value on scale of 1 - 5
    """
    while True:
        try:
            fb = int(input('Enter your satisfactory level on the scale of 1 to 5: '))
            assert (isinstance(fb, int)), 'Making sure it is a valid rating'
            assert (1 <= fb <= 5), 'Invalid Rating Range'
            return fb
        except ValueError:
            print('Not a valid rating! Please try again!')
            continue
        except AssertionError as ae:
            print(ae)
            continue


def restaurant_name():
    prompt1 = 'Enter the restaurant name: '
    restaurant_name = name_handling(prompt=prompt1)
    return restaurant_name


def get_recommendation():
    """ Get a binary value to whether recommend or not
    
    Arguments: None

    Returns: 
        binary1 (Boolean): answer to yes no quuestion
    """
    binary1 = binary_handling('Would you recommend: ')
    return binary1


def get_categories():
    """ Print all the options
    
    Arguments: None

    Returns:
        category: (string) a category
    """
    category = input('Enter a category: ')
    category_lt = ['grocery', 'eatingout', 'utilities']

    while category.lower() not in category_lt:
        print('Choose from', category_lt)
        category = input('Enter a category: ')
        if category.lower() in category_lt:
            break

    return category.lower()


def get_basic_info():
    """ Return price, onoff, itemname
    
    Arguments: None

    Returns:
        price: (float) price of an item
        onoff: (string) whether on- or off-line
        item_name: (string) the item's name
    """
    p1='Item Price: '
    p2='In-store/Online: '
    p3='Item Name: '
    price = handling_number(prompt=p1)
    store_online = binary_handling(prompt=p2)
    item_name = name_handling(prompt=p3)

    return price, store_online, item_name


def init_basic_info():
    """ Initialize an object of class grocery
    
    Returns:
        price: item price
        onoff: Boolean value
        item_name: item name
    """
    price, onoff, item_name = get_basic_info()

    return price, onoff, item_name


def get_util_category_and_provider():
    """ Get the utility category from the user

    Returns:
        util_category (string): utility category
        
        util_provider (string): utility provider
    """
    util_category = name_handling(prompt='Enter the utilities category: ')
    util_provider = name_handling(prompt='Enter the utilites provider: ')
    return util_category, util_provider


def continue_or_no():
    """ Ask if the user wants to keep continue
    Returns:

        a_decision (Boolean): answer to a yes/no question
    """
    a_decision = binary_handling('Do you want to continue? ')
    return a_decision
"""
Author: Albert Dinh
Date: December 19, 2020

"""
import datetime
import purchases, input_module, email_mod
import dbmodule

def execute_grocery():
    """ Executed when user input GROCERY or any of its variations

    This allows some leeway to add more functionalities
    """
    price, onoff, item_name = input_module.init_basic_info()
    gro_cat, retailer = input_module.fetch_category_retailer_grocery()
    grocery_obj = purchases.Grocery(price, onoff, item_name, gro_cat, retailer)
    grocery_obj.print_retailer()

    return grocery_obj


def execute_eatingout():
    """ Execute when user input EATINGOUT or any of its variations
    
    Returns:
        None
    """
    price, onoff, item_name = input_module.init_basic_info()
    fb = input_module.get_feedback()
    restaurant = input_module.restaurant_name()
    recommend_or_no = input_module.get_recommendation()
    eatingout_obj = purchases.EatingOut(price, onoff, item_name, restaurant, fb, recommend_or_no)
    eatingout_obj.print_eat_out_info()

    return eatingout_obj


def execute_utilities():
    """ Execute when user input UTILITIES or any of its variations

    Args:
        None

    Returns:
        utility_obj (Utilities)
    """
    price, onoff, item_name = input_module.init_basic_info()
    util_type, util_provider = input_module.get_util_category_and_provider()
    utility_obj = purchases.Utilities(price, onoff, item_name, util_type, util_provider)
    utility_obj.print_utilities_info()

    return utility_obj


def execute_subscription():
    """ Deals with subscription services"""
    price, onoff, item_name = input_module.init_basic_info()
    pass


def obj_collector():
    """ Make user interaction and collect data
    Arguments: None
    
    Returns:
        obj_dict (dictionary): a dictionary contains objects of 
                            the three dafault classes
    """ 
    # Initialize variables
    category = input_module.get_categories()
    cf = True
    obj_dict = {'Grocery':[], 'EatingOut':[], 'Utilities':[]}

    while cf:
        if category == 'grocery':
            grocery_obj = execute_grocery()
            obj_dict['Grocery'].append(grocery_obj)
        elif category == 'eatingout':
            eatout_obj = execute_eatingout()
            obj_dict['EatingOut'].append(eatout_obj)
        elif category == 'utilities':
            util_obj = execute_utilities()
            obj_dict['Utilities'].append(util_obj)

        a_decision = input_module.continue_or_no()

        if a_decision:
            category = input_module.get_categories()
        else:
            break

    return obj_dict


def write_to_db(conn, cret, dict_in):
    """ Write a dictionary into a file

    Args:
        dict_in (dictionary): a dictionary whose keys are categories 
                            while their values are objects of the same key

        buff_out (string): a file name to write out the data
    """
    for key in dict_in.keys():
        for obj in dict_in[key]:
            dbmodule.insert_item(conn=conn, cret=cret, an_item=obj)


def main():
    """ Take in info from the user and write out to a buffer file
    """
    conn, cret = dbmodule.get_cursor()

    # For first time running, make a table using
    # dbmodule.make_table(conn, cret)

    dict_object = obj_collector()
    write_to_db(conn, cret, dict_object)
    # dbmodule.fetch_all(cret) if print is needed
    conn.close()
    

if __name__ == '__main__':
    main()
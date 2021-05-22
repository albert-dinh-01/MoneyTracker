"""
    Author: Albert Dinh
    Date: Oct 13, 2020

    This file contains the basic template for 
    certain goods classes.
"""

from datetime import datetime, date


class BasicPurchases:
    def __init__(self, price, onoff, item_name):
        self.__time_stamp = date.today().strftime("%B %d, %Y")
        self.__date_stamp = datetime.now().strftime("%H:%M:%S")
        self.__price = price
        self.__online_or_offline = onoff
        self.__type = str(self.__class__)
        self.__name = item_name
        self.__f = 'buffer.txt'

    def __str__(self):
        return self.__type

    def get_f_out(self):
        return self.__default_f_out

    def get_time(self):
        return self.__time_stamp

    def get_date(self):
        return self.__date_stamp

    def get_price(self):
        return self.__price

    def get_off_on_line(self):
        return self.__online_or_offline

    def on_off_value(self):
        if self.get_off_on_line():
            a = 'online'
            return a
        else:
            a = 'offline'
            return a

    def get_item_name(self):
        return self.__name

    def get_buffer_loc(self):
        return self.__f

    def get_f_obj_loc(self):
        fout = open(self.get_buffer_loc(), 'a')
        return fout

    def set_buffer_loc(self, new_loc):
        self.__f = new_loc

    def print_item_info(self):
        f = self.get_f_obj_loc()
        print(file=f)
        print("Purchased: {}".format(self.get_item_name()), file=f)
        print('Price is: ${} CAD'.format(self.get_price()), file=f)
        print('The item was purchased {}'.format(self.on_off_value()), file=f)
        print('The item was purchased on {}'.format(self.get_time()), file=f)
        print()


class Grocery(BasicPurchases):
    def __init__(self, price, onoff, item_name, category, retailer):
        BasicPurchases.__init__(self, price, onoff, item_name)
        self.__food_category = category
        self.__retailer = retailer

    def get_retailer(self):
        return self.__retailer

    def get_food_category(self):
        return self.__food_category

    def print_retailer(self):
        print()
        print("======================*****======================")
        print('Grocery item is', self.get_item_name())
        print('Item was purchased in %s.' % self.get_retailer())
        print('Food sub-category is %s.' % self.get_food_category())
        print("======================*****======================")
        print()


class EatingOut(BasicPurchases):
    def __init__(self, price, onoff, item_name, restaurant, feedback, recommendation):
        BasicPurchases.__init__(self, price, onoff, item_name)
        self.__restaurant_name = restaurant
        self.__feedback = feedback
        self.__recommend_or_no = recommendation

    def get_fb(self):
        a = str(self.__feedback)
        return a

    def get_recommendation(self):
        return self.__recommend_or_no

    def get_restaurant_name(self):
        return self.__restaurant_name

    def decision_to_rec(self):
        if self.get_recommendation():
            a = 'to recommend'
            return a
        else:
            a = 'to not recommend'
            return a

    def print_eat_out_info(self):
        print()
        print("======================*****======================")
        print('Ate the following dish:', self.get_item_name())
        print('Ate at:', self.get_restaurant_name()) 
        print('Decided', self.decision_to_rec(), 'this restaurant.')
        print('Rate this restaurant at level %s.' % self.get_fb())
        print("======================*****======================")
        print()


class Utilities(BasicPurchases):
    def __init__(self, price, onoff, item_name, util_category, util_provider):
        BasicPurchases.__init__(self, price, onoff, item_name)
        self.__uti_category = util_category
        self.__util_provider = util_provider

    def get_category(self):
        return self.__uti_category

    def get_util_provider(self):
        return self.__util_provider

    def print_utilities_info(self):
        print()
        print("======================*****======================")
        print('Paid for:', self.get_item_name(), 'ON', self.get_time())
        print('The utility provider was:', self.get_util_provider())
        print('The utility was classified as:', self.get_item_name())
        print("======================*****======================")
        print()


class MonthlySubscription(BasicPurchases):
    def __init__(self, price, onoff, item_name, provider, category):
        BasicPurchases.__init__(self, price, onoff, item_name)
        self.__provider = provider
        self.__category = category

    def get_subscription_provider(self):
        return self.__provider

    def get_category_subscription(self):
        return self.__category

    def print_subscription_service(self):
        print()
        print("======================*****======================")
        print('Paid', self.get_price(), 'to', 
        self.get_subscription_provider(), 'for item', 
        self.get_item_name())
        print('The subscription is for', self.get_category_subscription())
        print("======================*****======================")
        print()

if __name__ == '__main__':
    pass


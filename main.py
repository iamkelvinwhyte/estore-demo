from Class import eStore
e = eStore()


def SetOffer():
    name = input("Do you want to set Special Offer ?  Enter Y for Yes  ")
    if(name=="Y"):
        e.add_offer(item="Apples", offer_value=10,
                    no_of_buy="1", prod_discount="Apples")
        print("---Offer----")
        print(e.view_offer())
    

def BuyItem():
    name = input("Enter product(s) ")
    e.add_to_basket(name)
    print("---Item----")
    print(e.view_basket())
    print("---Pricing----")
    print(e.pricing())


if __name__ == '__main__':
   SetOffer()
   BuyItem()

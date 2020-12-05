class Coffee_Machine:
    water=400
    milk=540
    coffee=120
    money=0
    def __init__(self,value):
        self.value=value
    def report(self,value):
        print("Water:",self.water,"ml\nMilk:",self.milk,"ml\nCoffee:",self.coffee,"g\nMoney:$",self.money)
    def start(self,value):
        if(value=='1'):
            self.water-=60
            self.milk-=80
            self.coffee-=60
            self.money+=2.50
            print("Here is your Latte.Enjoy!!!")
        elif(value=='2'):
            self.water-=90
            self.milk-=10
            self.coffee-=90
            self.money+=4.50
            print("Here is your espresso.Enjoy!!!")
        elif(value=='3'):
            self.water-=80
            self.milk-=40
            self.coffee-=80
            self.money+=6.50
            print("Here is your cappucino.Enjoy!!!")
        else:
            print("Invalid number")
            
    def available(self,value):
        if(value=='1'):
            if(self.water<60):
                print("**Sorry there is not enough water**")
            elif(self.milk<80):
                print("**Sorry there is not enough milk**")
            elif(self.coffee<60):
                print("**Sorry there is not enough coffee**")
            else:
                self.coin(value)
        elif(value=='2'):
            if(self.water<90):
                print("**Sorry there is not enough water**")
            elif(self.milk<10):
                print("**Sorry there is not enough milk**")
            elif(self.coffee<90):
                print("**Sorry there is not enough coffee**")
            else:
                self.coin(value)
        elif(value=='3'):
            if(self.water<80):
                print("**Sorry there is not enough water**")
            elif(self.milk<40):
                print("**Sorry there is not enough milk**")
            elif(self.coffee<80):
                print("**Sorry there is not enough coffee**")
            else:
                self.coin(value)
            
    def coin(self,value):
        q=0.25
        d=0.10
        n=0.05
        p=0.01
        print("Insert coin!")
        a=int(input("Enter  quarters:"))
        b=int(input("Enter  dimes:"))
        c=int(input("Enter  nickles:"))
        d=int(input("Enter  pennies:"))
        total=((a*q)+(b*d)+(c*n)+(d*p))
        self.transaction(value,total)

    def transaction(self,value,total):
        if(value=='1'):
            if(total<2.50):
                print("Sorry that's not enough money. **Money refunded**.")
            elif(total>2.50):
                print("Here is $",round(total-2.50,2),"dollars in change.")
                self.start(value)
            else:
                self.start(value)
        elif(value=='2'):
            if(totalt<4.50):
                print("Sorry that's not enough money. **Money refunded**.")
            elif(total>3.50):
                print("Here is $",round(total-4.50,2),"dollars in change.")
                self.start(value)
            else:
               self.start(value)
        elif(value=='3'):
            if(total<6.50):
                print("Sorry that's not enough money. **Money refunded**.")
            elif(total>4.50):
                print("Here is $",round(total-6.50,2),"dollars in change.")
                self.start(value)
            else:
                self.start(value)
     
choice=""
t=Coffee_Machine(choice)
while(True):
    print("\n\nLatte:$2.50\nEspresso:$3.50\nCappucino:$4.50")
    choice=input("What would you like?(1 - espresso,2 - Latte,3 - cappucino):")
    if(choice=="off"):
        break
    if(choice=="report"):
        t.report(choice)
        continue
    t.available(choice)

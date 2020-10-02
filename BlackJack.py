import random
class cards:
    def __init__(self):
        pass

class StandardCard(cards):
    def __init__(self,suit="",faceValue=""):
        cards.__init__(self)
        self.__suit=suit
        self.__faceValue=faceValue
    def getSuit(self):
        return self.__suit
    def getFaceValue(self):
        return  self.__faceValue

class Deck:
    def __init__(self,size:int,cursz:int,deck):
        self.size=size
        self.cursz=cursz
        self.deck=deck
    def shuffle(self):
        random.shuffle(self.deck)
    def Draw(self):
        if self.cursz==0:
            print("Error Deck Empty")
            return  None
        self.cursz=self.cursz-1
        return self.deck[self.cursz]
    def reset(self):
        pass

class StandardCardDeck(Deck):
    def __init__(self):
        self.suits=["Club","Spade","Heart","Diamond"]
        self.values=["","A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        temp=[]
        for i in range(4):
            for j in range(1,14):
                temp.append(StandardCard(self.suits[i],self.values[j]))
        Deck.__init__(self,52,52,temp)

    def reset(self):
        for i in range(4):
            for j in range(1,14):
                self.deck[i*13+j-1]=StandardCard(self.suits[i],self.values[j])



class Player:
    def __init__(self,name,user):
        self.__name=name
        self.__user=user

    def PrintPlayerInfo(self):
        pass
    def getName(self):
        return  self.__name
    def getUserName(self):
        return  self.__user


class BlackJackPlayer(Player):
    def __init__(self,name,user,cash:int):
        Player.__init__(self,name,user)
        if cash<0:
            cash=0
        self.cash=cash

    def PrintPlayerInfo(self):
        print("Username:",self.getUserName())
        print("Name:",self.getUserName())
        print("Cash:",self.cash)

UserSet={}
PlayerList=[]
def AddNewBlackJackPlayer():
    name=input("Enter your Name:")
    user=input("Enter your Username:")
    while user in UserSet:
        user=input("Username already Exists!\n Enter another userName")

    cash=int(input("Enter the Amount of money:"))
    player=BlackJackPlayer(name,user,cash)
    PlayerList.append(player)
    UserSet[user]=len(PlayerList)-1

def BlackJack():
    print("Welcome TO BlackJack!")
    AddNewBlackJackPlayer()
    newDeck=StandardCardDeck()
    roundcnt=0
    BlackJackValues={"A":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
    while True:
        roundcnt+=1
        print("##########################################################################################\n")
        print("Round ",roundcnt)
        newDeck.reset()
        newDeck.shuffle()
        DealerVal=0
        PlayerVal=0
        PlayerCards=[]
        DealerCards=[]
        dcard1=newDeck.Draw()
        dcard2=newDeck.Draw()
        print("Dealer Cards:\n",dcard1.getFaceValue(),dcard1.getSuit(),"\nHidden Card\n")
        DealerCards.append(dcard1)
        DealerCards.append(dcard2)
        pcard1=newDeck.Draw()
        pcard2=newDeck.Draw()
        PlayerCards.append(pcard1)
        PlayerCards.append(pcard2)
        print("Player Cards:\n",pcard1.getFaceValue(),pcard1.getSuit(),"\n",pcard2.getFaceValue(),pcard2.getSuit())
        PlayerVal+=BlackJackValues[pcard1.getFaceValue()]+BlackJackValues[pcard2.getFaceValue()]
        if PlayerList[0].cash < 50:
            print("########################################################################\n")
            print("Insufficient Funds Bring More Money Next Time.\n See You Again!")
            break
        bet=int(input("Enter the Amount you want to bet(Minimum-50 Maximum-"+str(PlayerList[0].cash)+") :\n"))
        while not bet >= 50 and bet <= (PlayerList[0].cash):
            bet=int(input("Enter a Valid amount between (Minimum-50 Maximum-"+str(PlayerList[0].cash)+") :"))
        PlayerList[0].cash-=bet
        DealerVal+=BlackJackValues[dcard1.getFaceValue()]+BlackJackValues[dcard2.getFaceValue()]

        if DealerVal==21:
            if PlayerVal==21:
                print("Both Dealer and Player has BlackJack!\nAll bets are returned!")
                print("Dealer Cards:\n", dcard1.getFaceValue(), dcard1.getSuit(), "\n",dcard2.getFaceValue(),dcard2.getSuit())
                PlayerList[0].cash+=bet
            elif PlayerVal!=21:
                print("Dealer Has a BlackJack!\nBetter Luck Next Time!")
                print("Dealer Cards:\n", dcard1.getFaceValue(), dcard1.getSuit(), "\n", dcard2.getFaceValue(),dcard2.getSuit())
        else:
            if PlayerVal==21:
                print("You have a BlackJack!")
                print("Dealer Cards:\n", dcard1.getFaceValue(), dcard1.getSuit(), "\n", dcard2.getFaceValue(),dcard2.getSuit())
                PlayerList[0].cash+=(1.5*bet)
            else:
                cntA=0
                if pcard1.getFaceValue()=="A":
                    PlayerVal-=10
                    cntA+=1
                if pcard2.getFaceValue()=="A":
                    PlayerVal-=10
                    cntA+=1
                x=int(input("Select one by typing respective number:\n1.Hit\n2.Stay\n"))
                flag=True
                while x==1:
                    cardi=newDeck.Draw()
                    print(cardi.getFaceValue(),cardi.getSuit())
                    PlayerVal+=BlackJackValues[cardi.getFaceValue()]
                    if cardi.getFaceValue()=="A":
                        PlayerVal-=10
                        cntA+=1

                    if cntA>0:
                        if PlayerVal+10 == 21:
                            print("BlackJack!")
                            break
                    if PlayerVal == 21:
                        print("BlackJack!")
                        break
                    if PlayerVal > 21:
                        flag=False
                        break
                    x = int(input("Select one by typing respective number:\n1.Hit\n2.Stay\n"))

                if flag==False:
                    print("Bust\nBetter Luck Next Time!")
                else:
                    if cntA>0:
                        if PlayerVal+10<=21:
                            PlayerVal+=10

                    cntA=0
                    if dcard1.getFaceValue()=="A":
                        DealerVal-=10
                        cntA+=1
                    if dcard2.getFaceValue()=="A":
                        DealerVal-=10
                        cntA+=1
                    print("Dealer Cards:")
                    print(dcard1.getFaceValue(),dcard1.getSuit())
                    print(dcard2.getFaceValue(),dcard2.getSuit())

                    flag1=True
                    while DealerVal<17:
                        cardi=newDeck.Draw()
                        print(cardi.getFaceValue(),cardi.getSuit())
                        DealerVal+=BlackJackValues[cardi.getFaceValue()]
                        if cardi.getFaceValue()=="A":
                            DealerVal-=10
                            cntA+=1
                        if cntA>0:
                            if DealerVal+10==21:
                                print("Dealer has got BlackJack!")
                                break
                        if DealerVal==21:
                            print("Dealer has got BlackJack!")
                            break
                        if DealerVal>21:
                            flag1=False
                            break

                    if flag1==False:
                        print("Dealer Busts!")
                        print("You Win!")
                        PlayerList[0].cash+=(2*bet)
                    else:
                        if cntA > 0:
                            if DealerVal+10<=21:
                                DealerVal+=10

                        if DealerVal==PlayerVal:
                            print("Draw!")
                            PlayerList[0].cash+=bet
                        elif PlayerVal>DealerVal:
                            print("You Win!")
                            PlayerList[0].cash+=(2*bet)
                        else:
                            print("Dealer Wins!\nBetter Luck Next Time!")



        if PlayerList[0].cash <50:
            print("Insufficient Funds to play another round!\nHope to see you again")
            print("\nYour Stats\n")
            PlayerList[0].PrintPlayerInfo()
            break
        else:
            y=int(input("Do you want to play more!   \n1:YES  0:NO\n"))
            if y!=1:
                print("\nYour Stats\n")
                PlayerList[0].PrintPlayerInfo()
                break






def main():
    BlackJack()

if __name__ == '__main__':
    main()












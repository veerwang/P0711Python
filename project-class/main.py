#! /usr/bin/python

# file define for class practice

# class define
#define the function outside the class body
def Set_ID(self,id):
	self.m_ID = id

class Baseclass:
	def __init__(self,id):
		self.m_ID = id 
		print("Baseclass create!")
	def __del__(self):
		print("Baseclass destroy!")

	def Showme(self):
		print(self.m_ID)

	SetID = Set_ID

class Driverclass(Baseclass):
	def __del__(self):
		print("Driverclass destroy!")
	def Show_Sum(self):
		print(sum(i for i in range(0,11)))

	m_Money = 10000

#private variables 
	__m_SpecialMoney = 1234

#private functions
	def __Showme(self):
		print(self.__m_SpecialMoney)

	def Showpmoney(self):
		self.__Showme()


class Gun():

    bullets = 1000          # some like static variable of C++

    def __init__(self,value):
        self.bullets = value;

    def dadada(self):
        print(self.bullets)

def main():
    # main function
    print("python class practice")

    bc = Baseclass(67)
    bc.SetID(100)
    bc.Showme()

    sc = Driverclass(20)
    sc.Showme()

    print(sc.m_Money)
    print(sc.Showpmoney())
    print(sc.Show_Sum())

    gun = Gun(5000)
    gun.dadada();
    print(Gun.bullets)      #be care there is something different
    print(gun.bullets)

if __name__ == '__main__':
    main()

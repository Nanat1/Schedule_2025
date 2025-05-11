class Schedule:
    def __init__(self, listing, body, length):
        self.listing = listing
        self.body = body
        self.length = length

    def __repr__(self):
        return self.listing


Scheduled = Schedule("   段导的动画Background Design(2)(1920*1080)(Procreate)(Portable) \n" \
"   (5/19前)Studio搬家 \n" \
"       -(5/19前)(前期准备:清理房间)去Studio拉行李(顺便倒垃圾) \n", 
["Background", Schedule("(5/19前)(前期准备:清理房间)去Studio拉行李(顺便倒垃圾)", "Studio", 1)], 2);

Coming = "   (5/20开始)Summer Course \n" \
"   (June/July)兼职游戏测试 买个可乐饼吧！ \n" ;

Monthly = "   洗衣服(包括学妹落下的两件)(8枚硬币) \n" ;

ASAP = "   清理房间 \n" \
"   (前期准备:清理房间)Grocery(顺便倒垃圾) \n" \
"   (前期准备:Grocery)做饭(顺便洗碗) \n" ;


def menu(Sche, Com, Mon, AS):
    print("WORK LIST \n")
    print(Sche)
    print(Com)
    print(Mon)
    print(AS)

ip = " "

while ip != "":
    menu(Scheduled, Coming, Monthly, ASAP)
    ip = input("Anything specific?")

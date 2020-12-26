import numpy as np

x1 = input('Enter 0 or 1 in x1: ')
# Enter x1
x1=int(x1)
x2 = input('Enter 0 or 1 in x2: ')
x2=int(x2)
# Enter x2
selected_gate =input('Enter gate(and,or,nand,xor): ')

class perceptron:
#liner--直線で表現が可能(XORは曲線)

    #def __init__(self,x1,x2):
    #    self.x1=x1
    #    self.x2=x2

    #def AND(self,x1,x2):
    #ANDゲート（簡易型）
    #   w1,w2,theta=0.5,0.5,0.2
    #    tmp=x1*w1+x2*w2
    #    if tmp <= theta:
    #        return 0
    #    elif tmp > theta:
    #        return 1
    
    def AND(self,x1,x2):
    #ANDゲート
        x=np.array([x1,x2])
        w=np.array([0.5,0.5])
        bias=-0.7
        tmp=np.sum(w*x)+bias
        if tmp <= 0:
            return 0
        else:
            return 1

    def NAND(self,x1,x2):
    #NANDゲート
        x=np.array([x1,x2])
        w=np.array([-0.5,-0.5])
        bias=0.7
        tmp=np.sum(w*x)+bias
        if tmp <= 0:
            return 0
        else:
            return 1

    def OR(self,x1,x2):
    #ORゲート
        x=np.array([x1,x2])
        w=np.array([0.5,0.5])
        bias=-0.1
        tmp=np.sum(w*x)+bias
        if tmp <= 0:
            return 0
        else:
            return 1

    def XOR(self,x1,x2):
    #XORゲート
        s1=self.NAND(x1,x2)
        #自身のクラス内の関数を呼び出す
        s2=self.OR(x1,x2)
        y=self.AND(s1,s2)
        return y

if selected_gate == "and":
    p=perceptron()
    output_date=p.AND(x1,x2)
    print(output_date)
elif selected_gate == "nand":
    p=perceptron()
    output_date=p.NAND(x1,x2)
    print(output_date)
elif selected_gate == "or":
    p=perceptron()
    output_date=p.OR(x1,x2)
    print(output_date)
elif selected_gate == 'xor':
    p=perceptron()
    output_date=p.XOR(x1,x2)
    print(output_date)
else:
    print("NO SELECTED!!")
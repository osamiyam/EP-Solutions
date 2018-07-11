## ２本の線分の交差判定について
山本修身

#### 1. **基礎理論**


２本の直線の交差判定がそれらの傾きによって決まってしまうのに比べて，２本の線分の交差判定は多少複雑である．まず，この問題を系統的に解くための道具を用意する．

**定理** 平面上の３つの点 $p_1, p_2, p_3$ が一直線に並ぶための必要十分条件は，
$$
L(p_1, p_2, p_3) = 
\left| \begin{array}{ccc}
  p_{1x} & p_{1y}  & 1 \\
  p_{2x} & p_{2y} & 1 \\
  p_{3x} & p_{3y} & 1
  \end{array} \right|  = 
  \left| \begin{array}{cc}
  p_{1x}  - p_{3x} & p_{1y} - p_{3y}  \\
    p_{2x}  - p_{3x} & p_{2y} - p_{3y}  
    \end{array} \right|
  = 0
$$
である．

この定理の最初の等号は３本の３次元ベクトルの成分による行列式がそれらのベクトルによって作られる平行６面体の体積に等しいということから得られる．さらに二つ目の等号は行列式の掃き出しによって得られる．

２本の線分$(p_1, p_2)$と$(p_3, p_4)$が交差している状況を考えると，一方の線分を含むような直線がもう一つの線分を分割している．すなわち，$p_1, p_2$を含む線分の両側に$p_3$と$p_4$が別れて配置されているはずである．この状況は前述の定理に当てはめることにより，

$$
L(p_1, p_2, p_3) \cdot L_(p_1, p_2, p_4) < 0
$$
と書くことができる．同様にして$p_3, p_4$を含む直線が$p_1, p_2$を分離しているので，
$$
L(p_3, p_4, p_1) \cdot L_(p_3, p_4, p_2) < 0
$$
という条件が成り立つ．逆にこれらの条件が成り立てば，明らかに２つの線分は交わる．

また，２つの線分の交点を求めるには，最初の式を用いれば求める交点は$p_3$と$p_4$による線分を$L(p_1, p_2, p_3) : -L(p_1, p_2, p_4)$の比に分割する点なので，
$$ p_{\rm intersection} = 
\frac{-L(p_1, p_2, p_4) p_3 + L(p_1, p_2, p_3)  p_4}
{-L(p_1, p_2, p_4) +  L(p_1, p_2, p_3) }
$$
と計算することができる．

#### 2. Python のプログラム例

上記の計算を現実のPythonプログラムとして書き下してみる．

```
# coding: utf-8                                                                 

def intersection(p1, p2, p3, p4):
    def sub(p1, p2):
        p1x, p1y = p1
        p2x, p2y = p2
        return (p1x - p2x, p1y -p2y)
    def L(p1, p2, p3):
        p13 = sub(p1, p3)
        p23 = sub(p2, p3)
        return p13[0] * p23[1] - p13[1] * p23[0]
    def lcomb(a, p1, b, p2):
        p1x, p1y = p1
        p2x, p2y = p2
        return (a * p1x + b * p2x, a * p1y + b * p2y)
    L123, L124 = L(p1, p2, p3), L(p1, p2, p4)
    L341, L342 = L(p3, p4, p1),	L(p3, p4, p2)
    if L123 * L124 >= 0 or L341 * L342 >= 0:
        return "交差なし"
    else:
        d = -L124 + L123
        return lcomb(-L124 / d, p3, L123 / d, p4)
        
if __name__ == '__main__':
    a = map(float, raw_input().split(" "))
    b = map(float, raw_input().split(" "))
    print intersection(a[0:2], a[2:4], b[0:2], b[2:4])
```

#### 3. 提出されたプログラムについて

まず，第一のグループから提出されたプログラムは以下のとおり．

```
### 7/6 zemi

def work():
    a = input().split()
    b = input().split()
    al = [0,0,0,0]
    bl = [0,0,0,0]

    # float型にする
    for i in range (len(a)):
        al[i] ,bl[i] = float(a[i]), float(b[i])
    
    # ベクトルにして外積を計算
    vA = toV(al)
    vB = toV(bl)
    vC = abV(al,bl)

    g = gaiseki(vA,vB)

    # 平行なら交差なし
    if g == 0:
        return "交差なし"

    # 内分比を求める
    t = gaiseki(vC, vA) / g
    s = gaiseki(vC, vB) / g

    if t < 0 or 1 < t or s < 0 or 1 < s:
        return "交差なし"
    
    else:
        x = al[0] + s * vA[0]
        y = al[1] + s * vA[1]
        return x,y

def gaiseki(v1,v2):
    return v1[0] * v2[1] - v1[1] * v2[0] 

def toV(a):
    return a[2] - a[0], a[3] - a[1]

def abV(a,b):
    return b[0] - a[0], b[1] - a[1]

print(work())
```

まず，細かいことだが，ASCII文字以外の文字をプログラム中で利用する場合には，そのプログラムの文字コードを登録する必要がある．これを怠ると何が起こるか保証されない．

さらに，最初の部分で線分が平行であるか否かを判定している．前述のように線分が交差しているかどうかの判定には割り算は必要ない．ここでは，外積がゼロになるケースを排除したいのだと考えられるが，`g == 0`という判定は`g`が実数値であるということからほとんど意味がない．もし，書くのであれば `abs(g) <= EPS`のようなプログラムにすべきである．また，最初の`input`は`raw_input`の間違いで`.split()`ではなく`.split(' ')` とすべきである（うまく動かないような気がする）．

あとは，交差していると考えたときの比を割り算によって計算して本来の交差判定を行っている．プログラム自体は正しく動いているように見える．

もう一つのグループのプログラムを以下に示す．

```
def work():
    x1, y1, x2, y2 = raw_input().split()
    x3, y3, x4, y4 = raw_input().split()

    x1, y1, x2, y2 = float(x1),float(y1),float(x2),float(y2)
    x3, y3, x4, y4 = float(x3),float(y3),float(x4),float(y4)

    i,j = 0,0

    i +=is_Cross(x1,y1,x2,y2,x3,y3)
    i +=is_Cross(x1,y1,x2,y2,x4,y4)
    j +=is_Cross(x3,y3,x4,y4,x1,y1)
    j +=is_Cross(x3,y3,x4,y4,x2,y2)
    
    if(i == 1 and j ==1):
        if(x1 == x2 or x3 == x4):
            return CrossZero(x1,y1,x2,y2,x3,y3,x4,y4)
        else:
            return Cross(x1,y1,x2,y2,x3,y3,x4,y4)
    else:
        return 'Nothing'

def is_Cross(x1,y1,x2,y2,x,y):
    if(x1 == x2):
        if(x >= x1):
            return 1
        else:
            return 0
    else:
        a12 = (y1-y2)/(x1-x2)
        
        if(y1+(x-x1)*a12 >= y):
            return 1
        else:
            return 0

def CrossZero(x1,y1,x2,y2,x3,y3,x4,y4):

    if(x1 == x2):
        a34 = (y3-y4)/(x3-x4)        
        b34 = y3 - a34*x3
        x = x1
        y = a34*x + b34    
    else:
        a12 = (y1-y2)/(x1-x2)
        b12 = y1 - a12*x1
        x = x3
        y = a12*x + b12
    return x,y

def Cross(x1,y1,x2,y2,x3,y3,x4,y4):
    a12 = (y1-y2)/(x1-x2)
    a34 = (y3-y4)/(x3-x4)
    b12 = y1 - a12*x1
    b34 = y3 - a34*x3
    x = (b34-b12)/(a12-a34)
    y = a12*x + b12

    return x, y

if __name__ == '__main__':
    print work()
```

このプログラムも前の例と同様に実数について`== 0`という判定を行っている．これは基本的に間違いである．実数値が正確に0になることはほとんど起こらない．また，傾きを基本にしているので，垂直な線や水平な線において例外処理が発生する．それに対処するためにプログラムが複雑になっている．

また本質的ではないが交差しない場合には「交差なし」を出力することが指定されているので，それに従うこと．

> Written with [StackEdit](https://stackedit.io/).

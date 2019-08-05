def args(**kwargs):
    text = "$var1"
    for k,v in kwargs.items():
        print(str(k) + "------------" + str(v))
        text = text.replace("$%s" %k, v)  #text.replace("$%s" %k, v)表示用v的值替换text中满足"$%k"的内容
        print(text)

args(var1="zs",var2="20")
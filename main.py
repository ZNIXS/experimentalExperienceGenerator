class Generate:
    def generator(self,topic,ques,solve):
        t = topic
        q = ques
        s = solve
        a = t+q
        print("经过这次的"+t+"""实验，我个人得到了不少的收获，一方面加深了我对课本理论的认识，另一方面也提高了实验操作本事。我总结了以下的体会和经验。
这次的实验跟之前做的实验不一样，因为这次实验遇到了"""+q+"""的问题。所以是我觉得这次实验我学到的最宝贵、最深刻的经验，就是弄懂这个问题。
我一开始产生了疑问："""+a+"""是怎么回事呢？"""+t+"""我很熟悉，但是关于"""+a+"""是怎么回事这个问题，本次实验就让我充分了解了。
我们弄懂"""+t+"""的问题必须知道它的的原理。
在理解原理的过程中，我深深体会到"""+q+"""的实现过程。最终我也弄懂了这个问题。"""
+a+"""，其实就是"""+s+"，"+t+"原来是这样"+q+"""的，我恍然大悟，事实原来是是这样，同时我也感到非常惊讶。
除了深刻体会到实验原理，我还提高了动手能力，对"""+t+"""的掌握更深入了。这就是关于"""+a+"""的实验总结，感谢老师的评阅！""")


if __name__ == "__main__":
    topic = input("请输入实验平台/类别：")
    ques = input("请输入实验需要解决的问题：")
    solve = input("请输入实验的解决方法/原理：")

    generate = Generate()
    generate.generator(topic,ques,solve)
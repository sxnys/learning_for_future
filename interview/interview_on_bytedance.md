# 字节跳动一面二面

*2019.03.06*

生平第一次面试，献给了最想去的宇宙条。基础有点差，补了一个多星期，到面试前脑子还是一片空白，啥都没记住的赶脚，广度优先导致了啥都记不住，深度优先又怕问的都是没遍历的知识。

总体感觉一般，主要是自己有点差劲，基础不怎么样，连算法也纠结半天，虽是研二，感觉也比不了人家大三的大佬，自惭形秽，莫名就是有一种走不出应试套路的感觉。

两个面试官都是在食堂面试（说是会议室没有空的），总之声音很嘈杂，有时候都听不清面试官说话，做题的时候也让我很烦躁。但是，两个面试官人都很好（第二个小哥哥不好意思开摄像头？不过声音很治愈），头条的面试体验果然还不错（除了今天嘈杂的环境）。

其实也不知道是两个面试官算一面（因为是连着的），还是算两面，从下午两点到五点，中间大概等了20分钟。一面一个半小时，一个小时耗在做题上（太菜了）；二面一个小时，整体感觉比一面轻松一点。

## 一面

**1、一上来就是问项目，有意思的或者说是有难度的（项目简历上写了一堆，含金量都不高）？**

A：我就挑了个有意思，一个学校助手小程序，也不知道重点说什么，就把功能和实现方法说了，其实蛮 low 的。

---

**2、HTTP 请求方法？**

A：我说5个嘛（其实有8个），说到最后还忘了一个，尴尬。

**追问：Post 和 Put 的区别？**

A：只说了 POST 的作用，也是一知半解，没有说清楚。PUT 不知道，哎。

---

**3、Cookie 和 Session 的区别？**

A：说了一些基本的区别。

**追问：跨域问题？**

A：记得看过，结果也不知道说什么了，硬是说了 Session 共享。

---

**4、Python 深浅拷贝？**

A：还算熟悉，就是有点紧张，语言组织不好

**追问：什么情况要用深拷贝？**

A：可变对象里包含可变对象，又想保存初始状态，又想修改里层对象，一个不得不要用到副本的情况。说不清楚，总感觉回答的怪怪的。

---

**5、Python 2 里面的字符乱码问题怎么解决？**

A：Python 2 字符乱码到现在我也没理清，只记得可以加一个全局的编码设置。还说了 Python 2 的 str、bytes 和 Python 3 的 str 类型。反正我知道的跟字符有关的东西都说了一下。

**追问：什么情况下涉及到编码问题？**

A：I/O 操作。是吗。。。

---

**6、HashMap 和 HashTable 的区别？**

A：emmmmm... 不会 Java，只会 System.out.println()

---

**7、数据库索引结构了解吗？**

A：B+ 树，还有哈希

**追问：B+ 树和 B 树的区别？**

A：脑子里有 B+ 树结构，看到哪里说哪里

**追问：聚集索引？**

A：以主键为索引的索引，大概就记得这点。还挖坑说了非聚集索引，说到回表时被问为什么会回表，因为有非主键字段，然后额，有点说不清楚了。

---

**8、来做个题吧，二叉树的序列化和反序列化**

（Leetcode 原题）一开始还没搞明白啥意思，光前序或者中序或者后序是不唯一的，后来才明白就是字符串的编解码。

要实现两个方法，中序 + 前序 或者 中序 + 后序能唯一确定一个二叉树，序列化就遍历结果相接，反序列化就倒推。

面试官提示的时候还说了层序，我就默默的开始想怎么层序，面试官又提示用特殊字符节点代替空节点，emmmm，好吧，开始写吧。尴尬的是居然不知道咋层序了，知道是用列表存节点遍历，硬是写不好（太菜了）。自己越想越乱，而且耳麦里时不时嘈杂，脑子一片空白，乱了乱了。好不容易层序完，反层序又乱了，总之整个过程就很乱，写的时候还发现序列化的结果有问题（代替所有空节点，形成满二叉树，而我却写成了只把叶子节点替换了）。

整个过程耗时一个小时，不知道面试官怎么这么有耐心的，尴尬，总之自己是真的菜。

---

**9、还有什么想问的吗？**

先问面试官的在哪个部门工作；字节某个产品的服务请求响应处理是不是按地区划分（其实我也不知道怎么问）；怎么处理海量数据的（几万台主机的集群）



## 二面

面试官没开摄像头（我还特地问了，小哥哥说他关了，应该是怕太帅影响我），问我感觉怎么样？emmmmm，第一次，有点紧张。问我专业，主要方向，就是聊天的那种，应该是让我放松一下吧。

**1、你擅长用的是 Python ，为什么用 Python？**

A：额，简单易学，充满哲学。

**追问：哲学？比如呢？**

A：鸭子类型，魔术方法，（装饰器忘说了。。。不过也是随便扯的）

---

**2、Python 和其他语言的比较？**

A：和 C/C++，Java 比了下，区别只能说出写很浅的。

---

**3、装饰器用过吗？**

A：用过

**追问：装饰器能做什么？自己有写过吗？**

A：程序计时器（装饰器典例）。写过。（然后就没了？还以为要我写，其实都已经准备好了）

---

**4、@staticmethod 和 @classmethod 的区别？**

A：一个静态方法，一个类方法，balabala，其实也没用过。

**追问：他们一般用在什么场景？**

A：不知道说什么了，好像最后还是说到了他们的区别，尴尬了。

---

**5、面向对象了解吗？**

A：了解（是不是我太菜了，为什么问我这个），我学的一门 coding 语言就是 C++，第一个概念就是面向对象，三大特征，封装继承多态。

**追问：有什么好处？**

A：emmmmm，模块化，属性方法继承，也不知道说什么，脑子里找不到什么专业的词汇了，尴尬。

**追问：能举个例子吗？**

A：学生类，张三李四等等。额，总感觉我是个弱智

---

**6、难度比较大的项目？**

A：来来来，计量你来，毕竟你是永远结束不了的项目。乱说一通，就这样吧

---

**7、做题了，根据用户阅读文章的情况（article_id, user_id, ...）统计阅读量 Top5 的文章**

A：第一反应，map 来统计嘛，Python 里字典嘛，然后找统计数最大的五个嘛

**追问：程序跑的时候 map 在内存吧，内存很小咋办？**

A：redis，本身就是个 map，能存很多数据嘛（redis 也不清楚底层，也不知道咋存的）

**追问：从数据结构上优化？**

A：想了许久，额，五个变量存五个最大的。。。尴尬了，意识到想偏了，我想的居然成了找 TOP5 的 article_id，我怕不是个智障。要是要找也是找统计数，那样还是没有解决内存放不下 map。

**追问：你说的五个变量也可以，。。。**

A：被我打断了，说自己跑偏了。然后就莫名其妙的跑到了 TOP K 问题，最后我就以最大堆结束了这个尴尬的话题。

**追问：说一下建堆的逻辑？**

A：两种方法，balabalabala，嗯，就这样。

一开始说是场景题，也不知道是场景题还是算法题，最后也没有写代码。

---

**8、下一题，滑动窗口，面经里有很多说过**

A：最后是要得到滑动窗口最大值集合，想了个方法，说了一通。

**追问：那你能实现一下吗？**

A：可以（其实我想说不能）。反反复复调整了几次代码结构，逻辑应该没问题，就让面试官看了（不用运行，因为题目也是面试官现场描述的，不然可能有问题），然后就给面试说了下详细思路。

**追问：你的算法复杂度怎么样？**

A：最差情况，数组倒序，复杂度 O(n^2)，好弱。然后就结束了。

---

**9、你接触过哪些技术？**

A：也不知道说什么。SqlServer？Mysql？Mongodb？Django？Flask？。。。

**追问：你现在在关注什么技术？**

A：Docker、redis、。。。尴尬，我在学什么，好弱。

------

**10、你有什么想问的吗？**

A：您在字节的哪个部门工作（我面试必问？）？怎么处理海量数据？系统有专门安全防护措施吗（明知故问，我在问什么）？



---



听了自己面试的录音，一个字，“弱”，对比一下大佬们的面经，我这次面试被问的问题都好水，然而很多问题也没有回答好。另外，气息跟不上，紧张；话说不清楚，脑子里没货，语言组织能力差；基础知识浅，技术能力差。

总之，临时抱佛脚是没用的，一切都在平时积累。

接下去是否还有后续面试？如果我是面试官我会拒绝继续面试这个人。听了录音发现自己真的菜。

不过，真的想进字节。
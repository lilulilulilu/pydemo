# prerequisite
run the code with python 3.10.13

# 1. Start the websocket server
` python main.py `

# 2. Test
- Open a browser tab with "http://localhost:8000/", while see the prompt window, enter a username, for example "ClientA", the connection will be extablished after username entered. Then, enter some content in the web page, for example "Hello, everyone!" in the content input box and click submit.
- Open one more new browser tab with username "ClientB", and enter content "Hi, ClientA!", check if ClientA has received the message "Hi, ClientA!" or not. If yes, it proves that the server is impletement as required.
- Open one more new browser tab with username "ClientC", and enter content "Hi, I am clientC!", check if both clientA and ClientB have received the message "Hi, I am clientC!", If yes, it proves that the server is impletement as required.

# notes
类的实例对象默认的__hash__方法行为如下：
 1. 调用id()函数获取对象的内存地址。这个地址在对象的生命周期内是不会变的。一旦对象被创建，它的id()就固定下来，直到对象被销毁，并且对象内容的变化不会改变其内存地址。换句话说，对于一个给定的对象，id()函数在对象存在期间总是返回相同的值。
 2. 将这个内存地址用作哈希值。


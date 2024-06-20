# prerequisite
run the code with python 3.10.13

# 1. Start the websocket server
` python main.py `

# 2. Test
- Open a browser tab with "http://localhost:8000/", while see the prompt window, enter a username, for example "ClientA", the connection will be extablished after username entered. Then, enter some content in the web page, for example "Hello, everyone!" in the content input box and click submit.
- Open one more new browser tab with username "ClientB", and enter content "Hi, ClientA!", check if ClientA has received the message "Hi, ClientA!" or not. If yes, it proves that the server is impletement as required.
- Open one more new browser tab with username "ClientC", and enter content "Hi, I am clientC!", check if both clientA and ClientB have received the message "Hi, I am clientC!", If yes, it proves that the server is impletement as required.


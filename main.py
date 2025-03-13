import tkinter as tk
from openai import OpenAI
# API 调用设置
client = OpenAI(api_key="你的api", base_url="https://api.deepseek.com")
messages = [{"role": "system", "content": "每次回答，请使用主人称呼我"}]  # 初始的系统消息
# 更新对话并获取模型回答
def update_conversation(user_message):
    # 将用户的消息添加到对话中
    messages.append({"role": "user", "content": user_message})
    # 调用 API 获取模型的回答
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        stream=False
    )
    # 获取模型的回答
    assistant_message = response.choices[0].message.content
    # 将模型的回答添加到对话中
    messages.append({"role": "assistant", "content": assistant_message})
    return assistant_message

# 发送消息的回调函数
def send_message():
    user_input = entry.get()  # 获取用户输入
    chat_window.insert(tk.END, f"你: {user_input}\n")  # 显示用户的消息
    assistant_reply = update_conversation(user_input)  # 获取模型回答
    chat_window.insert(tk.END, f"助手: {assistant_reply}\n")  # 显示模型的回应
    entry.delete(0, tk.END)  # 清空输入框

# 创建 Tkinter 窗口
root = tk.Tk()
root.title("桌宠聊天")

# 创建聊天框，用于显示对话记录
chat_window = tk.Text(root, height=20, width=50)
chat_window.pack()

# 创建输入框，用于用户输入消息
entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=10)

# 创建发送按钮
send_button = tk.Button(root, text="发送", command=send_message)
send_button.pack()

# 启动 Tkinter 窗口
root.mainloop()

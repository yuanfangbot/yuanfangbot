#!/usr/bin/env python3

"""一个简单的交互式机器人脚本。"""

def main():
    print("欢迎使用简单机器人")
    while True:
        try:
            user_input = input("你: ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if user_input.lower() in ("退出", "exit", "q", "quit"):
            print("机器人: 再见！")
            break
        if "你好" in user_input:
            print("机器人: 你好呀！")
        elif "你的名字" in user_input:
            print("机器人: 我叫元芳机器人")
        else:
            print("机器人: 很抱歉，我还不太懂如何回答。")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

"""更完善的交互式机器人脚本。"""

import datetime


def respond(user_input: str):
    """根据用户输入生成回复，并指示是否继续会话。"""
    text = user_input.strip().lower()
    if text in ("退出", "exit", "q", "quit"):
        return "再见！", False
    if text in ("帮助", "help", "h"):
        help_msg = (
            "可用命令:\n"
            "  你好  -> 问候\n"
            "  时间  -> 获取当前时间\n"
            "  天气  -> 获取示例天气\n"
            "  退出  -> 离开聊天"
        )
        return help_msg, True
    if "你好" in text:
        return "你好呀！", True
    if "你的名字" in text:
        return "我叫元芳机器人。", True
    if "时间" in text:
        now = datetime.datetime.now()
        return f"现在时间: {now:%Y-%m-%d %H:%M:%S}", True
    if "天气" in text:
        return "今天天气晴朗，适合出门散步！", True
    return "很抱歉，我还不太懂如何回答。", True

def main():
    print("欢迎使用元芳机器人。输入 '帮助' 查看可用命令。")
    with open("chat.log", "a", encoding="utf-8") as log:
        while True:
            try:
                user_input = input("你: ")
            except (EOFError, KeyboardInterrupt):
                print()
                break
            reply, cont = respond(user_input)
            print("机器人:", reply)
            log.write(f"你: {user_input}\n机器人: {reply}\n")
            if not cont:
                break

if __name__ == "__main__":
    main()

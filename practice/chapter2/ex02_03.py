msg = 'eric'
ans = "yeah"

# 通用
print("Hello " + msg.title() + ", would you like to learn some Python today?")

# 3.5或之前支持
print("Hello {}, would you like to learn some Python today? {}".format(
    msg.title(), ans.upper()))

# 3.6以上支持
print(f"Hello {msg.title()}, would you like to learn some Python today?")

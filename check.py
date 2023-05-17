import os
 
# 実行UID(EUID)とUIDを確認し、
# "0"(root)であれば管理者権限を持つ。
if os.geteuid() == 0 and os.getuid() == 0 :
    print("管理者権限を持っています。")
else:
    print("このスクリプトの実行には、管理者権限が必要です。")
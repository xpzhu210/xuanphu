import json
import traceback
import threading
from zlapi import ZaloAPI, ThreadType, Message
from zlapi.models import MultiMsgStyle

RED_COLOR = 'db342e'
MESSAGE_TTL = 60

def tstyles(full_text, b=False, color=RED_COLOR, size=16):
    styles = []
    current_pos = 0
    lines = full_text.split('\n')
    for line in lines:
        if not line.strip():
            current_pos += 1
            continue
        styles.append({
            "start": current_pos,
            "len": len(line),
            "st": ",".join(filter(None, [
                "b" if b else "",
                f"c_{color}" if color else "",
                f"f_{size}" if size else ""
            ]))
        })
        current_pos += len(line) + 1
    return json.dumps({"styles": styles, "ver": 0})

class Client(ZaloAPI):
    def __init__(self, api_key, secret_key, imei, session_cookies, allowed_user_ids, acc_index=0):
        super().__init__(api_key, secret_key, imei=imei, session_cookies=session_cookies)
        self.allowed_user_ids = allowed_user_ids
        self.acc_index = acc_index

    def onMessage(self, mid, author_id, message, message_object, thread_id, thread_type):
        if not isinstance(message, str):
            return
        if message.strip().lower() == "idgr" and thread_type == ThreadType.GROUP:
            if author_id in self.allowed_user_ids:
                self.send_group_id(thread_id)
            else:
                print(f"⛔ [ACC {self.acc_index}] Người dùng {author_id} không được phép sử dụng tool!")

    def send_group_id(self, thread_id):
        try:
            group_info = self.fetchGroupInfo(thread_id).gridInfoMap[thread_id]
            group_id = group_info.groupId
            m_st = tstyles(f"TOOL SHADOW WAR  🧸 Id: {group_id}", b=True)
            self.sendMessage(
                thread_id=thread_id,
                message=Message(text=f"TOOL SHADOW WAR 🧸 Id: {group_id}", style=m_st),
                thread_type=ThreadType.GROUP,
                ttl=MESSAGE_TTL
            )
            print(f"✅ [ACC {self.acc_index}] Đã gửi ID nhóm: {group_id}")
        except Exception as e:
            print(f"\033[1;31m❌ [ACC {self.acc_index}] Lỗi khi lấy ID nhóm:\033[0m", e)
            traceback.print_exc()
            m_st = tstyles("⚠️ Không thể lấy ID nhóm!", b=True)
            self.sendMessage(
                thread_id=thread_id,
                message=Message(text="⚠️ Không thể lấy ID nhóm!", style=m_st),
                thread_type=ThreadType.GROUP,
                ttl=MESSAGE_TTL
            )

def start_client(index, session_cookies, imei, allowed_user_ids):
    try:
        client = Client(API_KEY, SECRET_KEY, imei=imei, session_cookies=session_cookies, allowed_user_ids=allowed_user_ids, acc_index=index)
        client.listen(run_forever=True, delay=1, thread=True, type='requests')
    except Exception as e:
        print(f"❌ Lỗi khi khởi chạy ACC {index}:", e)

if __name__ == "__main__":
    print("🧸 Chức năng lấy ID nhóm bằng lệnh 'idgr' (đa tài khoản, đa admin)...")

    API_KEY = 'api_key'
    SECRET_KEY = 'secret_key'

    try:
        num_accs = int(input("Nhập số lượng tài khoản Zalo bạn muốn sử dụng: "))
    except ValueError:
        print("❌ Số lượng tài khoản phải là số nguyên!")
        exit()

    for i in range(num_accs):
        print(f"\n🔐 Nhập thông tin cho tài khoản {i+1}")
        imei = input(" - Nhập IMEI: ").strip()
        session_str = input(" - Nhập SESSION_COOKIES (dạng JSON): ").strip()
        allowed_ids_raw = input(" - Nhập các ID người dùng được phép dùng tool (cách nhau bằng dấu phẩy): ").strip()

        if not imei or not session_str or not allowed_ids_raw:
            print("❌ IMEI, SESSION_COOKIES và danh sách ID không được để trống!")
            continue

        try:
            session_cookies = json.loads(session_str)
        except json.JSONDecodeError:
            print("❌ SESSION_COOKIES không hợp lệ! Bỏ qua tài khoản này.")
            continue

        allowed_user_ids = [uid.strip() for uid in allowed_ids_raw.split(",") if uid.strip()]
        threading.Thread(target=start_client, args=(i+1, session_cookies, imei, allowed_user_ids), daemon=True).start()

    print("✅ Tất cả tool đang chạy. Nhập 'Ctrl + C' để dừng.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n👋 Đã dừng tool.")

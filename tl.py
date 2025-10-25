import requests
import threading
import time
import os
from datetime import datetime

treo_threads = {}

def send_loop(token, chat_ids, caption, photo, delay, stop_event):
    while not stop_event.is_set():
        for chat_id in chat_ids:
            if stop_event.is_set():
                break
            try:
                if photo and photo.startswith("http"):
                    url = f"https://api.telegram.org/bot{token}/sendPhoto"
                    data = {"chat_id": chat_id, "caption": caption, "photo": photo}
                    response = requests.post(url, data=data, timeout=10)
                elif photo:
                    url = f"https://api.telegram.org/bot{token}/sendPhoto"
                    with open(photo, "rb") as f:
                        files = {"photo": f}
                        data = {"chat_id": chat_id, "caption": caption}
                        response = requests.post(url, data=data, files=files, timeout=10)
                else:
                    url = f"https://api.telegram.org/bot{token}/sendMessage"
                    data = {"chat_id": chat_id, "text": caption}
                    response = requests.post(url, data=data, timeout=10)

                if response.status_code == 200:
                    print(f"[+] {token[:10]}... gửi OK tới {chat_id}")
                elif response.status_code == 429:
                    retry = response.json().get("parameters", {}).get("retry_after", 10)
                    print(f"[!] Token {token[:10]} bị chặn 429! Đợi {retry}s...")
                    time.sleep(retry)
                else:
                    print(f"[!] Token {token[:10]} lỗi: {response.status_code} - {response.text}")
            except Exception as e:
                print(f"[!] Token {token[:10]} lỗi kết nối: {e}")
            time.sleep(0.2)
        time.sleep(delay)

def check_token(token):
    try:
        res = requests.get(f"https://api.telegram.org/bot{token}/getMe", timeout=5)
        return res.status_code == 200 and res.json().get("ok", False)
    except:
        return False

def run_parallel_spam(tokens, chat_ids, text, img, delay):
    stop_event = threading.Event()
    for token in tokens:
        t = threading.Thread(target=send_loop, args=(token, chat_ids, text, img, delay, stop_event), daemon=True)
        t.start()
        treo_threads[token] = {
            "thread": t,
            "stop_event": stop_event,
            "start": datetime.now()
        }
    print(f"\n[+] Đã bắt đầu treo {len(tokens)} token vào {len(chat_ids)} group. Delay: {delay}s")

def stop_all():
    for token in treo_threads:
        treo_threads[token]["stop_event"].set()
    print("\n[!] Đã dừng toàn bộ spam.")

def main():
    print("TOOL SPAM TELE SHADOW WAR")

    chat_ids = input("Nhập ID group (phân tách bởi dấu ,): ").strip().split(",")
    chat_ids = [cid.strip() for cid in chat_ids if cid.strip()]

    raw_tokens = input("Nhập token bot (phân tách bởi dấu ,): ").strip().split(",")
    tokens = []
    for token in raw_tokens:
        token = token.strip()
        if check_token(token):
            tokens.append(token)
        else:
            print(f"[!] Token không hợp lệ: {token}")

    if not tokens:
        print("Không có token hợp lệ.")
        return

    file_path = input("Nhập đường dẫn file nội dung .txt: ").strip()
    if not os.path.isfile(file_path):
        print(f"[!] File không tồn tại: {file_path}")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print(f"[!] Lỗi đọc file: {e}")
        return

    choice = input("Bạn có muốn gửi kèm ảnh? (1 = Có, 2 = Không): ").strip()
    if choice == "1":
        img = input("Nhập link ảnh hoặc đường dẫn ảnh local: ").strip()
    else:
        img = None

    try:
        delay = int(input("Nhập delay giữa mỗi vòng lặp (giây): ").strip())
    except:
        print("Delay không hợp lệ.")
        return

    run_parallel_spam(tokens, chat_ids, text, img, delay)

    print("\n[!] Nhấn Ctrl+C để thoát và dừng spam.")
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        stop_all()

if __name__ == "__main__":
    main()
from config.client import *
from pystyle import Colors, Colorate, Center, Box
import json
import random
import paho.mqtt.client as mqtt
from urllib.parse import urlparse
import ssl
import requests
import time
import os
import sys
import threading
import hashlib
from bs4 import BeautifulSoup
RAINBOW_COLORS = [
    Colors.red_to_purple,
    Colors.purple_to_blue,
    Colors.blue_to_cyan,
    Colors.cyan_to_green,
    Colors.green_to_yellow,
    Colors.yellow_to_red,
    Colors.red_to_yellow
]

def get_rainbow_color():
    """Lấy màu ngẫu nhiên từ palette cầu vồng"""
    return random.choice(RAINBOW_COLORS)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_soft_banner():
    banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣶⣦⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⢀⠀⢹⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣷⣄⠨⣿⣿⣿⡌⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣷⣿⣿⣿⣿⣿⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣴⣾⣿⣮⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⠟⣹⣿⡿⢿⣿⣿⣬⣶⣶⡶⠦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣢⣙⣻⢿⣿⣿⣿⠎⢸⣿⠕⢹⣿⣿⡿⣛⣥⣀⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⡏⣿⡏⠿⢄⣜⣡⠞⠛⡽⣸⡿⣟⡋⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠾⠿⣿⠁⠀⡄⠀⠀⠰⠾⠿⠛⠓⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠠⢐⢉⢷⣀⠛⠠⠐⠐⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣠⣴⣶⣿⣧⣾⠡⠼⠎⢎⣋⡄⠆⠀⠱⡄⢉⠃⣦⡤⡀⠀⠀⠀⠀
⠀⠀⠐⠙⠻⢿⣿⣿⣿⣿⣿⣿⣄⡀⠀⢩⠀⢀⠠⠂⢀⡌⠀⣿⡇⠟⠀⠀⢄⠀
⠀⣴⣇⠀⡇⠀⠸⣿⣿⣿⣿⣽⣟⣲⡤⠀⣀⣠⣴⡾⠟⠀⠀⠟⠀⠀⠀⠀⡰⡀
⣼⣿⠋⢀⣇⢸⡄⢻⣟⠻⣿⣿⣿⣿⣿⣿⠿⡿⠟⢁⠀⠀⠀⠀⠀⢰⠀⣠⠀⠰
⢸⣿⡣⣜⣿⣼⣿⣄⠻⡄⡀⠉⠛⠿⠿⠛⣉⡤⠖⣡⣶⠁⠀⠀⠀⣾⣶⣿⠐⡀
⣾⡇⠈⠛⠛⠿⣿⣿⣦⠁⠘⢷⣶⣶⡶⠟⢋⣠⣾⡿⠃⠀⠀⠀⠰⠛⠉⠉⠀⠀
"""
    print(Center.XCenter(Colorate.Horizontal(get_rainbow_color(), banner)))

    info_box = """
┌─────────────────────────────────────────────────┐
│           Developer: Hồ Xuân Phú                │
│         Tool: MQTT Messenger Multi-Cookie       │
│          Version: XXX                           │
└─────────────────────────────────────────────────┘
"""
    print(Center.XCenter(Colorate.Horizontal(get_rainbow_color(), info_box)))

def print_section_header(title):
    header = f"\n┌{'─' * (len(title) + 4)}┐\n│ {title}   │\n└{'─' * (len(title) + 4)}┘"
    print(Colorate.Horizontal(get_rainbow_color(), header))

def soft_input(prompt_text):
    rainbow_prompt = Colorate.Horizontal(get_rainbow_color(), f"┌──(input)-[{prompt_text}]\n└─$ ")
    return input(rainbow_prompt)

def print_success(message):
    rainbow_msg = Colorate.Horizontal(Colors.green_to_cyan, f"✓ THÀNH CÔNG - {message}")
    print(rainbow_msg)

def print_error(message):
    rainbow_msg = Colorate.Horizontal(Colors.red_to_purple, f"✗ LỖI - {message}")
    print(rainbow_msg)

def print_info(message):
    rainbow_msg = Colorate.Horizontal(Colors.blue_to_cyan, f"ℹ INFO - {message}")
    print(rainbow_msg)

def print_warning(message):
    rainbow_msg = Colorate.Horizontal(Colors.yellow_to_red, f"⚠ WARNING - {message}")
    print(rainbow_msg)

def print_loading(message):
    rainbow_msg = Colorate.Horizontal(Colors.cyan_to_blue, f"⏳ LOADING - {message}")
    print(rainbow_msg)

def get_guid():
    return generate_client_id()

def format_id(id_str):
    return str(id_str)

def extract_keys(html):
    soup = BeautifulSoup(html, 'html.parser')
    code_div = soup.find('div', class_='plaintext')
    if code_div:
        keys = [line.strip() for line in code_div.get_text().split('\n') if line.strip()]
        return keys
    return []

def checkkey():
    # Đã xoá xác minh key
    print_section_header("LICENSE VERIFICATION")
    print_success("Tool đang ONLINE! Có thể sử dụng.")
    time.sleep(1)
    return
    print_section_header("LICENSE VERIFICATION")
    
    url = 'hxp'
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print_error(f"Không thể lấy dữ liệu từ anotepad: {e}")
        os.kill(os.getpid(), 9)
    
    md5_list = extract_keys(response.text)
    key = soft_input("Nhập License Key")
    hashed = hashlib.md5(key.encode()).hexdigest()
    
    if hashed in md5_list:
        success_msg = Colorate.Horizontal(Colors.green_to_yellow, "\n🎉 OK - KEY ĐÚNG RỒI (*´ω｀*)")
        print(success_msg)
        time.sleep(3)
    else:
        error_msg = Colorate.Horizontal(Colors.red_to_purple, "\n💥 KEY SAI MẤT RỒI (>0<；)")
        print(error_msg)
        time.sleep(2)
        os.kill(os.getpid(), 9)

def getUserName(dataFB, userID):
    try:
        dataForm = formAll(dataFB, requireGraphql=False)
        dataForm["ids[0]"] = userID
        req = mainRequests(
            "https://www.facebook.com/chat/user_info/",
            dataForm,
            dataFB["cookieFacebook"]
        )
        resp = requests.post(**req)
        jsonData = json.loads(resp.text.split("for (;;);")[1])["payload"]["profiles"][str(userID)]
        return jsonData.get("name", "Unknown")
    except Exception:
        return "Unknown"

class FacebookMQTTSender:
    def __init__(self, cookies: str, account_name: str = ""):
        self.cookies = cookies
        self.account_name = account_name
        self.dataFB = dataGetHome(cookies)
        self.user_id = self._extract_user_id()
        self.mqtt_client = None
        self.connected = False
        self.ws_task_number = 0
        self.ws_req_number = 0
        self.last_seq_id = None
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"

    def _extract_user_id(self):
        cookie_dict = parse_cookie_string(self.cookies)
        user_id = cookie_dict.get("c_user")
        if not user_id:
            raise ValueError("Invalid cookies: c_user not found")
        return user_id

    def _get_seq_id(self):
        rainbow_loading = Colorate.Horizontal(get_rainbow_color(), f"[{self.account_name}] Đang lấy Sequence ID...")
        print(rainbow_loading)
        
        form = formAll(self.dataFB, "CometChatInboxQuery", "3336396659757871")
        form["queries"] = json_minimal({
            "o0": {
                "doc_id": "3336396659757871",
                "query_params": {
                    "limit": 1,
                    "before": None,
                    "tags": ["INBOX"],
                    "includeDeliveryReceipts": False,
                    "includeSeqID": True
                }
            }
        })
        
        req_params = mainRequests(
            "https://www.facebook.com/api/graphqlbatch/",
            form,
            self.cookies
        )
        
        try:
            res = requests.post(**req_params)
            response_text = res.text
            
            if response_text.startswith("for(;;);"):
                response_text = response_text[9:]
            
            response_parts = response_text.split("\n")
            first_part = response_parts[0]
            
            if first_part.strip():
                response_data = json.loads(first_part)
                
                if ("o0" in response_data and
                    "data" in response_data["o0"] and
                    "viewer" in response_data["o0"]["data"] and
                    "message_threads" in response_data["o0"]["data"]["viewer"]):
                    
                    self.last_seq_id = response_data["o0"]["data"]["viewer"]["message_threads"]["sync_sequence_id"]
                    success_msg = Colorate.Horizontal(Colors.green_to_blue, f"[{self.account_name}] Sequence ID: {self.last_seq_id}")
                    print(success_msg)
                else:
                    raise Exception("Could not find sync_sequence_id in response")
            else:
                raise Exception("Empty response from Facebook")
                
        except Exception as e:
            raise Exception(f"Failed to get sequence ID: {str(e)}")

    def connect(self):
        if self.connected:
            return
        
        connect_msg = Colorate.Horizontal(get_rainbow_color(), f"[{self.account_name}] Đang kết nối đến Facebook MQTT...")
        print(connect_msg)
        
        self._get_seq_id()
        
        session_id = generate_session_id()
        user = {
            "a": self.user_agent,
            "u": self.user_id,
            "s": session_id,
            "chat_on": True,
            "fg": False,
            "d": get_guid(),
            "ct": "websocket",
            "aid": "219994525426954",
            "mqtt_sid": "",
            "cp": 3,
            "ecp": 10,
            "st": [],
            "pm": [],
            "dc": "",
            "no_auto_fg": True,
            "gas": None,
            "pack": []
        }
        
        host = f"wss://edge-chat.messenger.com/chat?sid={session_id}&cid={get_guid()}"
        
        cookie_dict = parse_cookie_string(self.cookies)
        cookie_str = "; ".join([f"{k}={v}" for k, v in cookie_dict.items()])
        
        client = mqtt.Client(
            client_id=f"mqttwsclient_{self.user_id}_{int(time.time())}",
            clean_session=True,
            protocol=mqtt.MQTTv31,
            transport="websockets",
        )
        
        client.tls_set(certfile=None, keyfile=None, cert_reqs=ssl.CERT_NONE, tls_version=ssl.PROTOCOL_TLSv1_2)
        client.tls_insecure_set(True)
        
        client.on_connect = self._on_connect
        client.on_disconnect = self._on_disconnect
        client.username_pw_set(username=json_minimal(user))
        
        parsed_host = urlparse(host)
        client.ws_set_options(
            path=f"{parsed_host.path}?{parsed_host.query}",
            headers={
                "Cookie": cookie_str,
                "Origin": "https://www.facebook.com",
                "User-Agent": self.user_agent,
                "Referer": "https://www.facebook.com/",
                "Host": "edge-chat.messenger.com",
            }
        )
        
        self.mqtt_client = client
        
        client.connect(
            host="edge-chat.messenger.com",
            port=443,
            keepalive=10,
        )
        
        client.loop_start()
        
        timeout = 10
        while not self.connected and timeout > 0:
            time.sleep(0.1)
            timeout -= 0.1
        
        if not self.connected:
            raise Exception("Failed to connect to MQTT within timeout")
        
        success_msg = Colorate.Horizontal(Colors.green_to_yellow, f"[{self.account_name}] 🚀 Kết nối MQTT thành công!")
        print(success_msg)

    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.connected = True
            
            client.publish(
                topic="/ls_app_settings",
                payload=json_minimal({"ls_fdid": "", "ls_sv": "6928813347213944"}),
                qos=1,
                retain=False,
            )
            
            queue = {
                "sync_api_version": 10,
                "max_deltas_able_to_process": 1000,
                "delta_batch_size": 500,
                "encoding": "JSON",
                "entity_fbid": self.user_id,
                "initial_titan_sequence_id": self.last_seq_id,
                "device_params": None
            }
            
            client.publish(
                topic="/messenger_sync_create_queue",
                payload=json_minimal(queue),
                qos=1,
                retain=False,
            )
        else:
            error_msg = Colorate.Horizontal(Colors.red_to_purple, f"[{self.account_name}] Kết nối MQTT thất bại với mã lỗi {rc}")
            print(error_msg)

    def _on_disconnect(self, client, userdata, rc):
        self.connected = False
        if rc != 0:
            warning_msg = Colorate.Horizontal(Colors.yellow_to_red, f"[{self.account_name}] MQTT ngắt kết nối bất ngờ với mã lỗi {rc}")
            print(warning_msg)

    def send_message(self, text: str, thread_id: str):
        if not self.connected:
            raise ValueError("Not connected to MQTT")
        
        if not text or not thread_id:
            raise ValueError("text and thread_id are required")
        
        self.ws_req_number += 1
        self.ws_task_number += 1
        
        task_payload = {
            "initiating_source": 0,
            "multitab_env": 0,
            "otid": generate_offline_threading_id(),
            "send_type": 1,
            "skip_url_preview_gen": 0,
            "source": 0,
            "sync_group": 1,
            "text": text,
            "text_has_links": 0,
            "thread_id": int(thread_id),
        }
        
        task = {
            "failure_count": None,
            "label": "46",
            "payload": json.dumps(task_payload, separators=(",", ":")),
            "queue_name": str(thread_id),
            "task_id": self.ws_task_number,
        }
        
        self.ws_task_number += 1
        
        task_mark_payload = {
            "last_read_watermark_ts": int(time.time() * 1000),
            "sync_group": 1,
            "thread_id": int(thread_id),
        }
        
        task_mark = {
            "failure_count": None,
            "label": "21",
            "payload": json.dumps(task_mark_payload, separators=(",", ":")),
            "queue_name": str(thread_id),
            "task_id": self.ws_task_number,
        }
        
        content = {
            "app_id": "2220391788200892",
            "payload": {
                "data_trace_id": None,
                "epoch_id": int(generate_offline_threading_id()),
                "tasks": [task, task_mark],
                "version_id": "7545284305482586",
            },
            "request_id": self.ws_req_number,
            "type": 3,
        }
        
        content["payload"] = json.dumps(content["payload"], separators=(",", ":"))
        
        self.mqtt_client.publish(
            topic="/ls_req",
            payload=json.dumps(content, separators=(",", ":")),
            qos=1,
            retain=False,
        )
        
        return True

    def disconnect(self):
        if self.mqtt_client and self.connected:
            self.mqtt_client.loop_stop()
            self.mqtt_client.disconnect()
            self.connected = False

class MultiCookieManager:
    def __init__(self):
        self.accounts = []
        self.stop_event = threading.Event()
        self.message_stats = {}
        self.message_content = ""
        self.message_file_path = None
        self.message_last_modified = None

    def add_account(self, cookies, delay, account_name, stt):
        self.accounts.append({
            'cookies': cookies,
            'delay': delay,
            'name': account_name,
            'sender': None,
            'stt': stt,
            'real_name': 'Unknown',
            'active': True
        })
        self.message_stats[account_name] = 0

    def check_and_reload_message(self):
        if not self.message_file_path:
            return
        
        try:
            current_modified = os.path.getmtime(self.message_file_path)
            if self.message_last_modified is None or current_modified != self.message_last_modified:
                with open(self.message_file_path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if content:
                        self.message_content = content
                        self.message_last_modified = current_modified
        except Exception:
            pass

    def start_all(self, thread_ids, message_file):
        self.message_file_path = message_file
        self.check_and_reload_message()
        
        clear_screen()
        print_soft_banner()
        print_section_header(f"KHỞI ĐỘNG {len(self.accounts)} ACCOUNTS & {len(thread_ids)} BOX")
        
        for acc in self.accounts:
            try:
                loading_msg = Colorate.Horizontal(get_rainbow_color(), f"Đang khởi tạo ACC[{acc['stt']}]...")
                print(loading_msg)
                
                sender = FacebookMQTTSender(acc['cookies'], acc['name'])
                acc['sender'] = sender
                sender.connect()
                
                acc['real_name'] = getUserName(sender.dataFB, sender.user_id)
                acc['active'] = True
                
                success_msg = Colorate.Horizontal(Colors.green_to_cyan, f"[{acc['real_name']}] - ACC[{acc['stt']}] ✓ Đã kết nối")
                print(success_msg)
                
            except Exception as e:
                error_msg = Colorate.Horizontal(Colors.red_to_purple, f"Lỗi kết nối {acc['name']}: {str(e)}")
                print(error_msg)
                acc['sender'] = None
                acc['active'] = False

        print_section_header("BẮT ĐẦU GỬI TIN NHẮN")
        info_msg = Colorate.Horizontal(Colors.blue_to_cyan, "Nhấn Ctrl+C để dừng")
        print(info_msg)
        
        while not self.stop_event.is_set():
            self.check_and_reload_message()
            
            for acc in self.accounts:
                if self.stop_event.is_set():
                    break
                
                sender = acc['sender']
                if sender is None or not sender.connected:
                    warning_msg = Colorate.Horizontal(Colors.yellow_to_red, f"[{acc['real_name']}] Account bị disconnect, delay {acc['delay']}s và tiếp tục")
                    print(warning_msg)
                    time.sleep(acc['delay'])
                    continue
                
                for thread_id in thread_ids:
                    if self.stop_event.is_set():
                        break
                    
                    try:
                        sender.send_message(self.message_content, thread_id)
                        self.message_stats[acc['name']] += 1
                        current_time = time.strftime("%H:%M:%S")
                        
                        success_msg = Colorate.Horizontal(get_rainbow_color(), f"🌈 {acc['real_name']} - ACC[{acc['stt']}] - OK - {thread_id}")
                        print(success_msg)
                        
                        delay = acc['delay']
                        if delay > 0 and thread_id != thread_ids[-1]:
                            delay_msg = Colorate.Horizontal(Colors.cyan_to_blue, f"⏰ Ho Xuan Phu < {delay}s >")
                            print(delay_msg)
                            
                            for _ in range(int(delay * 10)):
                                if self.stop_event.is_set():
                                    break
                                time.sleep(0.1)
                                
                    except Exception as e:
                        error_msg = Colorate.Horizontal(Colors.red_to_purple, f"[{acc['real_name']}] Lỗi gửi đến ID Box {thread_id}: {str(e)[:60]}")
                        print(error_msg)
                        
                        info_msg = Colorate.Horizontal(Colors.blue_to_cyan, f"[{acc['real_name']}] Delay {acc['delay']}s và tiếp tục với thread_id tiếp theo")
                        print(info_msg)
                        time.sleep(acc['delay'])
                        continue
                
                if not self.stop_event.is_set() and acc != self.accounts[-1]:
                    next_msg = Colorate.Horizontal(Colors.purple_to_blue, f"[{acc['real_name']}] Hoàn thành tất cả BOX. Chuyển account tiếp theo...")
                    print(next_msg)
                    time.sleep(1)
            
            if not self.stop_event.is_set():
                complete_msg = Colorate.Horizontal(Colors.green_to_yellow, "\n🎊 < Xuân Phú Đẹp Trai > 🎊")
                print(complete_msg)
                time.sleep(2)
        
        for acc in self.accounts:
            if acc['sender']:
                try:
                    acc['sender'].disconnect()
                    disconnect_msg = Colorate.Horizontal(Colors.cyan_to_blue, f"[{acc['real_name']}] Đã ngắt kết nối")
                    print(disconnect_msg)
                except:
                    pass
        
        final_msg = Colorate.Horizontal(Colors.green_to_cyan, "🏁 Đã dừng tất cả vòng lặp gửi tin nhắn")
        print(final_msg)

    def stop_all(self):
        stop_msg = Colorate.Horizontal(Colors.yellow_to_red, "⏹️ Đang dừng tất cả accounts...")
        print(stop_msg)
        self.stop_event.set()
        
        for account in self.accounts:
            if account['sender']:
                try:
                    account['sender'].disconnect()
                except:
                    pass

    def print_stats(self):
        print_section_header("THỐNG KÊ TIN NHẮN")
        total = 0
        
        for acc in self.accounts:
            name = acc.get('real_name', 'Unknown')
            stt = acc.get('stt', 'Unknown')
            count = self.message_stats.get(acc['name'], 0)
            status = "🟢 Active" if acc.get('active', False) else "🔴 Inactive"
            
            stats_msg = Colorate.Horizontal(get_rainbow_color(), f"{name} - Account[{stt}] - Số lần đã gửi: {count} - {status}")
            print(stats_msg)
            total += count
        
        total_msg = Colorate.Horizontal(Colors.green_to_blue, f"🎯 Tổng cộng: {total} messages")
        print(total_msg)

def read_message_from_file(file_path):
    try:
        if not os.path.exists(file_path):
            print_error(f"Không tìm thấy file: {file_path}")
            return None
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            
        if not content:
            print_error("File rỗng")
            return None
        
        print_success(f"Đã tải nội dung tin nhắn: {len(content)} ký tự")
        return content
        
    except Exception as e:
        print_error(f"Lỗi đọc file: {str(e)}")
        return None

def get_multi_cookies(delay):
    cookies_list = []
    
    try:
        print_section_header("NHẬP COOKIES")
        info_msg = Colorate.Horizontal(Colors.blue_to_cyan, "Nhập cookies từng dòng. Gõ 'done' để kết thúc nhập.")
        print(info_msg)
        
        idx = 1
        while True:
            cookie = soft_input(f"Cookie cho Account{idx} (hoặc 'done' để kết thúc)")
            
            if cookie.lower() == 'done':
                break
            
            if cookie.strip():
                cookies_list.append({
                    'cookies': cookie.strip(),
                    'delay': delay,
                    'name': f'Account{idx}'
                })
                success_msg = Colorate.Horizontal(Colors.green_to_cyan, f"✓ Đã thêm Account{idx} với delay {delay}s")
                print(success_msg)
                idx += 1
            else:
                print_warning("Cookie không được để trống!")
        
        if not cookies_list:
            print_error("Không có cookies nào được nhập!")
            return None
        
        print_success(f"Đã thêm tổng cộng {len(cookies_list)} accounts")
        
    except KeyboardInterrupt:
        print_warning("Đã hủy nhập liệu")
        return None
    
    return cookies_list

def get_user_input():
    try:
        clear_screen()
        print_soft_banner()
        print_section_header("CẤU HÌNH GỬI TIN NHẮN")
        
        thread_ids_input = soft_input("NHẬP ID BOX ( ID1,ID2,ID3 )")
        if not thread_ids_input:
            print_error("ID Box không được để trống!")
            return None, None
        
        thread_ids = [id.strip() for id in thread_ids_input.split(",") if id.strip()]
        print_success(f"Đã thêm {len(thread_ids)} ID Box")
        
        message_file = soft_input("NHẬP FILE CHỨA NỘI DUNG")
        if not message_file:
            print_error("Đường dẫn file không được để trống!")
            return None, None
        
        return thread_ids, message_file
        
    except KeyboardInterrupt:
        print_warning("Đã hủy nhập liệu")
        return None, None

def main():
    manager = None
    
    try:
        while True:
            clear_screen()
            print_soft_banner()
            sv()
            checkkey()
            
            thread_ids, message_file = get_user_input()
            if not all([thread_ids, message_file]):
                rainbow_enter = Colorate.Horizontal(get_rainbow_color(), "\nNhấn Enter để thử lại...")
                input(rainbow_enter)
                continue
            
            delay_input = soft_input("NHẬP DELAY")
            try:
                delay = float(delay_input)
                if delay < 0:
                    print_error("Delay phải là số dương!")
                    input(f"\nNhấn Enter để thử lại...")
                    continue
            except ValueError:
                print_error("Delay phải là số!")
                input(f"\nNhấn Enter để thử lại...")
                continue
            
            cookies_data = get_multi_cookies(delay)
            if not cookies_data:
                input(f"\nNhấn Enter để thử lại...")
                continue
            
            message_content = read_message_from_file(message_file)
            if not message_content:
                input(f"\nNhấn Enter để thử lại...")
                continue
            
            loading_msg = Colorate.Horizontal(get_rainbow_color(), f"Đang khởi tạo {len(cookies_data)} accounts...")
            print(loading_msg)
            
            wait_msg = Colorate.Horizontal(Colors.blue_to_cyan, "Vui lòng đợi...")
            print(wait_msg)
            
            try:
                manager = MultiCookieManager()
                
                for stt, cookie_data in enumerate(cookies_data, start=1):
                    manager.add_account(
                        cookie_data['cookies'],
                        cookie_data['delay'],
                        cookie_data['name'],
                        stt
                    )
                
                print_success("Tất cả accounts đã được khởi tạo thành công")
                
                ctrl_msg = Colorate.Horizontal(Colors.purple_to_blue, "Nhấn Ctrl+C để dừng\n")
                print(ctrl_msg)
                
                manager.start_all(thread_ids, message_file)
                
            except Exception as e:
                print_error(f"Lỗi: {str(e)}")
            
            manager.print_stats()
            
            choice_prompt = Colorate.Horizontal(get_rainbow_color(), "\nBạn có muốn thử lại không? (y/n): ")
            choice = input(choice_prompt).strip().lower()
            
            if choice not in ['y', 'yes', '1']:
                break
    
    except KeyboardInterrupt:
        exit_msg = Colorate.Horizontal(Colors.purple_to_blue, "\n👋 Đang thoát... Tạm biệt!")
        print(exit_msg)
        
    except Exception as e:
        print_error(f"Lỗi không mong muốn: {str(e)}")
        
    finally:
        if manager:
            try:
                manager.stop_all()
                final_msg = Colorate.Horizontal(Colors.green_to_cyan, "🔒 Đã đóng tất cả kết nối MQTT")
                print(final_msg)
            except:
                pass

if __name__ == "__main__":
    loading_start = Colorate.Horizontal(get_rainbow_color(), "🌈 Đợi Tí Đang Loading... (｡•̀ᴗ-)✧")
    print(loading_start)
    time.sleep(3)
    main()

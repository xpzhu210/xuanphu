from pystyle import Colors, Colorate, Center, Box
from colorama import init, Fore, Style
from urllib.parse import urlparse
from typing import Dict, Any
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
import random
import paho.mqtt.client as mqtt
import ssl
import requests
import time
import os
import sys
import threading
import hashlib
import re
import base64
import pyfiglet
from banner import logo


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
    art = Colorate.Horizontal(get_rainbow_color(), banner)
    print(art)
    loading_animation("Đang Vô Tool Shadow War")

def menu():
    print(logo)
    print(Fore.GREEN + "="*60)
    print(Fore.YELLOW + "               MENU SHADOW WAR")
    print(Fore.GREEN + "="*60)
    print(Fore.CYAN + "1. Treo Nhây Top")
    print(Fore.CYAN + "2. Spam Post")
    print(Fore.GREEN + "="*60)

# Lấy KEY từ Drive
def get_key_from_drive():
    print(Fore.LIGHTBLUE_EX + "\n[+] Đang tải KEY từ Google Drive...")
    fancy_loading("Tải KEY")
    try:
        response = requests.get(google_drive_url)
        if response.status_code == 200:
            print(Fore.GREEN + "[✓] KEY đã được tải thành công!\n")
            return response.text.strip()
        else:
            print(Fore.RED + "[!] Không thể truy cập file key từ Google Drive.")
            sys.exit()
    except Exception as e:
        print(Fore.RED + f"[!] Lỗi kết nối Google Drive: {e}")
        sys.exit()

def get_uid_fbdtsg(ck):
    try:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': ck,
            'Host': 'www.facebook.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }

        response = requests.get('https://www.facebook.com/', headers=headers)

        if response.status_code != 200:
            print(f"Status Code >> {response.status_code}")
            return None, None, None, None, None, None

        html_content = response.text

        user_id = None
        fb_dtsg = None
        jazoest = None

        script_tags = re.findall(r'<script id="__eqmc" type="application/json[^>]*>(.*?)</script>', html_content)
        for script in script_tags:
            try:
                json_data = json.loads(script)
                if 'u' in json_data:
                    user_param = re.search(r'__user=(\d+)', json_data['u'])
                    if user_param:
                        user_id = user_param.group(1)
                        break
            except:
                continue

        fb_dtsg_match = re.search(r'"f":"([^"]+)"', html_content)
        if fb_dtsg_match:
            fb_dtsg = fb_dtsg_match.group(1)

        jazoest_match = re.search(r'jazoest=(\d+)', html_content)
        if jazoest_match:
            jazoest = jazoest_match.group(1)

        revision_match = re.search(r'"server_revision":(\d+),"client_revision":(\d+)', html_content)
        rev = revision_match.group(1) if revision_match else ""

        a_match = re.search(r'__a=(\d+)', html_content)
        a = a_match.group(1) if a_match else "1"

        req = "1b"

        return user_id, fb_dtsg, rev, req, a, jazoest

    except requests.exceptions.RequestException as e:
        print(f"Lỗi Kết Nối Khi Lấy UID/FB_DTSG: {e}")
        return get_uid_fbdtsg(ck)

    except Exception as e:
        print(f"Lỗi: {e}")
        return None, None, None, None, None, None


def get_info(uid: str, cookie: str, fb_dtsg: str, a: str, req: str, rev: str) -> Dict[str, Any]:
    try:
        form = {
            "ids[0]": uid,
            "fb_dtsg": fb_dtsg,
            "__a": a,
            "__req": req,
            "__rev": rev
        }

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': cookie,
            'Origin': 'https://www.facebook.com',
            'Referer': 'https://www.facebook.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }

        response = requests.post(
            "https://www.facebook.com/chat/user_info/",
            headers=headers,
            data=form
        )

        if response.status_code != 200:
            return {"error": f"Lỗi Kết Nối: {response.status_code}"}

        try:
            text_response = response.text
            if text_response.startswith("for (;;);"):
                text_response = text_response[9:]

            res_data = json.loads(text_response)

            if "error" in res_data:
                return {"error": res_data.get("error")}

            if "payload" in res_data and "profiles" in res_data["payload"]:
                return format_data(res_data["payload"]["profiles"])
            else:
                return {"error": f"Không Tìm Thấy Thông Tin Của {uid}"}

        except json.JSONDecodeError:
            return {"error": "Lỗi Khi Phân Tích JSON"}

    except Exception as e:
        print(f"Lỗi Khi Get Info: {e}")
        return {"error": str(e)}


def format_data(profiles):
    if not profiles:
        return {"error": "Không Có Data"}

    first_profile_id = next(iter(profiles))
    profile = profiles[first_profile_id]

    return {
        "id": first_profile_id,
        "name": profile.get("name", ""),
        "url": profile.get("url", ""),
        "thumbSrc": profile.get("thumbSrc", ""),
        "gender": profile.get("gender", "")
    }


def get_guid():
    section_length = int(time.time() * 1000)

    def replace_func(c):
        nonlocal section_length
        r = (section_length + random.randint(0, 15)) % 16
        section_length //= 16
        return hex(r if c == "x" else (r & 7) | 8)[2:]

    return "".join(replace_func(c) if c in "xy" else c for c in "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx")


def cmt_gr_pst(cookie, grid, postIDD, ctn, user_id, fb_dtsg, rev, req, a, jazoest, uidtag=None, nametag=None):
    try:
        if not all([user_id, fb_dtsg, jazoest]):
            return False

        pstid_enc = base64.b64encode(f"feedback:{postIDD}".encode()).decode()

        client_mutation_id = str(round(random.random() * 19))
        session_id = get_guid()
        crt_time = int(time.time() * 1000)

        variables = {
            "feedLocation": "DEDICATED_COMMENTING_SURFACE",
            "feedbackSource": 110,
            "groupID": grid,
            "input": {
                "client_mutation_id": client_mutation_id,
                "actor_id": user_id,
                "attachments": None,
                "feedback_id": pstid_enc,
                "formatting_style": None,
                "message": {
                    "ranges": [],
                    "text": ctn
                },
                "attribution_id_v2": f"SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,tap_search_bar,{crt_time},775647,391724414624676,,",
                "vod_video_timestamp": None,
                "is_tracking_encrypted": True,
                "tracking": [],
                "feedback_source": "DEDICATED_COMMENTING_SURFACE",
                "session_id": session_id
            },
            "inviteShortLinkKey": None,
            "renderLocation": None,
            "scale": 3,
            "useDefaultActor": False,
            "focusCommentID": None,
            "__relay_internal__pv__IsWorkUserrelayprovider": False
        }

        if uidtag and nametag:
            name_position = ctn.find(nametag)
            if name_position != -1:
                variables["input"]["message"]["ranges"] = [
                    {
                        "entity": {
                            "id": uidtag
                        },
                        "length": len(nametag),
                        "offset": name_position
                    }
                ]

        payload = {
            'av': user_id,
            '__crn': 'comet.fbweb.CometGroupDiscussionRoute',
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'useCometUFICreateCommentMutation',
            'variables': json.dumps(variables),
            'server_timestamps': 'true',
            'doc_id': '24323081780615819'
        }

        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'identity',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': cookie,
            'Origin': 'https://www.facebook.com',
            'Referer': 'https://www.facebook.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }

        response = requests.post(
            "https://www.facebook.com/api/graphql/",
            headers=headers,
            data=payload
        )

        return response.status_code == 200

    except Exception as e:
        print(f"Lỗi khi đăng bình luận: {e}")
        return False


def worker(cookie, post_link, file_path, cookie_delay, tag_option):
    try:
        user_id, fb_dtsg, rev, req, a, jazoest = get_uid_fbdtsg(cookie)

        if not all([user_id, fb_dtsg, jazoest]):
            print(f"[COOKIE] ❌ Không thể lấy tham số từ cookie.")
            return

        grid = postIDD = None

        if "facebook.com/groups/" in post_link and "/permalink/" in post_link:
            parts = post_link.split("facebook.com/groups/")[1].split("/permalink/")
            grid = parts[0].strip('/')
            postIDD = parts[1].strip('/')
        elif "facebook.com/groups/" in post_link and "app=fbl" in post_link:
            url_parts = post_link.split('?')[0].split('/')
            for i, part in enumerate(url_parts):
                if part == "groups":
                    grid = url_parts[i+1]
                if part == "permalink":
                    postIDD = url_parts[i+1]
        elif "facebook.com/groups/" in post_link:
            group_match = re.search(r'groups/(\d+)', post_link)
            post_match = re.search(r'posts/(\d+)', post_link) or re.search(r'permalink/(\d+)', post_link)
            if group_match:
                grid = group_match.group(1)
            if post_match:
                postIDD = post_match.group(1)

        if postIDD and '?' in postIDD:
            postIDD = postIDD.split('?')[0]
        if postIDD:
            postIDD = postIDD.rstrip('/')

        if not (grid and postIDD):
            print(f"[POST] ❌ Link không hợp lệ: {post_link}")
            return

        print(f"[INFO] ID Group: {grid} | ID Post: {postIDD}")

        uidtag = nametag = None
        if tag_option == 'y':
            uidtag = input(f"[{cookie[:10]}...] Nhập UID cần tag: ")
            user_info = get_info(uidtag, cookie, fb_dtsg, a, req, rev)
            if "error" in user_info:
                print(f"[TAG] ❌ Lỗi lấy tên tag: {user_info['error']}")
                return
            nametag = user_info["name"]

        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            content = line.strip()
            if not content:
                continue

            if tag_option == 'y' and nametag:
                content = f"{nametag} {content}" if random.choice([True, False]) else f"{content} {nametag}"
                result = cmt_gr_pst(cookie, grid, postIDD, content, user_id, fb_dtsg, rev, req, a, jazoest, uidtag, nametag)
            else:
                result = cmt_gr_pst(cookie, grid, postIDD, content, user_id, fb_dtsg, rev, req, a, jazoest)

            status = "✅ Thành công" if result else "❌ Thất bại"
            print(f"[POST: {postIDD}] | Nội dung: {content} | {status}")

            time.sleep(cookie_delay.get(cookie, 1))  # Use the delay specific to this cookie

    except Exception as e:
        print(f"❌ Lỗi khi xử lý thread: {e}")
        time.sleep(5)


def main():
    
    while True:
        menu()
        try:
            spam_mode = int(input("Chọn (1 hoặc 2): "))
            if spam_mode in [1, 2]:
                break
            else:
                print("Vui lòng nhập 1 hoặc 2.")
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")
    num_cookies = int(input("Nhập số lượng cookie: "))
    cookies = [input(f"Nhập cookie thứ {i+1}: ") for i in range(num_cookies)]

    # Create a dictionary to store the delays for each cookie
    cookie_delay = {}
    for cookie in cookies:
        delay = float(input(f"Nhập delay (s) cho cookie {cookie[:10]}...: "))
        cookie_delay[cookie] = delay

    num_posts = int(input("Nhập số lượng link bài viết: "))
    posts = [input(f"Nhập link post thứ {i+1}: ") for i in range(num_posts)]

    file_path = input("Nhập tên file chứa nội dung (ví dụ: noidung.txt): ")
    tag_option = input("Bạn Có Muốn Nhây Tag Top Không? (Y/N): ").lower()



    threads = []

    def worker_mode(cookie, post_link):
        try:
            user_id, fb_dtsg, rev, req, a, jazoest = get_uid_fbdtsg(cookie)

            if not all([user_id, fb_dtsg, jazoest]):
                print(f"[COOKIE] ❌ Không thể lấy tham số từ cookie.")
                return

            grid = postIDD = None

            if "facebook.com/groups/" in post_link and "/permalink/" in post_link:
                parts = post_link.split("facebook.com/groups/")[1].split("/permalink/")
                grid = parts[0].strip('/')
                postIDD = parts[1].strip('/')
            elif "facebook.com/groups/" in post_link and "app=fbl" in post_link:
                url_parts = post_link.split('?')[0].split('/')
                for i, part in enumerate(url_parts):
                    if part == "groups":
                        grid = url_parts[i+1]
                    if part == "permalink":
                        postIDD = url_parts[i+1]
            elif "facebook.com/groups/" in post_link:
                group_match = re.search(r'groups/(\d+)', post_link)
                post_match = re.search(r'posts/(\d+)', post_link) or re.search(r'permalink/(\d+)', post_link)
                if group_match:
                    grid = group_match.group(1)
                if post_match:
                    postIDD = post_match.group(1)

            if postIDD and '?' in postIDD:
                postIDD = postIDD.split('?')[0]
            if postIDD:
                postIDD = postIDD.rstrip('/')

            if not (grid and postIDD):
                print(f"[POST] ❌ Link không hợp lệ: {post_link}")
                return

            print(f"[INFO] ID Group: {grid} | ID Post: {postIDD}")

            uidtag = nametag = None
            if tag_option == 'y':
                uidtag = input(f"[{cookie[:10]}...] Nhập UID cần tag: ")
                user_info = get_info(uidtag, cookie, fb_dtsg, a, req, rev)
                if "error" in user_info:
                    print(f"[TAG] ❌ Lỗi lấy tên tag: {user_info['error']}")
                    return
                nametag = user_info["name"]

            while True:  # Vô hạn
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                if spam_mode == 1:
                    for line in lines:
                        content = line.strip()
                        if not content:
                            continue
                        if tag_option == 'y' and nametag:
                            content = f"{nametag} {content}" if random.choice([True, False]) else f"{content} {nametag}"
                            result = cmt_gr_pst(cookie, grid, postIDD, content, user_id, fb_dtsg, rev, req, a, jazoest, uidtag, nametag)
                        else:
                            result = cmt_gr_pst(cookie, grid, postIDD, content, user_id, fb_dtsg, rev, req, a, jazoest)

                        status = "✅ Thành công" if result else "❌ Thất bại"
                        print(f"[POST: {postIDD}] | Nội dung: {content} | {status}")
                        time.sleep(cookie_delay.get(cookie, 1))
                else:  # spam_mode == 2
                    content = "".join(lines)
                    if tag_option == 'y' and nametag:
                        content = f"{nametag} {content}" if random.choice([True, False]) else f"{content} {nametag}"
                    result = cmt_gr_pst(cookie, grid, postIDD, content, user_id, fb_dtsg, rev, req, a, jazoest, uidtag, nametag) if tag_option == 'y' else cmt_gr_pst(cookie, grid, postIDD, content, user_id, fb_dtsg, rev, req, a, jazoest)
                    status = "✅ Thành công" if result else "❌ Thất bại"
                    print(f"[POST: {postIDD}] | Nội dung spam tất cả | {status}")
                    time.sleep(cookie_delay.get(cookie, 1))

        except Exception as e:
            print(f"❌ Lỗi khi xử lý thread: {e}")
            time.sleep(5)

    for cookie in cookies:
        for post_link in posts:
            t = threading.Thread(target=worker_mode, args=(cookie, post_link))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    main()

import json
import os
import time
import random
import threading
from pystyle import Colors, Colorate, Center, Write
from zlapi import ZaloAPI
from zlapi.models import *

class PhamTienDzai:
    def __init__(self):
        self.accounts = []  
        self.account_boxes = {} 
        self.account_configs = {}  
        self.running_threads = {} 
        
    def ui_deptraiquatienoi(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def tien_deptrai(self):
        banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠤⠤⠠⡖⠲⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠐⠀⠀⠀
⠀⠀⠀⠀⠀⡠⠶⣴⣶⣄⠀⠀⠀⢀⣴⣞⣼⣴⣖⣶⣾⡷⣶⣿⣿⣷⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠉⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠀⠀⠀⠙⢟⠛⠴⣶⣿⣿⠟⠙⣍⠑⢌⠙⢵⣝⢿⣽⡮⣎⢿⡦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠂⠁⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⢱⡶⣋⠿⣽⣸⡀⠘⣎⢢⡰⣷⢿⣣⠹⣿⢸⣿⢿⠿⡦⣄⠀⠀⠀⠀⠀⠀⡠⠀⠀⠂⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⢧⡿⣇⡅⣿⣇⠗⢤⣸⣿⢳⣹⡀⠳⣷⣻⣼⢿⣯⡷⣿⣁⠒⠠⢄⡀⠀⠀⡀⠀⠁⠄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⣼⣿⣧⡏⣿⣿⢾⣯⡠⣾⣸⣿⡿⣦⣙⣿⢹⡇⣿⣷⣝⠿⣅⣂⡀⠀⠡⢂⠄⣈⠀⠄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⣿⡟⣿⡇⡏⣿⣽⣿⣧⢻⡗⡇⣇⣤⣿⣿⣿⣧⣿⣿⡲⣭⣀⡭⠛⠁⠀⠀⣨⠁⠉⣂⢄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⢻⣿⣇⣥⣏⣘⣿⣏⠛⠻⣷⠿⡻⡛⠷⡽⡿⣿⣿⣿⣷⠟⠓⠉⠢⢄⡀⢠⠇⠀⠀⠀⠁⠫⢢⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀⢸⣾⣿⣽⣿⣏⣻⠻⠁⢠⠁⠀⠀⠀⠘⣰⣿⣿⢟⢹⢻⠀⠀⠀⠀⠀⠈⡒⢄⡀⠀⠀⠀⠀⠀⠀⠑⢄
⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⢸⣯⣿⣿⣿⢷⡀⠀⠀⠀⠀⠀⠀⠀⠛⣩⣿⣿⢿⣾⣸⠀⠀⠀⠀⠀⠀⣅⡠⠚⠉⠉⠁⠀⠀⠀⢀⠌
⠀⠀⠀⠀⠀⠀⠀⢡⠀⠀⠀⢟⣿⣯⡟⠿⡟⢇⡀⠀⠀⠐⠁⢀⢴⠋⡼⢣⣿⣻⡏⠀⠀⠀⣀⠄⠂⠁⠀⠀⠀⠀⠀⠀⢀⡤⠂⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠈⠊⢻⣿⣜⡹⡀⠈⠱⠂⠤⠔⠡⢶⣽⡷⢟⡿⠕⠒⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⡠⠐⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⢿⠿⠿⢿⠾⣽⡀⠀⠀⠀⠈⠻⣥⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠒⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣖⠂⠠⠐⠋⠀⠙⠳⣤⣠⠀⠀⠀⣀⠤⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠵⡐⠄⠀⠀⠀⠀⠀⠀⠀⠈⢷⣄⡀⠀⠠⡀⠀⠈⠙⠶⣖⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡥⠈⠂⠀⠀⠀⠀⠀⠀⠀⣼⠉⠙⠲⣄⠈⠣⡀⠀⠀⠈⢻⡦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠈⣷⡄⠈⠄⠀⠀⠀⢧⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⡀⠀⢠⣿⣤⣤⣶⣶⣾⣿⣿⡄⢸⠀⠀⠀⢸⣄⣤⣼⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠇⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢸⠀⠀⠀⣼⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣀⣀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠉⠁⠀⠈⠉⠙⠛⠿⠿⠽⠿⠟⠛⡉⠛⠲⣿⣿⠿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⢠⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⣠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢔⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠄⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠊⠀⠀⠀⠀⠀⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡠⣻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⢫⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⡿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠏⣸⣿⣷⢷⠙⣻⢶⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠾⠉⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠰⣏⠀⣿⣿⡘⣼⡇⠀⠁⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠁⠀⠀⣽⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢙⠓⠛⠘⣧⠾⢷⣄⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⣿⢟⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⠀⠀⠀⢸⣧⠀⠹⣆⠀⠀⠀⠀⠈⢻⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⢂⠙⢿⡷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢃⠀⠀⠈⠙⠀⠀⠻⡄⠀⠀⠀⠀⠸⡀⠹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠐⠠⠀⠻⠬⠄⡒⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠑⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

        """
        print(Colorate.Horizontal(Colors.rainbow, banner))
    
    def ui_dcmmvip(self):
        menu = """
 > MENU <

1. Treo Ngôn
2. Nhây Tag 
"""
        print(Colorate.Horizontal(Colors.green_to_blue, menu))
        print(Colors.cyan + "-" * 50 + Colors.reset)

    def tai_tokuda(self):
        num_accounts = int(input(Colors.yellow + "Bạn muốn treo bao nhiêu acc: " + Colors.reset).strip())
        
        existing_configs = []
        for i in range(1, num_accounts + 1):
            config_file = f"config{i}.json"
            if os.path.exists(config_file):
                existing_configs.append((i, config_file))
        
        if existing_configs:
            print(Colors.yellow + f"[!] Tìm thấy {len(existing_configs)} file config cũ" + Colors.reset)
            for acc_num, config_file in existing_configs:
                print(Colors.cyan + f"- {config_file}" + Colors.reset)
            
            choice = input(Colors.cyan + "Bạn có muốn sử dụng các file config cũ? (y/n): " + Colors.reset).lower().strip()
            if choice == 'y':
                configs = {}
                for acc_num, config_file in existing_configs:
                    try:
                        with open(config_file, 'r', encoding='utf-8') as f:
                            configs[acc_num] = json.load(f)
                    except:
                        print(Colors.red + f"[!] Lỗi đọc file {config_file}" + Colors.reset)
                        return self.config_tokuda(num_accounts)
                return configs, num_accounts
            else:
                for acc_num, config_file in existing_configs:
                    os.remove(config_file)
                print(Colors.green + "[!] Đã xóa các file config cũ" + Colors.reset)
        
        return self.config_tokuda(num_accounts)

    def config_tokuda(self, num_accounts):
        print(Colors.cyan + f"\n[TẠO CONFIG CHO {num_accounts} TÀI KHOẢN]" + Colors.reset)
        configs = {}
        
        for i in range(1, num_accounts + 1):
            print(Colors.yellow + f"\n--- Tài khoản {i} ---" + Colors.reset)
            imei = input(Colors.yellow + f"Nhập IMEI {i}: " + Colors.reset).strip()
            cookie_input = input(Colors.yellow + f"Nhập Cookie {i}: " + Colors.reset).strip()
            
            try:
                cookie_obj = json.loads(cookie_input)
                if "cookie" in cookie_obj:
                    cookie_data = cookie_obj["cookie"]
                    imei_to_use = cookie_obj.get("imei", imei)
                    phone = cookie_obj.get("phone", f"11012008{i}")
                    password = cookie_obj.get("password", f"PhamTienDepTrai{i}")
                else:
                    cookie_data = cookie_obj
                    imei_to_use = imei
                    phone = f"11012008"
                    password = f"PhamTienDepTrai{i}"
                    
                config = {
                    "cookie": cookie_data,
                    "imei": imei_to_use,
                    "phone": phone,
                    "password": password
                }
                
                config_file = f"config{i}.json"
                with open(config_file, 'w', encoding='utf-8') as f:
                    json.dump(config, f, ensure_ascii=False, indent=2)
                    
                configs[i] = config
                print(Colors.green + f"[+] Tạo config{i}.json thành công!" + Colors.reset)
                
            except json.JSONDecodeError:
                print(Colors.red + f"[!] Cookie {i} không đúng định dạng JSON!" + Colors.reset)
                return None, 0
            except Exception as e:
                print(Colors.red + f"[!] Lỗi tạo config {i}: {e}" + Colors.reset)
                return None, 0
        
        return configs, num_accounts

    def ini_sextranhalinh(self, configs):
        self.accounts = []
        
        for acc_num, config in configs.items():
            try:
                zalo_api = ZaloAPI(
                    phone=config["phone"],
                    password=config["password"],
                    imei=config["imei"],
                    session_cookies=config["cookie"]
                )
                
                if zalo_api.isLoggedIn():
                    self.accounts.append({
                        'number': acc_num,
                        'api': zalo_api,
                        'config': config
                    })
                    print(Colors.green + f"[+] Đăng nhập Account {acc_num} thành công!" + Colors.reset)
                else:
                    print(Colors.red + f"[!] Đăng nhập Account {acc_num} thất bại!" + Colors.reset)
                    
            except Exception as e:
                print(Colors.red + f"[!] Lỗi khởi tạo Account {acc_num}: {e}" + Colors.reset)
        
        if not self.accounts:
            print(Colors.red + "[!] Không có tài khoản nào đăng nhập thành công!" + Colors.reset)
            return False
            
        print(Colors.green + f"[+] Đã đăng nhập thành công {len(self.accounts)} tài khoản!" + Colors.reset)
        return True

    def glb_javikuiku(self, zalo_api):
        try:
            all_groups = zalo_api.fetchAllGroups()
            box_list = {}
            group_ids = []
            
            if hasattr(all_groups, 'groupList') and all_groups.groupList:
                for group in all_groups.groupList:
                    if hasattr(group, 'groupId'):
                        group_ids.append(str(group.groupId))
            elif hasattr(all_groups, 'gridVerMap'):
                group_ids = list(all_groups.gridVerMap.keys())
            else:
                if hasattr(all_groups, '__dict__'):
                    for key, value in all_groups.__dict__.items():
                        if isinstance(value, dict) and key != '__dict__':
                            group_ids = list(value.keys())
                            break
            
            if not group_ids:
                return {}
                
            batch_size = 10
            
            for i in range(0, len(group_ids), batch_size):
                batch_ids = group_ids[i:i + batch_size]
                batch_dict = {gid: 0 for gid in batch_ids}
                
                try:
                    batch_info = zalo_api.fetchGroupInfo(batch_dict)
                    self.jav_trungquoc(batch_info, batch_ids, box_list)
                except:
                    for group_id in batch_ids:
                        try:
                            group_info = zalo_api.fetchGroupInfo(group_id)
                            self.jav_nhatban(group_info, group_id, box_list)
                        except:
                            box_list[group_id] = {
                                "name": f"Box {group_id}",
                                "type": "group"
                            }
                time.sleep(0.5)
                
            return box_list
            
        except Exception as e:
            print(Colors.red + f"[!] Lỗi lấy danh sách box: {e}" + Colors.reset)
            return {}
    
    def jav_trungquoc(self, batch_info, group_ids, box_list):
        if hasattr(batch_info, 'groups') and batch_info.groups:
            for group in batch_info.groups:
                if hasattr(group, 'groupId'):
                    group_id = str(group.groupId)
                    if group_id in group_ids:
                        group_name = getattr(group, 'groupName', f"Box {group_id}")
                        if group_name is None:
                            group_name = f"Box {group_id}"
                        box_list[group_id] = {
                            "name": group_name,
                            "type": "group"
                        }
        
        elif hasattr(batch_info, 'mgInfos') and batch_info.mgInfos:
            for group_id, group_info in batch_info.mgInfos.items():
                if group_id in group_ids:
                    group_name = None
                    if hasattr(group_info, 'gn'):
                        group_name = group_info.gn
                    elif hasattr(group_info, 'groupName'):
                        group_name = group_info.groupName
                    
                    if group_name is None:
                        group_name = f"Box {group_id}"
                        
                    box_list[group_id] = {
                        "name": group_name,
                        "type": "group"
                    }
        
        else:
            for group_id in group_ids:
                if group_id not in box_list:
                    group_name = self._extract_group_name(batch_info, group_id)
                    box_list[group_id] = {
                        "name": group_name if group_name else f"Box {group_id}",
                        "type": "group"
                    }

    def jav_nhatban(self, group_info, group_id, box_list):
        if hasattr(group_info, 'groupName'):
            group_name = group_info.groupName
            if group_name is None:
                group_name = f"Box {group_id}"
            box_list[group_id] = {
                "name": group_name,
                "type": "group"
            }
        elif hasattr(group_info, 'gn'):
            group_name = group_info.gn
            if group_name is None:
                group_name = f"Box {group_id}"
            box_list[group_id] = {
                "name": group_name,
                "type": "group"
            }
        else:
            group_name = self._extract_group_name(group_info, group_id)
            box_list[group_id] = {
                "name": group_name if group_name else f"Box {group_id}",
                "type": "group"
            }
    
    def _extract_group_name(self, obj, group_id):
        common_name_attrs = ['groupName', 'gn', 'name', 'title']
        for attr in common_name_attrs:
            if hasattr(obj, attr):
                name = getattr(obj, attr)
                if name:
                    return name
        
        if hasattr(obj, '__dict__'):
            for key, value in obj.__dict__.items():
                if ('name' in key.lower() or 'title' in key.lower()) and isinstance(value, str) and value:
                    return value
                    
                if isinstance(value, dict):
                    for k, v in value.items():
                        if k == group_id and isinstance(v, dict) and ('name' in v or 'gn' in v or 'groupName' in v):
                            return v.get('name') or v.get('gn') or v.get('groupName') or f"Box {group_id}"
                
        return None 
    
    def jav_vietnam(self, box_list, page=0, items_per_page=10):
        if not box_list:
            print(Colors.red + "[!] Không có box nào!" + Colors.reset)
            return False
            
        box_items = list(box_list.items())
        total_pages = (len(box_items) + items_per_page - 1) // items_per_page
        
        if page >= total_pages:
            page = total_pages - 1
        if page < 0:
            page = 0
            
        start_idx = page * items_per_page
        end_idx = start_idx + items_per_page
        current_items = box_items[start_idx:end_idx]
        
        print(Colors.cyan + f"\n[DANH SÁCH BOX] - Trang {page + 1}/{total_pages}" + Colors.reset)
        print(Colors.cyan + "-" * 60 + Colors.reset)
        
        for i, (box_id, box_info) in enumerate(current_items, start=start_idx + 1):
            print(Colors.yellow + f"{i}. {box_info['name']} (ID: {box_id})" + Colors.reset)
            
        print(Colors.cyan + "-" * 60 + Colors.reset)
        print(Colors.green + f"Tổng số box: {len(box_items)}" + Colors.reset)
        
        if total_pages > 1:
            print(Colors.blue + "- next: Trang tiếp theo" + Colors.reset)
            print(Colors.blue + "- back: Trang trước" + Colors.reset)
        
        print(Colors.cyan + "\nChọn box cần gửi tin nhắn ('done' để dừng)" + Colors.reset)
            
        return True

    def linhtay_loclipnong(self, account_number, zalo_api):
        box_list = self.glb_javikuiku(zalo_api)
        if not box_list:
            print(Colors.red + f"[!] Account {account_number} không có box nào!" + Colors.reset)
            return []
            
        selected_boxes = []
        current_page = 0
        
        while True:
            self.ui_deptraiquatienoi()
            self.tien_deptrai()
            print(Colors.cyan + f"[CHỌN BOX CHO ACCOUNT {account_number}]" + Colors.reset)
            
            if not self.jav_vietnam(box_list, current_page):
                break
                
            if selected_boxes:
                print(Colors.green + f"\n[ĐÃ CHỌN] ({len(selected_boxes)} box):" + Colors.reset)
                for i, box in enumerate(selected_boxes, 1):
                    print(Colors.yellow + f"{i}. {box['name']} (ID: {box['id']})" + Colors.reset)
            
            choice = input(Colors.cyan + "\nLựa chọn: " + Colors.reset).strip().lower()
            
            if choice == 'done':
                break
            elif choice == 'next':
                current_page += 1
                box_items = list(box_list.items())
                total_pages = (len(box_items) + 9) // 10
                if current_page >= total_pages:
                    current_page = total_pages - 1
            elif choice == 'back':
                current_page -= 1
                if current_page < 0:
                    current_page = 0
            elif choice.isdigit():
                idx = int(choice) - 1
                box_items = list(box_list.items())
                if 0 <= idx < len(box_items):
                    box_id, box_info = box_items[idx]
                    
                    if any(box['id'] == box_id for box in selected_boxes):
                        print(Colors.red + f"[!] Box '{box_info['name']}' đã được chọn!" + Colors.reset)
                        time.sleep(1)
                    else:
                        selected_boxes.append({
                            'id': box_id,
                            'name': box_info['name']
                        })
                        print(Colors.green + f"[+] Đã chọn box: {box_info['name']}" + Colors.reset)
                        time.sleep(1)
                else:
                    print(Colors.red + "[!] Số thứ tự không hợp lệ!" + Colors.reset)
                    time.sleep(1)
            else:
                print(Colors.red + "[!] Lựa chọn không hợp lệ!" + Colors.reset)
                time.sleep(1)
                
        return selected_boxes

    def get_lmb(self, zalo_api, group_id):
        try:
            all_groups = zalo_api.fetchAllGroups()
            if hasattr(all_groups, 'gridVerMap') and group_id in all_groups.gridVerMap:
                group_version = all_groups.gridVerMap[group_id]
                versioned_info = zalo_api.fetchGroupInfo({group_id: group_version})
                
                if hasattr(versioned_info, 'gridInfoMap') and group_id in versioned_info.gridInfoMap:
                    group_data = versioned_info.gridInfoMap[group_id]
                    
                    if 'memVerList' in group_data:
                        members = []
                        for mem_ver in group_data['memVerList']:
                            user_id = mem_ver.split('_')[0]
                            try:
                                user_info = zalo_api.fetchUserInfo(user_id)
                                user_name = f"User {user_id}"
                                
                                if hasattr(user_info, 'changed_profiles') and user_info.changed_profiles:
                                    if user_id in user_info.changed_profiles:
                                        user_data = user_info.changed_profiles[user_id]
                                        user_name = user_data.get('displayName', user_name)
                                
                                members.append({
                                    'id': user_id,
                                    'name': user_name
                                })
                            except:
                                members.append({
                                    'id': user_id,
                                    'name': f"User {user_id}"
                                })
                        return members
            return []
        except Exception as e:
            print(Colors.red + f"[!] Lỗi lấy danh sách member: {e}" + Colors.reset)
            return []
    
    def chon_m(self, members, page=0, items_per_page=10):
        if not members:
            print(Colors.red + "[!] Không có member nào!" + Colors.reset)
            return False
            
        total_pages = (len(members) + items_per_page - 1) // items_per_page
        
        if page >= total_pages:
            page = total_pages - 1
        if page < 0:
            page = 0
            
        start_idx = page * items_per_page
        end_idx = start_idx + items_per_page
        current_items = members[start_idx:end_idx]
        
        print(Colors.cyan + f"\n[DANH SÁCH MEMBER] - Trang {page + 1}/{total_pages}" + Colors.reset)
        print(Colors.cyan + "-" * 60 + Colors.reset)
        
        for i, member in enumerate(current_items, start=start_idx + 1):
            print(Colors.yellow + f"{i}. {member['name']} (ID: {member['id']})" + Colors.reset)
            
        print(Colors.cyan + "-" * 60 + Colors.reset)
        print(Colors.green + f"Tổng số member: {len(members)}" + Colors.reset)
        
        if total_pages > 1:
            print(Colors.blue + "- next: Trang tiếp theo" + Colors.reset)
            print(Colors.blue + "- back: Trang trước" + Colors.reset)
        
        print(Colors.cyan + "\nChọn member cần tag ( 'done' để dừng)" + Colors.reset)
            
        return True

    def sl_mem(self, zalo_api, group_id, group_name):
        members = self.get_lmb(zalo_api, group_id)
        if not members:
            print(Colors.red + f"[!] Không lấy được danh sách member của box: {group_name}" + Colors.reset)
            return []
            
        selected_members = []
        current_page = 0
        
        while True:
            self.ui_deptraiquatienoi()
            self.tien_deptrai()
            print(Colors.cyan + f"[CHỌN MEMBER CHO BOX: {group_name}]" + Colors.reset)
            
            if not self.chon_m(members, current_page):
                break
                
            if selected_members:
                print(Colors.green + f"\n[ĐÃ CHỌN] ({len(selected_members)} member):" + Colors.reset)
                for i, member in enumerate(selected_members, 1):
                    print(Colors.yellow + f"{i}. {member['name']} (ID: {member['id']})" + Colors.reset)
            
            choice = input(Colors.cyan + "\nLựa chọn: " + Colors.reset).strip().lower()
            
            if choice == 'done':
                break
            elif choice == 'next':
                current_page += 1
                total_pages = (len(members) + 9) // 10
                if current_page >= total_pages:
                    current_page = total_pages - 1
            elif choice == 'back':
                current_page -= 1
                if current_page < 0:
                    current_page = 0
            elif choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(members):
                    member = members[idx]
                    
                    if any(m['id'] == member['id'] for m in selected_members):
                        print(Colors.red + f"[!] Member '{member['name']}' đã được chọn!" + Colors.reset)
                        time.sleep(1)
                    else:
                        selected_members.append(member)
                        print(Colors.green + f"[+] Đã chọn member: {member['name']}" + Colors.reset)
                        time.sleep(1)
                else:
                    print(Colors.red + "[!] Số thứ tự không hợp lệ!" + Colors.reset)
                    time.sleep(1)
            else:
                print(Colors.red + "[!] Lựa chọn không hợp lệ!" + Colors.reset)
                time.sleep(1)
                
        return selected_members

    def treo_ngon(self, zalo_api, box_id, box_name, message_file, delay, account_number):
        try:
            if not os.path.exists(message_file):
                print(Colors.red + f"[!] File tin nhắn không tồn tại: {message_file}" + Colors.reset)
                return
                
            with open(message_file, 'r', encoding='utf-8') as f:
                content = f.read().strip()
            
            if not content:
                print(Colors.red + f"[!] File tin nhắn trống: {message_file}" + Colors.reset)
                return
                
            print(Colors.green + f"[+] Account {account_number} bắt đầu treo box: {box_name}" + Colors.reset)
            
            while True:
                try:
                    styles = [{
                        "start": 0,
                        "len": len(content),
                        "st": "b,c_db342e,f_16"
                    }]
                    style_json = json.dumps({"styles": styles, "ver": 0})
                    
                    mention = Mention(uid="-1", length=len(content))
                    message = Message(text=content, mention=mention, style=style_json)
                    
                    zalo_api.setTyping(box_id, ThreadType.GROUP)
                    time.sleep(random.uniform(2, 4))
                    
                    zalo_api.send(message, box_id, ThreadType.GROUP)
                    
                    print(Colors.green + f"[ Acc{account_number} Treo ] Gửi thành công box > {box_name}" + Colors.reset)
                    
                    actual_delay = delay + random.uniform(-2, 2)
                    time.sleep(max(1, actual_delay))
                    
                except Exception as e:
                    print(Colors.red + f"[!] Account {account_number} lỗi gửi tin nhắn [{box_name}]: {e}" + Colors.reset)
                    time.sleep(5)
                    
        except Exception as e:
            print(Colors.red + f"[!] Account {account_number} lỗi treo zalo [{box_name}]: {e}" + Colors.reset)

    def nhay_tag(self, zalo_api, box_id, box_name, selected_members, delay, account_number):
        try:
            if not os.path.exists("nhay.txt"):
                print(Colors.red + f"[!] File nhay.txt không tồn tại" + Colors.reset)
                return
                
            with open("nhay.txt", 'r', encoding='utf-8') as f:
                messages = [line.strip() for line in f.readlines() if line.strip()]
            
            if not messages:
                print(Colors.red + f"[!] File nhay.txt trống" + Colors.reset)
                return
                
            if not selected_members:
                print(Colors.red + f"[!] Account {account_number} không có member nào được chọn cho box: {box_name}" + Colors.reset)
                return
                
            print(Colors.green + f"[+] Account {account_number} bắt đầu nhây tag box: {box_name}" + Colors.reset)
            
            while True:
                for msg in messages:
                    try:
                        mentions = []
                        final_msg = msg
                        
                        for i, member in enumerate(selected_members):
                            user_name = member['name']
                            final_msg += f" @{user_name}"
                            offset = final_msg.rfind(f"@{user_name}")
                            mentions.append(Mention(
                                uid=member['id'],
                                length=len(f"@{user_name}"),
                                offset=offset,
                                auto_format=False
                            ))
                        
                        zalo_api.setTyping(box_id, ThreadType.GROUP)
                        time.sleep(random.uniform(2, 4))
                        
                        from zlapi.models import MultiMention
                        message_to_send = Message(text=final_msg.strip(), mention=MultiMention(mentions))
                        zalo_api.send(message_to_send, thread_id=box_id, thread_type=ThreadType.GROUP)
                        
                        print(Colors.green + f"[ Acc{account_number} Nhây Tag ] Gửi thành công box > {box_name}" + Colors.reset)
                        
                        actual_delay = delay + random.uniform(-2, 2)
                        time.sleep(max(1, actual_delay))
                        
                    except Exception as e:
                        print(Colors.red + f"[!] Account {account_number} lỗi gửi tin nhắn tag [{box_name}]: {e}" + Colors.reset)
                        time.sleep(5)
                        
        except Exception as e:
            print(Colors.red + f"[!] Account {account_number} lỗi nhây tag [{box_name}]: {e}" + Colors.reset)

    def treo_zalo_function(self):
        self.ui_deptraiquatienoi()
        self.tien_deptrai()
        
        configs, num_accounts = self.tai_tokuda()
        if not configs:
            print(Colors.red + "[!] Không thể tạo config!" + Colors.reset)
            input("Nhấn Enter để tiếp tục...")
            return
            
        if not self.ini_sextranhalinh(configs):
            print(Colors.red + "[!] Không có tài khoản nào đăng nhập thành công!" + Colors.reset)
            input("Nhấn Enter để tiếp tục...")
            return

        all_account_configs = []
        for account in self.accounts:
            selected_boxes = self.linhtay_loclipnong(account['number'], account['api'])
            if not selected_boxes:
                print(Colors.red + f"[!] Account {account['number']} không có box nào được chọn!" + Colors.reset)
                continue

            box_configs = []
            for box in selected_boxes:
                self.ui_deptraiquatienoi()
                self.tien_deptrai()
                print(Colors.yellow + f"Account {account['number']}:" + Colors.reset)
                print(Colors.cyan + f"Box: {box['name']}" + Colors.reset)
                
                message_file = input(Colors.yellow + f"Nhập tên file tin nhắn: " + Colors.reset).strip()
                if not message_file:
                    print(Colors.red + "[!] Tên file không được để trống!" + Colors.reset)
                    input("Nhấn Enter để tiếp tục...")
                    continue
                    
                while True:
                    try:
                        delay = float(input(Colors.yellow + f"Nhập delay (giây): " + Colors.reset).strip())
                        if delay <= 0:
                            print(Colors.red + "[!] Delay phải lớn hơn 0!" + Colors.reset)
                            continue
                        break
                    except ValueError:
                        print(Colors.red + "[!] Delay phải là số!" + Colors.reset)
                        
                box_configs.append({
                    'box': box,
                    'message_file': message_file,
                    'delay': delay
                })
            
            if box_configs:
                all_account_configs.append({
                    'account': account,
                    'boxes': box_configs
                })
        
        if not all_account_configs:
            print(Colors.red + "[!] Không có cấu hình nào!" + Colors.reset)
            input("Nhấn Enter để tiếp tục...")
            return
            
        self.ui_deptraiquatienoi()
        self.tien_deptrai()
        print(Colors.green + "[BẮT ĐẦU TREO ZALO - TAG ALL]" + Colors.reset)
        print(Colors.cyan + "-" * 50 + Colors.reset)
        
        threads = []
        for account_config in all_account_configs:
            account = account_config['account']
            for box_config in account_config['boxes']:
                thread = threading.Thread(
                    target=self.treo_ngon,
                    args=(
                        account['api'],
                        box_config['box']['id'],
                        box_config['box']['name'],
                        box_config['message_file'],
                        box_config['delay'],
                        account['number']
                    )
                )
                thread.daemon = True
                thread.start()
                threads.append(thread)
                
        print(Colors.green + f"[+] Đã khởi động {len(threads)} luồng!" + Colors.reset)
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
  
    def nhay_tag_function(self):
        self.ui_deptraiquatienoi()
        self.tien_deptrai()
        
        configs, num_accounts = self.tai_tokuda()
        if not configs:
            print(Colors.red + "[!] Không thể tạo config!" + Colors.reset)
            input("Nhấn Enter để tiếp tục...")
            return
            
        if not self.ini_sextranhalinh(configs):
            print(Colors.red + "[!] Không có tài khoản nào đăng nhập thành công!" + Colors.reset)
            input("Nhấn Enter để tiếp tục...")
            return

        all_account_configs = []
        for account in self.accounts:
            selected_boxes = self.linhtay_loclipnong(account['number'], account['api'])
            if not selected_boxes:
                print(Colors.red + f"[!] Account {account['number']} không có box nào được chọn!" + Colors.reset)
                continue

            box_configs = []
            for box in selected_boxes:
                selected_members = self.sl_mem(account['api'], box['id'], box['name'])
                if not selected_members:
                    print(Colors.red + f"[!] Account {account['number']} không có member nào được chọn cho box: {box['name']}" + Colors.reset)
                    input("Nhấn Enter để tiếp tục...")
                    continue
                    
                self.ui_deptraiquatienoi()
                self.tien_deptrai()
                print(Colors.yellow + f"Account {account['number']}:" + Colors.reset)
                print(Colors.cyan + f"Box: {box['name']}" + Colors.reset)
                
                while True:
                    try:
                        delay = float(input(Colors.yellow + f"Nhập delay (giây): " + Colors.reset).strip())
                        if delay <= 0:
                            print(Colors.red + "[!] Delay phải lớn hơn 0!" + Colors.reset)
                            continue
                        break
                    except ValueError:
                        print(Colors.red + "[!] Delay phải là số!" + Colors.reset)
                        
                box_configs.append({
                    'box': box,
                    'members': selected_members,
                    'delay': delay
                })
            
            if box_configs:
                all_account_configs.append({
                    'account': account,
                    'boxes': box_configs
                })
        
        if not all_account_configs:
            print(Colors.red + "[!] Không có cấu hình nào!" + Colors.reset)
            input("Nhấn Enter để tiếp tục...")
            return
            
        self.ui_deptraiquatienoi()
        self.tien_deptrai()
        print(Colors.green + "[BẮT ĐẦU NHÂY TAG]" + Colors.reset)
        print(Colors.cyan + "-" * 50 + Colors.reset)
        
        threads = []
        for account_config in all_account_configs:
            account = account_config['account']
            for box_config in account_config['boxes']:
                thread = threading.Thread(
                    target=self.nhay_tag,
                    args=(
                        account['api'],
                        box_config['box']['id'],
                        box_config['box']['name'],
                        box_config['members'],
                        box_config['delay'],
                        account['number']
                    )
                )
                thread.daemon = True
                thread.start()
                threads.append(thread)
                
        print(Colors.green + f"[+] Đã khởi động {len(threads)} luồng!" + Colors.reset)
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print(Colors.red + "\n[!] Đang dừng các luồng..." + Colors.reset)

    def run(self):
        while True:
            self.ui_deptraiquatienoi()
            self.tien_deptrai()
            self.ui_dcmmvip()
            
            choice = input("Chọn chức năng: ").strip()
            
            if choice == '1':
                self.treo_zalo_function()
            elif choice == '2':
                self.nhay_tag_function()
            elif choice == '0':
                print(Colors.green + "Cảm ơn bạn đã sử dụng!" + Colors.reset)
                break
            else:
                print(Colors.red + "[!] Lựa chọn không hợp lệ!" + Colors.reset)
                time.sleep(1)

if __name__ == "__main__":
    bot = PhamTienDzai()
    bot.run()

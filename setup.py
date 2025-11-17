from curl_cffi import requests
from datetime import datetime
from colorama import *
import asyncio, random, json, uuid, os, pytz

init()

wib = pytz.timezone('Asia/Ho_Chi_Minh')

USER_AGENT = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.127 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.65 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.133 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:114.0) Gecko/20100101 Firefox/114.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:113.0) Gecko/20100101 Firefox/113.0",
    "Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:113.0) Gecko/20100101 Firefox/113.0",
    "Mozilla/5.0 (X11; Arch Linux; Linux x86_64; rv:112.0) Gecko/20100101 Firefox/112.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.127 Safari/537.36 Edg/113.0.1774.35",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.121 Safari/537.36 Edg/112.0.1722.64",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.64 Safari/537.36 Edg/111.0.1661.54",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.137 Safari/537.36 Edg/112.0.1722.68",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_7_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36 OPR/99.0.4788.77",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.127 Safari/537.36 OPR/98.0.4759.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36 Brave/1.52.129",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.126 Safari/537.36 Brave/1.51.110",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.127 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36 Vivaldi/6.1.3035.100",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.126 Safari/537.36 Vivaldi/6.0.2979.22",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/114.0.5735.91 Safari/537.36"
]

class Exeos:
    def __init__(self) -> None:
        self.BASE_API = "https://api.exeos.network"
        self.REF_CODE = "REF4VEVZRFI"
        self.HEADERS = {}
        self.proxies = []
        self.proxy_index = 0
        self.account_proxies = {}
        self.access_tokens = {}
        self.user_nodes = []
        self.node_datas = []
        self.nodes_count = 0

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL} "
            f"{Fore.WHITE + Style.BRIGHT}| {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Exeos {Fore.BLUE + Style.BRIGHT}Bot Tự Động
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    
    def load_accounts(self):
        filename = "accounts.json"
        try:
            if not os.path.exists(filename):
                self.log(f"{Fore.RED + Style.BRIGHT}Không tìm thấy file {filename}.{Style.RESET_ALL}")
                return

            with open(filename, 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                return []
        except json.JSONDecodeError:
            return []

    def save_nodes(self, new_nodes):
        filename = "nodes.json"
        try:
            if not os.path.exists(filename):
                with open(filename, 'w') as file:
                    json.dump([], file, indent=4)

            if os.path.getsize(filename) == 0:
                existing_nodes = []
            else:
                with open(filename, 'r') as file:
                    existing_nodes = json.load(file)

            for new_node in new_nodes:
                email = new_node["Email"]
                token = new_node["Token"]
                new_node_list = new_node.get("Nodes", [])

                found = False
                for existing_node in existing_nodes:
                    if existing_node["Email"] == email:
                        found = True
                        existing_node["Token"] = token

                        if not existing_node.get("Nodes"):
                            existing_node["Nodes"] = new_node_list
                        else:
                            existing_node_ids = {node["nodeId"] for node in existing_node["Nodes"]}
                            for node in new_node_list:
                                if node["nodeId"] not in existing_node_ids:
                                    existing_node["Nodes"].append(node)
                        break

                if not found:
                    existing_nodes.append(new_node)

            with open(filename, 'w') as file:
                json.dump(existing_nodes, file, indent=4)

            self.log(f"{Fore.GREEN + Style.BRIGHT}Dữ liệu node đã được lưu thành công{Style.RESET_ALL}")
        except Exception as e:
            self.log(
                f"{Fore.RED + Style.BRIGHT}Lưu node thất bại:{Style.RESET_ALL} "
                f"{Fore.YELLOW + Style.BRIGHT}{str(e)}{Style.RESET_ALL}"
            )
            return []
    
    async def load_proxies(self, use_proxy_choice: int):
        filename = "proxy.txt"
        try:
            if use_proxy_choice == 1:
                response = await asyncio.to_thread(requests.get, "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/all.txt")
                response.raise_for_status()
                content = response.text
                with open(filename, 'w') as f:
                    f.write(content)
                self.proxies = [line.strip() for line in content.splitlines() if line.strip()]
            else:
                if not os.path.exists(filename):
                    self.log(f"{Fore.RED + Style.BRIGHT}Không tìm thấy file {filename}.{Style.RESET_ALL}")
                    return
                with open(filename, 'r') as f:
                    self.proxies = [line.strip() for line in f.read().splitlines() if line.strip()]
            
            if not self.proxies:
                self.log(f"{Fore.RED + Style.BRIGHT}Không tìm thấy proxy.{Style.RESET_ALL}")
                return

            self.log(
                f"{Fore.GREEN + Style.BRIGHT}Tổng số proxy: {Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT}{len(self.proxies)}{Style.RESET_ALL}"
            )
        
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}Tải proxy thất bại: {e}{Style.RESET_ALL}")
            self.proxies = []

    def check_proxy_schemes(self, proxies):
        schemes = ["http://", "https://", "socks4://", "socks5://"]
        if any(proxies.startswith(scheme) for scheme in schemes):
            return proxies
        return f"http://{proxies}"

    def get_next_proxy_for_account(self, account):
        if account not in self.account_proxies:
            if not self.proxies:
                return None
            proxy = self.check_proxy_schemes(self.proxies[self.proxy_index])
            self.account_proxies[account] = proxy
            self.proxy_index = (self.proxy_index + 1) % len(self.proxies)
        return self.account_proxies[account]

    def rotate_proxy_for_account(self, account):
        if not self.proxies:
            return None
        proxy = self.check_proxy_schemes(self.proxies[self.proxy_index])
        self.account_proxies[account] = proxy
        self.proxy_index = (self.proxy_index + 1) % len(self.proxies)
        return proxy
        
    def generate_node_id(self):
        node_id = str(uuid.uuid4())
        return f"node:ext:{node_id}"

    def mask_account(self, account):
        if '@' in account:
            local, domain = account.split('@', 1)
            mask_account = local[:3] + '*' * 3 + local[-3:]
            return f"{mask_account}@{domain}"

    def print_question(self):
        while True:
            try:
                print(f"{Fore.WHITE + Style.BRIGHT}1. Tạo node mới{Style.RESET_ALL}")
                print(f"{Fore.WHITE + Style.BRIGHT}2. Lấy node hiện có{Style.RESET_ALL}")
                option = int(input(f"{Fore.BLUE + Style.BRIGHT}Chọn [1/2] -> {Style.RESET_ALL}").strip())

                if option in [1, 2]:
                    option_type = "Tạo mới" if option == 1 else "Lấy hiện có"
                    print(f"{Fore.GREEN + Style.BRIGHT}Đã chọn {option_type} node.{Style.RESET_ALL}")
                    break
                else:
                    print(f"{Fore.RED + Style.BRIGHT}Vui lòng nhập 1 hoặc 2.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED + Style.BRIGHT}Đầu vào không hợp lệ. Vui lòng nhập số (1 hoặc 2).{Style.RESET_ALL}")

        if option == 1:
            while True:
                try:
                    count = int(input(f"{Fore.YELLOW + Style.BRIGHT}Bạn muốn tạo bao nhiêu node cho mỗi tài khoản? -> {Style.RESET_ALL}").strip())
                    if count > 0:
                        self.nodes_count = count
                        break
                    else:
                        print(f"{Fore.RED + Style.BRIGHT}Vui lòng nhập số dương.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED + Style.BRIGHT}Đầu vào không hợp lệ. Vui lòng nhập số.{Style.RESET_ALL}")

        while True:
            try:
                print(f"{Fore.WHITE + Style.BRIGHT}1. Chạy với proxy miễn phí Proxyscrape{Style.RESET_ALL}")
                print(f"{Fore.WHITE + Style.BRIGHT}2. Chạy với proxy riêng{Style.RESET_ALL}")
                print(f"{Fore.WHITE + Style.BRIGHT}3. Chạy không dùng proxy{Style.RESET_ALL}")
                choose = int(input(f"{Fore.BLUE + Style.BRIGHT}Chọn [1/2/3] -> {Style.RESET_ALL}").strip())

                if choose in [1, 2, 3]:
                    proxy_type = (
                        "với proxy miễn phí Proxyscrape" if choose == 1 else 
                        "với proxy riêng" if choose == 2 else 
                        "không dùng proxy"
                    )
                    print(f"{Fore.GREEN + Style.BRIGHT}Đã chọn chạy {proxy_type}.{Style.RESET_ALL}")
                    break
                else:
                    print(f"{Fore.RED + Style.BRIGHT}Vui lòng nhập 1, 2 hoặc 3.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED + Style.BRIGHT}Đầu vào không hợp lệ. Vui lòng nhập số (1, 2 hoặc 3).{Style.RESET_ALL}")

        rotate = False
        if choose in [1, 2]:
            while True:
                rotate = input(f"{Fore.BLUE + Style.BRIGHT}Xoay proxy không hợp lệ? [y/n] -> {Style.RESET_ALL}").strip()
                if rotate in ["y", "n"]:
                    rotate = rotate == "y"
                    break
                else:
                    print(f"{Fore.RED + Style.BRIGHT}Đầu vào không hợp lệ. Vui lòng nhập 'y' hoặc 'n'.{Style.RESET_ALL}")

        return option, choose, rotate
    
    async def check_connection(self, proxy=None):
        url = "https://api.ipify.org?format=json"
        proxies = {"http": proxy, "https": proxy} if proxy else None
        try:
            response = await asyncio.to_thread(requests.get, url=url, proxies=proxies, timeout=30, impersonate="chrome110", verify=False)
            response.raise_for_status()
            return True
        except Exception as e:
            self.log(
                f"{Fore.CYAN + Style.BRIGHT}Trạng thái:{Style.RESET_ALL} "
                f"{Fore.RED + Style.BRIGHT}Kết nối không thành công{Style.RESET_ALL} "
                f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL} "
                f"{Fore.YELLOW + Style.BRIGHT}{str(e)}{Style.RESET_ALL}"
            )
            return None
    
    async def email_login(self, email: str, password: str, proxy=None, retries=5):
        url = f"{self.BASE_API}/auth/web/email/login"
        data = json.dumps({"email": email, "password": password, "referralCode": self.REF_CODE})
        headers = self.HEADERS[email].copy()
        headers["Content-Length"] = str(len(data))
        headers["Content-Type"] = "application/json"
        for attempt in range(retries):
            proxies = {"http": proxy, "https": proxy} if proxy else None
            try:
                response = await asyncio.to_thread(requests.post, url=url, headers=headers, data=data, proxies=proxies, timeout=60, impersonate="chrome110", verify=False)
                response.raise_for_status()
                return response.json()
            except Exception as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                self.log(
                    f"{Fore.CYAN + Style.BRIGHT}Trạng thái:{Style.RESET_ALL} "
                    f"{Fore.RED + Style.BRIGHT}Đăng nhập thất bại{Style.RESET_ALL} "
                    f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL} "
                    f"{Fore.YELLOW + Style.BRIGHT}{str(e)}{Style.RESET_ALL}"
                )
                return None
            
    async def user_data(self, email: str, proxy=None, retries=5):
        url = f"{self.BASE_API}/account/web/me"
        headers = self.HEADERS[email].copy()
        headers["Authorization"] = f"Bearer {self.access_tokens[email]}"
        for attempt in range(retries):
            proxies = {"http": proxy, "https": proxy} if proxy else None
            try:
                response = await asyncio.to_thread(requests.get, url=url, headers=headers, proxies=proxies, timeout=60, impersonate="chrome110", verify=False)
                response.raise_for_status()
                return response.json()
            except Exception as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                self.log(
                    f"{Fore.CYAN + Style.BRIGHT}Lỗi:{Style.RESET_ALL} "
                    f"{Fore.RED + Style.BRIGHT}Lấy danh sách node hiện có thất bại{Style.RESET_ALL} "
                    f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL} "
                    f"{Fore.YELLOW + Style.BRIGHT}{str(e)}{Style.RESET_ALL}"
                )
                return None
            
    async def process_check_connection(self, email: str, use_proxy: bool, rotate_proxy: bool):
        while True:
            proxy = self.get_next_proxy_for_account(email) if use_proxy else None
            self.log(
                f"{Fore.CYAN + Style.BRIGHT}Proxy:{Style.RESET_ALL} "
                f"{Fore.WHITE + Style.BRIGHT}{proxy}{Style.RESET_ALL}"
            )

            is_valid = await self.check_connection(proxy)
            if is_valid:
                return True
            
            if rotate_proxy:
                proxy = self.rotate_proxy_for_account(email)
                await asyncio.sleep(1)
                continue

            return False
            
    async def process_user_login(self, email: str, password: str, use_proxy: bool, rotate_proxy: bool):
        is_valid = await self.process_check_connection(email, use_proxy, rotate_proxy)
        if is_valid:
            proxy = self.get_next_proxy_for_account(email) if use_proxy else None

            login = await self.email_login(email, password, proxy)
            if login and login.get("status") == "success":
                self.access_tokens[email] = login["data"]["token"]

                self.log(
                    f"{Fore.CYAN + Style.BRIGHT}Trạng thái:{Style.RESET_ALL} "
                    f"{Fore.GREEN + Style.BRIGHT}Đăng nhập thành công{Style.RESET_ALL}"
                )
                return True
            
            elif login and login.get("status") == "fail":
                err_msg = login.get("error", "Lỗi không xác định")
                self.log(
                    f"{Fore.CYAN + Style.BRIGHT}Trạng thái:{Style.RESET_ALL} "
                    f"{Fore.RED + Style.BRIGHT}Đăng nhập thất bại{Style.RESET_ALL} "
                    f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL} "
                    f"{Fore.YELLOW + Style.BRIGHT}{err_msg}{Style.RESET_ALL}"
                )

            return False
            
    async def process_get_exiting_nodes(self, email: str, use_proxy: bool):
        proxy = self.get_next_proxy_for_account(email) if use_proxy else None
            
        user = await self.user_data(email, proxy)
        if user and user.get("status") == "success":
            exciting_nodes = user["data"]["networkNodes"]

            if isinstance(exciting_nodes, list) and len(exciting_nodes) == 0:
                self.log(
                    f"{Fore.CYAN + Style.BRIGHT}Node:{Style.RESET_ALL} "
                    f"{Fore.RED + Style.BRIGHT}Không tìm thấy node nào{Style.RESET_ALL}"
                )
                return self.node_datas

            for node in exciting_nodes:
                node_id = node["nodeId"]
                self.node_datas.append({"nodeId": node_id})

            self.log(
                f"{Fore.CYAN + Style.BRIGHT}Node:{Style.RESET_ALL} "
                f"{Fore.GREEN + Style.BRIGHT}Bạn có {Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT}{len(exciting_nodes)} node{Style.RESET_ALL}"
            )
            return self.node_datas

        return self.node_datas
                
    async def process_create_new_nodes(self):
        for i in range(self.nodes_count):
            node_id = self.generate_node_id()
            self.node_datas.append({"nodeId": node_id})

        self.log(
            f"{Fore.CYAN + Style.BRIGHT}Node:{Style.RESET_ALL} "
            f"{Fore.WHITE + Style.BRIGHT}{self.nodes_count} node {Style.RESET_ALL}"
            f"{Fore.GREEN + Style.BRIGHT}đã được tạo thành công{Style.RESET_ALL}"
        )
        return self.node_datas

    async def process_accounts(self, email: str, password: str, option: int, use_proxy: bool, rotate_proxy: bool):
        logined = await self.process_user_login(email, password, use_proxy, rotate_proxy)
        if logined:
            if option == 1:
                node_datas = await self.process_create_new_nodes()
                self.user_nodes.append({"Email": email, "Token": self.access_tokens[email], "Nodes": node_datas})
                self.save_nodes(self.user_nodes)
            elif option == 2:
                node_datas = await self.process_get_exiting_nodes(email, use_proxy)
                self.user_nodes.append({"Email": email, "Token": self.access_tokens[email], "Nodes": node_datas})
                self.save_nodes(self.user_nodes)

    async def main(self):
        try:
            accounts = self.load_accounts()
            if not accounts:
                self.log(f"{Fore.RED + Style.BRIGHT}Không tải được tài khoản nào.{Style.RESET_ALL}")
                return

            option, proxy_choice, rotate_proxy = self.print_question()

            use_proxy = False
            if proxy_choice in [1, 2]:
                use_proxy = True

            self.clear_terminal()
            self.welcome()
            self.log(
                f"{Fore.GREEN + Style.BRIGHT}Tổng số tài khoản: {Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT}{len(accounts)}{Style.RESET_ALL}"
            )

            if use_proxy:
                await self.load_proxies(proxy_choice)

            separator = "=" * 25
            for idx, account in enumerate(accounts, start=1):
                if account:
                    email = account["Email"]
                    password = account["Password"]
                    self.log(
                        f"{Fore.CYAN + Style.BRIGHT}{separator}[{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {idx} {Style.RESET_ALL}"
                        f"{Fore.CYAN + Style.BRIGHT}trong{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {len(accounts)} {Style.RESET_ALL}"
                        f"{Fore.CYAN + Style.BRIGHT}]{separator}{Style.RESET_ALL}"
                    )

                    if not "@" in email or not password:
                        self.log(
                            f"{Fore.CYAN + Style.BRIGHT}Trạng thái:{Style.RESET_ALL} "
                            f"{Fore.RED + Style.BRIGHT}Dữ liệu tài khoản không hợp lệ{Style.RESET_ALL}"
                        )
                        continue

                    self.HEADERS[email] = {
                        "Accept": "*/*",
                        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
                        "Origin": "https://app.exeos.network",
                        "Referer": "https://app.exeos.network/",
                        "Sec-Fetch-Dest": "empty",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Site": "same-site",
                        "User-Agent": random.choice(USER_AGENT)
                    }

                    self.log(
                        f"{Fore.CYAN + Style.BRIGHT}Tài khoản:{Style.RESET_ALL} "
                        f"{Fore.WHITE + Style.BRIGHT}{self.mask_account(email)}{Style.RESET_ALL}"
                    )

                    await self.process_accounts(email, password, option, use_proxy, rotate_proxy)
                    await asyncio.sleep(3)

            self.log(f"{Fore.CYAN + Style.BRIGHT}={Style.RESET_ALL}" * 60)

        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}Lỗi: {e}{Style.RESET_ALL}")
            raise e

if __name__ == "__main__":
    try:
        bot = Exeos()
        asyncio.run(bot.main())
    except KeyboardInterrupt:
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL} "
            f"{Fore.WHITE + Style.BRIGHT}| {Style.RESET_ALL}"
            f"{Fore.RED + Style.BRIGHT}[ THOÁT ] Exeos - BOT{Style.RESET_ALL}"
        )
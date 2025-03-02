try:
    import subprocess
    import platform 
    from time import sleep
    import httpx
except ModuleNotFoundError:
    exit("\033[38;5;129mSOME REQUIRED MODULES \033[38;5;208mARE MISSING IN \033[38;5;129mYOUR SYSTEM. TRY TO \033[38;5;46mINSTALL THEM MANUALLY.")

def OScheck():
    if platform.system() == "Windows":
        subprocess.run(["cls"], shell=True)
    elif platform.system() == "Linux":
        subprocess.run(["clear"], shell=True)

def banner():
    OScheck()
    print("""
  \033[31m__           __  __       ___ \033[33m  _      __  ___ __       _  ___  _  
 \033[32m/__))__///  //__)/__)//| )(_    \033[5m/ )(__// _)(_  \033[32m/__)/|/| /_|(_  //_| 
/   \033[36m/  /((__(/   /   (/ |/ /__  (__  / /(_) /__/ ( /   |(  |/  ((  |

\033[35mCODED BY \033[31m~PCM@\033[97mVend3ttA(v1.0)                                                                                                         
""")

def choices():
    OScheck()
    banner()
    print("""
\033[97m1. WAYBACK MACHINE SPECIFIC \033[95mDOMAIN SEARCH
\033[94m2. WAYBACK MACHINE SUBDOMAIN \033[91mSEARCH
\033[93m3. WAYBACK MACHINE FIND \033[96mSENSITIVE DATA (Coming Soon in v1.1)""")

def waybackDomainSearch():
    OScheck()
    banner()
    domain = input("[*] ENTER A TARGET DOMAIN (e.g., redacted.com): ")
    if domain.startswith(("http://", "https://", "http", "https")):
        print("[X] TRY AGAIN!")
    else:
        try:
            results = httpx.get(f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=text&fl=original&collapse=urlkey").text
            print("\033[1;32;40m[*] EXTRACTING ALL DOMAINS...")
            sleep(0.5)
            print(results)
            output = input("\033[1;32;40m[*] ENTER FILENAME TO SAVE (e.g., targets.txt): ")
            print("\033[1;36;40m[*] SAVING...")
            sleep(0.5)
            with open(output, 'w') as file:
                file.write(results)
            print(f"\033[1;31;40mSCAN RESULT SAVED IN {output}.")
            sleep(1)
            main()
        except Exception as e:
            print(f"[X] ERROR: {e}")

def waybackSubdomainSearch():
    OScheck()
    banner()
    domain = input("[*] ENTER A TARGET DOMAIN (e.g., redacted.com): ")
    if domain.startswith(("http://", "https://", "http", "https")):
        print("[X] TRY AGAIN!")
    else:
        try:
            results = httpx.get(f"https://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=text&fl=original&collapse=urlkey&filter=statuscode:200").text
            print("\033[1;32;40m[*] EXTRACTING ALL DOMAINS...")
            sleep(0.5)
            print(results)
            output = input("\033[1;32;40m[*] ENTER FILENAME TO SAVE: ")
            print("\033[1;36;40m[*] SAVING...")
            sleep(0.5)
            with open(output, 'w') as file:
                file.write(results)
            print(f"\033[1;31;40mSCAN RESULT SAVED IN {output}.")
            sleep(1)
            main()
        except Exception as e:
            print(f"[X] ERROR: {e}")

def main():
    OScheck()
    banner()
    choices()
    while 1:
        try:
            usr = input("\033[38;5;196m\n\nPLEASE \033[38;5;129mCHOOSE: ")
            if usr == "1":
                waybackDomainSearch()
            elif usr == "2":
                waybackSubdomainSearch()
            elif usr == "3":
                print("\033[1;33;40m[*] FEATURE COMING SOON IN v1.1")
            elif usr in ["0","4","5","6","7","8","9","10"]:
                print("\033[31;5;40m[*] NOT AVAILABLE\033[38;5;40m")
            elif usr.lower() in ("exit", "x"):
                print("\033[31;5;40m[*] EXITING...\033[38;5;40m")
                sleep(1)
                exit("\033[38;5;196mTHANK YOU FOR USING MY TOOL.\033[0m")
            else:
                print("\033[1;33;40m[X] INVALID INPUT!")
        except ValueError:
            print("\033[1;33;40m[X] INVALID INPUT!")
        except KeyboardInterrupt:
            print("\n\033[31;5;40m[*] EXITING...\033[38;5;40m")
            sleep(1)
            exit("\033[38;5;196mTHANK YOU FOR USING MY TOOL.\033[0m")

if __name__ == "__main__":
    main()

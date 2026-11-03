#!/usr/bin/env python3

import time

print("")
print("="*50)
print("      Welcome to CLI Downloader Simulator      ")
print("="*50)
print("")

while True:
    
    file_size_dul = ["GB", "MB", "KB"]
    file_size = input("Enter File Size: ").strip().upper().split()
    # print(file_size, "\n")

    if not file_size:
        print("Enter proper Values\n")
        continue

    if file_size[0].startswith("-"):
        print("Negative Numbers are not acceptable\n")
        continue

    if len(file_size) > 2:
        print("Invalid Input\n")
        continue

    try:

        if "." not in file_size[0]:    
            file_size[0] = int(file_size[0])
            # print(f"Num= {file_size[0]}, type= {type(file_size[0])}")
        elif "." in file_size[0]:
            file_size[0] = float(file_size[0])
            # print(f"Num= {file_size[0]}, type= {type(file_size[0])}")

        if file_size[0] == 0:
            print("File Size should be higher than 0\n")
            continue
        else:
            if file_size[1] in file_size_dul:
                print(f"File Size: {file_size[0]}")
                print(f"File Size Unit: {file_size[1]}")
                
                match file_size[1]:
                    case "KB":
                        filesize_in_bytes = file_size[0]*1000
                        print(f"File Size in Bytes: {filesize_in_bytes:.2f}\n") 
                        # print(f"File Size in Bytes: {file_size[0]*1000:.2f}\n")
                    case "MB":
                        filesize_in_bytes = file_size[0]*(1000**2)
                        print(f"File Size in Bytes: {filesize_in_bytes:.2f}\n") 
                        # print(f"File Size in Bytes: {file_size[0]*(1000**2):.2f}\n")
                    case "GB":
                        filesize_in_bytes = file_size[0]*(1000**3)
                        print(f"File Size in Bytes: {filesize_in_bytes:.2f}\n") 
                        # print(f"File Size in Bytes: {file_size[0]*(1000**3):.2f}\n")
                break
            else:
                print("Invalid Input\n")
                continue

    except IndexError:
        print(f"Enter input properly. Example: 23 GB\n")
        continue
    except ValueError:
        print(f"Enter input properly. Example: 23 MB\n")
        continue


while True:
    internet_speed_dul = ["bps", "kbps", "mbps", "gbps"]
    internet_speed = input("Enter Internet Speed: ").strip().lower().split()

    if not internet_speed:
        print("Enter proper Values\n")
        continue

    if internet_speed[0].startswith("-"):
        print("Negative Numbers are not acceptable")
        continue

    if len(internet_speed) > 2:
        print("Invalid Input\n")
        continue

    try:
        
        if "." not in internet_speed[0]:
            internet_speed[0] = int(internet_speed[0])
        elif "." in internet_speed[0]:
            internet_speed[0] = float(internet_speed[0])
        
        if internet_speed[0] == 0:
            print("Internet Speed should be higher than 0\n")
            continue
        else:
            if internet_speed[1] in internet_speed_dul:
                print(f"Internet Speed: {internet_speed[0]}")
                print(f"Internet Speed Unit: {internet_speed[1].capitalize()}")
                
                match internet_speed[1]:
                    case "bps":
                        internetspeed_in_bytes = internet_speed[0] / 8
                        print(f"Internet Speed in Bytes: {internetspeed_in_bytes:.2f}")
                        # print(f"Internet Speed in Bytes: {internet_speed[0] / 8:.2f}\n")
                    case "kbps":
                        internetspeed_in_bytes = (internet_speed[0] * 1000) / 8
                        print(f"Internet Speed in Bytes: {internetspeed_in_bytes:.2f}")
                        # print(f"Internet Speed in Bytes: {(internet_speed[0] * 1000) / 8:.2f}\n")
                    case "mbps":
                        internetspeed_in_bytes = (internet_speed[0] * 1000**2) / 8
                        print(f"Internet Speed in Bytes: {internetspeed_in_bytes:.2f}")
                        # print(f"Internet Speed in Bytes: {(internet_speed[0] * 1000**2) / 8:.2f}\n")
                    case "gbps":
                        internetspeed_in_bytes =(internet_speed[0] * 1000**3) / 8
                        print(f"Internet Speed in Bytes: {internetspeed_in_bytes:.2f}")
                        # print(f"Internet Speed in Bytes: {(internet_speed[0] * 1000**3) / 8:.2f}\n")   
                break
            else:
                print("Invalid Input\n")
                continue

    except IndexError:
        print("Enter input properly. Example: 23 Gbps\n")
        continue
    except ValueError:
        print("Enter input properly. Example: 23 Mbps\n")
        continue

while True:
    
    try:
        # bar_length = int(input("\nEnter Bar Length (1-100): "))
        bar_length = 100
        
        if bar_length >= 1 and bar_length < 101:
            break
        else:
            print("Value should be greater than 100 and 0\n")
            continue
    
    except ValueError:
        print("Invalid Input. Try Again.\n")
        continue


bar = ["░"] * bar_length
full_bar = "█"

time.sleep(1)
print("\nStarting Download...\n")
time.sleep(1)

remaining_download = max(filesize_in_bytes, internetspeed_in_bytes) - internetspeed_in_bytes

if filesize_in_bytes > internetspeed_in_bytes:
    downloaded = filesize_in_bytes - remaining_download
else:
    downloaded = filesize_in_bytes - min(remaining_download, internetspeed_in_bytes)

downloaded_percentage = float((downloaded / filesize_in_bytes) * 100)

time.sleep(1)

print(f"\033[38;2;121;255;143mDownloading: {"".join(bar)}\033[0m", end="\r")
time.sleep(1)

while True:
    
    time.sleep(1)
    
    if downloaded_percentage == 100.0:
            # print(f"Downloaded (in %): {downloaded_percentage:.2f}% | Downloaded (in B): {downloaded} | Downloading (in B): {remaining_download}")
            print(f"\033[38;2;121;255;143mDownloaded: {"█"*bar_length} [ 100.0% | {filesize_in_bytes}/{filesize_in_bytes} ]\033[0m")
            print("")
            print("\nDownload Finished!!\n")
            break
    
    remaining_download -= internetspeed_in_bytes
    downloaded = filesize_in_bytes - remaining_download
    downloaded_percentage = float((downloaded / filesize_in_bytes) * 100)
    round_downloaded_percentage = int(downloaded_percentage)
    
    dp_list = []
    
    for i in range(1, round_downloaded_percentage + 1):
        dp_list.append(i)
    
    if remaining_download <= 0:
        remaining_download = 0
        print("\033[K")
        print(f"\033[38;2;121;255;143mDownloaded: {"█"*bar_length} [ 100.0% | {filesize_in_bytes}/{filesize_in_bytes} ]\033[0m")
        time.sleep(2)
        print("")
        print("\nDownload Finished!!\n")
        break

    if len(dp_list) >= 1 and len(dp_list) <= 100:

        if len(dp_list) != 0:

            if dp_list[-1] == 100:
                print("Break 1")
                print(f"Testing: {full_bar * bar_length}")

            
            else:
                bar[:round_downloaded_percentage] = full_bar * round_downloaded_percentage
    
    print(f"\033[38;2;121;255;143mDownloading: {"".join(bar)} [ {downloaded_percentage:.2f}% | {int(downloaded):.2f}/{filesize_in_bytes} ]\033[0m", end="\r")
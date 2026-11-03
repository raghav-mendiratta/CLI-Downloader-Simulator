import time

print("")
print("Empty Bar: ", "[ " + "░"*100 + " ]")
print("Full Bar: ", "[ " + "█"*100 + " ]")
print("")

download_percentage = 50

dp_list = []

for i in range(1, download_percentage + 1):
    # print(i)
    dp_list.append(i)

print(dp_list)
print("")

# exit(1)

bar_length = 100
bar = ["░"] * bar_length
full_bar = "█"
print(f"Bar Length: {len(bar)}")
print(f"Bar Length Total Index: {len(bar) - 1}")
print("List length: ", len(dp_list))
print(f"Dp List: {dp_list}")
print(f"DP List all Index: {len(dp_list) - 1}")
# print(dp_list[59])

full_bar_placement = len(dp_list) - 1
print(f"Full Bar Placement Value: {full_bar_placement + 1}")
print(f"Full Bar Placement Index Value: {full_bar_placement}")
print("")

print(len(bar[:download_percentage]))
print(bar[:download_percentage - 1])
print(f"Download Percentage: {download_percentage}")
exit(1)
time.sleep(1)

if len(dp_list) != 0:

    if dp_list[-1] == 100:
        print("Break 1")
        print(f"Testing: {full_bar * bar_length}")

    else:
        bar[:download_percentage - 1] = full_bar * download_percentage
        print(f"Testing: {"".join(bar)}")
        print("Break 2")    
else:
    print(f"Testing: {"".join(bar)}")
    print("Break 3")
    
exit(1)


# while len(dp_list) >= 1 and len(dp_list) <= 100:
    
    
#     bar[-1 + dp_list[-1]] = full_bar
    
#     print(f"Testing: {"".join(bar)}")
    
#     if dp_list[-1] == 100:
#         print("Break 1")
#         break

# bar[-1 + dp_list[-1]] = full_bar
dp_list_last_value = dp_list[-1]
bar[0 : dp_list_last_value] = full_bar
print(f"Testing: {"".join(bar)}")






# while len(dp_list) >= 1 and len(dp_list) <= 101:
    
#     print(f"Full Bar Placement (Bar | Real): {full_bar_placement}")
#     print(f"Full Bar Placement (Bar): {full_bar_placement + 1}")
#     full_bar_input = dp_list[full_bar_placement] - 1
#     print(f"Full bar Input (Index | Real): {full_bar_input + 1}")
#     print(f"Full bar Input (Index): {full_bar_input}")
#     # exit(1)
#     bar[full_bar_input] = "█"
#     # print(f"Testing: {"".join(bar)}", end="\r")
#     print(f"Testing: {"".join(bar)}")
    
#     full_bar_placement += 1
    
#     print(f"DP List previous Value: {dp_list[-1]}")
    
#     if full_bar_placement == dp_list[-1]:
#         print("Break 1")
#         break
    
    
    # time.sleep(0.03)

    
# print("\n")
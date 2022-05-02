import sys
from daqhats import hat_list, HatIDs, mcc118

board_list = hat_list(filter_by_id = HatIDs.ANY)
if board_list[0].id == HatIDs.MCC_118:
    board = mcc118(board_list[0].address)

g_var = board.a_in_scan_read(0,0)
print(g_var)
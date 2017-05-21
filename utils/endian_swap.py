def swap_endian(input_num):
    part_1 = (input_num & 0xff00) >> 8
    part_2 = input_num & 0x00ff
    mid_proc = part_2 << 8
    part_1_1 = (part_1 & 0xf0) >> 4
    part_1_2 = part_1 & 0x0f
    part_1_2 <<= 4
    part_1_2 |= part_1_1
    mid_proc |= part_1_2
    last_hex = mid_proc & 0x000f
    if (hex(last_hex) == '0x0'):
        print("DERP")
        mid_proc = ((mid_proc & 0xff00) | (mid_proc & 0x00f0) >> 4)
    return mid_proc
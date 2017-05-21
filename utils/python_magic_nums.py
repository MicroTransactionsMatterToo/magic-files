magic_codes = {
     "Python 1.5": 20121,
     "Python 1.5.1": 20121,
     "Python 1.5.2": 20121,
     "Python 1.6": 50428,
     "Python 2.0": 50832,
     "Python 2.0.1": 50823,
     "Python 2.1": 60202,
     "Python 2.1.1": 60202,
     "Python 2.1.2": 60202,
     "Python 2.2": 60717,
     "Python 2.3a0": 62011,
     "Python 2.3a0 (2nd)": 62021,
     "Python 2.4a0": 62041,
     "Python 2.5a0": 62071,
     "Python 2.5a0 (AST-BRANCH)": 62081,
     "Python 2.5a0 (WITH)": 62091,
     "Python 2.5a0 (changed WITH_CLEANUP opcode)": 62092,
     "Python 2.5b3 (fix wrong code: for x, in ...)": 62101,
     "Python 2.5b3 (fix wrong code: x+= yield)": 62111,
     "Python 2.5c1": 62121,
     "Python 2.5c22": 62131,
     "Python 2.6a0": 62151,
     "Python 2.7a0 (optimise list comprehensions/change LIST_APPEND)": 62171,
     "Python 2.7a0 (optimise conditional branches)": 62181,
     "Python 2.7a0 (introduce SETUP_WITH)": 62191,
     "Python 2.7a0 (introduce BUILD_SET)": 62201,
     "Python 2.7a0 (introduce MAP_ADD and SET_ADD)": 62211,
     "Python 3000": 3000,
     "Python 3000 (removed UNARY_CONVERT)": 3010,
     "Python 3000 (added BUILD_SET)": 3020,
     "Python 3000 (added keyword-only parameters)": 3030,
     "Python 3000 (added signature annotations)": 3040,
     "Python 3000 (print becomes a function)": 3050,
     "Python 3000 (PEP 3115 metaclass syntax)": 3060,
     "Python 3000 (string literals become unicode)": 3061,
     "Python 3000 (PEP 3109 raise changes)": 3071,
     "Python 3000 (PEP 3137 make __file__ and __name__ unicode)": 3081,
     "Python 3000 (kill str8 interning)": 3091,
     "Python 3000 (merge from 2.6a0, see 62151)": 3101,
     "Python 3000 (__file__ points to source file)": 3103,
     "Python 3.0a4": 3111,
     "Python 3.0a5": 3131,
     "Python 3.1a0": 3141,
     "Python 3.1a0 (optimise conditional branches)": 3151,
     "Python 3.2a0": 3160,
     "Python 3.2a1": 3170,
     "Python 3.2a2": 3180,
     "Python 3.3a0": 3190,
     "Python 3.3a0 (__qualname added)": 3200,
     "Python 3.3a1": 3220,
     "Python 3.3a4": 3230,
     "Python 3.4a1": 3250,
     "Python 3.4a1 (add LOAD_CLASSDEREF)": 3260,
     "Python 3.4a1 (various tweaks to the __class__ closure)": 3270,
     "Python 3.4a1 (remove implicit class argument)": 3280,
     "Python 3.4a4": 3290,
     "Python 3.4a4 (more changes to __qualname__ computation)": 3300,
     "Python 3.4rc2": 3310,
     "Python 3.5a0": 3320,
     "Python 3.5b1": 3330,
     "Python 3.5b2": 3340,
     "Python 3.5b2 (add GET_YIELD_FROM_ITER opcode #24400)": 3350,
     "Python 3.5.2": 3351,
     "Python 3.6a0": 3360,
     "Python 3.6a0 (lineno delta of code.co_lnotab becomes signed)": 3361,
     "Python 3.6a1": 3370,
     "Python 3.6a1 (add BUILD_CONST_KEY_MAP opcode #27140)": 3371,
     "Python 3.6a1 (MAKE_FUNCTION simplification, remove MAKE_CLOSURE)": 3372,
     "Python 3.6b1": 3373,
     "Python 3.6b1 (add SETUP_ANNOTATIONS and STORE_ANNOTATIONS opcodes #27985)": 3375,
     "Python 3.6b1 (simplify CALL_FUNCTIONS & BUILD_MAP_UNPACK_WITH_CALL)": 3376,
     "Python 3.6b1 (set __class__ cell from type.__new__)": 3377,
     "Python 3.6b2": 3378,
     "Python 3.6rc1": 3379,
     "Python 3.7a0": 3390
}

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


def verbose_dump():
     return ["0 belong 0x{code:x} {pver} BYTE COMPILED FILE".format(code=((swap_endian(x)<<16) | 0x0d0a), pver=y) for y, x in magic_codes.items()]



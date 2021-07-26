# P1

P1 = {
    "DCO": "A1",
    "nDCO": "B1",
    "DATACLK_PORT2": "A3",
    "DATACLK_PORT": "A4",
    "DB0": "A5",
    "DB1": "A6",
    "DB2": "A7",
    "DB3": "A8",
    "DB4": "A9",
    "DB5": "A10"
}

P2 = {
    "DB6": "A1",
    "DB7": "A2",
    "DB8": "A3",
    "DB9": "A4",
    "DB10": "A5",
    "DB11": "A6",
    "DB12": "A7",
    "DB13": "A8",
    "DCO": "C10",
    "nDCO": "D10"
}

# ---

J17_AB_lines = [
    "CLK_DCOA_",
    "CLK_TXI_O_",
    *[f"TXI_DATA_{i}" for i in reversed(range(8, 16))]
]
J17_CD_lines = [
    None,
    None,
    *[f"TXQ_DATA_{i}" for i in reversed(range(8, 16))]
]
J18_AB_lines = [
    *[f"TXI_DATA_{i}" for i in reversed(range(0, 8))],
    None,
    None
]
J18_CD_lines = [
    *[f"TXQ_DATA_{i}" for i in reversed(range(0, 8))],
    "CLK_TXQ_O_",
    "CLK_DCOB_"
]

J17_dict = {}
for i, l in enumerate(J17_AB_lines):
    if l is None: continue
    J17_dict[f"A{i+1}"] = f"{l}_P"
    J17_dict[f"B{i+1}"] = f"{l}_N"
for i, l in enumerate(J17_CD_lines):
    if l is None: continue
    J17_dict[f"C{i+1}"] = f"{l}_P"
    J17_dict[f"D{i+1}"] = f"{l}_N"

J18_dict = {}
for i, l in enumerate(J18_AB_lines):
    if l is None: continue
    J18_dict[f"A{i+1}"] = f"{l}_P"
    J18_dict[f"B{i+1}"] = f"{l}_N"
for i, l in enumerate(J18_CD_lines):
    if l is None: continue
    J18_dict[f"C{i+1}"] = f"{l}_P"
    J18_dict[f"D{i+1}"] = f"{l}_N"

# ---

FMC_map = {
    # H
    "TXI_DATA_13": "LA02",
    "TXI_DATA_14": "LA04",
    "TXI_DATA_9":  "LA07",
    "TXI_DATA_5":  "LA11",
    "TXI_DATA_0":  "LA15",
    "TXQ_DATA_14": "LA19",
    "TXQ_DATA_11": "LA21",
    "TXQ_DATA_8":  "LA24",
    "TXQ_DATA_6":  "LA28",
    "TXQ_DATA_4":  "LA30",
    "TXQ_DATA_2":  "LA32",
    # G
    "CLK_TXI_O":   "LA00",
    "TXI_DATA_12": "LA03",
    "TXI_DATA_10": "LA08",
    "TXI_DATA_6": "LA12",
    "TXI_DATA_2": "LA16",
    "TXQ_DATA_15": "LA20",
    "TXQ_DATA_12": "LA22",
    "TXQ_DATA_9": "LA25",
    "TXQ_DATA_7": "LA29",
    "TXQ_DATA_5": "LA31",
    "TXQ_DATA_3": "LA33",
    # D
    "CLK_TXQ_O": "LA01",
    "TXI_DATA_7": "LA05",
    "TXI_DATA_3": "LA09",
    "TXI_DATA_4": "LA13",
    "CLK_DCOB": "LA17",
    "TXQ_DATA_13": "LA23",
    "TXQ_DATA_10": "LA26",
    # C
    "TXI_DATA_11": "LA06",
    "TXI_DATA_8": "LA10",
    "TXI_DATA_1": "LA14",
    "TXQ_DATA_1": "LA18",
    "TXQ_DATA_0": "LA27"
}

FMC_dict = {}
for k,v in FMC_map.items():
    FMC_dict[f"{k}_P"] = f"{v}_P"
    FMC_dict[f"{k}_N"] = f"{v}_N"

from pprint import pprint
# pprint(FMC_dict)

# ---

# P1 -> J17
# P2 -> J18

def connect(P, J):
    for k in P.keys():
        adapter_net = J[P[k]]
        # print(adapter_net)
        try:
            # print(f"{k.lower()} ->", adapter_net, "->", )
            # print("(\"{}\", 0, Pins(\"fmc1:{}\")),".format(k.lower(), FMC_dict[adapter_net]))
            print("\"fmc1:{}\",  # {}".format(FMC_dict[adapter_net], k.lower()))
        except KeyError:
            pass

connect(P1, J17_dict)
connect(P2, J18_dict)

# import re
# from natsort import natsorted
# from pprint import pprint
# pprint(natsorted(filter(lambda x: re.match(r'TXI_DATA_\d+', x), FMC_dict.keys())))
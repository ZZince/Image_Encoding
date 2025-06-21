from numpy import uint8
import os
def merge(base_list: list, merged: list):
    for elt in merged:
        base_list.append(elt)

    return base_list

def save_raw_data(raw_data: list[uint8], file_path: str = "data/raw_data/image.raw"):
    with open(file_path, "w", encoding="utf-8") as file:
        for data in raw_data:
            casted_data: str = chr(int(data))
            print(casted_data)
            file.write(casted_data)

    file.close()
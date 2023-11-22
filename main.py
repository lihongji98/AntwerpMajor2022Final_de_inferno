import json
import pandas as pd
from demo_parser import demo_parse

if __name__ == '__main__':
    # Set the parse_rate equal to the tick rate at which you would like to parse the frames of the demo.
    # This parameter only matters if parse_frames=True ()
    # For reference, MM demos are usually 64 ticks, and pro/FACEIT demos are usually 128 ticks.
    with open("D:/Liquid-Faze-BLAST2022.json", 'r') as file:
        # Load JSON data from the file into a Python object
        data = json.load(file)

    print(data.keys())

    round_info, round_num = data["gameRounds"], len(data["gameRounds"])
    # round_info
    print(round_info[0])


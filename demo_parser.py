from awpy import DemoParser


def demo_parse():
    demo_parser = DemoParser(
            demofile="demo/liquid-vs-faze-m1-mirage.dem",
            demo_id="Liquid-Faze-BLAST2022",
            parse_rate=128)

    print("========= parsing ============")
    data = demo_parser.parse(return_type='df')
    print("======== parse completed ==========")

    return data

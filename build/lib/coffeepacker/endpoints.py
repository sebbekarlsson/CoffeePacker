from coffeepacker.CoffeePacker import CoffeePacker
import argparse


parser = argparse.ArgumentParser()


def pack():
    parser.add_argument('--path')
    parser.add_argument('--execute')
    parser.add_argument('--export')
    args = parser.parse_args()
    
    packer = CoffeePacker()
    results = packer.pack(args.path, args.execute, args.export)

    print(results)

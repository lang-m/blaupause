import argparse

def main():
    args = argparse.ArgumentParser()
    args.add_argument('--test')
    ca = args.parse_args()
    print('executed as "python -m blaupause"')
    print(ca)
    print('DONE') 

if __name__ == '__main__':
    main()

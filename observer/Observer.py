from observer.BinaryFormatter import BinaryFormatterObs
from observer.DefaultFormatter import DefaultFormatter
from observer.HexFormatter import HexFormatterObs
from observer.OctalFormatter import OctalFormatterObs


def main():
    df = DefaultFormatter('test1')
    hf = HexFormatterObs()
    bf = BinaryFormatterObs()
    of = OctalFormatterObs()

    while True:
        print('1. Add observer |==| 2. Delete observer |==| 3. Insert number |==| 4. Close')
        key = input('Choose option: ')
        if key == '1':
            print('Add Observer:')
            print('1. Hex |==| 2. Binary |==| 3. Octal')
            key = input('Choose option: ')
            if key == '1':
                df.add(hf)
            elif key == '2':
                df.add(bf)
            elif key == '3':
                df.add(of)
            else:
                print(f'unknown option: {key}')
        elif key == '2':
            print('Remove Observer:')
            print('1. Hex |==| 2. Binary |==| 3. Octal')
            key = input('Choose option: ')
            if key == '1':
                if df.observers.__contains__(hf):
                    df.remove(hf)
                    print('Observer was deleted ')
                else:
                    print('The observer cannot be removed because it has not been previously added!')
            elif key == '2':
                if df.observers.__contains__(bf):
                    df.remove(bf)
                    print('Observer was deleted ')
                else:
                    print('The observer cannot be removed because it has not been previously added!')
            elif key == '3':
                if df.observers.__contains__(of):
                    df.remove(of)
                    print('Observer was deleted ')
                else:
                    print('The observer cannot be removed because it has not been previously added!')
            else:
                print(f'unknown option: {key}')
        elif key == '3':
            df.data = input('Insert number: ')
            print(df)
        elif key == '4':
            exit()
        else:
            print(f'unknown option: {key}')


if __name__ == '__main__':
    main()

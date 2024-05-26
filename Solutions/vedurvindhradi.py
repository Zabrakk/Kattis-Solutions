def main():
    inp = float(input())
    if 0 <= inp <= 0.2:
        print('Logn')
    elif 0.3 <= inp <= 1.5:
        print('Andvari')
    elif 1.6 <= inp <= 3.3:
        print('Kul')
    elif 3.4 <= inp <= 5.4:
        print('Gola')
    elif 5.5 <= inp <= 7.9:
        print('Stinningsgola')
    elif 8.0 <= inp <= 10.7:
        print('Kaldi')
    elif 10.8 <= inp <= 13.8:
        print('Stinningskaldi')
    elif 13.9 <= inp <= 17.1:
        print('Allhvass vindur')
    elif 17.2 <= inp <= 20.7:
        print('Hvassvidri')
    elif 20.8 <= inp <= 24.4:
        print('Stormur')
    elif 24.5 <= inp <= 28.4:
        print('Rok')
    elif 28.5 <= inp <= 32.6:
        print('Ofsavedur')
    else:
        print('Farvidri')


if __name__ == '__main__':
    main()

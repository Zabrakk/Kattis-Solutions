def main():
    from sys import stdin
    for line in stdin:
        while '0x' in line or '0X' in line:
            hex_str = ''
            if '0x' in line and '0X' in line:
                line = line[min(line.find('0x'), line.find('0X')):]
            elif '0x' in line:
                line = line[line.find('0x'):]
            elif '0X' in line:
                line = line[line.find('0X'):]
            hex_str += line[:2]
            line = line[2:]
            for char in line:
                if 97 <= ord(char.lower()) <= 102 or char.isnumeric():
                    hex_str += char
                else:
                    break
            if len(hex_str) > 2:
                line.replace(hex_str[2:], '', 1)
                print(hex_str, int(hex_str, 16))


if __name__ == '__main__':
    main()

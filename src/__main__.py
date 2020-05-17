from peon.comandline.comandline import CommandLine


def main():
    cmd = CommandLine()
    cmd.argument_initialization()
    cmd.parse_input()


if __name__ == '__main__':
    main()

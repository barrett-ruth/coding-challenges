import argparse
from typing import Any, Iterator


def count_bytes(data) -> int:
    # read data as bytes
    # length of line is num bytes
    return sum(len(line.encode('utf-8')) for line in data)


def count_lines(data) -> int:
    # python's iterator appends newline to last line, avoiding fencepost error
    # similarly, count newline chars
    return sum(1 for _ in data)


def count_words(data) -> int:
    return sum(len(line.split()) for line in data)


def count_chars(data) -> int:
    return sum(len(line) for line in data)


def read_data(filename: str | None) -> Iterator[str]:
    if filename == 'None':
        import sys

        for line in sys.stdin:
            yield line
    else:
        with open(filename) as f:
            for line in f:
                yield line


def run(config: dict) -> None:
    filename = str(config.get('filename'))

    def fmt(result: Any) -> str:
        return f'    {result} {filename if filename else "stdin"}'

    data = read_data(filename)

    if config.get('c'):
        print(fmt(count_bytes(data)))
    elif config.get('l'):
        print(fmt(count_lines(data)))
    elif config.get('w'):
        print(fmt(count_words(data)))
    elif config.get('m'):
        print(fmt(count_chars(data)))
    else:
        data = list(data)
        print(
            f'    {count_lines(data)}   {count_words(data)}  {count_bytes(data)} {filename}'
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='pywc', description="pywc – word, line, character, and byte count"
    )
    parser.add_argument('filename', nargs='?', type=str)
    parser.add_argument('-c', action='store_true', help='number of bytes')
    parser.add_argument('-l', action='store_true', help='number of lines')
    parser.add_argument('-w', action='store_true', help='number of words')
    parser.add_argument('-m', action='store_true', help='number of characters')
    args = parser.parse_args()

    config = vars(args)

    run(config)


if __name__ == '__main__':
    main()

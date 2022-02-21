from typing import List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'Mike, John, Eddie',
        'Blacklist Mike',
        'Error 0',
        'Report',
    ),
    (
        'Mike, John, Eddie, William',
        'Error 3',
        'Error 3',
        'Change 0 Mike123',
        'Report',
    ),
    (
        'Mike, John, Eddie, William',
        'Blacklist Maya',
        'Error 1',
        'Change 4 George',
        'Report',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


FIRST: int = 0
LAST: int = -1


class Directions(Enum):
    UP: Tuple[int] = (-1, 0,)
    RIGHT: Tuple[int] = (0, 1,)
    DOWN: Tuple[int] = (1, 0,)
    LEFT: Tuple[int] = (0, -1,)


class Base:

    def __init__(self) -> None:
        pass

    @classmethod
    def FromInput(cls) -> 'Base':
        print(input())
        return cls()


class ControlClass:

    def __init__(self) -> None:
        self.friends: List[str] = input().split(', ')

    def __str__(self) -> str:
        return_str: str = str()
        return_str += f"Blacklisted names: {self.friends.count('Blacklisted')}\n"
        return_str += f"Lost names: {self.friends.count('Lost')}\n"
        return_str += ' '.join(self.friends)
        return return_str

    def run(self) -> None:
        while True:
            cmd: str = input()
            if cmd == 'Report':
                print(self)
                break
            else:
                cmd_parts = cmd.split(' ')
                option: str = cmd_parts[0]
                if option == 'Blacklist':
                    val: str = cmd_parts[1]
                    if val in self.friends:
                        print(f'{val} was blacklisted.')
                        self.friends[self.friends.index(val)] = 'Blacklisted'
                    else:
                        print(f'{val} was not found.')
                elif option == "Error":
                    val: int = int(cmd_parts[1])
                    if val in range(len(self.friends)) and self.friends[val] not in ('Blacklisted', 'Lost',):
                        print(f'{self.friends[val]} was lost due to an error.')
                        self.friends[val] = 'Lost'
                elif option == "Change":
                    index: int = int(cmd_parts[1])
                    name: str = cmd_parts[2]
                    if index in range(len(self.friends)):
                        print(
                            f'{self.friends[index]} changed his username to {name}.')
                        self.friends[index] = name


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        print('=== NEW RUN ===')
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
# Tower of Hanoi

## Introduction
The Tower of Hanoi is a classic puzzle consisting of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks neatly stacked in ascending order of size on one rod, the smallest at the top, thus making a conical shape.

## Objective
The goal of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
3. No disk may be placed on top of a smaller disk.

## Lore
Legend has it that there is a temple that contains a large room with three time-worn posts in it surrounded by 64 golden disks. These disks are constantly being moved by monks in accordance with the rules of the ancient puzzle. According to the legend, when the last move of the puzzle is completed, the world will end.

But don't worry, with `2^64 - 1` moves required, we have a bit of time left... unless.........

## Usage
This Python script solves the Tower of Hanoi problem for a given number of disks and prints the initial and final state of the towers.

### Requirements
- Python 3.x

### Running the Script
To run the script with a smaller number of disks (e.g., 5), use:
```sh
python3 hanoi.py

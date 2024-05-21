def move_disk(source, destination):
    print(f"Move disk from {source} to {destination}")

def print_tower(tower, label):
    max_height = max(tower) if tower else 0
    for level in range(max_height - 1, -1, -1):
        num_spaces = max_height - tower[level]
        print(f"{' ' * num_spaces}{'* ' * tower[level]}")
    print(label)


def hanoi(n, source, auxiliary, destination):
    towers = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print_tower(towers['A'], "Tower A")
    print()
    
    def move_disk_with_visual(source, destination):
        move_disk(source, destination)
        towers[destination].append(towers[source].pop())

    def move_tower(n, source, auxiliary, destination):
        if n == 1:
            move_disk_with_visual(source, destination)
        else:
            move_tower(n-1, source, destination, auxiliary)
            move_disk_with_visual(source, destination)
            move_tower(n-1, auxiliary, source, destination)

    move_tower(n, source, auxiliary, destination)
    print("\nFinal state of Tower C:")
    print_tower(towers['C'], "Tower C")

# Test the function with 5 disks
hanoi(5, 'A', 'B', 'C')
# Note: Uncommenting the line below will run the process for 64 disks, but it is not practical to execute.
# hanoi(64, 'A', 'B', 'C')
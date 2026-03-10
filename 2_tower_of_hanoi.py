def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary using target as buffer
    tower_of_hanoi(n - 1, source, target, auxiliary)
    # Move nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    # Move n-1 disks from auxiliary to target using source as buffer
    tower_of_hanoi(n - 1, auxiliary, source, target)

#Example: Solve for 3 disks
n = 3
tower_of_hanoi(n, 'A', 'B', 'C')

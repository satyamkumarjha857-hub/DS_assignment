def hanoi(n, src, aux, dst):
    if n == 1:
        print(f"Move disk 1 from {src} → {dst}")
        return 1
    moves = hanoi(n-1, src, dst, aux)
    print(f"Move disk {n} from {src} → {dst}")
    moves += 1
    moves += hanoi(n-1, aux, src, dst)
    return moves

# For n = 3
print("Hanoi(3):")
total_moves_3 = hanoi(3, "A", "B", "C")
print("Total moves:", total_moves_3)

# For n = 4
print("\nHanoi(4):")
total_moves_4 = hanoi(4, "A", "B", "C")
print("Total moves:", total_moves_4)
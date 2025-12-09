import random

# Returns a tuple of:
# the original list deduplicated and sorted
# and a list containing two values per element, of which is numbers that have duplicates and count of duplicates of that number
def counting_sort(list_input: list[int]) -> tuple[list[int], list[int, int]]:
    list_output: list[int] = list_input.copy()
    max_value: int = max(list_output)
    duplicate_values: list[int, int] = []

    count: list[int] = [0] * (max_value + 1)

    while len(list_output) > 0:
        num = list_output.pop(0)
        count[num] += 1

    for index in range(len(count)):
        while count[index] > 0:
            list_output.append(index)
            # Adds to duplicate_values list if a number is in the original list more than once
            if count[index] > 1:
                duplicate_values.append((index, count[index] - 1))

            count[index] = 0

    return (list_output, duplicate_values)

def main() -> None:
    numbers: list[int] = random.choices(range (0, 10), k=10)
    list_output: list[int] = counting_sort(numbers)[0]
    duplicate_values: list[int, int] = counting_sort(numbers)[1]

    print(f"Original list: {numbers}\n")

    # For each element in duplicate_values list, print number that has duplicate(s) and the count of duplicates of that number
    for value, count in duplicate_values:
            print(f"The number {value} had {count} duplicate(s) removed")

    print(f"\nResulting list: {list_output}\n")

if __name__ == "__main__":
    main()
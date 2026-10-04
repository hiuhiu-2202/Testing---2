from Code1 import deliveryFee


def main():
    tests = 0

    with open("Testing---2/test1.txt", "r", encoding="utf-8") as file:

        for line in file:

        
            parts = line.strip().split(maxsplit=3)

            price = float(parts[0])
            distance = float(parts[1])
            member = parts[2]
            expectOut = parts[3]

            tests += 1

            # Gọi hàm kiểm thử
            output = deliveryFee(price, distance, member)

            # In kết quả
            print(
                f"Test #{tests}: "
                f"Input: price = {price:.2f}, "
                f"distance = {distance:.2f}, "
                f"member = {member}, "
                f"Expected Output: {expectOut}, "
                f"Output: {output}",
                end=""
            )

            # So sánh kết quả
            if output == expectOut:
                print(", Result: pass")
            else:
                print(", Result: fail")


if __name__ == "__main__":
    main()
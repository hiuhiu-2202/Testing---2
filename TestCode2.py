from Code2 import homeCredit


def main():
    tests = 0

    with open("test2.txt", "r", encoding="utf-8") as file:

        for line in file:

        
            parts = line.strip().split(maxsplit=3)

            income = float(parts[0])
            credit = float(parts[1])
            loan = parts[2]
            expectOut = parts[3]

            tests += 1

            # Gọi hàm kiểm thử
            output = homeCredit(income, credit, loan)

            # In kết quả
            print(
                f"Test #{tests}: "
                f"Input: income = {income:.2f}, "
                f"credit = {credit:.2f}, "
                f"loan = {loan}, "
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
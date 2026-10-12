def main():
    lines1 = ["Laptop,1000,3", " ", "Phone,500,5", "\n", "Tablet,700,2"]
    results1 = clean_lines(lines1)
    print(results1)

    lines2 = ["Laptop,1000,3", "Phone,500,5", "Tablet,700,2"]
    results2 = parse_products(lines2)
    print(results2)

def clean_lines(lines):
    results = []
    for line in lines:
        result = line.strip()
        if result:
            results.append(result)

    return results

def parse_products(lines):
    results = []

    for line in lines:
        try:
            parts = line.split(",")
            if len(parts) != 3:
                continue

            name = parts[0].strip()
            price = float(parts[1])
            quantity = int(parts[2])

            results.append((name, price, quantity))

        except ValueError:
            continue

    return results

if __name__ == "__main__":
    main()


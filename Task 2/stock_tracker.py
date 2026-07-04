import csv


DATASET_FILE = "investment_summary.csv"

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135,
}


def load_stock_dataset(filename=DATASET_FILE):
    stocks = {}

    try:
        with open(filename, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                symbol = row.get("Symbol", "").strip().upper()

                if symbol:
                    stocks[symbol] = {
                        "name": row.get("Security Name", "").strip(),
                        "exchange": row.get("Listing Exchange", "").strip(),
                        "is_etf": row.get("ETF", "").strip(),
                    }
    except FileNotFoundError:
        print(f"Dataset file '{filename}' was not found. Using hardcoded stocks only.\n")

    return stocks


def get_positive_integer(prompt):
    while True:
        value = input(prompt).strip()

        if value.isdigit() and int(value) > 0:
            return int(value)

        print("Please enter a positive whole number.")


def display_available_stocks(stock_dataset):
    print("Stocks with manually defined prices:")

    for stock, price in STOCK_PRICES.items():
        company_name = stock_dataset.get(stock, {}).get("name", "Name not in dataset")
        print(f"{stock}: ${price} - {company_name}")


def collect_investments(stock_dataset):
    investments = []

    display_available_stocks(stock_dataset)
    print("\nEnter stock details. Type 'done' when finished.\n")

    while True:
        stock_name = input("Stock symbol: ").strip().upper()

        if stock_name == "DONE":
            break

        if stock_dataset and stock_name not in stock_dataset:
            print("Stock symbol was not found in the dataset.\n")
            continue

        if stock_name not in STOCK_PRICES:
            print("This stock exists, but no manual price is defined for it yet.\n")
            continue

        quantity = get_positive_integer("Quantity: ")
        price = STOCK_PRICES[stock_name]
        total_value = price * quantity
        company_name = stock_dataset.get(stock_name, {}).get("name", "")

        investments.append(
            {
                "stock": stock_name,
                "name": company_name,
                "quantity": quantity,
                "price": price,
                "total": total_value,
            }
        )

        print(f"Added {quantity} shares of {stock_name} worth ${total_value}.\n")

    return investments


def display_summary(investments):
    if not investments:
        print("No investments entered.")
        return 0

    grand_total = sum(item["total"] for item in investments)

    print("\nInvestment Summary")
    print("-" * 80)
    print(f"{'Stock':<10}{'Company':<30}{'Quantity':<12}{'Price':<12}{'Total'}")
    print("-" * 80)

    for item in investments:
        print(
            f"{item['stock']:<10}"
            f"{item['name'][:28]:<30}"
            f"{item['quantity']:<12}"
            f"${item['price']:<11}"
            f"${item['total']}"
        )

    print("-" * 80)
    print(f"Total investment value: ${grand_total}")

    return grand_total


def save_as_txt(investments, grand_total, filename="portfolio_summary.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Investment Summary\n")
        file.write("-" * 80 + "\n")
        file.write(f"{'Stock':<10}{'Company':<30}{'Quantity':<12}{'Price':<12}{'Total'}\n")
        file.write("-" * 80 + "\n")

        for item in investments:
            file.write(
                f"{item['stock']:<10}"
                f"{item['name'][:28]:<30}"
                f"{item['quantity']:<12}"
                f"${item['price']:<11}"
                f"${item['total']}\n"
            )

        file.write("-" * 80 + "\n")
        file.write(f"Total investment value: ${grand_total}\n")

    print(f"Result saved to {filename}")


def save_as_csv(investments, grand_total, filename="portfolio_summary.csv"):
    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Company", "Quantity", "Price", "Total"])

        for item in investments:
            writer.writerow(
                [item["stock"], item["name"], item["quantity"], item["price"], item["total"]]
            )

        writer.writerow(["Total Investment", "", "", "", grand_total])

    print(f"Result saved to {filename}")


def offer_save(investments, grand_total):
    if not investments:
        return

    choice = input("\nSave the result? (txt/csv/no): ").strip().lower()

    if choice == "txt":
        save_as_txt(investments, grand_total)
    elif choice == "csv":
        save_as_csv(investments, grand_total)
    else:
        print("Result not saved.")


def main():
    stock_dataset = load_stock_dataset()
    investments = collect_investments(stock_dataset)
    grand_total = display_summary(investments)
    offer_save(investments, grand_total)


if __name__ == "__main__":
    main()

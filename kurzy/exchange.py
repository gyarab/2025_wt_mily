import httpx

CNB_URL = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt;jsessionid=861D4434867C5AE3FAA91B21976B3B47?"


def load_rates():
    response = httpx.get(CNB_URL)
    response.raise_for_status()

    lines = response.text.splitlines()
    rates = {}

    for line in lines[2:]:
        parts = line.split("|")
        code = parts[3]
        amount = int(parts[2])
        rate = float(parts[4].replace(",", "."))

        rates[code] = rate / amount

    return rates


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(" Zadejte prosím platné číslo.")


def get_direction():
    while True:
        direction = input("Zadejte směr převodu (1 = EURO → CZK, 2 = CZK → EUR0): ")
        if direction in ("1", "2"):
            return direction
        print(" Neplatná volba.")


def main():

    rates = load_rates()

    if "EUR" not in rates:
        print(" Kurz EUR nebyl nalezen.")
        return

    eur_rate = rates["EUR"]
    print(f"Aktuální kurz EUR: {eur_rate:.2f} CZK")

    amount = get_float("Zadejte částku: ")
    direction = get_direction()

    if direction == "1":
        result = amount * eur_rate
        print(f"{amount:.2f} EUR = {result:.2f} CZK")
    else:
        result = amount / eur_rate
        print(f"{amount:.2f} CZK = {result:.2f} EUR")


if __name__ == "__main__":
    main()

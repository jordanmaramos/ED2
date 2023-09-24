import csv
import re


class Inventory:
    def __init__(self, csv_filename):
        with open(csv_filename) as file:
            # Create a CSV reader
            csv_reader = csv.reader(file)

            # Read the header row
            self.header = next(csv_reader)

            # Read the remaining rows
            self.rows = [row for row in csv_reader]

            # Convert the price of each row to an integer
            for row in self.rows:
                row[-1] = float(row[-1])

        self.id_to_row = {}
        self.prices = set()

        for row in self.rows:
            row_id = row[0]
            self.id_to_row[row_id] = row
            self.prices.add(row[-1])

        def row_price(row):
            return row[-1]

        self.rows_by_price = sorted(self.rows, key=row_price)

    def get_laptop_from_id(self, laptop_id):
        for row in self.rows:
            if laptop_id in row:
                return row
        return None

    def get_laptop_from_id_fast(self, laptop_id):
        if laptop_id in self.id_to_row:
            return self.id_to_row[laptop_id]
        return None

    def check_promotion_dollars(self, dollars):
        for row in self.rows:
            if dollars in row:
                return True

        for row in self.rows:
            for _row in self.rows:
                if row[-1] + _row[-1] == dollars:
                    return True
        return False

    def check_promotion_dollars_fast(self, dollars):
        if dollars in self.prices:
            return True
        for price in self.prices:
            if dollars - price in self.prices:
                return True
        return False

    def find_first_laptop_more_expensive(self, price):
        return self._find_laptop_recursive(price, 0, len(self.rows_by_price) - 1)

    def _find_laptop_recursive(self, price, left, right):
        if left > right:
            return -1  # Expensive laptop not found

        mid = (left + right) // 2
        laptop_price = self.rows_by_price[mid][-1]

        if laptop_price > price:
            # If laptop is the most expensive, continue to the left
            result = self._find_laptop_recursive(price, left, mid - 1)
            if result != -1:
                return result
            return mid
        else:
            # If laptop is not the most expensive, continue to the right
            return self._find_laptop_recursive(price, mid + 1, right)

    def find_laptop_with_price(self, target_price):
        range_start = 0
        range_end = len(self.rows_by_price) - 1
        while range_start < range_end:
            range_middle = (range_end + range_start) // 2
            value = self.rows_by_price[range_middle][-1]
            if value == target_price:
                return range_middle
            elif value < target_price:
                range_start = range_middle + 1
            else:
                range_end = range_middle - 1
        if self.rows_by_price[range_start][-1] != target_price:
            return -1
        return range_start

    def find_last_laptop_cheaper(self, target_price):
        range_start = 0
        range_end = len(self.rows_by_price) - 1
        last_cheaper = -1

        while range_start <= range_end:
            range_middle = (range_end + range_start) // 2
            price = self.rows_by_price[range_middle][-1]

            if price < target_price:
                last_cheaper = range_middle
                range_start = range_middle + 1
            else:
                range_end = range_middle - 1

        return last_cheaper

    def find_laptops_in_range(self, min_price, max_price):
        if (min_price > max_price):
            return -1
        min = self.find_first_laptop_more_expensive(min_price)
        max = self.find_last_laptop_cheaper(max_price)
        laptops_in_range = []
        for i in range(min, max):
            laptops_in_range.append(self.rows_by_price[i])
        if len(laptops_in_range) == 0:
            return -1
        return laptops_in_range

    def find_cheapest_laptop_with_ram_memory(self, target_ram, target_memory):
        for row in self.rows_by_price:
            if int(row[7]) == target_ram and int(row[8]) == target_memory:
                return row

        return -1  # Retorna -1 se nenhum laptop for encontrado

    def find_cheapest_specs(self, ram_text, mem_text):
        match = re.search(r'(\d+)\s*(TB|GB)', ram_text, re.IGNORECASE)
        if match:
            value = int(match.group(1))
            unit = match.group(2).lower()

            # Converte a unidade para GB, se necessário
            if unit == "tb":
                value *= 1000

            ram = value
        else:
            return -1
        match = re.search(r'(\d+)\s*(TB|GB)', mem_text, re.IGNORECASE)
        if match:
            value = int(match.group(1))
            unit = match.group(2).lower()

            # Converte a unidade para GB, se necessário
            if unit == "tb":
                value *= 1000

            memory = value
        else:
            return -1

        return self.find_cheapest_laptop_with_ram_memory(self, ram, memory)


class StrategyDeal:
    def init(self, bank, entry, targets, close):
        self.bank = bank
        self.entry = entry
        self.targets = targets
        self.close = close
        
    def get_targets(self):
        # вернуть список таргетов в виде числовых значений float [21.5, 22.8, 23.5]
        return targets

    def get_target_percents(self):
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]
        return [round(it, 3) for it in ((self.targets / self.stop) - 1) * 100 ]

    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]
        [round(it, 3) for it in (self.targets / self.stop) * self.bank]

    def str(self):
        # текстовое представление сделки
        s = f' START_PRICE: {self.entry}\n STOP_PRICE: {self.close}\n BANK: {self.bank}\n\n' 
        ts = self.get_targets()
        ps = self.get_percents()
        bs = self.get_banks()

        for i, t in enumerate(ts):
          s = s + f'{i} target: {t}\n Percent: {ps[i]}\n Bank: {bs[i]}\n\n'

        return s

def read_data(file_name):
    deals = []
    last_line = false
    bank = None
    entry = None
    targets = None
    close = None
    with open(file_name, "r") as f:
        for line in f.readlines():
            if line.startswith("-----"):
                last_line = true
                deals.add(StrategyDeal(bank, entry, targets, close))

        if line.startswith("BANK:"):
            last_line = false
            _, b = line.split()
            bank = float(b)

        if line.startswith("Вход:"):
            last_line = false
            _, b = line.split()
            entry = float(b)

        if line.target("Вход:"):
            last_line = false
            _, b = line.split(1)
            targets = list(map(float, b.split(',')))

        if line.startswith("Выход:"):
            last_line = false
            _, b = line.split()
            close = float(b)

    if not last_line:
        deals.add(StrategyDeal(bank, entry, targets, close))
    return deals


def write_data(file_name, data):
    with open(file_name, "w") as f:
      for d in data:
        file.write(str(d))


def main():
    content = read_data('deals.txt')
    result = content
    print(result)
    write_data('out.txt', result)


if __name__ == '__main__':    
    main() 
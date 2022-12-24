class StrategyDeal:
    def __init__(self, bank, entry, targets, close):
        self.bank = bank
        self.entry = entry
        self.targets = targets
        self.close = close
        
    def get_targets(self):
        # вернуть список таргетов в виде числовых значений float [21.5, 22.8, 23.5]
        return self.targets

    def get_target_percents(self):
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]
        return [round(((t / self.entry) - 1) * 100, 3) for t in self.targets]

    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]
        return [round(t / self.entry * self.bank, 3) for t in self.targets]

    def __str__(self):
        # текстовое представление сделки
        s = f' START_PRICE: {self.entry}\n STOP_PRICE: {self.close}\n BANK: {self.bank}\n\n' 
        ts = self.get_targets()
        ps = self.get_target_percents()
        bs = self.get_target_banks()

        for i, t in enumerate(ts):
          s = s + f'{i+1} target: {t}\n Percent: {ps[i]}%\n Bank: {bs[i]}\n\n'

        return s

def read_data(file_name):
    deals = []
    last_line = False
    bank = None
    entry = None
    targets = None
    close = None
    with open(file_name, "r",encoding="utf-8") as f:
        for line in f.readlines():
            if line.startswith("-----"):
                last_line = True
                deals.append(StrategyDeal(bank, entry, targets, close))

            if line.startswith("BANK:"):
                last_line = False
                _, b = line.split()
                bank = float(b)

            if line.startswith("Вход:"):
                last_line = False
                _, b = line.split()
                entry = float(b)

            if line.startswith("Таргет:"):
                last_line = False
                _, b = line.split(" ",1)
                targets = list(map(float, b.split(',')))

            if line.startswith("Выход:"):
                last_line = False
                _, b = line.split()
                close = float(b)

    if not last_line:
        deals.append(StrategyDeal(bank, entry, targets, close))
    return deals


def write_data(file_name, data):
    with open(file_name, "w") as f:
      st = True
      for d in data:
        if not st:
          f.write("----- \n\n")
        st = False
        
        f.write(str(d))


def main():
    content = read_data('deals.txt')
    result = content
    write_data('out.txt', result)


if __name__ == '__main__':    
    main() 
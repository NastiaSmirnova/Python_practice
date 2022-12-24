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
        s = f'START_PRICE: {self.entry}\nSTOP_PRICE: {self.close}\nBANK: {self.bank}\n\n' 
        ts = self.get_targets()
        ps = self.get_target_percents()
        bs = self.get_target_banks()

        for i, (t,p,b) in enumerate(zip(ts,ps,bs)):
          s = s + f'{i+1} target: {t}\nPercent: {p}%\nBank: {b}\n\n'

        return s
def parse_deal(l_deal):
    bank = None
    entry = None
    targets = None
    close = None

    for s in l_deal:
        if s.startswith("BANK:"):
            _, b = s.split()
            bank = float(b)

        if s.startswith("Вход:"):
            _, b = s.split()
            entry = float(b)

        if s.startswith("Таргет:"):
            _, b = s.split(" ",1)
            targets = list(map(float, b.split(',')))

        if s.startswith("Выход:"):
            _, b = s.split()
            close = float(b)

    return StrategyDeal(bank, entry, targets, close)

def read_data(file_name):
    with open(file_name, "r",encoding="utf-8") as f:
        return list(map(
            lambda d: parse_deal(filter(lambda x: len(x.strip()) > 0, d.split('\n'))),
            f.read().split("-----")
            ))

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
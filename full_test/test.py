class SNR:
    def __init__(self, s: str):
        self.s = s

class SN_SNR(SNR):
    def __init__(self, s: str, t: str):
        super().__init__(s)
        self.t = t

    def Same_number(self) -> bool:
        def parse_number(num: str) -> float:
            if '.' in num:
                return float(num)
            return float(num + '.0')

        return parse_number(self.s) == parse_number(self.t)
def test_run(content1,content2):
    return SN_SNR(content1,content2)


METADATA = {}


def check(candidate):
    assert candidate("0.(52)","0.5(25)")==True
    assert candidate("0.1666(6)","0.166(66)")==True
    assert candidate("0.9(9)","1.")==True

check(test_run)
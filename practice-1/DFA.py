class DFA:
    TOTAL_STATES = 3
    FINAL_STATES = 1

    class STATE:
        Q0, Q1, Q2 = range(3)

    class RESULT:
        NOT_REACHED_FINAL_STATE, REACHED_FINAL_STATE = range(2)

    ALPHABET = ["a", "b"]
    ACCEPTED_STATES = [STATE.Q2]
    TRANSITION_TABLE = []
    CURRENT_STATE = STATE.Q0

    @classmethod
    def setup_transitions(self):
        self.TRANSITION_TABLE = [[0] * len(self.ALPHABET) for k in range(self.TOTAL_STATES)]

        self.TRANSITION_TABLE[self.STATE.Q0][0] = self.STATE.Q1
        self.TRANSITION_TABLE[self.STATE.Q0][1] = self.STATE.Q0

        self.TRANSITION_TABLE[self.STATE.Q1][0] = self.STATE.Q1
        self.TRANSITION_TABLE[self.STATE.Q1][1] = self.STATE.Q2

        self.TRANSITION_TABLE[self.STATE.Q2][0] = self.STATE.Q2
        self.TRANSITION_TABLE[self.STATE.Q2][1] = self.STATE.Q2

    def DFA(self, symbol):
        pos = -1
        for i, ch in enumerate(self.ALPHABET):
            if symbol == ch:
                pos = i
                break

        if pos == -1:
            return False

        self.CURRENT_STATE = self.TRANSITION_TABLE[self.CURRENT_STATE][pos]
        return True

    def is_accepted(self):
        return self.CURRENT_STATE in self.ACCEPTED_STATES

    def process(self, text):
        for ch in text:
            if not self.DFA(ch):
                return self.RESULT.NOT_REACHED_FINAL_STATE

        if self.is_accepted():
            return self.RESULT.REACHED_FINAL_STATE
        return self.RESULT.NOT_REACHED_FINAL_STATE


def main():
    DFA.setup_transitions()

    print("ДКА: цепочки вида w1abw2, w1,w2 ∈ {a,b}*")
    print("Введите строку:")

    dfa = DFA()

    line = input()

    result = dfa.process(line)

    if result == DFA.RESULT.REACHED_FINAL_STATE:
        print("Accepted")
    else:
        print("Rejected")


if __name__ == "__main__":
    main()
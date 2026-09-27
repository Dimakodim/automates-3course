class NFA:
    TOTAL_STATES = 4
    FINAL_STATES = 3

    class STATE:
        Q0, Q1, Q2, Q3 = range(4)

    class RESULT:
        NOT_REACHED_FINAL_STATE, REACHED_FINAL_STATE = range(2)

    ALPHABET = ["0", "1"]
    ACCEPTED_STATES = [STATE.Q0, STATE.Q1, STATE.Q2]
    TRANSITION_TABLE = []
    CURRENT_STATES = {STATE.Q0}

    @classmethod
    def setup_transitions(self):
        self.TRANSITION_TABLE = [[0] * len(self.ALPHABET) for k in range(self.TOTAL_STATES)]

        self.TRANSITION_TABLE[self.STATE.Q0][0] = [self.STATE.Q0, self.STATE.Q2]
        self.TRANSITION_TABLE[self.STATE.Q0][1] = [self.STATE.Q1]

        self.TRANSITION_TABLE[self.STATE.Q1][0] = [self.STATE.Q2]
        self.TRANSITION_TABLE[self.STATE.Q1][1] = [self.STATE.Q1]

        self.TRANSITION_TABLE[self.STATE.Q2][0] = [self.STATE.Q0]
        self.TRANSITION_TABLE[self.STATE.Q2][1] = [self.STATE.Q3]

        self.TRANSITION_TABLE[self.STATE.Q3][0] = [self.STATE.Q3]
        self.TRANSITION_TABLE[self.STATE.Q3][1] = [self.STATE.Q3]


    def NFA(self, symbol):
        pos = -1
        for i, ch in enumerate(self.ALPHABET):
            if symbol == ch:
                pos = i
                break
        if pos == -1:
            return False

        new_states = set()
        for state in self.CURRENT_STATES:
            for nxt in self.TRANSITION_TABLE[state][pos]:
                new_states.add(nxt)
        self.CURRENT_STATES = new_states
        return True

    def is_accepted(self):
        return any(s in self.ACCEPTED_STATES for s in self.CURRENT_STATES)

    def process(self, text):
        for ch in text:
            if not self.NFA(ch):
                return self.RESULT.NOT_REACHED_FINAL_STATE
        if self.is_accepted():
            return self.RESULT.REACHED_FINAL_STATE
        return self.RESULT.NOT_REACHED_FINAL_STATE


def main():
    NFA.setup_transitions()

    print("НКА: цепочки из 0 и 1, не содержащие подцепочку 101")
    print("Введите строку:")

    line = input()
    result = NFA().process(line)

    if result == NFA.RESULT.REACHED_FINAL_STATE:
        print("Accepted")
    else:
        print("Rejected")


if __name__ == "__main__":
    main()
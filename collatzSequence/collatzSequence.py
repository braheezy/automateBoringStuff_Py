class CollatzSequence():
    def __init__(self, intial_input):
        self.intial_input = intial_input

    def collatz(self, number):
        if number == 1:
            return number
        elif number % 2 == 0:
            return number / 2
        else:
            return 3 * number + 1

    def main(self):
        while self.intial_input > 1:
            print(int(self.intial_input))
            self.intial_input = self.collatz(self.intial_input)
        print(int(self.intial_input))


if __name__ == '__main__':
    try:
        num = int(input("Enter a number: "))
        sequencer = CollatzSequence(num)
        sequencer.main()
    except ValueError:
        print("Please enter an integer.")

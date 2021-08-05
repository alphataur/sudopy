class Parser:
    def __init__(self, d_path, limit = 100):
        self.d_path = d_path
        self.limit = limit
        self.questions = []
        self.answers = []

    def process(self, data):
        matrix = []
        line_length = 9
        index = 0
        temp = []
        while True:
            temp.append(int(data[index]))
            index += 1
            if index % line_length == 0:
                matrix.append(temp)
                temp = []
                if len(matrix) == 9:
                    break
        return matrix

    def read_data(self):
        with open(self.d_path) as f:
            # skip headers
            f.readline()
            for line in f.readlines():
                q, s = line.split(",")
                self.questions.append(self.process(q))
                self.answers.append(self.process(s))
                if len(self.answers) == self.limit:
                    break

__all__ = [Parser]




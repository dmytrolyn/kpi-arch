class Blackboard:
    def __init__(self):
        self.data = {}

    def get_data(self, key):
        return self.data.get(key)

    def set_data(self, key, value):
        self.data[key] = value

class TextExtractor:
    def __init__(self, blackboard):
        self.blackboard = blackboard

    def extract_text(self, data):
        self.blackboard.set_data('data', data)


class Analyzer:
    def __init__(self, blackboard):
        self.blackboard = blackboard

    def analyze(self):
        text = self.blackboard.get_data('data')
        if text:
            analyzed_data = self.perform_analysis(text)
            self.blackboard.set_data('analyzed_data', analyzed_data)

    def perform_analysis(self, text):
        return len(text)



class ResultViewer:
    def __init__(self, blackboard):
        self.blackboard = blackboard

    def display_result(self):
        data = self.blackboard.get_data('data')
        analyzed_data = self.blackboard.get_data('analyzed_data')

        if data and analyzed_data:
            print("Data:", data)
            print("Analyzed data:", analyzed_data)

class Controller:
    def __init__(self, blackboard):
        self.blackboard = blackboard
        self.knowledge_sources = []

    def add_knowledge_source(self, knowledge_source):
        self.knowledge_sources.append(knowledge_source)

    def process_data(self, data):
        for knowledge_source in self.knowledge_sources:
            if isinstance(knowledge_source, TextExtractor):
                knowledge_source.extract_text(data)
            elif isinstance(knowledge_source, Analyzer):
                knowledge_source.analyze()

        result_viewer = ResultViewer(self.blackboard)
        result_viewer.display_result()

if __name__ == "__main__":
    blackboard = Blackboard()
    controller = Controller(blackboard)

    text_extractor = TextExtractor(blackboard)
    analyzer = Analyzer(blackboard)

    controller.add_knowledge_source(text_extractor)
    controller.add_knowledge_source(analyzer)

    data = "Lorem ipsum dolor sit amet"

    controller.process_data(data)
import unittest
from unittest.mock import patch
from main import Blackboard, TextExtractor, Analyzer, ResultViewer, Controller

class TestHandler(unittest.TestCase):
    def test_process_data(self):
        blackboard = Blackboard()
        controller = Controller(blackboard)

        text_extractor = TextExtractor(blackboard)
        analyzer = Analyzer(blackboard)

        controller.add_knowledge_source(text_extractor)
        controller.add_knowledge_source(analyzer)

        data = "Lorem impsum dolor sit amet!"

        with patch.object(ResultViewer, 'display_result') as mock_display_result:
            controller.process_data(data)

            mock_display_result.assert_called_once()

    def test_text_extractor(self):
        blackboard = Blackboard()
        text_extractor = TextExtractor(blackboard)

        data = "Lorem impsum dolor sit amet!"

        text_extractor.extract_text(data)

        self.assertEqual(blackboard.get_data('data'), data)

    def test_analyzer(self):
        blackboard = Blackboard()
        analyzer = Analyzer(blackboard)

        text_to_analyze = "Lorem impsum dolor sit amet!"

        blackboard.set_data('data', text_to_analyze)

        analyzer.analyze()

        self.assertIsNotNone(blackboard.get_data('analyzed_data'))
        self.assertEqual(blackboard.get_data('analyzed_data'), len(text_to_analyze))

    def test_result_viewer(self):
        blackboard = Blackboard()
        result_viewer = ResultViewer(blackboard)

        text_to_analyze = "Lorem impsum dolor sit amet!"

        blackboard.set_data('data', text_to_analyze)
        blackboard.set_data('analyzed_data', len(text_to_analyze))

        with patch('builtins.print') as mock_print:
            result_viewer.display_result()

            mock_print.assert_called_with("Analyzed data:", len(text_to_analyze))

if __name__ == "__main__":
    unittest.main()
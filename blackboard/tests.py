import unittest
from unittest.mock import patch
from main import Blackboard, TextExtractor, Analyzer, ResultViewer, Controller

class TestBlackboardPattern(unittest.TestCase):
    def test_process_social_media_data(self):
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

    def test_sentiment_analyzer(self):
        blackboard = Blackboard()
        analyzer = Analyzer(blackboard)

        blackboard.set_data('data', "Lorem impsum dolor sit amet!")

        analyzer.analyze()

        self.assertIsNotNone(blackboard.get_data('analyzed_data'))

    def test_result_viewer(self):
        blackboard = Blackboard()
        result_viewer = ResultViewer(blackboard)

        blackboard.set_data('data', "Lorem impsum dolor sit amet!")
        blackboard.set_data('analyzed_data', 0.5)

        with patch('builtins.print') as mock_print:
            result_viewer.display_result()

            mock_print.assert_called_with("Analyzed data:", 0.5)

if __name__ == "__main__":
    unittest.main()
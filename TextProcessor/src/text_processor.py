class TextProcessorInterface:
    def process_text(self, text: str) -> str:
        pass

class AVFoundationTextProcessor(TextProcessorInterface):
    def __init__(self, language: str):
        self.language = language

    def process_text(self, text: str) -> str:
        # Use AVFoundation to transcribe the text
        transcribed_text = "This is the avfoundation transcribed text"

        # Process the transcribed text
        processed_text = transcribed_text.lower().strip()

        return processed_text

class ChromebookTextProcessor(TextProcessorInterface):
    def __init__(self, module_name: str):
        self.module_name = module_name

    def process_text(self, text: str) -> str:
        # Use the Chromebook module to process the text
        processed_text = "This is the chromebook processed text"

        return processed_text

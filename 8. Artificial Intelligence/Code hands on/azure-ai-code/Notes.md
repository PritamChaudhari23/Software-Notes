SDK Modules, classes, methods:

- azure (root module)
  - core (sub module)
    - credentials
      - AzureKeyCredential (class) => input: Resource key
  - ai
    - language (sub sub module)
      - conversations (sub sub sub module)
        - ConversationAnalysisClient (class) => input: Resource key, credentials object
          1. analyze_conversation()
      - questionanswering
        - QuestionAnsweringClient (class) => input: Resource key, credentials object
          1. get_answers()
    - textanalytics
      - TextAnalyticsClient (class) => input: Resource key, credentials object
        1. detect_language()
        2. analyze_sentiment()
        3. extract_key_phrases()
        4. recognize_entities()
        5. recognize_linked_entities()
        6. begin_single_label_classify()
        7. begin_recognize_custom_entities()
    - translation
      - TranslatorCredential (class)
    - vision
    - formrecognizer
  - congnitiveservices
  - common
  - profiles
  - search

eg: Import namespaces

from azure.core.credentials import AzureKeyCredential

from azure.ai.textanalytics import TextAnalyticsClient

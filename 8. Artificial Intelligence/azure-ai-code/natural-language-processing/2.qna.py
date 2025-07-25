# STEPS TO FOLLOW ON PORTAL:
# 1.Create Language resource, select custom question answering option
# 2.Language studio portal -  https://language.cognitive.azure.com/
# 3.Create new project - Custom question answering
# 4.Add sources to the knowledge base:
# 	- Add source - URL - https://docs.microsoft.com/en-us/learn/support/faq
# 	- Add source - Chit Chat
# 5.Edit the knowledge base:
# 	- Add new question answer pair
# 	- Add alternate question
# 	- Add follow up prompt - For multi turn conversations
# 6.Train and test the knowledge base
# 7.Deploy the knowledge base

# ---------------------------------------------------------------------------------------------------

from dotenv import load_dotenv
import os

# Import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient
# from azure.ai.language.conversations 

def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')
        ai_project_name = os.getenv('QA_PROJECT_NAME')
        ai_deployment_name = os.getenv('QA_DEPLOYMENT_NAME')

        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)

        # Submit a question and display the answer
        user_question = ''
        while user_question.lower() != 'quit':
            user_question = input('\nQuestion:\n')
            response = ai_client.get_answers(question=user_question,
                                            project_name=ai_project_name,
                                            deployment_name=ai_deployment_name)
            for candidate in response.answers:
                print(candidate.answer)
                print("Confidence: {}".format(candidate.confidence))
                print("Source: {}".format(candidate.source))

    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------
#  pip install azure-ai-language-questionanswering
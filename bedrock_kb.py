import boto3

from config import AWS_REGION, KNOWLEDGE_BASE_ID, MODEL_ID


class KnowledgeBaseService:

    def __init__(self):

        self.client = boto3.client(
            "bedrock-agent-runtime",
            region_name=AWS_REGION
        )

    def ask(self, question):

        response = self.client.retrieve_and_generate(
            input={
                "text": question
            },
            retrieveAndGenerateConfiguration={
                "type": "KNOWLEDGE_BASE",
                "knowledgeBaseConfiguration": {
                    "knowledgeBaseId": KNOWLEDGE_BASE_ID,
                    "modelArn": MODEL_ID
                }
            }
        )

        answer = response["output"]["text"]

        citations = response.get("citations", [])

        return {
            "answer": answer,
            "citations": citations
        }
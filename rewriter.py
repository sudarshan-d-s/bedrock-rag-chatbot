import boto3

from config import AWS_REGION, MODEL_ID


class QuestionRewriter:

    def __init__(self):
        self.client = boto3.client(
            "bedrock-runtime",
            region_name=AWS_REGION
        )

    def rewrite(self, chat_history, current_question):

        history_text = self._format_history(chat_history)

        prompt = f"""
You are a question rewriting assistant.

Your task is to convert the user's latest question into a
standalone question that can be understood without the
previous conversation.

Use the conversation history only to resolve references,
pronouns, omitted context, or ambiguous terms.

Do not answer the question.

Return ONLY the rewritten standalone question.

Conversation history:
{history_text}

Latest user question:
{current_question}

Standalone question:
"""

        response = self.client.converse(
            modelId=MODEL_ID,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ],
            inferenceConfig={
                "temperature": 0
            }
        )

        return response["output"]["message"]["content"][0]["text"].strip()

    @staticmethod
    def _format_history(chat_history):

        if not chat_history:
            return "No previous conversation."

        lines = []

        for message in chat_history:
            role = message["role"]
            content = message["content"]

            lines.append(
                f"{role.upper()}: {content}"
            )

        return "\n".join(lines)
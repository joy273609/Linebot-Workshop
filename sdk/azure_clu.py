import os
#Azure CLU
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

azureKeyCredential = AzureKeyCredential(os.getenv("AZURE_CLU_API_KEY"))
azureEndpoint = os.getenv("AZURE_CLU_ENDPOINT")
azureProjectName = os.getenv("AZURE_CLU_PROJECT_NAME")
azureDeploymentName = os.getenv("AZURE_CLU_DEPLOYMENT_NAME")

def analyze_address(address):
    client = ConversationAnalysisClient(azureEndpoint, azureKeyCredential)
    with client:
        result = client.analyze_conversation(
            task={
                "kind": "Conversation",
                "analysisInput": {
                    "conversationItem": {
                        "participantId": "1",
                        "id": "1",
                        "modality": "text",
                        "language": "zh-hant",
                        "text": address
                    },
                    "isLoggingEnabled": False
                },
                "parameters": {
                    "projectName": azureProjectName,
                    "deploymentName": azureDeploymentName,
                    "verbose": True
                }
            }
        )
    return result['result']

result = analyze_address("106320 臺北市大安區和平東路2段134號")
print(result)
import boto3
import json
import os

bedrock = boto3.client("bedrock-runtime", region_name=os.getenv("AWS_REGION"))

def generate_text(prompt: str):
    body = {
        "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
        "max_tokens_to_sample": 200,
        "temperature": 0.7,
        "top_p": 0.9,
        "stop_sequences": ["\n\nHuman:"]
    }

    response = bedrock.invoke_model(
        modelId="anthropic.claude-v2:1",
        contentType="application/json",
        accept="application/json",
        body=json.dumps(body)
    )

    result = json.loads(response['body'].read())
    return result["completion"]

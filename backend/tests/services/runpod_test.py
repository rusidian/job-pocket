from services import call_runpod_ollama


if __name__ == "__main__":
    from langchain_core.prompts import ChatPromptTemplate

    vocabs = ["python", "langchain", "langgraph"]
    for vocab in vocabs:
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "당신은 아주 친절한 챗봇입니다. 질문에 잘 답변해주세요"),
                ("human", "{topic}에 대해 자세하게 설명해 주세요."),
            ]
        )
        final_prompt = prompt.invoke({"topic": vocab})
        input_messages = [
            {"role": "user" if m.type == "human" else m.type, "content": m.content}
            for m in final_prompt.to_messages()
        ]

        print(call_runpod_ollama(input_messages))

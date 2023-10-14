import openai

openai.api_key = "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"

while True:
    ask = input("Enter your question (type 'break' to exit): ")
    if ask.lower() == "break":
        print("Thank you")
        break
    else:
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=ask,
                temperature=0.9,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=["Human: ", "AI: "]
            )
            print("AI's response:")
            print(response.choices[0].text)
        except Exception as e:
            print("An error occurred:", e)
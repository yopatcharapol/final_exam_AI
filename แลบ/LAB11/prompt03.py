
from openrouter_client import call_openrouter


def main():
    print("OpenRouter Chat")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        # Get input from terminal
        message = input("You: ").strip()

        # Exit condition
        if message.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Skip empty messages
        if not message:
            continue

        try:
            # Call OpenRouter library
            response = call_openrouter(message)

            print("\n******************************")
            print("Answer")
            print("******************************")

            # Print assistant answer
            content = response.get("content")

            if content:
                print(content)
            else:
                print("No answer returned.")

            print()

        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()

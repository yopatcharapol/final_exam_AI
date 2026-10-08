from openrouter_client import call_openrouter


def main():
    message = "สวัสดี บอกชื่อตัวเองหน่อย"

    response = call_openrouter(message)

    print("******************************")
    print("Thinking...")
    print("******************************")

    reasoning = response.get("reasoning")
    if reasoning:
        print(reasoning)
    else:
        print("No reasoning returned.")

    print("******************************")
    print("Answer")
    print("******************************")

    # Usually the actual model answer is in `content`
    content = response.get("content")

    if content:
        print(content)
    else:
        # Fallback to reasoning_details if needed
        reasoning_details = response.get("reasoning_details", [])

        if reasoning_details:
            for detail in reasoning_details:
                if "text" in detail:
                    print(detail["text"])
        else:
            print("No answer returned.")


if __name__ == "__main__":
    main()
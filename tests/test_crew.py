from agents.crew import create_crew


if __name__ == "__main__":

    question = input("\nAsk your question: ")

    crew = create_crew()

    result = crew.kickoff(
        inputs={
            "question": question
        }
    )

    print("\n\nFINAL ANSWER\n")
    print(result)
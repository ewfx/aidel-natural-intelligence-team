from genai_prompt import ask_genai

def main():
    print("Starting the analysis...")
    # Reading the file
    with open("D:\\RAJESHGOLD\\HACKATHON\\aidel-natural-intelligence-team\\artifacts\\testdata\\transaction.txt", "r") as file:
        transactionDetails = file.read()
    
    # Step 1: Extract entities using GenAI
    entities = ask_genai(transactionDetails)
    print("Entities identified:")
    print(entities)

    

if __name__ == "__main__":
    main()

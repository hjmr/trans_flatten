import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Flatten Microsoft Teams Transcript.")
    parser.add_argument("input", help="Input file")
    return parser.parse_args()


def main():
    args = parse_args()
    with open(args.input, "r") as f:
        doc = f.readlines()

    dialogues = []

    num_utterance = len(doc) // 3
    for idx in range(num_utterance):
        name = doc[idx * 3 + 1].strip()
        utterance = doc[idx * 3 + 2].strip()
        if len(dialogues) == 0 or dialogues[-1]["name"] != name:
            dialogues.append({"name": name, "utterances": [utterance]})
        else:
            dialogues[-1]["utterances"].append(utterance)

    for dialogue in dialogues:
        print(f"{dialogue["name"]}: {" ".join(dialogue["utterances"])}")

if __name__ == "__main__":
    main()

import argparse
import re

def parse_args():
    parser = argparse.ArgumentParser(description="Flatten Microsoft Teams Transcript (vtt).")
    parser.add_argument("input", help="Input file")
    return parser.parse_args()

block_lines = 3

def main():
    args = parse_args()
    with open(args.input, "r") as f:
        doc = f.readlines()
    doc.pop(0) # remove WEBVTT

    dialogues = []
    
    num_utterance = len(doc) // block_lines
    for idx in range(num_utterance):
        period = doc[idx * block_lines + 1].strip() # time period
        line = doc[idx * block_lines + 2].strip()

        match = re.match(r"\<v ([^>]+)\>([^<]+)\<\/v\>", line)
        if match:
            name = match.group(1)
            utterance = match.group(2)
            if len(dialogues) == 0 or dialogues[-1]["name"] != name:
                dialogues.append({"name": name, "utterances": [utterance]})
            else:
                dialogues[-1]["utterances"].append(utterance)
        else:
            print(f"Failed to parse line {idx * block_lines + 2}: {line}")

    for dialogue in dialogues:
        print(f"{dialogue["name"]}: {" ".join(dialogue["utterances"])}")

if __name__ == "__main__":
    main()

# morse_transformer/train.py

import time
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from model import TransformerTranslationModel
from datetime import timedelta

import json

# Start the timer
start_time = time.time()

with open("eng2morse.json", "r") as f:
    words_2_morse_dataset = json.load(f)

# Example English ↔ Morse dataset (use larger set for real)
pairs = list(words_2_morse_dataset.items())[:10000]

# Create vocab
from string import ascii_lowercase

morse_symbols = [".", "-", " "]

src_vocab = ["<pad>", "<bos>", "<eos>"] + list(ascii_lowercase)
tgt_vocab = ["<pad>", "<bos>", "<eos>"] + morse_symbols

src_stoi = {s: i for i, s in enumerate(src_vocab)}
tgt_stoi = {s: i for i, s in enumerate(tgt_vocab)}
src_itos = {i: s for s, i in src_stoi.items()}
tgt_itos = {i: s for s, i in tgt_stoi.items()}

PAD_IDX = src_stoi["<pad>"]
BOS_IDX = src_stoi["<bos>"]
EOS_IDX = src_stoi["<eos>"]


def encode(text, vocab):
    return [vocab["<bos>"]] + [vocab[c] for c in text if c in vocab] + [vocab["<eos>"]]


def collate_fn(batch):
    src, tgt = [], []
    for s, t in batch:
        s_tensor = torch.tensor(encode(s, src_stoi))
        t_tensor = torch.tensor(encode(t, tgt_stoi))
        src.append(s_tensor)
        tgt.append(t_tensor)
    src = nn.utils.rnn.pad_sequence(src, batch_first=True, padding_value=PAD_IDX)
    tgt = nn.utils.rnn.pad_sequence(tgt, batch_first=True, padding_value=PAD_IDX)
    return src, tgt


loader = DataLoader(pairs, batch_size=64, collate_fn=collate_fn)

# Model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = TransformerTranslationModel(len(src_vocab), len(tgt_vocab)).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
loss_fn = nn.CrossEntropyLoss(ignore_index=PAD_IDX)


def generate_square_subsequent_mask(sz):
    return torch.triu(torch.ones((sz, sz)) * float("-inf"), diagonal=1)


# Train
for epoch in range(30):
    model.train()
    total_loss = 0
    sample = 0
    for src, tgt in loader:
        src, tgt = src.to(device), tgt.to(device)
        tgt_input = tgt[:, :-1]
        tgt_out = tgt[:, 1:]

        src_mask = None
        tgt_mask = generate_square_subsequent_mask(tgt_input.size(1)).to(device)
        src_padding_mask = src == PAD_IDX
        tgt_padding_mask = tgt_input == PAD_IDX

        logits = model(
            src,
            tgt_input,
            src_mask,
            tgt_mask,
            src_padding_mask,
            tgt_padding_mask,
            src_padding_mask,
        )

        optimizer.zero_grad()
        loss = loss_fn(logits.reshape(-1, logits.shape[-1]), tgt_out.reshape(-1))
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        # print(sample)
        sample += 1

    print(f"Epoch {epoch + 1} Loss: {total_loss:.4f}")

torch.save(model.state_dict(), "morse_model.pt")

# End the timer
end_time = time.time()

# Time taken
elapsed_seconds = end_time - start_time
formatted_time = str(timedelta(seconds=round(elapsed_seconds)))
print(f"Elapsed time: {formatted_time}")

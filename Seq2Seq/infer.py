# morse_transformer/inference.py

import torch
from model import TransformerTranslationModel
from string import ascii_lowercase

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Reload vocab (same as train.py)
morse_symbols = ['.', '-', ' ']
src_vocab = ['<pad>', '<bos>', '<eos>'] + list(ascii_lowercase)
tgt_vocab = ['<pad>', '<bos>', '<eos>'] + morse_symbols

src_stoi = {s: i for i, s in enumerate(src_vocab)}
tgt_stoi = {s: i for i, s in enumerate(tgt_vocab)}
src_itos = {i: s for s, i in src_stoi.items()}
tgt_itos = {i: s for s, i in tgt_stoi.items()}

PAD_IDX = src_stoi['<pad>']
BOS_IDX = src_stoi['<bos>']
EOS_IDX = src_stoi['<eos>']

model = TransformerTranslationModel(len(src_vocab), len(tgt_vocab)).to(device)
model.load_state_dict(torch.load("morse_model.pt"))
model.eval()

def encode(text, vocab):
    return [vocab['<bos>']] + [vocab[c] for c in text if c in vocab] + [vocab['<eos>']]

def decode(indices, itos):
    tokens = [itos[idx] for idx in indices]
    return ''.join([t for t in tokens if t not in ['<bos>', '<eos>', '<pad>']])

def translate(text):
    src = torch.tensor(encode(text.lower(), src_stoi)).unsqueeze(0).to(device)
    src_mask = None
    memory = model.transformer.encoder(model.positional_encoding(model.src_tok_emb(src)), src_mask)

    ys = torch.tensor([[BOS_IDX]], dtype=torch.long).to(device)

    for _ in range(50):
        tgt_mask = torch.triu(torch.ones((ys.size(1), ys.size(1)))*float('-inf'), diagonal=1).to(device)
        out = model.transformer.decoder(model.positional_encoding(model.tgt_tok_emb(ys)), memory, tgt_mask)
        out = model.fc_out(out[:, -1])
        next_token = out.argmax(dim=-1).item()
        ys = torch.cat([ys, torch.tensor([[next_token]]).to(device)], dim=1)
        if next_token == EOS_IDX:
            break

    return decode(ys.squeeze().tolist(), tgt_itos)

# Try it
print("English: aaronitic")
print("Morse:   ", translate("aaronitic"))

# # Try it
# print("English: hello")
# print("Morse:   ", translate("hello"))

# print("English: world")
# print("Morse:   ", translate("world"))
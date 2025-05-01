import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import numpy as np
import os

# torch.set_num_threads(2)

print("PyTorch version:", torch.__version__)
print("PyTorch is using", torch.get_num_threads(), "CPU threads")


# ----------------------------
# Model Definition
# ----------------------------


class MLPClassifier(nn.Module):
    def __init__(self, input_size=7, hidden_sizes=[64, 32], output_size=3):
        super(MLPClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_sizes[0])
        self.fc2 = nn.Linear(hidden_sizes[0], hidden_sizes[1])
        self.output = nn.Linear(hidden_sizes[1], output_size)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        logits = self.output(x)
        return logits

# ----------------------------
# Dataset from CSV
# ----------------------------


class CSVDataset(Dataset):
    def __init__(self, csv_path):
        data = pd.read_csv(csv_path)
        self.X = torch.tensor(data.iloc[:, :-1].values, dtype=torch.float32)
        # Assumes class labels 0,1,2
        self.y = torch.tensor(data.iloc[:, -1].values, dtype=torch.long)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# ----------------------------
# Accuracy Calculation
# ----------------------------


def accuracy(outputs, labels):
    _, preds = torch.max(outputs, 1)
    return (preds == labels).float().mean().item()

# ----------------------------
# Training Loop with Early Stopping
# ----------------------------


def train_model(train_csv_path, val_csv_path, num_epochs=50, patience=5, batch_size=32, model_save_path='best_model.pth'):
    train_dataset = CSVDataset(train_csv_path)
    val_dataset = CSVDataset(val_csv_path)

    train_loader = DataLoader(
        train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size)

    model = MLPClassifier()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    best_val_acc = 0.0
    patience_counter = 0

    for epoch in range(num_epochs):
        model.train()
        train_loss = 0.0

        for inputs, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            train_loss += loss.item()

        # Validation
        model.eval()
        val_loss = 0.0
        val_acc = 0.0
        with torch.no_grad():
            for inputs, labels in val_loader:
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                val_loss += loss.item()
                val_acc += accuracy(outputs, labels)

        val_acc /= len(val_loader)
        print(
            f"Epoch {epoch+1}: Train Loss = {train_loss/len(train_loader):.4f}, Val Acc = {val_acc:.4f}")

        # Checkpointing
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            patience_counter = 0
            torch.save(model.state_dict(), model_save_path)
            print(f"✅ New best model saved (val acc = {val_acc:.4f})")
        else:
            patience_counter += 1
            print(
                f"⚠️ No improvement. Patience: {patience_counter}/{patience}")

        if patience_counter >= patience:
            print("⏹️ Early stopping triggered.")
            break

    print(f"🎯 Training complete. Best validation accuracy: {best_val_acc:.4f}")
    model.load_state_dict(torch.load(model_save_path))

    # Final Evaluation on Validation Set
    from sklearn.metrics import confusion_matrix, classification_report
    import matplotlib.pyplot as plt
    import seaborn as sns

    all_preds = []
    all_labels = []

    model.eval()
    with torch.no_grad():
        for inputs, labels in val_loader:
            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)
            all_preds.extend(preds.tolist())
            all_labels.extend(labels.tolist())

    print("\n🧾 Classification Report:")
    print(classification_report(all_labels, all_preds, digits=3))

    # Confusion Matrix Plot
    cm = confusion_matrix(all_labels, all_preds)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=[0, 1, 2], yticklabels=[0, 1, 2])
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.title("Confusion Matrix")
    # plt.show()

    return model


if __name__ == "__main__":

    import time
    st = time.time()
    trained_model = train_model(
        'train-data.csv', 'eval-data.csv', num_epochs=100, patience=5)
    nd = time.time() - st
    print(f"Training took {nd:.2f} seconds.")

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader, TensorDataset
import numpy as np

# Load Wine dataset
data = load_wine()
X = data['data']  # Features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_tensor = torch.tensor(X_scaled, dtype=torch.float32)

# Dataset and Dataloader
dataset = TensorDataset(X_tensor)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Define the VAE model
class VAE(nn.Module):
    def __init__(self, input_dim, latent_dim):
        super(VAE, self).__init__()
        # Encoder
        self.encoder_fc1 = nn.Linear(input_dim, 64)
        self.encoder_fc2 = nn.Linear(64, 32)
        self.encoder_fc3_mean = nn.Linear(32, latent_dim)
        self.encoder_fc3_logvar = nn.Linear(32, latent_dim)

        # Decoder
        self.decoder_fc1 = nn.Linear(latent_dim, 32)
        self.decoder_fc2 = nn.Linear(32, 64)
        self.decoder_fc3 = nn.Linear(64, input_dim)

    def encode(self, x):
        h = torch.relu(self.encoder_fc1(x))
        h = torch.relu(self.encoder_fc2(h))
        mean = self.encoder_fc3_mean(h)
        log_var = self.encoder_fc3_logvar(h)
        return mean, log_var

    def reparameterize(self, mean, log_var):
        std = torch.exp(0.5 * log_var)
        eps = torch.randn_like(std)
        return mean + eps * std

    def decode(self, z):
        h = torch.relu(self.decoder_fc1(z))
        h = torch.relu(self.decoder_fc2(h))
        return self.decoder_fc3(h)

    def forward(self, x):
        mean, log_var = self.encode(x)
        z = self.reparameterize(mean, log_var)
        return self.decode(z), mean, log_var

# Loss function (Reconstruction + KL Divergence)
def vae_loss_function(recon_x, x, mean, log_var):
    recon_loss = nn.functional.mse_loss(recon_x, x, reduction='sum')
    kl_loss = -0.5 * torch.sum(1 + log_var - mean.pow(2) - log_var.exp())
    return recon_loss + kl_loss

# Hyperparameters
input_dim = X.shape[1]  # 13 features
latent_dim = 2  # Latent space dimension
epochs = 50
learning_rate = 0.001

# Initialize VAE and optimizer
vae = VAE(input_dim=input_dim, latent_dim=latent_dim)
optimizer = optim.Adam(vae.parameters(), lr=learning_rate)

# Training loop
vae.train()
for epoch in range(epochs):
    total_loss = 0
    for batch in dataloader:
        x_batch = batch[0]
        optimizer.zero_grad()
        recon_batch, mean, log_var = vae(x_batch)
        loss = vae_loss_function(recon_batch, x_batch, mean, log_var)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch [{epoch + 1}/{epochs}], Loss: {total_loss / len(dataloader.dataset)}")

# Evaluate reconstruction
vae.eval()
with torch.no_grad():
    sample_data = X_tensor[:10]  # Select a small batch of data
    recon_data, _, _ = vae(sample_data)

# Compare original and reconstructed data
print("Original Data:\n", sample_data.numpy())
print("\nReconstructed Data:\n", recon_data.numpy())

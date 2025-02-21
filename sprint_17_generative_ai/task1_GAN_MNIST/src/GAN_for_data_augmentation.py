import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

# Device configuration
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Hyperparameters
latent_size = 64
hidden_size = 256
image_size = 28 * 28
batch_size = 100
lr = 0.0002
epochs = 10

# MNIST dataset
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=(0.5,), std=(0.5,))
])

train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)


# Generator network
class Generator(nn.Module):
    def __init__(self, latent_size):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, image_size),
            nn.Tanh()
        )

    def forward(self, z):
        img = self.model(z)
        return img


# Discriminator network
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(image_size, hidden_size),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_size, hidden_size),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_size, 1),
            nn.Sigmoid()
        )

    def forward(self, img):
        out = self.model(img)
        return out


# Initialize networks
generator = Generator(latent_size).to(device)
discriminator = Discriminator().to(device)

# Optimizers
optimizer_g = optim.Adam(generator.parameters(), lr=lr)
optimizer_d = optim.Adam(discriminator.parameters(), lr=lr)

# Loss function
criterion = nn.BCELoss()


# Helper function to generate images
def generate_images(generator, num_images):
    latent_vectors = torch.randn(num_images, latent_size).to(device)
    fake_images = generator(latent_vectors)
    return fake_images.view(num_images, 28, 28)

# Training loop
def train_gan(generator, discriminator, train_loader, epochs):
    for epoch in range(epochs):
        for batch_idx, (real_image, _) in enumerate(train_loader):
            batch_size = real_image.size(0)
            real_images = real_image.view(batch_size, -1).to(device)

            # Labels for real and fake images
            real_labels = torch.ones(batch_size, 1).to(device)
            fake_labels = torch.zeros(batch_size, 1).to(device)

            # Train Discriminator
            # Compute BCELoss using real images
            outputs = discriminator(real_images)
            d_loss_real = criterion(outputs, real_labels)
            real_score = outputs

            # Compute BCELoss using fake images
            latent_vectors = torch.randn(batch_size, latent_size).to(device)
            fake_images = generator(latent_vectors)
            outputs = discriminator(fake_images)
            d_loss_fake = criterion(outputs, fake_labels)
            fake_score = outputs

            # Backpropagation and optimization
            d_loss = d_loss_real + d_loss_fake
            optimizer_d.zero_grad()
            d_loss.backward()
            optimizer_d.step()

            # Train Generator
            # Generate fake images and compute loss
            latent_vectors = torch.randn(batch_size, latent_size).to(device)
            fake_images = generator(latent_vectors)
            outputs = discriminator(fake_images)
            g_loss = criterion(outputs, real_labels)

            # Backpropagation and optimization
            optimizer_g.zero_grad()
            g_loss.backward()
            optimizer_g.step()

            if (batch_idx + 1) % 100 == 0:
                print(f'Epoch [{epoch}/{epochs}], '
                      f'Step [{batch_idx + 1}/{len(train_loader)}], '
                      f'D Loss: {d_loss.item():.4f}, '
                      f'G Loss: {g_loss.item():.4f}, '
                      f'D(x): {real_score.mean().item():.4f}, '
                      f'D(G(z)): {fake_score.mean().item():.4f}')

train_gan(generator, discriminator, train_loader, epochs)

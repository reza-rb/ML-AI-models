# Normalizing Flow on 2D Data

## Goal
This project implements a 2D normalizing flow from scratch to learn complex probability distributions using invertible transformations and exact likelihood training.

## Main Concepts
- Change of variables formula
- Invertible neural networks
- Affine coupling layers
- Log determinant of the Jacobian
- Maximum likelihood training
- Sampling from latent space

## Datasets
- Two moons
- Circles
- Gaussian mixture
- Spiral

## Model
The model maps data points x to latent variables z:

z = f(x)

The inverse transformation generates new samples:

x = f⁻¹(z)

## Loss
The model is trained by minimizing negative log-likelihood:

L = - log p_X(x)

where:

log p_X(x) = log p_Z(f(x)) + log |det J_f(x)|

## Results
Results will include:
- original data
- latent space
- generated samples
- density contour plots
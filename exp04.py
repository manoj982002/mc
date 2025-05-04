import numpy as np
from scipy.special import erfc
import matplotlib.pyplot as plt


N = int(1e6)  # Number of bits
Eb_N0_dB = np.arange(-3, 60)  # SNR range


ip = np.random.rand(N) > 0.5  # 0 or 1
s = 2*ip - 1  # BPSK: 0 -> -1, 1 -> 1


nErr = np.zeros(len(Eb_N0_dB))

for i, Eb_N0 in enumerate(Eb_N0_dB):
    n = np.sqrt(0.5) * (np.random.randn(N) + 1j*np.random.randn(N))  
    h = np.sqrt(0.5) * (np.random.randn(N) + 1j*np.random.randn(N)) 
    y = h * s + np.sqrt(10**(-Eb_N0/10)) * n  # received signal
    y_hat = y/h  # equalization
    ipHat = (np.real(y_hat) > 0).astype(int)  
    nErr[i] = np.sum(ip != ipHat)


simBer = nErr / N
theoryBerAWGN = 0.5 * erfc(np.sqrt(10**(Eb_N0_dB/10)))
theoryBer = 0.5 * (1 - np.sqrt((10*(Eb_N0_dB/10)) / (1 + 10*(Eb_N0_dB/10))))  


plt.semilogy(Eb_N0_dB, theoryBerAWGN, 'cd-', linewidth=2)
plt.semilogy(Eb_N0_dB, theoryBer, 'bp-', linewidth=2)
plt.semilogy(Eb_N0_dB, simBer, 'mx-', linewidth=2)
plt.axis([-3, 60, 1e-5, 1])  
plt.grid(True, which="both")
plt.legend(['AWGN - Theory', 'Rayleigh - Theory', 'Rayleigh - Simulation'])
plt.xlabel('Eb/No (dB)')
plt.ylabel('Bit Error Rate (BER)')
plt.title('BER for BPSK modulation in Rayleigh fading channel')
plt.show()

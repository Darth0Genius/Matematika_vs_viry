from scipy.integrate import solve_ivp  # Funkce pro numerické řešení systému ODE
import matplotlib.pyplot as plt  # Knihovna pro vykreslování grafů
import numpy as np  # Knihovna pro efektivní práci s poli


# Definice modelu (systému ODE)
def model(t, u):
    # Rozdělení vstupního vektoru u na jednotlivé proměnné
    I, V, T, E, A = u

    # Parametry modelu
    lamba = 3300
    d = 0.003
    beta = 0.000001
    delta = 0.2
    mu = 0.0005
    le = 100
    de = 0.1
    la = 100
    da = 0.1
    q = 0.005
    alpha = 0.0003
    p = 2
    c = 0.2
    k = 0.002
    omega = 0.000001

    # Definice diferenciálních rovnic pro jednotlivé proměnné
    dT = lamba - d * T - beta * V * T   # Změna populace T (zdravé buňky)
    dI = beta * V * T - delta * I - mu * I * E   # Změna populace I (infikované buňky)
    dE = le - de * E + q * V + alpha * I * E - omega * V * E  # Změna populace E (CTL)
    dV = p * I - c * V - k * A * V  # Změna populace V (virus)
    dA = la - da * A + q * V - k * A * V  # Změna populace A (protilátky)

    # Vrácení výsledků jako seznam
    return [dI, dV, dT, dE, dA]


# Počáteční podmínky
I0 = 1
V0 = 1
T0 = 10 ** 6
E0 = 1000
A0 = 1000
initial_conditions = [I0, V0, T0, E0, A0]

# Časový interval ve dnech pro řešení ODE
time_span = [0, 100]

# Řešení systému ODE
sol = solve_ivp(model, time_span, initial_conditions, t_eval=np.linspace(time_span[0], time_span[1], 500))

# Vykreslení výsledků
variables = ['I (Infikované b.)', 'V (Virus)', 'T (Zdravé b.)', 'E (CTL)', 'A (Protilátky)']
fig, axs = plt.subplots(len(variables), 1, figsize=(10, 12), sharex=True)

for i in range(len(variables)):
    axs[i].plot(sol.t, sol.y[i])
    axs[i].set_ylabel(variables[i])
    axs[i].grid(True)

axs[-1].set_xlabel('Čas (dny)')  # Popisek osy x pro poslední subplot
fig.suptitle('Časový průběh modelu')
plt.tight_layout()
plt.subplots_adjust(top=0.95)
plt.show()

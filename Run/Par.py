import numpy as np 
import scipy.constants as cost 

L = 10
N = 500
dt = 1
m = 100
FRAME = 500
STD_NORMA = 1
V_flag = 0
FPS = 20
real_flag = 1
imag_flag = 0
x_V_centered_coefficient = 0.5
step_x_coefficient = 0.6
barrier_width_coefficient = 0.1
RF_l = 1
V0_coefficient = 0.03722222222222222
a_coefficient = 0.1
α_coefficient = 0.1
x0_coefficient = 0.36666666666666664
p0_coefficient = 0.05555555555555558
σ0_coefficient = 0.05
n = 1
Level = 2
h = 1
ψ_name = 'Wave Packet'
Potential = 'Barrier'
PATH_CHECK = '/home/luca/Documents/Bachelor/Finale'
V_function = ''
lib = 'numpy'
sim = 't dependent'
debug_E = 0
debug_norma = 0
STOP_BOUNDARIES = 0
ST_BD_COEFF = 0.025
norm_factor = 0
LEC = [	[[1, 1]], [[1./2, 1], [1./2, 0]], [[1, -1./24], [-2./3, 3./4], [2./3, 7./24]] ]
LEC_MAX = [1, 1/2, 1]
Potential_list = ['Free','Step', 'Barrier', 'Hole', 'Coulomb', 'Armonic Oscillator', 'Reflectionless', 'Insert...', 'Infinite Barrier' ] 
ψ_list = ['Wave Packet','Armonic oscillator eingestate','Reflecionless WP', 'Coherent' ,'Custom']
cont = 0 
norm =STD_NORMA 
x0 = x0_coefficient * L 
P_MAX = np.pi*h*N / L
p0 = p0_coefficient * P_MAX  
σ0 = σ0_coefficient * L
x_V_centered = x_V_centered_coefficient * L
step_x = step_x_coefficient * L
barrier_width = barrier_width_coefficient * L
V_MAX = 2 * np.pi * h / dt / LEC_MAX[Level-1]
V0 = V0_coefficient * V_MAX
a_MAX = (V_MAX - 0.0001) * 4 / L**2
a = a_coefficient * a_MAX
ω = np.sqrt(2 * a / m)
α_MAX = np.sqrt(V_MAX*(2*m / h**2)*(1/(RF_l*(RF_l+1))))
α = α_coefficient * α_MAX
x = np.linspace(0, L, N, endpoint = False)
p = np.linspace(0, 2*P_MAX, N, endpoint = False)



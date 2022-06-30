# %% Importing the fuels data and math library for some basic calculations
from dataclasses import dataclass
import json
from math import atan, cos, exp, pi, sin, sqrt, tan

_fuel_data = {}

def load_fuel_data(file_name):
    # Load fuel data from the specified file, stored as nested JSON objects
    # (fuel categories and individual properties).
    with open(file_name) as f:
        fuel_dict = json.load(f)

    # Capture any default values provided.
    default = fuel_dict.pop('default', {})

    # Update the internal fuel tables from the file data.
    _fuel_data.clear()
    for cat_name in fuel_dict:
        properties = {}
        for k,v in default.items():             # start with defaults
            properties[k] = v
        for k,v in fuel_dict[cat_name].items(): # set explicit properties
            properties[k] = v
        _fuel_data[cat_name] = properties


@dataclass
class BalbiROS:
    U       : float         # Model parameters
    alpha   : float
    W_0     : float
    T_a     : float

    m       : float         # Input fuel data
    sigma   : float
    sigma_t : float
    h       : float
    s       : float
    rho_v   : float
    delta_H : float
    C_p     : float

    beta    : float         # Preliminary computations
    beta_t  : float
    S       : float
    S_t     : float
    nu      : float
    delta_T : float
    q       : float
    T_f     : float
    u_0     : float

    R_b     : float         # Radiative contributions
    A       : float
    gamma   : float
    H_f     : float
    l_f     : float
    R_r     : float

    W_00    : float         # Convective contributions
    a_up    : float
    a_lat   : float
    K       : float
    b       : float
    R_c     : float

    R       : float         # Total ROS
    n_iter  : int


def ros_balbi(category, speed, tanphi, fmc_g, T_a):
    # Fuel category values
    fuel        = _fuel_data[category]
    cmbcnst     = fuel['cmbcnst']
    fgi         = fuel['fgi']
    fgi_t       = fuel['fgi_t']
    fueldens    = fuel['fueldens']
    fueldepthm  = fuel['fueldepthm']
    savr        = fuel['savr']
    specheat    = fuel['specheat']


    #---------------------------------------------------------------------------
    # Constants and model parameters (slide 9)
    #
    # NOTE: Local terrain slope angle is maintained in radians here
    # instead of degrees.

    B           = 5.6e-8                # Stefan-Boltzman constant              [W/m^2/K^4]
    chi_0       = 0.3                   # Radiative factor
    r_00        = 2.5e-5                # Model parameter
    delta_h     = 2.3e6                 # Heat of latent evaporation            [J/kg]
    tau_0       = 75591.                # Anderson's residence time coefficient
    rho_a       = 1.125                 # Air density                           [kg/m3]
    s_t         = 16.                   # Stoichiometric coefficient
    T_i         = 600.                  # Ignition temperature                  [K]
    g           = 9.81                  # Gravitational acceleration            [m/s^2]
    C_pa        = 1150.                 # Specific heat of air                  [J/kg/K]

    U           = speed                 # Normal component of wind speed        [m/s]
    alpha       = atan(tanphi)          # Local terrain slope angle             [rad]
    W_0         = 50                    # NOTE: needs to be parameter


    #---------------------------------------------------------------------------
    # Input fuel data (slide 2)

    m           = fmc_g                 # Dead fuel moisture content
    sigma       = fgi                   # Dead fine fuel load                   [kg/m^2]
    sigma_t     = fgi_t                 # Total fine fuel load                  [kg/m^2]
    h           = fueldepthm            # Fuel height                           [m]
    s           = savr / 0.3048         # Surface area to volume ratio          [1/m]
    rho_v       = 500.                  # Fuel density                          [kg/m^3]
    delta_H     = cmbcnst               # Heat of combustion of pyrolysis gases [J/kg]
    C_p         = specheat              # Specific heat                         [J/kg/K]


    #---------------------------------------------------------------------------
    # Preliminary computations (slide 3)
    #
    # NOTE: An average value for bulk density (rho_v) is established above, so
    # it is not computed here.

    # Packing ratios
    beta    = sigma / (h * rho_v)   # dead fuel
    beta_t  = sigma_t / (h * rho_v) # total fuel

    # Leaf areas
    S       = s * h * beta          # dead fuel
    S_t     = s * h * beta_t        # total fuel

    # Absorbtion coefficient
    nu      = min(S, 2. * pi * beta / beta_t)

    # Temperature difference
    delta_T = T_i - T_a

    # Activation energy
    q       = C_p * delta_T + m * delta_h

    # Flame temperature
    T_f     = T_a + (delta_H * (1. - chi_0)) / ((s_t + 1.) * C_pa)

    # Upward gas velocity
    #
    # NOTE: This uses rho_v, whereas the slides show the variable rho.
    # The latter is not defined anywhere in the slides; this merits clarification.
    u_0     = 2. * nu * ((s_t + 1.) / tau_0) * (rho_v / rho_a) * (T_f / T_a)

    # Bulk density (rho_v) is not computed here; an average value is set above.


    #---------------------------------------------------------------------------
    # Radiative contributions (slide 4)

    # Flame base radiation contribution to ROS
    R_b     = min(S_t / (2 * pi), 1.) * (beta / beta_t)**2 * (B * T_f**4) / (beta * rho_v * q)

    # Radiative coefficient
    A       = min(S_t / (2. * pi), beta / beta_t) * chi_0 * delta_H / (4. * q)

    # Flame tilt angle
    gamma   = atan(tan(alpha) + U / u_0)

    # Flame height
    H_f     = (u_0 ** 2) / (g * (T_f / T_a - 1.) * (cos(alpha))**2)

    # Flame length
    l_f     = H_f / (cos(gamma - alpha))

    # Free flame radiation contribution to ROS
    def _R_r(_R):
        return A * _R * ((1 + sin(gamma) - cos(gamma)) / (1 + ((_R * cos(gamma)) / (s * r_00))))


    #---------------------------------------------------------------------------
    # Convective contribution (slide 5)

    # Heat loss coefficients
    #
    # NOTE: W_00 needs to be supplied via fuel category table; it is
    # hard-coded here for now.

    W_00    = 50.                       # 50 for shrubland, 33 for grassland
    a_up    = 0.025 * s * beta_t * sqrt(h)
    a_lat   = min(W_0 / W_00, 1.)

    # Drag force coefficient
    #
    # NOTE: denominator is identical to a_lat above; perhaps slide meant to
    # specified a_lat instead?
    K       = (beta_t / min(W_0 / W_00, 1.))

    # Convective coefficient
    b       = (a_up * a_lat * rho_a * delta_H * T_a) / (2. * q * (s_t + 1) * rho_v * beta_t * T_f)

    # Convective contribution to ROS
    def _R_c(_R):
        return b * (u_0 * (tan(alpha) / 2) + (U * exp(-K * _R)))


    #---------------------------------------------------------------------------
    # Algorithm (slide 7)

    # Iteratively solve for the total ROS.  Seed the search using the flame
    # base radiation contribution, which is invariant.
    R0 = R_b

    for i in range(20):
        # Update the iterative ROS contributions, then recompute the total ROS.
        R_r = _R_r(R0)
        R_c = _R_c(R0)
        R1  = R_b + R_r + R_c

        tol_R = 1e-7
        if abs(R1 - R0) < tol_R:    # converged?
            return BalbiROS(
                U       = U,        # Model parameters
                alpha   = alpha,
                W_0     = W_0,
                T_a     = T_a,

                m       = m,        # Input fuel data
                sigma   = sigma,
                sigma_t = sigma_t,
                h       = h,
                s       = s,
                rho_v   = rho_v,
                delta_H = delta_H,
                C_p     = C_p,

                beta    = beta,     # Preliminary computations
                beta_t  = beta_t,
                S       = S,
                S_t     = S_t,
                nu      = nu,
                delta_T = delta_T,
                q       = q,
                T_f     = T_f,
                u_0     = u_0,

                R_b     = R_b,      # Radiative contributions
                A       = A,
                gamma   = gamma,
                H_f     = H_f,
                l_f     = l_f,
                R_r     = R_r,

                W_00    = W_00,     # Convective contributions
                a_up    = a_up,
                a_lat   = a_lat,
                K       = K,
                b       = b,
                R_c     = R_c,

                R       = R1,       # Total ROS
                n_iter  = i + 1,
            )

        R0 = R1

    return None


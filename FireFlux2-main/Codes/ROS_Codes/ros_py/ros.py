import csv
import json
from math import atan, cos, exp, nan, pi, sin, tan
import numpy as np

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


def ros_rothermel(category, speed, tanphi, fmc_g):
    # Fuel category values
    fuel        = _fuel_data[category]
    cmbcnst     = fuel['cmbcnst']
    fgi         = fuel['fgi']
    fueldens    = fuel['fueldens']
    fueldepthm  = fuel['fueldepthm']
    fuelmce     = fuel['fuelmce']
    ichap       = fuel['ichap']
    savr        = fuel['savr']
    se          = fuel['se']
    st          = fuel['st']

    fuelmc_g    = fmc_g

    bmst        = fuelmc_g / (1. + fuelmc_g)
    fuelheat    = cmbcnst * 4.30e-04        # convert J/kg to BTU/lb
    fuelloadm   = (1. - bmst) * fgi         # fuelload without moisture

    fuelload    = fuelloadm * 0.3048**2 * 2.205     # to lb/ft^2
    fueldepth   = fueldepthm / 0.3048               # to ft
    betafl      = fuelload / (fueldepth * fueldens) # packing ratio  jm: lb/ft^2/(ft * lb*ft^3) = 1
    betaop      = 3.348 * savr**(-0.8189)           # optimum packing ratio jm: units??  
    qig         = 250. + 1116. * fuelmc_g           # heat of preignition, btu/lb
    epsilon     = exp(-138. / savr)                 # effective heating number
    rhob        = fuelload / fueldepth              # ovendry bulk density, lb/ft^3
    c           = 7.47 * exp(-0.133 * savr**0.55)   # const in wind coef
    bbb         = 0.02526 * savr**0.54              # const in wind coef
    e           = 0.715 * exp(-3.59e-4 * savr)      # const in wind coef
    phiwc       = c * (betafl / betaop)**(-e) 
    rtemp2      = savr**1.5
    gammax      = rtemp2 / (495. + 0.0594 * rtemp2) # maximum rxn vel, 1/min
    a           = 1. / (4.774 * savr**0.1 - 7.27)   # coef for optimum rxn vel
    ratio       = betafl / betaop   
    gamma       = gammax * (ratio**a) * exp(a * (1. - ratio))   # optimum rxn vel, 1/min
    wn          = fuelload / (1. + st)              # net fuel loading, lb/ft^2
    rtemp1      = fuelmc_g / fuelmce
    etam        = 1. - 2.59 * rtemp1 + 5.11 * rtemp1**2 - 3.52 * rtemp1**3  # moist damp coef
    etas        = 0.174 * se**(-0.19)                       # mineral damping coef
    ir          = gamma * wn * fuelheat * etam * etas       # rxn intensity,btu/ft^2 min
    irm         = ir * 1055. / (0.3048**2 * 60.) * 1e-6     # for mw/m^2 (set but not used)
    xifr        = exp((0.792 + 0.681 * savr**0.5) * (betafl+0.1)) /     \
                    (192. + 0.2595 * savr)                  # propagating flux ratio
    r_0         = ir * xifr / (rhob * epsilon * qig)        # default spread rate in ft/min

    if ichap == 0:
        # if wind is 0 or into fireline, phiw = 0, &this reduces to backing ros.
        spdms   = max(speed, 0.)
        umidm   = min(spdms, 30.)                   # max input wind spd is 30 m/s
        umid    = umidm * 196.850                   # m/s to ft/min
        #  eqn.: phiw = c * umid**bbb * (betafl/betaop)**(-e) ! wind coef
        phiw    = umid**bbb * phiwc                 # wind coef
        phis    = 5.275 * betafl**(-0.3) * max(0., tanphi)**2   # slope factor
        ros = r_0 * (1. + phiw + phis) * .00508     # spread rate, m/s
    else:
        # spread rate has no dependency on fuel character, only windspeed
        spdms   = max(speed, 0.);
        ros     = max(.03333, 1.2974 * spdms**1.41) # spread rate, m/s

    return min(ros, 6.)


def ros_balbi(category, speed, tanphi, fmc_g, T_a):
    # Fuel category values
    fuel        = _fuel_data[category]
    cmbcnst     = fuel['cmbcnst']
    fgi         = fuel['fgi']
    fueldens    = fuel['fueldens']
    fueldepthm  = fuel['fueldepthm']
    savr        = fuel['savr']

    fuelmc_g    = fmc_g

    # Universal constants
    g           = 9.81                  # Gravitational acceleration [m/s2]
    Chi_0       = 0.3                   # Radiative factor
    st          = 17.                   # Stochiometric coefficient
    B           = 5.67e-8               # Stefan-Boltzman [W/m2/K4)
    deltah_w    = 2.257e6               # Water Evap Enthalpy [J/kg]
    tau_0       = 75591.                # Anderson's residence time coefficient
    T_i         = 600.                  # ignition temperature [K]

    # Fuel Constants
    C_p         = 2000.                 # Specific heat of fuel [J/kg/K] - Balbi 2009
    C_pa        = 1150.                 # Specific heat of air [J/Kg/K]
    m           = fuelmc_g              # FUEL PARTICLE MOISTURE CONTENT as fraction (0 - 1) [-]
    #rho_v       = fueldens * 16.0185    # FUEL Particle Density [Kg/m^3]
    h           = fueldepthm            # Fuel thickness (depth) (m)
    DeltaH      = cmbcnst               # Combustion Enthalpy [J/kg]
    sigma       = fgi                   # Dead fuel load [kg/m2]
    sigma_t     = fgi                   # Total fuel load [kg/m2]
    rho         = 1500.                 # Fuel density [kg/m3]
    rho_v       = 500.                  # fuel density (From the video [kg/m3])
    rho_a       = 1.125                 # Air density [kg/m3]
    rho_flame   = 0.25                  # Gas Flame Density [kg/m^3]
    beta        = sigma / (h * rho_v)     # packing ratio of the dead fuel (eq. 1)
    beta_t      = sigma_t / (h * rho_v)   # total packing ratio (eq. 2)
    s           = savr / 0.3048         # surface area to volume ratio 1/m converted form 1/ft
    LAI         = (s * h * beta) / 2.   # Leaf area index for dead fuel (eq. 3)
    LAI_t       = (s * h * beta_t) / 2. # Total fuel leaf area index (eq. 4)
    S           = 2 * LAI               # Leaf area
    S_t         = 2 * LAI_t             # Leaf area
    nu          = min(2. * LAI, 2. * pi * beta / beta_t)    # Absorption coeffcient (eq. 5) 
    lv          = h                     # fuel length (m)
    DeltaT      = (T_i - T_a)
    # Model parameters
    K1          = 100.                  # 100 for field, 1400 for the lab
    r_00        = 2.5e-5                # Model parameter

    alpha       = atan(tanphi)          # Slope angle [rad]
    U           = speed                 # winds speed normal to the fire front line (m/s)
    W_0         = 50                    # Fire Front width (ignition line) (m). This is a guess and needs to be modified
    W_00        = 50                    # 50 for shrubland, 30 for grassland
    # Heat loss coefficients
    a_up = 0.025 * s * beta_t * np.sqrt(h)
    a_lat = min(W_0 / W_00, 1)
    simple_radiation = False
    tol_R       = 1e-5  # tolerance to compute R
    maxit_R     = 20    # max iterations to compute R

    # compute drag force coefficient (eq. 7)
    K       = (beta_t / min(W_0 / W_00, 1))
    #K_drag  = K1 * beta_t * min(h / lv, 1.)

    # compute activation energy (eq. 14)
    q       = C_p * DeltaT + m * deltah_w

    # compute radiant coeffcient (eq. 13)
    A       = min(S_t / (2. * pi), beta / beta_t) * Chi_0 * DeltaH / (4. * q)

    # as a first guess take Rothermel ROS
    R       = ros_rothermel(category, speed, tanphi, fmc_g)
    R_old   = R
    gamma   = alpha     # first guess no extra tilt

    for i in range(maxit_R):
        # compute radiative fraction (eq. 20)
        if simple_radiation:    # start from the initial guess
            Chi = Chi_0
        else:   # compute radiative fraction from rate of spread and gamma which are unkown...
            Chi = Chi_0 / (1. + R * cos(gamma) / (s * r_00))

        # compute flame temperature (eq. 16)
        T_f     = T_a + (DeltaH * (1. - Chi_0)) / ((st + 1.) * C_pa)

        # compute upward gas velocity (eq. 19)
        u_0     = 2. * nu * ((st + 1.) / tau_0) * (rho / rho_a) * (T_f / T_a)

        # compute flame tilt angle (eq. 15)
        gamma   = atan(tan(alpha) + U / u_0)

        # compute flame height (eq. 17)
        H_f     = u_0 * u_0 / (g * (T_f / T_a - 1.) * (cos(alpha))**2)
        
        # compute flame length
        l_f     = H_f / (cos(gamma - alpha))
        
        # compute convective coefficient (eq. 8)
        #b       = 1. / (q * tau_0 * u_0 * beta_t) * deltah_w * nu * min(st / 30., 1.)
        b       = (a_up * a_lat * rho_a * DeltaH * T_a) / (2 * q * (st + 1) * rho_v
                                                           * beta_t * T_f)
        # compute rate of spread
        
        # Contribution of the free flame radiation to the ROS
        R_r = A * R * ((1 + sin(gamma) - cos(gamma)) / (1 + ((R * cos(gamma))/(s * r_00))))
        
        # rate of spread from base radiation
        R_b     = min(S_t / (2 * pi), 1.) * (beta / beta_t)**2 * (B * T_f**4) / (beta * rho_v * q)

        # compute rate of spread due to flame radiation (eq. 11)
        R_f     = A * R * (1. + sin(gamma) - cos(gamma)) / (1. + R * cos(gamma) / (s * r_00))

        # compute rate of spread due to convection
        R_c     = b * (u_0 * (tan(alpha) / 2) + (U * exp(- K * R)))
        #R_c     = b * (tan(alpha) + 2. * U / u_0 * exp(-K_drag * R))

        # compute the total rate of spread
        R       = R_b + R_f + R_c

        if abs(R - R_old) < tol_R:
            return R

        R_old = R

    return nan


# Coronavirus Pandemic Simulation with Vaccination Strategies

This project simulates the spread of the coronavirus pandemic using stochastic simulation techniques based on probability. It evaluates the effectiveness of different vaccination plans implemented by governments, considering factors such as vaccine effectiveness, research and development time, and vaccine distribution.

## Overview

The simulation model is built in Python and utilizes stochastic methods to simulate the spread of the virus within a population grid. It incorporates various parameters such as vaccination rate, vaccine effectiveness, and the duration of immunity to analyze the impact of different vaccination strategies on controlling the pandemic.

## Table of Contents
- [Key Components](#key-components)
- [Simulation Parameters](#simulation-parameters)
- [Key Components](#key-components)
- [Dependancies](#dependancies)
- [Structure](#structure)
- [Results](#results)
- [License](#license)

## Key Components

- **Simulation Script**: The main script `simulate_pandemic.py` drives the simulation process by updating the state of each individual in the population grid based on infection probabilities and vaccination status.

- **Vaccination Strategies**: The simulation implements different vaccination plans, including standard distribution, enhanced distribution, and optimized distribution, each with varying parameters such as vaccine effectiveness and distribution rate.

- **Visualization**: The project includes visualization capabilities to plot the spread of the pandemic over time, the percentage of susceptible, infected, and immune individuals, and the impact of vaccination strategies on controlling the outbreak.


## Simulation Parameters

- `Day`: Number of days of simulation.
- `herd_immunity`: Days until herd immunity is achieved.
- `vac_day`: Number of days until the vaccine is released.
- `vaccine_eff`: Effectiveness of the vaccine in preventing infection.
- `vaccine_eff_2`: Effectiveness of the second vaccine dose.
- `percent_of_pop_1`: Percent of population that would want the first vaccine
- `percent_of_pop_2`: Percent of population that would want both vaccines
- `vac_pop_percent`: How quickly the vaccine was distributed after release
- `beta`: Contagionist
- `h`: Contracting the disease outside of neighbours
- `unimmuneDay`: Days an agent would remain immune
- `infectedDays`: Days an agent would remain infected
- `infectedDays_vaccine`: Days an agent would remain infected after having the vaccine
- `immunityChance`: Probability a person would become immune after 'infectedDays'
- `immunityChance_vac`: = Probability a person would become immune after 'infectedDays_vaccine'

## Dependancies


- This project relies on the following libraries:

- **math**: Provides mathematical functions and constants.
- **random.gauss**: Generates random numbers according to a Gaussian distribution (normal distribution).
- **random.randint**: Generates random integers within a specified range.
- **numpy**: A powerful library for numerical computing, including arrays, matrices, and mathematical functions.
- **copy**: Used for creating shallow and deep copies of objects.
- **scipy.integrate.simpson**: Part of the SciPy library, used for numerical integration using Simpson's rule.
- **matplotlib.pyplot**: A plotting library for creating visualizations in Python.
- **csv**: Provides functionality for reading and writing CSV files.
- **datetime**: Offers classes for working with dates and times.


## Structure

## Results

The simulation generates visualizations and comparative analysis of different vaccination plans, including:

- Spread of the pandemic over time.
- Impact of vaccination on infection rates.
- Comparison of government strategies in controlling the pandemic.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

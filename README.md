# Coronavirus Pandemic Simulation with Various Vaccination Strategies

## Overview

This project is abuilt in Python and utilises stochastic methods to simulate the spread of the Coronavirus within a population grid. The project aims to provide insights into the dynamics of disease transmission and the impact of various interventions, particularly vaccination strategies, on controlling the spread of the virus.

## Table of Contents
- [Purpose and Goals](#purpose-and-goals)
- [Key Features and Functionality](#key-features-and-functionality)
- [Target Audience](#target-audience)
- [Simulation Parameters](#simulation-parameters)
- [Dependancies](#dependancies)
- [Results](#results)
- [License](#license)

## Purpose and Goals:
- **Understanding Disease Spread:** The primary goal is to simulate the spread of COVID-19 within a community to better understand its transmission dynamics.
- **Assessing Vaccination Strategies:** The project evaluates the effectiveness of different vaccination plans and parameters, including vaccine types, research and development (R&D) timelines, distribution logistics, and the role of mask-wearing in reducing transmission.
- **Optimising Outbreak Management:** By conducting various simulations, the project aims to identify optimal strategies for containing and mitigating the impact of the COVID-19 outbreak.

## Key Features and Functionality:
- **Agent-Based Simulation:** Utilises stochastic simulations to model the interactions between individuals within a community, considering factors such as social contacts and infection probabilities.
- **Vaccine Distribution Analysis:** Examines the effects of different vaccination plans on disease spread, including the choice of vaccines, deployment timelines, and distribution logistics.
- **Scenario Analysis:** Conducts multiple simulations with variations in vaccination strategies to assess their impact on controlling the outbreak.
- **Integration of Real-World Data:** Incorporates real-world data on vaccine effectiveness,  transmission rates, and population demographics to enhance the accuracy of simulations.
- **Visualisation and Analysis:** Provides visualisations and statistical analysis of simulation results to facilitate interpretation and decision-making.

## Target Audience:
- **Public Health Officials:** Offers insights and recommendations for public health policymakers and officials involved in designing and implementing vaccination strategies and outbreak management plans.
- **Researchers and Scientists:** Serves as a research tool for epidemiologists, infectious disease experts, and scientists studying the dynamics of infectious diseases and vaccination efficacy.
- **General Public:** Raises awareness about the importance of vaccination and preventive measures in combating COVID-19 and other infectious diseases.

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
- **matplotlib.pyplot**: A plotting library for creating visualisations in Python.
- **csv**: Provides functionality for reading and writing CSV files.
- **datetime**: Offers classes for working with dates and times.

## Results

The simulation generates visualisations and comparative analysis of different vaccination plans, including:

- Spread of the pandemic over time.
- Impact of vaccination on infection rates.
- Comparison of government strategies in controlling the pandemic.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

from skfuzzy import control as ctrl
import skfuzzy as fuzz
import numpy as np


error = ctrl.Antecedent(np.arange(-4, 4, 1), 'error')
error_dot = ctrl.Antecedent(np.arange(-10, 10, 1), 'error')

error_names = ['too_cold', 'just_right', 'too_hot']
error_dot_names = ['getting_colder', 'no_change', 'getting_hotter']

#Outputing them into auto-membership functions
error.automf(names=error_names)
error_dot.automf(names=error_dot_names)

error.view()
error_dot.view()

# Washing Time Universe
percent['cool'] = fuzz.trimf(percent.universe, [-100, -50, 0])
percent['do_nothing'] = fuzz.trimf(percent.universe, [-50, 0, 50])
percent['heat'] = fuzz.trimf(percent.universe, [0, 50, 100])


percent.view()

# Rule Application
rule1 = ctrl.Rule(degree_dirt['too_hot'] | type_dirt['getting_colder'], percent['cool'])
rule2 = ctrl.Rule(degree_dirt['just_right'] | type_dirt['getting_colder'], percent['heat'])
rule3 = ctrl.Rule(degree_dirt['too_cold'] | type_dirt['getting_colder'], percent['heat'])
rule4 = ctrl.Rule(degree_dirt['too_hot'] | type_dirt['no_change'], percent['cool'])
rule5 = ctrl.Rule(degree_dirt['just_right'] | type_dirt['no_change'], percent['do_nothing'])
rule6 = ctrl.Rule(degree_dirt['too_cold'] | type_dirt['no_change'], percent['heat'])
rule7 = ctrl.Rule(degree_dirt['too_hot'] | type_dirt['getting_hotter'], percent['cool'])
rule8 = ctrl.Rule(degree_dirt['just_right'] | type_dirt['getting_hotter'], percent['cool'])
rule9 = ctrl.Rule(degree_dirt['too_cold'] | type_dirt['getting_hotter'], percent['heat'])

# Washing Control Simulation
percent_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
percent_fi = ctrl.ControlSystemSimulation(percent_ctrl)




error_input = float(input())
error_dot_input = float(input())


if error_input < 0.0 or error_input > 100.0:
    raise Exception("Invalid Type of Dirtiness: %lf" %error_input)
if error_dot_input < 0.0 or error_input > 100.0:
    raise Exception("Invalid Degree of Dirtiness: %lf" %error_dot_input)

percent_fi.input['type_dirt'] = error_input
percent_fi.input['degree_dirt'] = error_dot_input

percent_fi.compute()

percent.view(sim=percent_fi)

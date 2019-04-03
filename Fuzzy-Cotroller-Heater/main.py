import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership
# functions
TempExt = ctrl.Antecedent(np.arange(-5, 25+1, 1), 'TempExt')
IntensAquec = ctrl.Consequent(np.arange(0, 100+1, 1), 'IntensAquec')

# Auto-membership function population is possible with .automf(3, 5, or 7)
TempExt.automf(names=['too-cold', 'cold', 'warm', 'hot', 'too-hot'])
IntensAquec.automf(names=['very-low', 'low', 'medium', 'high', 'very-high'])


# Custom membership functions can be built interactively with a familiar,

# Classificando
TempExt['too-cold'] = fuzz.trimf(TempExt.universe, [-5, -5, 0])
TempExt['cold'] = fuzz.trimf(TempExt.universe, [-1, 3, 8])
TempExt['warm'] = fuzz.trimf(TempExt.universe, [7, 10, 14])
TempExt['hot'] = fuzz.trimf(TempExt.universe, [13, 16, 20])
TempExt['too-hot'] = fuzz.trimf(TempExt.universe, [19, 26, 26])

IntensAquec['very-low'] = fuzz.trimf(IntensAquec.universe, [0, 0, 25])
IntensAquec['low'] = fuzz.trimf(IntensAquec.universe, [20, 35, 45])
IntensAquec['medium'] = fuzz.trimf(IntensAquec.universe, [40, 50, 65])
IntensAquec['high'] = fuzz.trimf(IntensAquec.universe, [60, 70, 85])
IntensAquec['very-high'] = fuzz.trimf(IntensAquec.universe, [75, 101, 101])

##Para conseguir ver o grafico
TempExt.view()
plt.savefig('TempExt.png')
IntensAquec.view()
plt.savefig('IntensAquec.png')

rule0 = ctrl.Rule(antecedent=TempExt['too-hot'],consequent=IntensAquec['very-low'], label='rule very-low')

rule1 = ctrl.Rule(antecedent=TempExt['hot'],consequent=IntensAquec['low'], label='rule low')

rule2 = ctrl.Rule(antecedent=TempExt['warm'],consequent=IntensAquec['medium'], label='rule medium')

rule3 = ctrl.Rule(antecedent=TempExt['cold'],consequent=IntensAquec['high'], label='rule high')

rule4 = ctrl.Rule(antecedent=TempExt['too-cold'],consequent=IntensAquec['very-high'], label='rule very-high')

system = ctrl.ControlSystem(rules=[rule0, rule1, rule2, rule3, rule4])
sim = ctrl.ControlSystemSimulation(system)


for TE in range(-5,26):
#Valor da temperatura externa
  sim.input['TempExt'] = TE
#Calculo de inferencia
  sim.compute()
#Temperatura de saida do aquecedor
  IA = sim.output['IntensAquec']
#Calcula da temperatura da agua
#TA = TE + ( IA / 2,7 ) + 5 * abs( sen( 33127 / 500 ) )
#TA = TE + ( IA / 2,7 ) + 5 * abs( 0.27688829471823573 )
  TA = TE + ( IA / 2.7 ) + 5 * abs( 0.2768 )
  print("TE =","%.2f" %TE,"ºC"," IA =","%.2f" %IA,"%"," TA =","%.2f" %TA,"ºC")
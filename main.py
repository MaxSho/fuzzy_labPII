from fuzzy_controller import FuzzyController
import model_2
import model
from t2_plot import draw_lv

choosen_model = 2
S_max = 100
S_min = 30
F_max = 20
D_max = 15

Controller = FuzzyController(choosen_model, S_max, S_min, F_max, D_max)


area = 100
floor = 20
condition = 10
distance = 7

# area = 30
# floor = 1
# condition = 1
# distance = 15

# area = 60
# floor = 8
# condition = 7
# distance = 15

crisp = [area, floor, condition, distance]


result = Controller.get_result(crisp)
print(result)
# for lv in model_2.input_lvs:
# 	draw_lv(lv)

# draw_lv(model_2.output_lv)
t = 1.44
r1 = 270
r2 = 150
ct = 22e-9

f = t / ((r1 + (2 * r2)) * ct)
print("Calculated frequency =",f )

measured_period = 359.677e-6

calc_frequency = 1 / measured_period
print("Measured period ",calc_frequency )

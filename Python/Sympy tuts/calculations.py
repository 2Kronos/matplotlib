t = 1.44
r1 = 1000
r2 = 2000
ct = 1.6e-6

f = t / ((r1 + (2 * r2)) * ct)
print("Calculated frequency =",f )

measured_period = 359.677e-6

calc_frequency = 1 / measured_period
print("Measured period ",calc_frequency )

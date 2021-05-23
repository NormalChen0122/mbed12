import matplotlib.pyplot as plt
import numpy as np

Ts = 30;   # signal interval
end = 90; # signal end point
n = int(end/Ts)+1

x = np.linspace(0, end, num=n) # signal vector

# TODO: revise this array to your results
# y = np.array([0.000, 5.501, 11.799, 15.147, 16.263, 16.821]) # speed vector
y = np.array([0.000, 6.697, 12.676, 15.546]) # speed vector
# y = np.array([0.000, 5.501, 10.443, 10.045, 10.125, 10.204]) # speed vector

z = np.polyfit(x, y, 3) # Least squares polynomial fit, and return the coefficients.

goal = 5             # if we want to let the servo run at 7 cm/sec
                     # equation : z[0]*x^2 + z[1]*x + z[2] = goal
z[3] -= goal         # z[0]*x^2 + z[1]*x + z[2] - goal = 0

result = np.roots(z) # Return the roots of a polynomial with coefficients given

# output the correct one
if (0 <= result[0]) and (result[0] <= end):
    print(result[0])
else:
    print(result[1])

if (0 <= result[0]) and (result[0] <= end):
    print(result[0])
elif (0 <= result[1]) and (result[1] <= end):
    print(result[1])
else:
    print(result[2])

print(result)
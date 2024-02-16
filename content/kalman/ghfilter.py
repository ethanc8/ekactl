/**
 * Author: Ethan Charoenpitaks
 * Date: 2024-01-15
 * License: CC0
 * Source: Own work
 * Description: Given the scale for $x$, $g$, and the scale for $dx$ (velocity), $h$,
 * a starting position, $x_0$, an estimated velocity, $dx$, a time scale, $dt$, and
 * measurement data, $\text{data}$, returns the estimated position after each measurement.
 * Time: O(\text{len}(\text{data}))
 * Status: tested
 */

import numpy as np
def g_h_filter(data, x0, dx, g, h, dt):
    predictions = []
    estimates = []
    x = x0
    for measurement in data:
        # Prediction step
        x += dx*dt
        predictions.append(x)

        # Update step
        residual = measurement - x

        # Make dx change by part of the measured dx
        dx += h * (residual / dt)
        # Make x change by part of the measured x
        x += g * residual

        estimates.append(x)
    return np.array(estimates)
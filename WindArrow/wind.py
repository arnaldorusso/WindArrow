#!/usr/bin/env python
# -*- coding: utf-8 -*-

def windplot(t, windv, pos=5, angle=0.0, color='k'):
    """Computes angle of arrows based on wind direction.
    t : arr
        time position (inform as integers values. Datatime
        will be processed in the near future)
    windv : arr
        Wind Velocity.
    angle : arr
        Wind direction.
    """
    dx = windv*np.cos(angle*np.pi/180.)/15.
    dy = windv*np.sin(angle*np.pi/180.)/15.
    arr = plt.Arrow(t, pos, dx, dy, width=0.3,
		    edgecolor=color,
                    facecolor=color,
                    lw=0.003,
                    ls='solid'
                    )
    return arr

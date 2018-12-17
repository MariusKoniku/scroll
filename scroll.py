import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


class ScrollPlot(object):

    def __init__(self, ax,window_size=90, color = 'b', marker = None,
                 alpha = 1, y0 = 50):
        self.ax = ax
        self.window_size = window_size
        self.s_frame = []
        self.t_frame = []

        # Add line to plot
        self.line = Line2D(self.t_frame, self.s_frame,color= color,
                           marker = marker, alpha = alpha)
        self.ax.add_line(self.line)

        # Set initial axis limits
        self.ax.set_ylim(y0 - 5,y0 + 5)
        #self.ax.set_ylim(0.5,0.55)
        self.ax.set_xlim(0, self.window_size)


    def update(self, t_val, s_val):
        if t_val is None:
            print('time value is None')
        else:
            # append new signal values to frame
            self.t_frame.append(t_val)
            self.s_frame.append(s_val)
            self.line.set_data(self.t_frame,self.s_frame)
            y_min,y_max = self.ax.get_ylim()
            if s_val < y_min:
                y_min = s_val - 0.1
                self.ax.set_ylim(y_min, y_max) # or 0 to 255, or min in history to max in history (keep in object as m_vars)
            if s_val > y_max:
                y_max = s_val + 0.1
                self.ax.set_ylim(y_min, y_max) # or 0 to 255, or min in history to max in history (keep in object as m_vars)


            # check frame overrun and ~ s c r o l l ~
            #if t_val-self.t_frame[0] > self.window_size: # after the first time hitting the boundary
            if t_val > self.window_size: # after the first time hitting the boundary
                self.t_frame.pop(0)
                self.s_frame.pop(0)
                self.ax.set_xlim(self.t_frame[0], self.t_frame[0] + self.window_size)

        return self.line

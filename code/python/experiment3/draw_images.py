import matplotlib.pyplot as plt
import matplotlib.patches as patches
import _tkinter
import matplotlib.axes as ax
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab

from action_blame import rewards_multi, kemp_model_reward_act, kemp_model, kemp_model_reward_exp_conditioned
from math import atan, sin, cos, pi
from random import shuffle
from matplotlib.path import Path
from matplotlib.patches import PathPatch, Circle, Ellipse, Rectangle, BoxStyle, Wedge, Arrow
from color import hsl_to_rgb

# bright colors
# [red, blue, pink, purple, orange, yellow]
COLOR = [(0, 100), (240, 100), (330, 100), (280, 100), (22, 100), (55, 100)]

# background color in hsl
# background = (84, 48, 78)
background = '#A0C567'
bark = '#614126'

FISHERMAN_SIZE = .05

def draw_image(strengths, trees, color, dirname="stimuli/", **attr):
    
    # set size of figure
    # fig = plt.figure(figsize=(1, 5))
    # fig.set_size_inches(18, 10, forward=True)

    # center_x = .9
    # center_y = .5

    # width = 1.8
    # height = 1.
    fig = plt.figure()
    fig.set_size_inches(18, 11, forward=True)


    center_x = .9
    center_y = .55

    width = 1.8
    act_height = 1.1
    height = 1.0

    # create axis
    ax = plt.axes()
    plt.axis([0, width, 0, act_height])

    # set background color
    ax.patch.set_facecolor(background) 


    num_fishermen = len(strengths)


    # add road
    road_len = act_height/2.  
    road_width = .1
    road = plt.Rectangle((width/2 - road_width/2, act_height-road_len), .1, road_len, angle=0.0, lw=2, ec='.1', facecolor='.2')
    ax.add_artist(road)

    # add road lines
    line_width = .01
    line_len = road_len/11
    for i in range(0,13):
        line = plt.Rectangle((width/2 - line_width/2, act_height-road_len + i*1.9*line_len + .6*line_len), line_width, line_len, angle=0.0, facecolor='yellow', alpha=.3)
        ax.add_artist(line)

    # add trees
    tree_offset = .07
    tree_spacing = (road_len-tree_offset)/(trees+1)

    for tree in range(trees):
        x = .91
        y = act_height - tree_offset - tree*tree_spacing

        add_tree(ax, x, y-.01)
        add_leaves(ax, x, y, tree+1)

    # add number of trees
    x = center_x - road_width/2.
    y = act_height - road_len - road_width*1.2

    box = Rectangle((x, y), road_width, road_width, joinstyle='round', lw=2, ec='.2', facecolor='.99')
    ax.add_artist(box)
    ax.text(x + road_width/2., y+road_width/2., trees, size=20, color='.2', va="center", ha="center")



    # add ponds
    pond_offset = .13
    pond_size = (width/3) * (1./5.)

    radius_y = width/3.*.9
    radius_x = width/3.*.9

    curr_angle = 0
    angle_shift = 180./(num_fishermen-1)

    for pond in range(num_fishermen):
        x = center_x - radius_x*cos(curr_angle*pi/180.) 
        y = 1 - radius_y*sin(curr_angle*pi/180.) - .25

        curr_angle = curr_angle + angle_shift

        add_pond(ax, pond_size, num_fishermen, x, y)

    fishermen_size = FISHERMAN_SIZE
    curr_angle = 0


    # add homes
    for i in range(num_fishermen):

        x = center_x - radius_x*cos(curr_angle*pi/180.) + 1.3*pond_size
        y = 1 - radius_y*sin(curr_angle*pi/180.) - .25 - pond_size
        if curr_angle <= 90:
            x = center_x - radius_x*cos(curr_angle*pi/180.) - 1.3*pond_size


        fishermen_spacing = (width-.2)/num_fishermen
        add_home(ax, fishermen_size*1.5, curr_angle, color[i], x, y)
        add_strength(ax, strengths[i], fishermen_size, color[i], x, y)

        curr_angle = curr_angle + angle_shift
    
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    

    # add fishermen
    if 'starting' in attr:
        choices = [2 for f in range(num_fishermen)]
        add_fishermen(ax, num_fishermen, choices, fishermen_size, pond_size, center_x, center_y, radius_x, radius_y, color, width, height)
        
    elif 'outcome' in attr:
        choices = attr['outcome']
        add_fishermen(ax, num_fishermen, choices, fishermen_size, pond_size, center_x, center_y, radius_x, radius_y, color, width, height)
        
    if 'file' in attr:
        fig.savefig(attr['file'], bbox_inches='tight', dpi=100)
    elif 'starting' in attr:
        fig.savefig('start.png', bbox_inches='tight', dpi=100)
    elif 'outcome' in attr:
        fig.savefig('outcome.png', bbox_inches='tight', dpi=100)


    plt.close('all')


    return 

def add_tree(ax, x, y):

    trunk = plt.Rectangle((x, y), .017, .08, angle=100., lw=2.3,  ec='k', facecolor=bark)
    ax.add_artist(trunk)

    return 

def add_leaves(ax, x, y, tree):

    radius = .023

    leaves = plt.Circle((x+.03, y+.006), radius=radius+.0025, facecolor='green', zorder=tree+5)
    ax.add_artist(leaves)

    leaves = plt.Circle((x+.025, y+.03), radius=radius, lw=2, ec='k', facecolor='green', zorder=tree+4)
    ax.add_artist(leaves)

    leaves = plt.Circle((x+.03, y-.01), radius=radius+.002, lw=2, ec='k', facecolor='green', zorder=2)
    ax.add_artist(leaves)

    leaves = plt.Circle((x+.015, y+.01), radius=radius, lw=2, ec='k', facecolor='green', zorder=3)
    ax.add_artist(leaves)

    leaves = plt.Circle((x+.04, y+.01), radius=radius+.004, lw=2, ec='k', facecolor='green', zorder=3)
    ax.add_artist(leaves)

    return

def add_pond(ax, radius, num, x, y):

    pond = plt.Circle((x, y), radius=radius, lw=3,ec=hsl_to_rgb(200, 60, 60), facecolor='none', zorder=10)
    ax.add_artist(pond)

    delta = 0.025
    x = np.arange(x-.5, x+.5, delta)
    y = np.arange(y-.5, y+.5, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
    Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
    Z = Z2 - Z1  # difference of Gaussians

    # add gradient for each pond
    if num == 2:
        im = plt.imshow(Z, interpolation='bilinear', cmap=cm.Blues, extent=[0, .9, .5, 1], aspect='auto', origin='upper', clip_path=pond, clip_on=True)
        im = plt.imshow(Z, interpolation='bilinear', cmap=cm.Blues, extent=[.9, 1.8, .37, .9], aspect='auto', origin='upper', clip_path=pond, clip_on=True)
        im = plt.imshow(Z, interpolation='bilinear', cmap=cm.Blues, extent=[.5, 1.3, 0, .85], aspect='auto', origin='upper', clip_path=pond, clip_on=True)
    elif num == 3:
        im = plt.imshow(Z, interpolation='bilinear', cmap=cm.Blues, extent=[0, .9, .5, 1], aspect='auto', origin='upper', clip_path=pond, clip_on=True)
        im = plt.imshow(Z, interpolation='bilinear', cmap=cm.Blues, extent=[.9, 1.8, .37, .9], aspect='auto', origin='upper', clip_path=pond, clip_on=True)
        im = plt.imshow(Z, interpolation='bilinear', cmap=cm.Blues, extent=[.5, 1.3, 0, .85], aspect='auto', origin='upper', clip_path=pond, clip_on=True)
    elif num == 4:
        im = plt.imshow(Z, interpolation='bilinear', cmap=cm.Blues, extent=[.2, .9, .1, .67], aspect='auto', origin='upper', clip_path=pond, clip_on=True)
        im = plt.imshow(Z, interpolation='bilinear', cmap=cm.Blues, extent=[.9, 1.8, .1, .67], aspect='auto', origin='upper', clip_path=pond, clip_on=True)
        im = plt.imshow(Z, interpolation='bilinear', cmap=cm.Blues, extent=[0, .9, .5, 1], aspect='auto', origin='upper', clip_path=pond, clip_on=True)
        im = plt.imshow(Z, interpolation='bilinear', cmap=cm.Blues, extent=[.9, 1.8, .4, .9], aspect='auto', origin='upper', clip_path=pond, clip_on=True)



    im.set_clip_path(pond)

    return

def add_fishermen(ax, num_fishermen, choices, fishermen_size, pond_size, center_x, center_y, radius_x, radius_y, color, width, height):
    
    curr_angle = 0
    angle_shift = 180./(num_fishermen-1)

    for i in range(num_fishermen):

        y = 1 - radius_y*sin(curr_angle*pi/180.) - .25

        if curr_angle <= 90:
            x = center_x - radius_x*cos(curr_angle*pi/180.) - .3*pond_size
            if choices[i] == 2:
                add_fisherman(ax, fishermen_size, color[i], x - 3*fishermen_size, y - fishermen_size)
            elif choices[i] == 0:
                add_fisherman(ax, fishermen_size, color[i], x, y)
                add_boat(ax, fishermen_size, curr_angle, x, y)
        else:
            x = center_x - radius_x*cos(curr_angle*pi/180.) + .3*pond_size
            if choices[i] == 2:
                add_fisherman(ax, fishermen_size, color[i], x + 3*fishermen_size, y - fishermen_size)
            elif choices[i] == 0:
                add_fisherman(ax, fishermen_size, color[i], x, y)
                add_boat(ax, fishermen_size, curr_angle, x, y)

        if choices[i] == 1:
            if curr_angle <= 90:
                x = center_x - 2.7*fishermen_size
                y = height - 2*pond_size*(i) - 2*fishermen_size
                add_fisherman(ax, fishermen_size, color[i], x, height - 2*pond_size*(i) - 2*fishermen_size)
                add_axe(ax, fishermen_size, curr_angle, x, y)
            else:
                x = center_x + 2.7*fishermen_size
                y = center_y + 2*pond_size*(i%2) + 2*fishermen_size
                add_fisherman(ax, fishermen_size, color[i], x, y)
                add_axe(ax, fishermen_size, curr_angle, x, y)


        fishermen_spacing = (width-.2)/num_fishermen
        x = .1 +.145 + fishermen_size + i*fishermen_spacing

        curr_angle = curr_angle + angle_shift

    return

def add_fisherman(ax, size, color, x, y):

    body = plt.Circle((x, y), radius=size, lw=2, ec=hsl_to_rgb(color[0], color[1], 30), facecolor=hsl_to_rgb(color[0], color[1], 50), zorder=9)
    ax.add_artist(body)

    # add left eye
    eye = Ellipse((x-size*cos(65*pi/180.), y+size*sin(65*pi/180.) - size*.5), angle=359, width=.035, height=.05, lw=1.5, ec='k', facecolor='white', zorder=9)
    ax.add_artist(eye)

    # add right eye
    eye = Ellipse((x+size*cos(65*pi/180.), y+size*sin(65*pi/180.) - size*.5), angle=1, width=.035, height=.05, lw=1.5, ec='k', facecolor='white', zorder=9)
    ax.add_artist(eye)
   
    # add left pupil
    eye = Ellipse((x-size*cos(65*pi/180.), y+size*sin(65*pi/180.) - size*.6), width=.02, height=.02, facecolor='k', zorder=9)
    ax.add_artist(eye)

    # add right pupil
    eye = Ellipse((x+size*cos(65*pi/180.), y+size*sin(65*pi/180.) - size*.6), width=.02, height=.02, facecolor='k', zorder=9)
    ax.add_artist(eye)

    return

def add_strength(ax, strength, size, color, x, y):

    width = .27
    height = .05

    # add dot box
    box = Rectangle((x - size - width/3., y - size - height/3.), width, height, joinstyle='round', lw=2, ec=hsl_to_rgb(color[0], color[1], 50), facecolor=hsl_to_rgb(color[0], color[1], 100))
    ax.add_artist(box)
    
    # add number box
    box = Rectangle((x - size - width/3., y - size - height/3.), height, height, joinstyle='round', lw=2, ec=hsl_to_rgb(color[0], color[1], 50), facecolor=hsl_to_rgb(color[0], color[1], 100))
    ax.add_artist(box)

    # add number
    ax.text(x - size - width/3. + width/11., y - size + height/15., str(strength), size=20, color=hsl_to_rgb(color[0], color[1], 30), va="center", ha="center")

    spacing = (width-height)/11.2

    # add dots
    for i in range(1, strength+1):
        if i > 5:
            dot = plt.Circle((x - size - width/3. + height + (i+.3)*spacing, y - size - height/3. + height/2.), radius=.008, facecolor=hsl_to_rgb(color[0], color[1], 40))
            ax.add_artist(dot)
        # after five dots include a space
        else:
            dot = plt.Circle((x - size - width/3. + height + i*spacing, y - size - height/3. + height/2.), radius=.008, facecolor=hsl_to_rgb(color[0], color[1], 40))
            ax.add_artist(dot)

    # ax.annotate(str(strength), xy=(x - size - width/3., y - size - height/3.), xytext=(x - size - width/3. + width/30., y - size - height/3. + height/3.))

    return

def add_boat(ax, radius, angle, x, y):
    # create boat from polygon
    if angle <= 90:
        verts = [
        (x-.9*radius, y-1.2*radius), # left, bottom
        (x-1.2*radius, y-radius/2), # left, top
        (x+1.2*radius+radius/3.2, y-radius/2), # right, top
        (x+.9*radius+radius/3.2, y-1.2*radius), # right, bottom
        (0., 0.), # ignored
        ]
    else:
        verts = [
        (x-.9*radius-radius/3.2, y-1.2*radius), # left, bottom
        (x-1.2*radius-radius/3.2, y-radius/2), # left, top
        (x+1.2*radius, y-radius/2.), # right, top
        (x+.9*radius, y-1.2*radius), # right, bottom
        (0., 0.), # ignored
        ]

    codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

    path = Path(verts, codes)
    boat = PathPatch(path, lw=2, ec='.2', facecolor='.3', zorder=10)
    ax.add_artist(boat)

    # create fishing rod
    if angle <= 90:
        rod = Wedge((x+1.8*radius, y+.7*radius), radius*1.3, 228, 230, width=None, color='k')
        string = Wedge((x+1.8*radius, y+.7*radius), .9*radius, 270, 270, width=None, color='.9')
    else:
        rod = Wedge((x-1.7*radius, y+.7*radius), radius*1.3, 306, 308, width=None, color='k')
        string = Wedge((x-1.7*radius, y+.7*radius), .9*radius, 270, 270, width=None, color='.9')

    ax.add_artist(rod)
    ax.add_artist(string)
    return

def add_axe(ax, radius, angle, x, y):

    if angle <= 90:
        head = Wedge((x-.85*radius, y+.63*radius), radius*1.1, 195, 230, width=radius*.4, lw=1, ec='.1', color='.3')
        handle =  Rectangle((x - radius, y-.5*radius), radius*.15, 1.1*radius, angle=30,  lw=1, ec=hsl_to_rgb(40, 100, 15), facecolor=hsl_to_rgb(40, 100, 35))
    else:
        head = Wedge((x+.8*radius, y+.5*radius), radius*1.1, 315, 350, width=radius*.4, lw=1, ec='.1', color='.3')
        handle =  Rectangle((x + .85*radius , y-.5*radius), radius*.15, 1.1*radius,  angle=330, lw=1, ec=hsl_to_rgb(40, 100, 15), facecolor=hsl_to_rgb(40, 100, 35))
    
    ax.add_artist(head)
    ax.add_artist(handle)

    return

def add_home(ax, size, angle, color, x, y):

    width = size*1.8
    height = size*1.3

    if angle <= 90:
        body = Rectangle((x - size - width*.7, y - size + 1.3*height), width, height, lw=1.5, ec=hsl_to_rgb(color[0], color[1], 70), facecolor=hsl_to_rgb(color[0], color[1], 80))
        roof = ax.arrow(x - size - width*.2, y - size + 2.3*height, 0, 0, head_width=size*2.5, head_length=size*.8, length_includes_head=False, width=width, lw=1, ec=hsl_to_rgb(color[0], color[1], 10), facecolor=hsl_to_rgb(color[0], color[1], 30))
        door = Rectangle((x - size - width*.5, y - size + 1.3*height), width/3., size, lw=1.5, ec=hsl_to_rgb(color[0], color[1], 20), facecolor=hsl_to_rgb(color[0], color[1], 30))
    else: 
        body = Rectangle((x - size + width*.75, y - size + 1.3*height), width, height, lw=1.5, ec=hsl_to_rgb(color[0], color[1], 70), facecolor=hsl_to_rgb(color[0], color[1], 80))
        roof = ax.arrow(x - size + width*1.25, y - size + 2.3*height, 0, 0, head_width=size*2.5, head_length=size*.8, length_includes_head=False,  width=width, lw=1, ec=hsl_to_rgb(color[0], color[1], 10), facecolor=hsl_to_rgb(color[0], color[1], 30))
        door = Rectangle((x - size + width*1.25, y - size + 1.3*height), width/3., size, lw=1.5, ec=hsl_to_rgb(color[0], color[1], 20), facecolor=hsl_to_rgb(color[0], color[1], 30))


    ax.add_artist(body)
    ax.add_artist(roof)
    ax.add_artist(door)
    return

def add_truck(ax, x, y):

    box = Rectangle((x - size - width/3., y - size - height/3.), height, height, joinstyle='round', lw=2, ec='.2', facecolor='.9')
    ax.add_artist(box)

    return

if __name__ == '__main__':
    strengths = (1, 2, 1)
    choices = (1, 1, 1)

    shuffle(COLOR)
    color = [c for i, c in enumerate(COLOR) if i < len(choices)]


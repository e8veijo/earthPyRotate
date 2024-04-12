# ascii_game calc flat earth map to round

import time
import os
import math

SPINS           = 10        # Number of planet spins in PERCENT 10 is one spinn
HORIZONTAL      = True      # rotate direction True = normal, False alien
x_cnt           = 0         # Horizontal counter
y_cnt           = 0         # Vertical counter
l_cnt           = 0         # lap counter 100 is one lap
earth_active    = True      # loop start value
circ_sym        = '0'       # Earth delimiter
fill_sym        = 'å'       # Ocean fill symbol to match map format, normally this will be SPACE
map_lines       = []
circ_line_lengths = []

file = open('lines2.txt', 'r') # selfie2.txt jorden4.txt eye2.txt world2.txt lines2.txt
map_lines = file.readlines()

if not map_lines:
    print("Input file is empty")
    sys.exit()

# Strip all newline-symbols
for i in range(0, len(map_lines)):
    map_lines[i] = map_lines[i].strip('\n')

x_len = len( map_lines[0] )
y_len = len( map_lines )
print("X length: " + str(x_len) )
print("Y length: " + str(y_len) )

y_cent  = int( y_len / 2 )
for i in range(0, y_cent): # calculate unity circle lengths forr each line(y_cent)
    x_width = math.sqrt( 1 - ( 1 - (i/y_cent) ) ** 2 )
    circ_line_lengths.append( x_width )
    
if  y_len % 2: #if ODD number of lines duplicate the middle item
    print('ODD')
    circ_line_lengths.append( circ_line_lengths[-1] )

for data in reversed(circ_line_lengths): #and the lower half is mirror of first half
    circ_line_lengths.append(data)

if not HORIZONTAL:  # Alien rotation, then we need to copy the hidden part 
                    # from RIGHT to BELOW with mirror and upside down
    t_map = []
    for line in reversed(map_lines):
        t_str = line[::-1]  # Mirror operation
        t_map.append( t_str )

    for t in t_map:
        map_lines.append(t)

while earth_active: # do the rotate
    #os.system('clear')
    if HORIZONTAL: # Normal rotation
        for i in range(0, y_len): # First we rotate the 2D map
            map_lines[i] = map_lines[i][1:] + map_lines[i][1] # offset to next time
            
        if x_cnt < x_len / 10:
            x_cnt += 1
        else:   # First percent done
            l_cnt += 1
            x_cnt = 0
            
    else: # Alien rotation
        first_line = map_lines[0]
        for i in range(0, y_len): # First we rotate the 2D map
            
            if i + 1 < y_len - 1:
                map_lines[i] = map_lines[i+1]
            else: # last items should get first data
                map_lines[i] = first_line
                
        if y_cnt < y_len / 10:
            y_cnt += 1
        else:   # First percent done
            l_cnt += 1
            y_cnt = 0
            
    # recreate the print_map to NOT destroy map_lines
    print_map = []
        
    # Scale lines with delimiters and fill with data to print
    for i in range(0, y_len):
    
        # Half the map is hidden at all times, will be on the backside of the earth
        x_vis = x_len / 2
        line_length = int( x_vis * circ_line_lengths[i] )
        line_offset = int( (x_vis - line_length) / 2 )
        
        # fill the beginning of the line with SPACE's
        line_start  = ' ' * line_offset
        tmp_line    = ''
        line_end    = ''
        
        if line_length > 0:
            line_start += circ_sym # Add FIRST delimiter
            
            # use exponential offset scaling, skip the linear below
            x_circ = int( line_length / 2 )
            circ_column_lengths = []
            
            for j in range(0, x_circ): # calculate unity circle lengths for half line length
                x_step = math.sqrt( 1 - (j/x_circ)**2 )
                circ_column_lengths.append( x_step )

            for data in reversed(circ_column_lengths): #and the lower half is mirror of first half
                circ_column_lengths.append(data)
                
            column_sum = 0
            for j in range(0, len(circ_column_lengths) ):
                column_sum += circ_column_lengths[j]

            index_scale = x_vis / column_sum
            index_sum   = 0
            indexes     = []
            #print("index_scale: " + str( index_scale ) )
            
            # Calculate the indexes, beware of duplicates that needs to be replaced with fill_sym                                                                             
            for k in range(0, len(circ_column_lengths)):
                index_sum += circ_column_lengths[k] * index_scale
                indexes.append( int(index_sum) )
                #print("index calc :: " + str(i) + " " + str(int(index_sum)))
                #tmp_line +=  map_lines[i][ int(index_sum) ]
                
            for l in range(0, len(indexes) ):
                if (l-1) > 0 and (l+1) < len(indexes):
                    if indexes[l] == indexes[l+1]:
                        #print("Removed NEXT duplicate: " + str( indexes[l] ) )
                        tmp_line  += map_lines[i][ indexes[l-1] ]
                        #indexes[l] = 0
                        
                    elif indexes[l] == indexes[l-1]:
                        tmp_line += map_lines[i][ indexes[l+1] ]
                        #indexes[l] = 0
                    else:
                        tmp_line +=  map_lines[i][ indexes[l] ]
                        
                else: # Add the data to the line with the exponential offset
                    tmp_line +=  map_lines[i][ indexes[l] ]
                
            line_end = circ_sym + ' ' * line_offset # Add LAST delimiter and SPACE's
            
            if len(tmp_line) < line_length:
                tmp_line += ' '
            
        print_map.append( line_start + tmp_line + line_end )
        
    # just print the lines
    for i in range(0, len(print_map)):
        print(print_map[i])
            
    
    if l_cnt == SPINS:
        earth_active = False
        
    print("X        : " + str(x_cnt) + '/' + str(x_len) )
    print("Y        : " + str(y_cnt) + '/' + str(y_len) )
    print("SPINN    : " + str(l_cnt) + '/' + str(SPINS) )

    # input("Press Enter to continue...")
    time.sleep(0.1)
    

    
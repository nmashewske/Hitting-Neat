#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  genetic.py
#  
#  Copyright 2017 Matthew Mashewske <matthew@matthew-W65-67SJ>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


from __future__ import print_function
import sys
import os
import neat
import visualize
import mem
import joy
import time
import pyscreenshot as ImageGrab

buttonsSupers = [ '4', '2', '6', '8', '1', '3', '7', '9', '5x', '5y', 'i', 'o', 'p', 'j', 'k', 'l', 'q', 'b', 'h', 'g', 'w', 'z', 's', 't', 'y']
buttonsNoSupers = [ '4', '2', '6', '8', '1', '3', '7', '9', '5x', '5y', 'i', 'o', 'p', 'j', 'k', 'l', 'q', 'b', 'h', 'g', 'w', 'z', 's', 't', 'y']
controller = joy.createController()
print("Set up the virtual controller with Xboxdrv, then setup the game\n")
while(True):
    button = input('Enter controller button input to input it on the controller, or input x to continue\n')
    if(button == 'x'):
        break
    else:
        joy.waitPress(5, button, controller)
while(True):
    try:
        pid = int(input('What is the game\'s pid?'))
        break
    except:
        print("That is not a valid number")


def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        joy.press('5x', controller)
        joy.press('5y', controller)
        originalHealth = mem.health2(pid)
        comboStage = mem.comboStage1(pid)
        i = 1
        buttons = buttonsNoSupers
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        comboDamage = 0
        while(True):
            seconds = time.time()
            #output = net.activate( (i,) )
            output = net.activate( list(ImageGrab.grab(bbox=(0,300, 960, 850)).resize([25,25]).convert('L').getdata() ) )
            joy.pressCombination(output, controller)
            currentStage = mem.comboStage1(pid)
            currentDamage = mem.comboDamage1(pid)
            if (currentStage < comboStage) or (mem.health1(pid) < originalHealth and currentDamage < comboDamage):
                break
            else:
                comboStage = currentStage
                comboDamage = currentDamage
            if i > 6 and comboStage == 0:
                break
            i+=1
            print(time.time()-seconds)
            
        newHealth = mem.health2(pid)
        healthDifference = originalHealth-newHealth
        if(healthDifference == 0):
            genome.fitness = 0
        else:
            genome.fitness = ( .6*( (healthDifference)/(originalHealth) ) **2 + .4*( 1 - ( ( healthDifference - comboDamage ) / (healthDifference) ) ) ** 3 )

        joy.press('!', controller)
        joy.press('5x', controller)
        joy.press('5y', controller)
        


def run(config_file):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)
    
    #checkpoint = "neat-checkpoint-{0}".format(input("What checkpoint do you want to use?"))
    
    #p = neat.Checkpointer.restore_checkpoint(checkpoint)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))
    
    print('\nThe training will start in: \n')
    for i in range(5):
        print("{0}\n".format(5-i))
        time.sleep(1)
    
    
    # Run for up to 1000 generations.
    winner = p.run(eval_genomes, 10000)
    
    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))
    
    node_names = {-1:'Frame Number', 0:'Move'}
    visualize.draw_net(config, winner, True, node_names=node_names)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward')
    run(config_path)

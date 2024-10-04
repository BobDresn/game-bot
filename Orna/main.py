from findEntity import *
from getPicture import *
import pyautogui as pag
import os
import time
import mss
    
with mss.mss() as sct:
    def main():
        
        #Creates list of files to search through in desired path
        spritesFolder = os.path.join('Orna', 'Sprites')
        mobs = []
            
        #Finds each mob file (.png) in Sprites folder
        for each in os.listdir(spritesFolder):
            if each.endswith('.png'):
                mobs.append(each)
        #Cache last found mob
        lastMob = ''
        
        #Start your marks
        start_time = time.time()
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ BEGIN LOOP @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        while True:
            
            #Pulls frame from screen recording
            frame = np.array(sct.grab(sct.monitors[0]))
            frame = cv.cvtColor(frame, cv.COLOR_BGRA2BGR)
            
            #Checks frame for image
            attack = findImage('attack.png', frame, x=(frame.shape[1] / 2), y=(frame.shape[0] / 3 * 2), w=(frame.shape[0] / 3), h=(frame.shape[1] / 2))
            next = findImage('continue.png', frame, x=(frame.shape[1] / 2), y=(frame.shape[0] / 3 * 2), w=(frame.shape[0] / 3), h=(frame.shape[1] / 2))
            battle = findImage('battle.png', frame, x=(frame.shape[1] / 5 * 2), y=(frame.shape[0] / 5 * 2), w=(frame.shape[0] / 5), h=(frame.shape[1] / 5 * 2))
            player = findImage('player.png', frame, x=(frame.shape[1] / 5 * 2), y=(frame.shape[0] / 3 * 2), w=(frame.shape[0] / 5), h=(frame.shape[1] / 3))
            X = findImage('X.png', frame)
            
            #Whatever attack is
            if attack is not False:
                print('Attack')
                pag.click(attack)
            #Continue
            elif next is not False:
                print('Continue')
                pag.click(next)
            #Enters battle
            elif battle is not False:
                print('Battle')
                pag.click(battle)
                pag.click(X)
            #If player is found, searches for mobs
            elif player is not False:
                pag.moveTo(findImage('items.png', frame, x=(frame.shape[1] / 5 * 2), y=(frame.shape[0] / 3 * 2), w=(frame.shape[0] / 5), h=(frame.shape[1] / 3)))
                pag.mouseDown()
                time.sleep(0.5)
                pag.mouseUp()
                for each in mobs:
                    #Searches for each mob in the list
                    #Passes whole file path
                    mob = findImage(os.path.join(spritesFolder, each), frame, x=(frame.shape[1] / 5), y=(frame.shape[0] / 3), w=(frame.shape[0] / 5 * 3), h=(frame.shape[1] / 3))
                    if mob is not False:
                        print(f'{each}')
                        pag.click(mob)
                        lastMob = each #Sets found mob
                        
                        #Removes found mob from list and appends, stops repeat attempts
                        #Failsafe of lost fight to not reenter
                        mobs.remove(each) 
                        mobs.append(each)
                        break
            elif X is not False:
                pag.click(X)
            else:
                continue
            time.sleep(0.1)
            #Checks if time is up, counted in seconds
            if time.time() - start_time > 3600:
                break
            
            
        
if __name__ == '__main__':
    main()
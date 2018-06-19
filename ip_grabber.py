import socket

restart = True



def enter_url():
    URL_input = input("Enter URL to Scan: ")
    print(socket.gethostbyname(URL_input))

def intro():
    print("""
                                                                                                    
                                                                                                    
                                     `-::/++oooooo++//:-`                                           
                                .:+syyyyhhhhhhhhhhhhhhyyyys+:.                                      
                            `-+syhhhhhhhhhhhhhhhhhhhhhhhhhhhyys/.                                   
                          `/syhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhys:`                                
                        `/yhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhs/`                              
                       :shhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhs/`                            
                     `+yhhhhhhhhhhhhhhhhhyyyyyssyyyhhhhhhhhhhhhhhhhhhhyo:`                          
                    `ohhhhhhhhhhhhhhhyyysooo++//::::+syhhhhhhhhhhhhhhhhhs/.                         
                    +hhhhhhhhhhhhhhyyssssooo+/-``    `-+yhhhhhhhhhhhhhhhhs+.                        
                   :hhhhhhhhhhhhyhyysssssso/.           -shhhhhhhhhhhhhhhho+`                       
                   shhhhhhhhhhhhhyyyyyssso.              .shhhhhhhhhhhhhhhyo/                       
                  .hhhhhhhhhhhhhyyyyyyyss.                :hhhhhhhhhhhhhhhyoo                       
                  :yyhhhhhhhhhhhyyyyyyys-                 .hhhhhhhhhhhhhhhhoo`                      
                  `--://+oosssyssoooooo/                  -hhhhhhhhhhhhhhhy/:                       
                            ````````                     `ohhhhhhhhhhhhhhhs-.                       
                                                        `+hhhhhhhhhhhhhhyy/-`                       
                                                      `:shhhhhhhhhhhhhhhyo-`                        
                                                    `:syhhhhhhhhhhhhhyyyo.`                         
                                                  ./shhhhhhhhhhhhhhyyyy/`                           
                                                -+yyhyhhhhhhhhhhhyyyyo.                             
                                             `:ohhhyyyyyyyyyyhyyyyyo-                               
                                           `:shhhhyyyyyyyyyyyyyyyo-                                 
                                          -shyyyyyyyyyyyhyyyyyy+.                                   
                                        `+yyyyyyyyyyyyyyyyyys/`                                     
                                       `oyyyyyyyyyyyyyyyyyo-                                        
                                       +yyyyyyyyyyyyyyyy+-                                          
                                      `yyyyyyyyyyyyyyy+/+`                                          
                                      :yyyyyyyyyyyyys++o+                                           
                                      +yyyyyyyyyyyyyoooo/                                           
                                      oyyyyyyyyyyyysooo:`                                           
                                      +yyyyyyyyyyyyso:`                                             
                                      -++oosyhhhhhyyyo++-                                           
                                         `/shhhhhhhhhhys/                                           
                                       ./shhhdddddddhyso:                                           
                                      :yhhhhhhdddddyssoo:                                           
                                      /hhhhhhhhhhhhsssso:                                           
                                      :hhhhhhhhhhhhsssss/                                           
                                      :hhhhhhhhhhhhssssy/.```                                       
                                   ```/hhhhhhhhhhhhyyyyo/-..``                                      
                                  ``../hhhhhhhhhhhhyyy+:--..```                                     
                                  ``.-/ddddddddddddys/:--..```                                      
                                   ``.-/+ossyyhhhhho:--..```                                        
                                     ```....-------.````                                            
                                           ``````                                                   
""")

while True:
    intro()
    enter_url()

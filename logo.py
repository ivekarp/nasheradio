#color for terminal
from termcolor import colored

#Logo for nashe.py
logo = """                                                                                                                           
                ':cc;.     ':cc;.       ';:cc:'        .,,,,'.    .,:c:,.    ':cc:.  .;:ccccccc:::;,.                   
               .OWWWKl.   ,OWWWXc      ;0WWWWW0;      .kWWWWKc   .lKWWW0;   .xNWWWx..cKWWWWWWWWWWWWXl.                  
               .OMMMXo.   :KMMMNl     .dNMMMMMWx.     .OMMMMXl.  .oNMMMXc   'kWMMMk..cKMMMMWNNNNXXX0:                   
               'OMMMNd.  .cKMMMNc     ;KMMMMMMMKc     .OMMMMXl.  .dWMMMNc   'kWMMWk..cKMMMNd,''''''..                   
               '0MMMNk'  .oXMMMNc    .dNMMMMMMMWk.    .OMMMMXl.  .dWMMMNc   'kWMMWk..cKMMMNc                            
               '0MMMWN0OOOXWMMMNc    :KWMMNNWMMMXc.   .OMMMMXl.  .dWMMMNl   'kWMMWk..cKMMMWx:;;,,'.                     
               '0MMMMMMMMMMMMMMNc   .xWMMWko0WMMWO'   'OMMMMXo.  .dWMMMNl   'kWMMWk..cXMMMMWWWWWWKl.                    
               '0MMMWNKKKKXWMMMNc   :0MMMNl.lXMMMXc.  'OMMMMXo.  .xWMMMNl   'kWMMWk..cKMMMMWNNNXX0c.                    
               '0MMMNx;..'oXMMMNc  .xWMMWKc.:KMMMWO'  'OMMMMNo.  .xWMMMNl   ,OWMMWx..cKMMMWx;,,''..                     
               '0MMMNd.   :KMMMNc  ;0MMMMWNXXWMMMMXc  'OMMMMNo.  .xWMMMNl   ,OWMMWx..cKMMMNc                            
               '0MMMNd.   :KMMMNc .dNMMMMMMMMMMMMMWk' .OMMMMNd.  .xWMMMWo. .:0WMMWx..cXMMMNl.                           
               '0MMMXo.   :0MMMNc ,0MMMN0kxxkkKWMMMXc .OMMMMWKkxxkXMMMMWKxxk0NMMMWx..cKMMMWKxxxxxdddc.                  
               .OWMMXo.   ;0MMMX:.lXMMM0;    .;OWMMWx.'OMMMMMMMMMMMMMMMMMMMMMMMMMWx..cKMMMMMMMMMMMMMXc                  
               .cOK0x,    .o00Od..ck0Kk:.      ;xO00d..ckkkOOOOOOOOOOOOOOOOOOOOOkx;  ,dOOO000000000Od'                  
                 ...        ...    ....          ...       .....................       .............                    
                                                                                                                        
               .lxdddoll;.   .:ooo:.      ,odddddddd:. .:ddo;.  ,odo;   ':lddol;.                                       
               ,0MMNK0NMNk. .lXMMMXl.     lWMWX0KNMWk. 'kWWWk'.oKWMMx.'dXWNK0KNNKo.                                     
               ,0MMXkxKMW0,.cXWK0XWK:     oWMXc.;OWWk' .kWMWKdkNMMMMx;xNMXo'.'dNMNl   .;loddo,                          
               ,0MMWXK0Od;.:KWNOxKWW0;   .kWWO' 'OWWO' .kWWMWWWXKNMMx;kWM0;  .cXMWo  ,kNWWWXk:                          
               '0MMKc..   ,OWWNXXNWMWk' ,xNMWKdcdKWMXl.'kWMMMNk;:KMMx'cKWW0oco0WW0;  'odoc;'.                           
               'ONXd.    .oKXOc,,;o0XKc'dNMWNNXXXNNWM0c,dXXKkc. .xKKo. ,ok0KKKKOl'     'c;.                             
                .'..      .''.     .''..xXNk;'''',cON0:..''..    ....    ...'...      .dKd.                             
                                        .;;.       .;'.                               cKk'                              
                                                                                     .x0c.                              
                                                                                     :0x.                               
                                                                                    .xKl                                
                                                           .....',;;:ccccc;.        ;OO,                                
                                            ...',;;:clodxkkO0KXXXNNNNNXX0Od;.      .oKo.                                
                                ...',;cloxkOO0KXXNNNNXXKK00OkxdoxKN0o;''..         .kKc                                 
                            .coxO0XNNNNNXXXKOkxdolc:;,'....     .c0k'              .xk,                                 
                            lXWNK0kOXXx:'....                    'kk'              .,;.      ....                       
                            .;;,.. .x0:                          .xk:...'',,;;:ccllodxxxxxkkkOOOOo.                     
                                   .xO;              ...'',;:cloxOXNXXXXXXXNNNNNNWWWWWWWWNNNNNWMWk.                     
                                   .:l'.....';:clodxkO0KXNNWWMWWNNNXXKKK00Okxdollc:;;;,,,,'''cKW0;                      
                           ...',;ccldxkO0KXNNNWWWWWWWNNK0Okxolc:;,,''......                 .dX0:                       
                       .ok00KXXNWWMMMMMMWNXK0Okxdoc:;,'...........,;;;;clol,  .;cooc,.     .oX0:                        
                       ,ONMWWNNXXK0kxoloddolc::;::cclloooodddxxxkOXWXkxxOXXl.,OX0dloxx:   .lX0:                         
                        'ldxkxl:;,'.  .c0XXK0OOkkxxxddolcc:;,,'..;OXo. .:K0,.lKx,   ,kx. .lK0:                          
                    .;. .,d0K0kxxkkd; .xXkc;''....               'kO,   oKd..xk,  .,dk: .cKKc                           
                    :Oo;oKKkl:,'',cxO:'x0c                       ,kl.  ,kO; .o0xodxxl' .c0K:                            
                    :0K0XO;       .lOl.l0c              ........':dl,,:dKd.  .';;,..   :00:                             
                    '0WNX0o;,,,,:ldxl. ,OOlccclllloooodddddddooolllcc:;;,.            :00:                              
                    .kNdcdkkxxddoc,.   .lOOkkxxdoolc:;,'.......                      :00:                               
                    .dXl   ...           ..                    .........'''.        :O0:                                
                    .lKo.                   ...',,;:cllodddxxkOO00KKKKKKXKOo'      ;OO;                                 
                     ;0x.      ....',:cloxkO00KXNNWWMMWWWNNNXXKKKKKK00Oxo:'.      ;OO;                                  
                     .kk'  ,loxk0KXNNNNNNNXK00OOkkxxdddxxxxkkkkkOO00KKKKO:       ;OO;                                   
                     .dO; .dWMWWXK0OkxoollcclloddxxkOO0KXXXXXXKK0Okxdol:,.      ,kk;                                    
                      lOl. .:c:;;cdxxxkO0KXNNNNNXXXKK0kxddolc:::::::ccllc,.    ,kk,                                     
                      ;Ox.      .lNMMMMWNXKK00OkkxxxxxxxkkkOO0KKK00OOkxdc,.   'xk,                                      
                      .dO,      .c0WMWWWNXKK0KXXXXXXKK0Okkxdolc:;,'..        'dk;                                       
                       l0l.   .l0XNWWWNNX0Okdolc:;,'....                    .dk;                                        
                       ;Ox.   .oOkdlc;,'...                                .lx;                                         
                       .oO:    .........'',,;;;;;:::::::::cccc:::cc::::::ccd0k;.                                        
                        ;OOdoodxkkO000OOOOOOOOOkkkkkkxxxxxxddddddddoooooodkkxlc:.                                       
                        .;dkkkxdolc::;,,''.........                        .                                            
"""
developer = """
                                                                           by Ive Karp
"""

#Functions
#-------------------------------------------------
def print_logo():
	print(colored(logo,'green'))
	print(colored(developer,'green',attrs=['blink','bold']))
	
def info():
	info = """
	                       Logo maded with https://www.ascii-art-generator.org/
	"""
	print(colored(info,'green',attrs=['bold']))

#-------------------------------------------------

if __name__ == '__main__':
	print_logo()
	info()


#CRIA OS BACKUPs                                                                                        
def backupfull():                                                                                       
    disk        = '/dev/sdb'        #Define onde está a partição que será usada para guardar o backup   
    horaInicio  = time.strftime('%H:%M:%S')                                                             
    pathlog     = geralog()                                                                             
    backup      = gerabackup()                                                                          
    log         = ' >> %s' % pathlog                                                                    
    start       = inicio(horaInicio)                                                                    
                                                                                                        
    #Printa o Banner                                                                                    
    l = open(pathlog, 'w')                                                                              
    l.write(start)                                                                                      
    l.close()                                                                                           
                                                                                                        
    #Monta todos os discos que estão no FSTAB                                                           
    mount = 'mount -a'                                                                                  
    subprocess.call(mount, shell=True)                                                                  
                                                                                                        
    #RODA O BACKUP                                                                                      
    subprocess.call(backup + log, shell=True)                                                           
                                                                                                        
    #Printa o final e relatório                                                                         
    diaInicio   = (time.strftime("%d-%m-%Y"))                                                           
    final       = termino(diaInicio, horaInicio, backup, pathlog)                                       
    r           = open(pathlog, 'w')                                                                    
    r.write(final)                                                                                      
    r.close()                                                                                           
                                                                                                        
    #Descomente essa função para desmontar a partição que será utilizada para armazenar o backup        
    desmonta_hd(disk)                      
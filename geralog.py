#CONSTROI OS LOGS DO SISTEMA - Aqui selecionamos o nome do backup e o arquivo de logs que iremos criar.    
def geralog():                                                                                             
    date = (time.strftime("%Y-%m-%d"))              #                                                      
    logfile     = '%s-backup-full.txt' % date       # Cria o arquivo de Log                                
    pathlog     = '/var/log/backup/backup-full/%s' % logfile    # Arquivo de log                           
                                                                                                           
    return pathlog              
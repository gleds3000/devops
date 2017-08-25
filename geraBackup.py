#CONSTROI O ARQUIVO E PATH DE BACKUP E RETORNA                                                       
def gerabackup():                                                                                    
    date = (time.strftime("%Y-%m-%d"))                                                               
    backupfile  = '%s-backup-full.tar.gz' % date    # Cria o nome do arquivo de Backup               
    pathdestino = '/mnt/hdbackup/%s' % backupfile   # Destino onde será gravado o Backup             
    pathorigem  = '/mnt/storage/'                   # pasta que será 'backupeada'  passar como nome do arquivo                   
    backup      = 'tar cvf %s %s' % (pathdestino, pathorigem) # Comando de execução                  
                                                                                                     
    return backup 
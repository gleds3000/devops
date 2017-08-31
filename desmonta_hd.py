#ESSA FUNÇÃO DESMONTA O HD DE BACKUP POR SEGURANÇA.
#DESCOMENTE A LINHA desmonta_hd() DENTRO DE backupfull() PARA UTILIZÁ-LA
def desmonta_hd(disk):
    try:
        umount = 'umount %s' % disk
        subprocess.call(umount, shell=True)
        return True
    except:
        return False
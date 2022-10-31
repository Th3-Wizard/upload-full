from pyobigram.utils import sizeof_fmt,nice_time
import datetime
import time
import os
from os import walk

def dashboard():
    start_msg = '⚡Bot Creado por el @EL_Wizard⚡\n'
    return start_msg

def text_progres(index,max,size=21,step_size=5):
    try:
        if max<1:
            max += 1
        porcent = index / max
        porcent *= 100
        porcent = round(porcent)
        make_text = ''
        index_make = 1
        make_text += '[\n'
        while(index_make<size):
            if porcent >= index_make * step_size:make_text+='✭'
            else:make_text+='✩'
            index_make+=1
        make_text += '\n]'
        return make_text
    except Exception as ex:
            return ''

def porcent(index,max):
    porcent = index / max
    porcent *= 100
    porcent = round(porcent)
    return porcent

def createDownloading(filename,totalBits,currentBits,speed,time,tid=''):
     msg = 'Descargando Archivo ❤️🔸🔸🔸\n\n'
    msg += '📄Nombre: ' + filename + '\n'
    msg += text_progres(currentBits, totalBits) + '\n'
    msg += 'ඞ Porcentaje: ' + str(porcent(currentBits, totalBits)) + '%\n\n'
    msg += 'ඞ Total: ' + sizeof_fmt(totalBits) + '\n\n'
    msg += 'ඞ Descargado: ' + sizeof_fmt(currentBits) + '\n\n'
    msg += 'ඞ Velocidad: ' + sizeof_fmt(speed) + '/s\n\n'
    msg += 'ඞ Tiempo de Descarga: ' + str(datetime.timedelta(seconds=int(time))) + 's\n\n'
    return msg
def createUploading(filename,totalBits,currentBits,speed,time,originalname=''):
        msg = 'Subiendo A La Nube 🧡🔸🔸🔸\n\n'
    msg += 'ඞ Nombre: ' + filename + '\n'
    if originalname != '':
        msg = str(msg).replace(filename, originalname)
        msg += 'ඞ Nombre: ' + str(filename) + '\n'
    msg += text_progres(currentBits, totalBits) + '\n'
    msg += 'ඞ Porcentaje: ' + str(porcent(currentBits, totalBits)) + '%\n\n'
    msg += 'ඞ Total: ' + sizeof_fmt(totalBits) + '\n\n'
    msg += 'ඞ Subido: ' + sizeof_fmt(currentBits) + '\n\n'
    msg += 'ඞ Velocidad: ' + sizeof_fmt(speed) + '/s\n\n'
    msg += 'ඞ Tiempo de Subida: ' + str(datetime.timedelta(seconds=int(time))) + 's\n\n'
    return msg
def createCompresing(filename,filesize,splitsize):
    msg = 'Comprimiendo 💚🔸🔸🔸\n\n'
    msg+= 'ඞ Nombre: ' + str(filename)+'\n'
    msg+= 'ඞ Tamaño Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= 'ඞ Tamaño Partes: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= 'ඞ Cantidad Partes: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'
    return msg
def createFinishUploading(filename,filesize,datacallback=None):
    msg = 'Nombre' + str(filename)+ f'\nSubido {str(sizeof_fmt(filesize))}\n'
    if datacallback:
       msg += 'datacallback: ' + datacallback
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>🔹Enlaces🔹</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            #msg+= '<a href="'+f['url']+'">🔹' + f['name'] + '🔹</a>'
            msg+= "<a href='"+url+"'>🔸"+f['name']+'🔸</a>\n'
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = '🔶Archivos ('+str(len(evfiles))+')♻️\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= '/txt_'+ str(i) + ' /del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg

def files(username, path):
    listado=os.listdir(path)
    dir, subdirs, archivos = next(walk(path))
    sms = f'Sesión: @{username}\n'
    sms += f'ඞ Archivos: {str(len(listado))}\n'
    sn = -1
    for s in subdirs:
        sn += 1
        sms +=f'\n/cdir_{sn} 💠 {s}'
    an = -1
    for a in archivos:
        an += 1
        size=(a,os.stat(os.path.join(path, a)).st_size)
        size=(size[1] / 1024 / 1024)
        sms +=f'\n◈━━━━━━━/up_{an}━━━━━━━━◈'
        sms +=f'\n/rm_{an} - {a}\n💠{str(size)[:4]}MB\n╰────────────────'
    return sms

def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = 'Sesión: @' + str(username)+'\n'
    msg+= 'ඞ User: ' + str(userdata['moodle_user'])+'\n'
    msg+= 'ඞ Pass: ' + str(userdata['moodle_password']) +'\n'
    msg+= 'ඞHost: ' + str(userdata['moodle_host'])+'\n'
    if userdata['cloudtype'] == 'moodle':
        msg+= 'ඞ RepoID: ' + str(userdata['moodle_repo_id'])+'\n'
    msg += 'ඞ CloudType: ' + str(userdata['cloudtype']) + '\n'
    if userdata['cloudtype'] == 'cloud':
        msg+= '➤ Dir: /' + str(userdata['dir'])+'\n'
    msg+= 'ඞ Zips: ' + sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'
    msgAdmin = '✔️'

    if isadmin:
        msgAdmin = '✅'
    msg+= 'ඞ Admin: ' + msgAdmin + '\n'
    proxy = '✔️'
    if userdata['proxy'] !='':
       proxy = '✅'
    msg+= 'ඞ Proxy: ' + proxy + '\n'
    shorturl = (userdata['urlshort'] == 1)
    shortener = '✔️'
    if shorturl:
       shortener = '✅'
    msg += 'ඞ ShortUrl: ' + shortener + '\n'
    autoup = '✔️'
    if userdata['autoup'] == 1:
        autoup = '✅'
    msg += 'ඞ Autoup: ' + autoup
    return msg

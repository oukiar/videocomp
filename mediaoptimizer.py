

import os
import sys

inputdir = sys.argv[1]

dirs = os.listdir(inputdir)

outdir = sys.argv[2]

print dirs

for h in dirs:
    
    files = os.listdir(os.path.join(inputdir, h) )
    
    #crear directorio en destino
    os.mkdir(os.path.join(outdir, h))
    
    for i in files:
                
        name, ext = os.path.splitext(i)
        
        if ext.upper() in (".JPG", ".PNG", ".JPEG", ".BMP", ".GIF"):
            os.system('cp "' + os.path.join(inputdir, h, str(i) ) + '" "' + os.path.join(outdir, h, str(i) ) + '"')
            continue
        
        print("Convirtiendo: " + i )
        
        outfile = "\"" + os.path.join(outdir, h, name) + ".mp4\""
        
        print("Archivo de salida: " + outfile)
        
        os.system('ffmpeg -i "' + os.path.join(inputdir, h, str(i) ) + '" -strict -2  -vcodec libx264 -b:v 700k -acodec aac ' + outfile )

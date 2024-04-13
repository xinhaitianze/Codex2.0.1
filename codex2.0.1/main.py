#coding=gbk
########################
#[xinhaitianze] 2024.4.5
########################
import os
import sys
import time
import about
import platform
from function import *
import math



#inpaaaaaa = input('enter file path: ')
inpaaaaaa = "code.codex"
with open(inpaaaaaa,'r') as file:
    code = file.read()
    #print(code)

cbl = {}
bl = {}
h = 0
by = about.by
x = ''

def jx(code):
    global h,cbl,bl,x
    for line in code.splitlines():
        line = line.rstrip(';')
        line = line.strip()
        if line.startswith('import <'):
            try:
                name = 'Lib/' + line[8:-1]
                with open(name,'r',encoding='utf-8') as name:
                    name = name.read()
                    code = name + '\n\n' + code
            except FileNotFoundError:
                print(f'line {h}')
                print(line)
                print(f'~~~~~~~~' + '^' * (len(line) - 8))
                print(f'ERROR:Unknown Module: {line[8:-1]}')
                sys.exit()
            
    for line in code.splitlines():
        h = h + 1
        line = line.rstrip(';')
        line = line.strip()
        if line in x:
            pass
        elif line.startswith('cprint('):
            l = line[7:-1]
            try:
                if l in bl:
                    print(eval(f"cbl['{l}']"))
                else:
                    print(eval(l))
            except NameError:
                print(f'line {h}')
                print(line)
                print('^' * len(line))
                print(f"ERROR: name '{l}' is not defined.")
                break
            except KeyError:
                print(f'line {h}')
                print(line)
                print('^' * len(line))
                print(f"ERROR: name '{l}' is not defined.")
                break
        elif line.startswith('printf('):
            l = line[7:-1]
            try:
                if l in bl:
                    sys.stdout.write(eval(f"cbl['{l}']"))
                else:
                    sys.stdout.write(eval(l))
            except NameError:
                    print(f'line {h}')
                    print(line)
                    print('^' * len(line))
                    print(f"ERROR: name '{l}' is not defined.")
                    break
        elif line.startswith('!'):
            pass

        elif line in x:
            pass
        elif line.startswith('}'):
            pass
        elif line.startswith('cbl '):
            try:
                    line1 = line[4:]
                    line1 = line1.split('=')
                    name = line1[0]
                    text = line1[1]
                    if "k{" in text:
                        import re
                        pattern = r'k\{(.*?)\}'
                        matches = re.findall(pattern, code, re.DOTALL)
                        #print(matches[0])
                        x = x + matches[0].replace('    ', '')
                        cbl[name.strip()] = matches[0].replace('    ', '').strip('')
                        bl[name.strip()] = ''
                    else:
                        cbl[name.strip()] = eval(text.strip())
                        bl[name.strip()] = ''
                #print(bl)
                #print(cbl)
            except SyntaxError:
                print(f'line {h}')
                print(line)
                print('    ' + '^' * (len(line) - 4))
                print('ERROR: Incomplete variables')
                break


        elif line.startswith('input('):
            try:    
                linen = line[6:-1]
                numbers = linen.split(',')
                text = numbers[0]
                bl1 = numbers[1]
                print(text, end="", flush=True)
                user_input = sys.stdin.readline().strip()
                cbl[bl1] = str(user_input)
                bl[bl1] = ''
            except IndexError:
                print(f'line {h}')
                print(line)
                print('^' * len(line))
                print('ERROR: The statement needs two numbers, and no characters other than numbers appear')

        elif line.startswith('int('):
            line = line[4:-1]
            l = int(eval(f"cbl['{line}']"))
            cbl[line] = l
        elif line.startswith('add('):
            try:
                lines = line[4:-1]
                nline = lines.split(',')
                num1 = int(eval(f"cbl['{nline[0]}']"))
                num2 = int(eval(f"cbl['{nline[1]}']"))
                name = nline[2]
                num3 = num1 + num2
                cbl[name] = num3
                bl[name] = ''
            except KeyError as e:
                print(f'line {h}')
                print(line)
                print('^' * len(line))
                print(f"ERROR: name {e} is not defined.")
                break
        elif line.startswith('sub('):
            try:
                lines = line[4:-1]
                nline = lines.split(',')
                num1 = int(eval(f"cbl['{nline[0]}']"))
                num2 = int(eval(f"cbl['{nline[1]}']"))
                name = nline[2]
                num3 = num1 - num2
                cbl[name] = num3
                bl[name] = ''
            except KeyError as e:
                print(f'line {h}')
                print(line)
                print('^' * len(line))
                print(f"ERROR: name {e} is not defined.")
                break
        elif line.startswith('mul('):
            try:
                lines = line[4:-1]
                nline = lines.split(',')
                num1 = int(eval(f"cbl['{nline[0]}']"))
                num2 = int(eval(f"cbl['{nline[1]}']"))
                name = nline[2]
                num3 = num1 * num2
                cbl[name] = num3
                bl[name] = ''
            except KeyError as e:
                print(f'line {h}')
                print(line)
                print('^' * len(line))
                print(f"ERROR: name {e} is not defined.")
                break
        elif line.startswith('div('):
            try:
                lines = line[4:-1]
                nline = lines.split(',')
                num1 = int(eval(f"cbl['{nline[0]}']"))
                num2 = int(eval(f"cbl['{nline[1]}']"))
                name = nline[2]
                num3 = num1 / num2
                cbl[name] = num3
                bl[name] = ''
            except KeyError as e:
                print(f'line {h}')
                print(line)
                print('^' * len(line))
                print(f"ERROR: name {e} is not defined.")
                break
            except ZeroDivisionError as e:
                print(f'line {h}')
                print(line)
                print('^' * len(line))
                print(f'ERROR: {e}')
                break

        elif line.startswith('ropen('):
            line1 = line[6:-1]
            line1 = line1.split(',')
            name = line1[0]
            bln = line1[1]
            try:
                with open(name,'r',encoding='utf-8') as file:
                    file = file.read()
                    cbl[bln.strip()] = file
                    bl[bln.strip()] = ''
            except FileNotFoundError:
                print(f'line {h}')
                print(line)
                print('^' * len(line))
                print(f'ERROR: No such file or directory: "{name}"')
                break

        elif line.startswith('wopen('):
            line = line[6:-1]
            open(line,'w',encoding='utf-8')

        elif line.startswith('sleep('):
            line = line[6:-1]
            time.sleep(eval(line))
            
        elif line.startswith('fopen('):
            line = line[6:-1].split(',')
            #print(line)
            name = line[0]
            #print(name)
            nr = line[1]
            #print(nr)
            with open(name,'w',encoding='utf-8') as file:
                file.write(eval(nr))
                file.close()
        
        elif line.startswith('aopen('):
            line = line[6:-1].split(',')
            #print(line)
            name = line[0]
            #print(name)
            nr = line[1]
            #print(nr)
            with open(name,'a',encoding='utf-8') as file:
                file.write(eval(nr))
                file.close()

        elif line.startswith('exit()'):
            sys.exit()
        
        elif line.startswith('system('):
            line = line[7:-1]
            os.system(eval(line))
            

        elif line.startswith('if('):
            line = line[3:-1].split(',')
            tj = line[0]
            bl = line[1]
            tj = eval(tj)
            if tj:
                jx(eval(f"cbl['{bl}']"))
            else:
                pass

        elif line.startswith('while('):
            line = line[6:-1].split(',')
            tj = line[0]
            bl = line[1]
            tj = eval(tj)
            if tj:
                while True:
                    jx(eval( f"cbl['{bl}']"))
            else:
                pass
            
        elif line.startswith('js('):
            try:
                t = line[3:-1].split(",")
                sc = t[0]
                blzz = t[1]
                sc = eval(sc)
                cbl[blzz] = sc
                bl[blzz] = ''
            except ZeroDivisionError as e:
                print(f'line {h}')
                print(line)
                print('^' * len(line))
                print(f'ERROR: {e}')
                break
        elif line.startswith('for('):
            line = line[4:-1].split(',')
            cs = line[0]
            bl = line[1]
            for i in range(eval(cs)):
                jx(eval(f"cbl['{bl}']"))
                
        elif line.startswith('run('):
            line = line[4:-1]
            jx(eval(line))
        
        elif line.startswith('zfpj('):
            t = line[5:-1]
            t = t.split(',')
            t1 = t[0]
            t2 = t[1]
            t3 = t[2]
            t4 = t1 + t2
            cbl[t3] = t4
            bl[t3] = ''

        elif line.startswith('music('):
            try:
                t = line[6:-1].split(',')
                t1 = t[0]
                t2 = t[1]
                play(t1,int(t2))
            except IndexError:
                print(f'line {h}')
                print(line)
                print('^' * len(line))
                print('ERROR: Two parameters are required')
                break
        
        elif line.startswith('printcbl()'):
            print(cbl)
            
        elif line.startswith('stop()'):
            stop()
            
        elif line.startswith('len('):
            text1 = line[4:-1].split(',')
            text = text1[0]
            bla = text1[1]
            number = len(eval(text))
            cbl[bla] = number
            bl[bla] = ''
            
        elif line.startswith('osname('):
            text = line[7:-1]
            os_name = platform.system()
            cbl[text] = os_name
            bl[text] = ''
            
        elif line == '':
            pass
        elif '=' in line:
            pass
        elif line.startswith('import <'):
            pass
        elif 'by' in line:
            print(by)
        elif line.startswith('time('):
            text = line[5:-1]
            t = time.time()
            cbl[text] = int(t)
            bl[text] = ''
        elif line.startswith('strftime('):
            text = line[9:-1].split(',')
            now = time.localtime()
            formatted_time = time.strftime(text[0],now)
            cbl[text[1]] = formatted_time
            bl[text[1]] = ''
        
        elif line.startswith('clrprint('):
            text = line[9:-1].split(',')
            clrprint(eval(text[0]),text[1])

        elif line.startswith('random('):
            text = line[7:-1].split(',')
            start = int(text[0])
            end = int(text[1])
            bla = text[2]
            r = random(start=start,end=end)
            cbl[bla] = int(r)
            bl[bla] = ''

        elif line.startswith('abs('):
            text = line[4:-1].split(',')
            num = math.fabs(int(eval(text[0])))
            cbl[text[1]] = num
            bl[text[1]] = ''

        elif line.startswith('del '):
            text = line[4:]
            try:
                del cbl[text]
            except KeyError:
                print(f'line {h}')
                print(line)
                print('^' * len(line))
                print(f"ERROR: name '{l}' is not defined.")
                break
        else:
            print(f'line {h}')
            print(line)
            print('^' * len(line))
            print('ERROR: unknown instruction')
            break




#---------------------------------main--------------------------------------------#


for line in code.splitlines():
    h = h + 1
    line = line.rstrip(';')
    line = line.strip()
    if line.startswith('import <'):
        try:
            name = 'Lib/' + line[8:-1]
            with open(name,'r',encoding='utf-8') as name:
                name = name.read()
                code = name + '\n\n' + code
        except FileNotFoundError:
            print(f'line {h}')
            print(line)
            print(f'~~~~~~~~' + '^' * (len(line) - 8))
            print(f'ERROR:Unknown Module: {line[8:-1]}')
            sys.exit()
        
for line in code.splitlines():
    h = h + 1
    line = line.rstrip(';')
    line = line.strip()
    if line in x:
        pass
    elif line.startswith('cprint('):
        l = line[7:-1]
        try:
            if l in bl:
                print(eval(f"cbl['{l}']"))
            else:
                print(eval(l))
        except NameError:
            print(f'line {h}')
            print(line)
            print('^' * len(line))
            print(f"ERROR: name '{l}' is not defined.")
            break
        except KeyError:
            print(f'line {h}')
            print(line)
            print('^' * len(line))
            print(f"ERROR: name '{l}' is not defined.")
            break
    elif line.startswith('printf('):
        l = line[7:-1]
        try:
            if l in bl:
                sys.stdout.write(eval(f"cbl['{l}']"))
            else:
                sys.stdout.write(eval(l))
        except NameError:
                print(f'line {h}')
                print(line)
                print('^' * len(line))
                print(f"ERROR: name '{l}' is not defined.")
                break
    elif line.startswith('!'):
        pass
    elif line.startswith('}'):
        pass
    elif line.startswith('cbl '):
        try:
                line1 = line[4:]
                line1 = line1.split('=')
                name = line1[0]
                text = line1[1]
                if "k{" in text:
                    import re
                    pattern = r'k\{(.*?)\}'
                    matches = re.findall(pattern, code, re.DOTALL)
                    #print(matches[0])
                    x = x + matches[0].replace('    ', '')
                    cbl[name.strip()] = matches[0].replace('    ', '').strip('')
                    bl[name.strip()] = ''
                else:
                    cbl[name.strip()] = eval(text.strip())
                    bl[name.strip()] = ''
            #print(bl)
            #print(cbl)
        except SyntaxError:
            print(f'line {h}')
            print(line)
            print('    ' + '^' * (len(line) - 4))
            print('ERROR: Incomplete variables')
            break


    elif line.startswith('input('):
        try:    
            linen = line[6:-1]
            numbers = linen.split(',')
            text = numbers[0]
            bl1 = numbers[1]
            print(text, end="", flush=True)
            user_input = sys.stdin.readline().strip()
            cbl[bl1] = str(user_input)
            bl[bl1] = ''
        except IndexError:
            print(f'line {h}')
            print(line)
            print('^' * len(line))
            print('ERROR: The statement needs two numbers, and no characters other than numbers appear')

    elif line.startswith('int('):
        line = line[4:-1]
        l = int(eval(f"cbl['{line}']"))
        cbl[line] = l
    elif line.startswith('add('):
        try:
            lines = line[4:-1]
            nline = lines.split(',')
            num1 = int(eval(f"cbl['{nline[0]}']"))
            num2 = int(eval(f"cbl['{nline[1]}']"))
            name = nline[2]
            num3 = num1 + num2
            cbl[name] = num3
            bl[name] = ''
        except KeyError as e:
            print(f'line {h}')
            print(line)
            print('^' * len(line))
            print(f"ERROR: name {e} is not defined.")
            break
    elif line.startswith('sub('):
        try:
            lines = line[4:-1]
            nline = lines.split(',')
            num1 = int(eval(f"cbl['{nline[0]}']"))
            num2 = int(eval(f"cbl['{nline[1]}']"))
            name = nline[2]
            num3 = num1 - num2
            cbl[name] = num3
            bl[name] = ''
        except KeyError as e:
            print(f'line {h}')
            print(line)
            print('^' * len(line))
            print(f"ERROR: name {e} is not defined.")
            break
    elif line.startswith('mul('):
        try:
            lines = line[4:-1]
            nline = lines.split(',')
            num1 = int(eval(f"cbl['{nline[0]}']"))
            num2 = int(eval(f"cbl['{nline[1]}']"))
            name = nline[2]
            num3 = num1 * num2
            cbl[name] = num3
            bl[name] = ''
        except KeyError as e:
            print(f'line {h}')
            print(line)
            print('^' * len(line))
            print(f"ERROR: name {e} is not defined.")
            break
    elif line.startswith('div('):
        try:
            lines = line[4:-1]
            nline = lines.split(',')
            num1 = int(eval(f"cbl['{nline[0]}']"))
            num2 = int(eval(f"cbl['{nline[1]}']"))
            name = nline[2]
            num3 = num1 / num2
            cbl[name] = num3
            bl[name] = ''
        except KeyError as e:
            print(f'line {h}')
            print(line)
            print('^' * len(line))
            print(f"ERROR: name {e} is not defined.")
            break
        except ZeroDivisionError as e:
            print(f'line {h}')
            print(line)
            print('^' * len(line))
            print(f'ERROR: {e}')
            break

    elif line.startswith('ropen('):
        line1 = line[6:-1]
        line1 = line1.split(',')
        name = line1[0]
        bln = line1[1]
        try:
            with open(name,'r',encoding='utf-8') as file:
                file = file.read()
                cbl[bln.strip()] = file
                bl[bln.strip()] = ''
        except FileNotFoundError:
            print(f'line {h}')
            print(line)
            print('^' * len(line))
            print(f'ERROR: No such file or directory: "{name}"')
            break

    elif line.startswith('wopen('):
        line = line[6:-1]
        open(line,'w',encoding='utf-8')

    elif line.startswith('sleep('):
        line = line[6:-1]
        time.sleep(eval(line))
        
    elif line.startswith('fopen('):
        line = line[6:-1].split(',')
        #print(line)
        name = line[0]
        #print(name)
        nr = line[1]
        #print(nr)
        with open(name,'w',encoding='utf-8') as file:
            file.write(eval(nr))
            file.close()
    
    elif line.startswith('aopen('):
        line = line[6:-1].split(',')
        #print(line)
        name = line[0]
        #print(name)
        nr = line[1]
        #print(nr)
        with open(name,'a',encoding='utf-8') as file:
            file.write(eval(nr))
            file.close()

    elif line.startswith('exit()'):
        sys.exit()
    
    elif line.startswith('system('):
        line = line[7:-1]
        os.system(eval(line))
        

    elif line.startswith('if('):
        line = line[3:-1].split(',')
        tj = line[0]
        bl = line[1]
        tj = eval(tj)
        if tj:
            jx(eval(f"cbl['{bl}']"))
        else:
            pass

    elif line.startswith('while('):
        line = line[6:-1].split(',')
        tj = line[0]
        bl = line[1]
        tj = eval(tj)
        if tj:
            while True:
                jx(eval(f"cbl['{bl}']"))
        else:
            pass
        
    elif line.startswith('js('):
        try:
            t = line[3:-1].split(",")
            sc = t[0]
            blz = t[1]
            sc = eval(sc)
            cbl[blz] = sc
            bl[blz] = ''
        except ZeroDivisionError as e:
            print(f'line {h}')
            print(line)
            print('^' * len(line))
            print(f'ERROR: {e}')
            break
    elif line.startswith('for('):
        line = line[4:-1].split(',')
        cs = line[0]
        bl = line[1]
        for i in range(eval(cs)):
            jx(eval(f"cbl['{bl}']"))
            
    elif line.startswith('run('):
        line = line[4:-1]
        jx(eval(line))
     
    elif line.startswith('zfpj('):
        t = line[5:-1]
        t = t.split(',')
        t1 = t[0]
        t2 = t[1]
        t3 = t[2]
        t4 = t1 + t2
        cbl[t3] = t4
        bl[t3] = ''

    elif line.startswith('music('):
        try:
            t = line[6:-1].split(',')
            t1 = t[0]
            t2 = t[1]
            play(t1,int(t2))
        except IndexError:
            print(f'line {h}')
            print(line)
            print('^' * len(line))
            print('ERROR: Two parameters are required')
            break
    
    elif line.startswith('printcbl()'):
        print(cbl)
        
    elif line.startswith('stop()'):
        stop()
        
    elif line.startswith('len('):
        text1 = line[4:-1].split(',')
        text = text1[0]
        bla = text1[1]
        number = len(eval(text))
        cbl[bla] = number
        bl[bla] = ''
        
    elif line.startswith('osname('):
        text = line[7:-1]
        os_name = platform.system()
        cbl[text] = os_name
        bl[text] = ''
        
    elif line == '':
        pass
    elif '=' in line:
        pass
    elif line.startswith('import <'):
        pass
    elif 'by' in line:
        print(by)
    elif line.startswith('time('):
        text = line[5:-1]
        t = time.time()
        cbl[text] = int(t)
        bl[text] = ''
    elif line.startswith('strftime('):
        text = line[9:-1].split(',')
        now = time.localtime()
        formatted_time = time.strftime(text[0],now)
        cbl[text[1]] = formatted_time
        bl[text[1]] = ''
    
    elif line.startswith('clrprint('):
        text = line[9:-1].split(',')
        clrprint(eval(text[0]),text[1])

    elif line.startswith('random('):
        text = line[7:-1].split(',')
        start = int(text[0])
        end = int(text[1])
        bla = text[2]
        r = random(start=start,end=end)
        cbl[bla] = int(r)
        bl[bla] = ''

    elif line.startswith('abs('):
        text = line[4:-1].split(',')
        num = math.fabs(int(eval(text[0])))
        cbl[text[1]] = num
        bl[text[1]] = ''

    elif line.startswith('del '):
        text = line[4:]
        try:
            del cbl[text]
        except KeyError:
            print(f'line {h}')
            print(line)
            print('^' * len(line))
            print(f"ERROR: name '{l}' is not defined.")
            break
    else: 
            print(f'line {h}')
            print(line)
            print('^' * len(line))
            print('ERROR: unknown instruction')
            break

#print(f"处理后的代码: {code}")
#print(f"变量注册表: {bl}")
print(f"cbl: {cbl}")
#print(f"多行变量注册表{x}")
#print(f"行:{h}")

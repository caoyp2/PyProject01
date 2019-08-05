'''
    子进程
    通过subprocess模块创建子进程
'''
import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'],shell=False) #相当于命令行执行nslookup www.python.org
# print('Exit code:', r)


# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('GBK'))
# print('Exit code:', p.returncode)

obj = subprocess.Popen(["ipconfig"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=False)

cmd_out = obj.stdout.read()
obj.stdout.close()
print(cmd_out)





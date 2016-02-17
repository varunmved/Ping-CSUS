from flask import Flask, render_template, flash
import flask
import os
import csv
import paramiko, base64

with open("PASSWORD.txt") as f:
        content = f.readlines()

#hardcoding because i'm a dumbass
PASSWORD = str(content)
PASSWORD = PASSWORD[2:-4]

app = Flask(__name__)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

@app.route("/", methods=['GET','POST'])
def start():
    #servers  = ['athena.ecs.csus.edu','atoz.ecs.csus.edu','sp1.ecs.csus.edu','sp2.ecs.csus.edu']
    servers = ['athena.ecs.csus.edu']
    out_list = []
    
    for server in servers:
        out_string = pull(server)
        out_list.append(out_string)
    return str(out_list)

def pull(server_name):
    ssh.connect(server_name, username='vedv', password=PASSWORD)
    #stdin, stdout, stderr = ssh.exec_command("sudo dmesg") 
    stdin, stdout, stderr = \
    ssh.exec_command("uptime")
    type(stdin)
    out_string = stdout.readlines()
    ssh.exec_command("logout")
    #type("logout")
    return out_string

    #out_list = []
    #out_list.append(out_string)
    #return out_list

if __name__ == '__main__':
    app.debug = True
    app.run()

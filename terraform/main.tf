resource "aws_instance" "webserver" {
    ami = "ami-0022f774911c1d690"
    instance_type = "t2.micro"
    tags = {
        name = "nginx-webserver"
        tier = "frontend"
    }

user_data     = <<EOF
        #!/bin/bash
        sudo apt update
        sudo apt install nginx -y
        systemctl enable nginx
        systemctl start nginx
EOF
key_name = aws_key_pair.webserver.id
vpc_security_group_ids = [ aws_security_group.ssh-access.id]
}

resource "aws_key_pair" "websrv" {
  public_key = file("~/.ssh/id_rsa.pub")
}

resource "aws_security_group" "open-ssh" {
    name = "ssh-access"
    description = "Add access for SSH"
    ingress = {
      cidr_blocks = [ "0.0.0.0/0" ]
      from_port = "22"
      protocol = "tcp"
    }
    egress = [ {
      cidr_blocks = [ "0.0.0.0/0" ]
      from_port = 80
      to_port = 80
    } ]
}

output "public_ip" {
    value = aws_instance.webserver.public_ip  
}

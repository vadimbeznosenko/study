provider "aws" {}


resource "aws_instance" "my_Ubuntu" {
 # count         = 3
  ami           = "ami-090f10efc254eaf55"
  instance_type = "t2.micro"
  tags = {
    Name    = "My AWS Server"
    Owner   = "Vadym"
    Project = "Lessons"
  }
}
resource "aws_instance" "my_Amazon" {
  ami           = "ami-03a71cec707bfc3d7"
  instance_type = "t2.micro"

  tags = {
    Name    = "My AWS Server"
    Owner   = "Vadym"
    Project = "Lessons"
  }
}
